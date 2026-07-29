"""
Arbitrates commands from the remote operator console (and future input
sources, e.g. a joystick), forwards validated decisions to amr_engine, and
streams live telemetry (map, battery, lift/fault status) out over a websocket.
"""

import asyncio
import threading
import math
import time
import os
import re


import rclpy
from rclpy.node import Node

from geometry_msgs.msg import Twist, PoseStamped
from nav_msgs.msg import OccupancyGrid, Odometry, Path

from slam_toolbox.srv import ( 
    SerializePoseGraph, 
    DeserializePoseGraph
)

from amr_command.map_encoder import encode_occupancy_grid
from amr_command.websocket_server import WebsocketServer



class OperatorInputArbiter:

    def __init__(self):
        self._linear = 0.0
        self._angular = 0.0
        self._last_command_time = None
        self._lock = threading.Lock()

    def submit_command(self, source: str, linear: float, angular: float):
        with self._lock:
            self._linear = linear
            self._angular = angular
            self._last_command_time = time.monotonic()

    def get_active_command(self):
        with self._lock:
            return (
                self._linear,
                self._angular,
                self._last_command_time,
            )


class CommandGatewayNode(Node):

    def __init__(self):
        super().__init__("amr_command")
        self.get_logger().info("CommandGatewayNode started")

        self.websocket_server = WebsocketServer()
        self.websocket_server._on_message_cb = self._on_ws_frame

        self.arbiter = OperatorInputArbiter()

        self._latest_pose = None

        self.declare_parameter(
            "maps_directory",
            "maps",
        )

        self.maps_directory = self.get_parameter(
            "maps_directory"
        ).value

        self.declare_parameter(
            "slam_mode",
            "mapping",
        )

        self.slam_mode = self.get_parameter(
            "slam_mode"
        ).value

        os.makedirs(
            self.maps_directory,
            exist_ok=True,
        )

        threading.Thread(
            target=self._run_ws,
            daemon=True,
        ).start()

        self.cmd_vel_pub = self.create_publisher(
            Twist,
            "/cmd_vel",
            10,
        )

        self.goal_pose_pub = self.create_publisher(
            PoseStamped,
            "/goal_pose",
            10,
        )

        self.serialize_client = self.create_client(
            SerializePoseGraph,
            "/slam_toolbox/serialize_map",
        )

        self.deserialize_client = self.create_client(
            DeserializePoseGraph,
            "/slam_toolbox/deserialize_map",
        )

        self.map_sub = self.create_subscription(
            OccupancyGrid,
            "/map",
            self._map_callback,
            10,
        )

        self.odom_sub = self.create_subscription(
            Odometry,
            "/odom",
            self._odom_callback,
            10,
        )

        self.create_timer(
            0.1,
            self._publish_cmd_vel,
        )
        self.plan_sub = self.create_subscription(
            Path,
            "/plan",
            self.plan_callback,
            10,
        )
        self.get_logger().info("CommandGatewayNode initialized")
        self._send_slam_mode()
        self.create_timer(
            2.0,
            self._send_slam_mode,
        )
   

    def plan_callback(self, msg):

        if len(msg.poses) == 0:

            frame = {
                "type": "plan",
                "points": [],
            }

            asyncio.run_coroutine_threadsafe(
                self.websocket_server.broadcast(frame),
                self.websocket_server.loop,
            )

            return

        points = []

        for pose in msg.poses[::5]:

            points.append([
                pose.pose.position.x,
                pose.pose.position.y,
            ])

        frame = {
            "type": "plan",
            "points": points,
        }

        asyncio.run_coroutine_threadsafe(
            self.websocket_server.broadcast(frame),
            self.websocket_server.loop,
        )

        self.get_logger().info(
            f"Broadcasted plan with {len(points)} points"
        )


    def _on_ws_frame(self, data):
        try:

            frame_type = data.get("type")

            if frame_type == "drive":

                self.arbiter.submit_command(
                    source="browser",
                    linear=float(data.get("linear", 0.0)),
                    angular=float(data.get("angular", 0.0)),
                )

            elif frame_type == "nav_goal":

                x = float(data["x"])
                y = float(data["y"])
                theta = float(data["theta"])

                if not (
                    math.isfinite(x)
                    and math.isfinite(y)
                    and math.isfinite(theta)
                ):
                    self.get_logger().warning(
                        "Rejected invalid goal"
                    )
                    return

                goal = PoseStamped()

                goal.header.stamp = self.get_clock().now().to_msg()
                goal.header.frame_id = "map"

                goal.pose.position.x = x
                goal.pose.position.y = y
                goal.pose.position.z = 0.0

                half_theta = theta / 2.0

                goal.pose.orientation.x = 0.0
                goal.pose.orientation.y = 0.0
                goal.pose.orientation.z = math.sin(half_theta)
                goal.pose.orientation.w = math.cos(half_theta)

                self.goal_pose_pub.publish(goal)

                self.get_logger().info(
                    f"Goal published ({x:.2f}, {y:.2f})"
                )

            elif frame_type == "map_save":

                map_name = self._sanitize_map_name(
                    data.get("name", "")
                )

                if map_name is None:

                    asyncio.run_coroutine_threadsafe(
                        self.websocket_server.broadcast({
                            "type": "map_op_result",
                            "ok": False,
                            "error": "Invalid map name",
                        }),
                        self.websocket_server.loop,
                    )

                    return

                self._save_map(map_name)

            elif frame_type == "map_load":

                map_name = self._sanitize_map_name(
                    data.get("name", "")
                )

                if map_name is None:

                    asyncio.run_coroutine_threadsafe(
                        self.websocket_server.broadcast({
                            "type": "map_op_result",
                            "ok": False,
                            "error": "Invalid map name",
                        }),
                        self.websocket_server.loop,
                    )

                    return

                self._load_map(map_name)

            elif frame_type == "map_list":

                self._send_map_list()

        except Exception as e:
            self.get_logger().error(str(e))

    def _odom_callback(self, msg):
        pose = msg.pose.pose
        self.get_logger().info(
            f"Received odom: x={pose.position.x:.2f}, y={pose.position.y:.2f}"
        )

        q = pose.orientation

        siny_cosp = 2.0 * (q.w * q.z + q.x * q.y)
        cosy_cosp = 1.0 - 2.0 * (q.y * q.y + q.z * q.z)

        yaw = math.atan2(siny_cosp, cosy_cosp)

        self._latest_pose = {
            "x": pose.position.x,
            "y": pose.position.y,
            "yaw": yaw,
        }

    def _map_callback(self, msg):
        self.get_logger().info("MAP RECEIVED")
        
        try:
            frame = encode_occupancy_grid(msg)
            frame["type"] = "map"
            frame["pose"] = self._latest_pose

            if self.websocket_server.loop:
                asyncio.run_coroutine_threadsafe(
                    self.websocket_server.broadcast(frame),
                    self.websocket_server.loop,
                )

        except Exception as e:
            self.get_logger().error(f"Map broadcast failed: {e}")
    
    def _run_ws(self):
        asyncio.run(self.websocket_server.start())

    
    def _sanitize_map_name(self, name: str):

            if not isinstance(name, str):
                return None

            if not re.fullmatch(
                r"[a-zA-Z0-9_-]+",
                name,
            ):
                return None

            return name
        
        

    def _save_map(self, map_name):

        if not self.serialize_client.service_is_ready():

            asyncio.run_coroutine_threadsafe(
                self.websocket_server.broadcast({
                    "type": "map_op_result",
                    "ok": False,
                    "error": "Serialize service unavailable",
                }),
                self.websocket_server.loop,
            )

            return

        request = SerializePoseGraph.Request()

        request.filename = os.path.join(
            self.maps_directory,
            map_name,
        )

        future = self.serialize_client.call_async(request)

        future.add_done_callback(
            self._save_map_done
        )

    def _save_map_done(self, future):

        try:

            response = future.result()

            ok = getattr(response, "result", True)

            error = ""

        except Exception as e:

            ok = False
            error = str(e)

        asyncio.run_coroutine_threadsafe(

            self.websocket_server.broadcast({

                "type": "map_op_result",

                "ok": ok,

                "error": error,

            }),

            self.websocket_server.loop,

        )
    def _load_map(self, map_name):

        if not self.deserialize_client.service_is_ready():

            asyncio.run_coroutine_threadsafe(
                self.websocket_server.broadcast({
                    "type": "map_op_result",
                    "ok": False,
                    "error": "Deserialize service unavailable",
                }),
                self.websocket_server.loop,
            )

            return

        map_path = os.path.join(
            self.maps_directory,
            map_name,
        )

        if not os.path.exists(map_path + ".posegraph"):

            asyncio.run_coroutine_threadsafe(

                self.websocket_server.broadcast({

                    "type": "map_op_result",

                    "ok": False,

                    "error": "Map does not exist",

                }),

                self.websocket_server.loop,

            )

            return

        request = DeserializePoseGraph.Request()

        request.filename = os.path.join(
            self.maps_directory,
            map_name,
        )

        future = self.deserialize_client.call_async(request)

        future.add_done_callback(
            self._load_map_done
        )

    def _load_map_done(self, future):

        try:

            response = future.result()

            ok = getattr(response, "result", True)

            error = ""

        except Exception as e:

            ok = False
            error = str(e)

        asyncio.run_coroutine_threadsafe(

            self.websocket_server.broadcast({

                "type": "map_op_result",

                "ok": ok,

                "error": error,

            }),

            self.websocket_server.loop,

        )

    def _send_map_list(self):

        try:

            maps = []

            for filename in os.listdir(self.maps_directory):

                if filename.endswith(".posegraph"):

                    maps.append(
                        filename[:-10]
                    )

            maps.sort()

            frame = {

                "type": "map_list",

                "maps": maps,

            }

        except Exception as e:

            frame = {

                "type": "map_op_result",

                "ok": False,

                "error": str(e),

            }

        asyncio.run_coroutine_threadsafe(

            self.websocket_server.broadcast(frame),

            self.websocket_server.loop,

        )

    def _send_slam_mode(self):

        mode = self.slam_mode.capitalize()

        frame = {
            "type": "slam_mode",
            "mode": mode,
        }

        asyncio.run_coroutine_threadsafe(
            self.websocket_server.broadcast(frame),
            self.websocket_server.loop,
        )
    

    def _publish_cmd_vel(self):
        linear, angular, last_command_time = self.arbiter.get_active_command()

        if (
            last_command_time is None
            or (time.monotonic() - last_command_time) > 0.5
        ):
            return

        msg = Twist()
        msg.linear.x = linear
        msg.angular.z = angular

        self.cmd_vel_pub.publish(msg)




def main(args=None):
    rclpy.init(args=args)

    node = CommandGatewayNode()

    try:
        rclpy.spin(node)
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == "__main__":
    main()
