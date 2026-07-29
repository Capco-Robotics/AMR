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
import json


import rclpy
from rclpy.node import Node

from geometry_msgs.msg import Twist, PoseStamped
from nav_msgs.msg import OccupancyGrid, Odometry, Path

from rcl_interfaces.srv import GetParameters

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
            # Absolute by default. We list this directory relative to our own
            # process CWD, but slam_toolbox writes the file relative to *its*
            # CWD -- if the two are launched from different places a
            # "successful" save never appears in the list and Load's existence
            # check fails. An absolute path removes the ambiguity, which is
            # also why the filenames handed to the services below are absolute.
            os.path.join(os.path.expanduser("~"), ".ros", "amr_maps"),
        )

        # Normalise whatever we were handed, so a relative override still
        # resolves to an absolute path instead of quietly reintroducing the
        # CWD mismatch above.
        self.maps_directory = os.path.abspath(
            os.path.expanduser(
                self.get_parameter("maps_directory").value
            )
        )

        self.declare_parameter(
            "paths_directory",
            os.path.join(os.path.expanduser("~"), ".ros", "amr_paths"),
        )

        # Same treatment as maps_directory: paths are written and read back by
        # name, so a relative default would resolve against whatever CWD the
        # gateway happened to be launched from.
        self.paths_directory = os.path.abspath(
            os.path.expanduser(
                self.get_parameter("paths_directory").value
            )
        )

        # Latest known slam_toolbox mode, refreshed from the node itself (see
        # _refresh_slam_mode). None until we have actually heard back.
        self.slam_mode = None

        os.makedirs(
            self.maps_directory,
            exist_ok=True,
        )
        os.makedirs(
            self.paths_directory,
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

        # Both slam.launch.py and localization.launch.py name their node
        # "slam_toolbox", so the node name cannot tell mapping from
        # localization. The node's own "mode" parameter can: the mapping config
        # sets online_async, the localization config sets localization.
        self.slam_mode_client = self.create_client(
            GetParameters,
            "/slam_toolbox/get_parameters",
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
        self._refresh_slam_mode()
        self.create_timer(
            2.0,
            self._refresh_slam_mode,
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


            elif frame_type == "nav_path":

                points = data.get("points", [])

                if not isinstance(points, list):

                    self.get_logger().warning(
                        "Rejected invalid path"
                    )

                    return


                for p in points:

                    if (
                        not isinstance(p, list)
                        or len(p) != 3
                        or not all(
                            isinstance(v, (int, float))
                            and math.isfinite(v)
                            for v in p
                        )
                    ):

                        self.get_logger().warning(
                            "Rejected invalid path points"
                        )

                        return


                self.get_logger().info(
                    f"Received nav_path with {len(points)} points"
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
            elif frame_type == "path_save":

                path_name = self._sanitize_map_name(
                    data.get("name", "")
                )

                if path_name is None:

                    asyncio.run_coroutine_threadsafe(
                        self.websocket_server.broadcast({
                            "type": "path_op_result",
                            "ok": False,
                            "error": "Invalid path name",
                        }),
                        self.websocket_server.loop,
                    )

                    return

                self._save_path(
                    path_name,
                    data.get("points", []),
                )

            elif frame_type == "path_load":

                path_name = self._sanitize_map_name(
                    data.get("name", "")
                )

                if path_name is None:

                    asyncio.run_coroutine_threadsafe(
                        self.websocket_server.broadcast({
                            "type": "path_op_result",
                            "ok": False,
                            "error": "Invalid path name",
                        }),
                        self.websocket_server.loop,
                    )

                    return

                self._load_path(path_name)

            elif frame_type == "path_list":

                 self._send_path_list()

            elif frame_type == "path_delete":

                path_name = self._sanitize_map_name(
                    data.get("name", "")
                )

                if path_name is None:

                    asyncio.run_coroutine_threadsafe(
                        self.websocket_server.broadcast({
                            "type": "path_op_result",
                            "ok": False,
                            "error": "Invalid path name",
                        }),
                        self.websocket_server.loop,
                    )

                    return

                self._delete_path(path_name)


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

            # SerializePoseGraph.Response is `uint8 result` with
            # RESULT_SUCCESS = 0 and RESULT_FAILED_TO_WRITE_FILE = 255. Reading
            # it as a truthy value inverts the meaning: a successful save
            # returns 0, which is falsy, so the console showed a failure toast
            # with an empty error string every time a save actually worked.
            ok = (
                response.result
                == SerializePoseGraph.Response.RESULT_SUCCESS
            )

            error = (
                ""
                if ok
                else f"slam_toolbox failed to write the map (result={response.result})"
            )

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

        # match_type defaults to UNSET(0), which makes the deserialize a no-op:
        # the pose graph loads but the robot is never placed on it, so "Load"
        # appeared to succeed and changed nothing. START_AT_FIRST_NODE is the
        # right choice for reloading a map in mapping mode; localization mode
        # would want LOCALIZE_AT_POSE with an initial_pose.
        request.match_type = (
            DeserializePoseGraph.Request.START_AT_FIRST_NODE
        )

        future = self.deserialize_client.call_async(request)

        future.add_done_callback(
            self._load_map_done
        )

    def _load_map_done(self, future):

        try:

            # Unlike SerializePoseGraph, DeserializePoseGraph.Response carries
            # no fields at all -- slam_toolbox gives us no success/failure code
            # for a load. So the only failure we can actually observe is the
            # call itself raising. (The pre-flight existence check in _load_map
            # is what catches the common "no such map" case.)
            future.result()

            ok = True
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
    def _save_path(self, name, points):

        if not isinstance(points, list):
            self._path_error("Invalid points")
            return

        if len(points) == 0 or len(points) > 1000:
            self._path_error("Invalid point count")
            return

        for p in points:

            if (
                not isinstance(p, list)
                or len(p) != 3
            ):
                self._path_error("Invalid point format")
                return

            # Shape alone is not enough: json.dump happily writes NaN and
            # Infinity, which are not valid JSON, so a poisoned point would
            # round-trip out of _load_path as a value no consumer can use --
            # and reach Nav2 as an unreachable goal. The nav_goal branch
            # already screens for this; match it here.
            if not all(
                isinstance(v, (int, float))
                and not isinstance(v, bool)
                and math.isfinite(v)
                for v in p
            ):
                self._path_error("Invalid point value")
                return

        filepath = os.path.join(
            self.paths_directory,
            name + ".json"
        )

        with open(filepath, "w") as f:

            json.dump(
                {
                    "points": points
                },
                f
            )

        asyncio.run_coroutine_threadsafe(
            self.websocket_server.broadcast({
                "type": "path_op_result",
                "ok": True,
                "error": "",
            }),
            self.websocket_server.loop,
        )


    def _load_path(self, name):

        filepath = os.path.join(
            self.paths_directory,
            name + ".json"
        )


        if not os.path.exists(filepath):

            self._path_error(
                "Path does not exist"
            )

            return


        with open(filepath) as f:

            data=json.load(f)


        asyncio.run_coroutine_threadsafe(
            self.websocket_server.broadcast({
                "type":"path_data",
                "name":name,
                "points":data["points"],
            }),
            self.websocket_server.loop,
        )



    def _send_path_list(self):

        try:

            paths=[]

            for file in os.listdir(
                self.paths_directory
            ):

                if file.endswith(".json"):

                    paths.append(
                        file[:-5]
                    )


            paths.sort()


            frame={
                "type":"path_list",
                "paths":paths,
            }


        except Exception as e:

            frame={
                "type":"path_op_result",
                "ok":False,
                "error":str(e),
            }


        asyncio.run_coroutine_threadsafe(
            self.websocket_server.broadcast(frame),
            self.websocket_server.loop,
        )



    def _delete_path(self,name):

        filepath=os.path.join(
            self.paths_directory,
            name+".json"
        )


        if os.path.exists(filepath):

            os.remove(filepath)

            asyncio.run_coroutine_threadsafe(
                self.websocket_server.broadcast({
                    "type":"path_op_result",
                    "ok":True,
                    "error":"",
                }),
                self.websocket_server.loop,
            )

        else:

            self._path_error(
                "Path does not exist"
            )



    def _path_error(self,msg):

        asyncio.run_coroutine_threadsafe(
            self.websocket_server.broadcast({
                "type":"path_op_result",
                "ok":False,
                "error":msg,
            }),
            self.websocket_server.loop,
        )
    def _odom_callback(self, msg):

      pose = msg.pose.pose

      q = pose.orientation

      siny_cosp = 2.0 * (
            q.w * q.z +
            q.x * q.y
        )

      cosy_cosp = 1.0 - 2.0 * (
            q.y * q.y +
            q.z * q.z
        )

      yaw = math.atan2(
            siny_cosp,
            cosy_cosp
        )

      self._latest_pose = {
            "x": pose.position.x,
            "y": pose.position.y,
            "yaw": yaw,
        }



    def _map_callback(self, msg):

        # The websocket thread sets .loop once it is up. Maps can arrive
        # before that, and run_coroutine_threadsafe(None) raises inside a
        # subscription callback, so gate on it.
        if not self.websocket_server.loop:
            return

        try:

            frame = encode_occupancy_grid(msg)
            frame["type"] = "map"
            frame["pose"] = self._latest_pose

            asyncio.run_coroutine_threadsafe(
                self.websocket_server.broadcast(frame),
                self.websocket_server.loop,
            )

        except Exception as e:

            self.get_logger().error(
                f"Map broadcast failed: {e}"
            )

    # slam_toolbox's "mode" parameter -> what the operator should see.
    _SLAM_MODE_LABELS = {
        "online_async": "Mapping",
        "online_sync": "Mapping",
        "mapping": "Mapping",
        "localization": "Localization",
    }

    def _refresh_slam_mode(self):
        """Ask slam_toolbox what mode it is in, then broadcast the answer.

        This used to be a hardcoded parameter that nothing ever set, so the
        console read "Mapping" permanently -- including when no SLAM node was
        running at all.
        """

        if not self.slam_mode_client.service_is_ready():
            # No slam_toolbox up (or not up yet). Say so rather than claiming
            # a mode we cannot observe.
            self.slam_mode = None
            self._broadcast_slam_mode()
            return

        request = GetParameters.Request()
        request.names = ["mode"]

        future = self.slam_mode_client.call_async(request)
        future.add_done_callback(self._slam_mode_done)

    def _slam_mode_done(self, future):

        try:
            response = future.result()

            if response.values:
                self.slam_mode = response.values[0].string_value or None
            else:
                self.slam_mode = None

        except Exception as e:
            self.get_logger().warning(
                f"Could not read slam_toolbox mode: {e}"
            )
            self.slam_mode = None

        self._broadcast_slam_mode()

    def _broadcast_slam_mode(self):

        # Fires on a ROS timer that starts before the websocket thread has
        # published its loop; same guard as _map_callback.
        if not self.websocket_server.loop:
            return

        if self.slam_mode is None:
            mode = "Unknown"
        else:
            mode = self._SLAM_MODE_LABELS.get(
                self.slam_mode,
                self.slam_mode.capitalize(),
            )

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
