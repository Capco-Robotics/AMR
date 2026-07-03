"""
Gateway node for AMR operator control.

It receives commands from a WebSocket-based operator console,
stores the latest valid command, and publishes it to ROS2 /cmd_vel.
Also includes a basic safety timeout so the robot stops if input stops.
"""

import json
import threading
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

from amr_command.websocket_server import WebsocketServer


class CommandGatewayNode(Node):

    def __init__(self):
        super().__init__('amr_command')

        # WebSocket setup
        self.ws_server = WebsocketServer()
        self.ws_server._on_message_cb = self._on_ws_frame

        # run websocket in background
        threading.Thread(
            target=self._run_ws,
            daemon=True
        ).start()

        # latest command state
        self.linear = 0.0
        self.angular = 0.0
        self.last_update = self.get_clock().now()

        # ROS publisher
        self.pub = self.create_publisher(Twist, "/cmd_vel", 10)

        # control loop
        self.create_timer(0.1, self._publish)

    # ---------------- websocket ----------------

    def _run_ws(self):
        import asyncio
        asyncio.run(self.ws_server.start())

    def _on_ws_frame(self, message: str):
        try:
            data = json.loads(message)

            if data.get("type") == "drive":
                self.linear = float(data.get("linear", 0.0))
                self.angular = float(data.get("angular", 0.0))
                self.last_update = self.get_clock().now()

        except Exception as e:
            self.get_logger().error(str(e))

    # ---------------- control ----------------

    def _publish(self):
        msg = Twist()

        # stop robot if no recent command
        if (self.get_clock().now() - self.last_update).nanoseconds * 1e-9 > 1.0:
            msg.linear.x = 0.0
            msg.angular.z = 0.0
        else:
            msg.linear.x = self.linear
            msg.angular.z = self.angular

        self.pub.publish(msg)