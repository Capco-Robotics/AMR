"""Arbitrates commands from the remote operator console (and future input
sources, e.g. a joystick), forwards validated decisions to amr_engine, and
streams live telemetry (map, battery, lift/fault status) out over a websocket.
"""
import rclpy
from rclpy.node import Node

from amr_command.websocket_server import WebsocketServer


class CommandGatewayNode(Node):
    def __init__(self):
        super().__init__('amr_command')
        self.websocket_server = WebsocketServer()
        # TODO: subscribe to /map, battery, lift/fault status; relay them
        # over the websocket; receive operator commands and forward to amr_engine.


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
