"""
Arbitrates commands from the remote operator console (and future input
sources, e.g. a joystick), forwards validated decisions to amr_engine, and
streams live telemetry (map, battery, lift/fault status) out over a websocket.
"""

import json
import threading

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

from amr_command.websocket_server import WebsocketServer

# TODO: from amr_msgs.action import NavigateToGoal
# TODO: from amr_msgs.srv import TriggerEstop
# TODO: from rclpy.action import ActionClient


class OperatorInputArbiter:
    """
    Stores the latest operator command.

    This class is intentionally simple for now. The 'source' parameter is
    included so that future command sources (joystick, autonomy, etc.) can be
    arbitrated without changing the public API.
    """

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

        # Existing websocket server
        self.websocket_server = WebsocketServer()
        self.websocket_server._on_message_cb = self._on_ws_frame

        # TODO: subscribe to /map, battery, lift/fault status; relay them
        # over the websocket; receive operator commands and forward to amr_engine.

        # TODO: instantiate clients and uncomment
        # self._navigate_client = ActionClient(self, NavigateToGoal, "navigate_to_goal")
        # self._estop_client = self.create_client(TriggerEstop, "trigger_estop")

        # Operator input arbiter
        self.arbiter = OperatorInputArbiter()

        # Run websocket server in background
        threading.Thread(
            target=self._run_ws,
            daemon=True,
        ).start()

        # ROS publisher
        self.cmd_vel_pub = self.create_publisher(
            Twist,
            "/cmd_vel",
            10,
        )

        self.get_logger().info("cmd_vel publisher created")

        # Publish commands every 100 ms
        self.create_timer(
            0.1,
            self._publish_cmd_vel,
        )

    def _run_ws(self):
        import asyncio

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