"""
Arbitrates commands from the remote operator console (and future input
sources, e.g. a joystick), forwards validated decisions to amr_engine, and
streams live telemetry (map, battery, lift/fault status) out over a websocket.
"""

import asyncio
import threading
import math

import rclpy
from rclpy.node import Node

from geometry_msgs.msg import Twist
from nav_msgs.msg import OccupancyGrid, Odometry

from amr_command.map_encoder import encode_occupancy_grid
from amr_command.websocket_server import WebsocketServer


class OperatorInputArbiter:

    def __init__(self):
        self._linear = 0.0
        self._angular = 0.0
        self._lock = threading.Lock()

    def submit_command(self, source: str, linear: float, angular: float):
        with self._lock:
            self._linear = linear
            self._angular = angular

    def get_active_command(self):
        with self._lock:
            return self._linear, self._angular


class CommandGatewayNode(Node):

    def __init__(self):
        super().__init__("amr_command")
        self.get_logger().info("CommandGatewayNode started")

        self.websocket_server = WebsocketServer()
        self.websocket_server._on_message_cb = self._on_ws_frame

        self.arbiter = OperatorInputArbiter()

        self._latest_pose = None

        threading.Thread(
            target=self._run_ws,
            daemon=True,
        ).start()

        self.cmd_vel_pub = self.create_publisher(
            Twist,
            "/cmd_vel",
            10,
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

        self.get_logger().info("CommandGatewayNode initialized")

    def _run_ws(self):
        asyncio.run(self.websocket_server.start())

    def _on_ws_frame(self, data):
        try:
            if data.get("type") == "drive":
                self.arbiter.submit_command(
                    source="browser",
                    linear=float(data.get("linear", 0.0)),
                    angular=float(data.get("angular", 0.0)),
                )

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
  

    def _publish_cmd_vel(self):
        linear, angular = self.arbiter.get_active_command()

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
