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


class CommandGatewayNode(Node):

    def __init__(self):
        super().__init__('amr_command')

        # Existing websocket server
        self.websocket_server = WebsocketServer()
        self.websocket_server._on_message_cb = self._on_ws_frame

        # TODO: subscribe to /map, battery, lift/fault status; relay them
        # over the websocket; receive operator commands and forward to amr_engine.

        # TODO: instantiate clients and uncomment
        # self._navigate_client = ActionClient(self, NavigateToGoal, 'navigate_to_goal')
        # self._estop_client = self.create_client(TriggerEstop, 'trigger_estop')

        # Run websocket server in background
        threading.Thread(
            target=self._run_ws,
            daemon=True
        ).start()

        # Latest command state
        self.linear = 0.0
        self.angular = 0.0
        self.last_update = self.get_clock().now()

        # ROS publisher
        self.cmd_vel_pub = self.create_publisher(
            Twist,
            "/cmd_vel",
            10,
        )

        # Publish commands every 100 ms
        self.create_timer(0.1, self._publish)

    def _run_ws(self):
        import asyncio
        asyncio.run(self.websocket_server.start())

    def _on_ws_frame(self, message: str):
        try:
            data = json.loads(message)

            if data.get("type") == "drive":
                self.linear = float(data.get("linear", 0.0))
                self.angular = float(data.get("angular", 0.0))
                self.last_update = self.get_clock().now()

        except Exception as e:
            self.get_logger().error(str(e))

    def _publish(self):
        msg = Twist()

        # Stop robot if command becomes stale
        if (self.get_clock().now() - self.last_update).nanoseconds * 1e-9 > 1.0:
            msg.linear.x = 0.0
            msg.angular.z = 0.0
        else:
            msg.linear.x = self.linear
            msg.angular.z = self.angular

        self.cmd_vel_pub.publish(msg)


def main(args=None):
    rclpy.init(args=args)
    node = CommandGatewayNode()

    try:
        rclpy.spin(node)
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()