"""Decides what fault means what siren/light pattern.

Subscribes to diagnostics/fault topics from amr_engine and the amr_pico_bridge
fault_event stream, publishes amr_msgs/SignalCommand to amr_pico_bridge.
"""
import rclpy
from rclpy.node import Node


class SignalSystemNode(Node):
    def __init__(self):
        super().__init__('amr_error')
        # TODO: diagnostic_msgs/DiagnosticArray subscriber, amr_msgs/SignalCommand publisher.


def main(args=None):
    rclpy.init(args=args)
    node = SignalSystemNode()
    try:
        rclpy.spin(node)
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
