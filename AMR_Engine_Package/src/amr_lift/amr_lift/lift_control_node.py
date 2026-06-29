"""Decides the lift's target height and tracks its reported state.

Publishes amr_msgs/LiftCommand to amr_pico_bridge and subscribes to
amr_msgs/LiftState for the Pico's closed-loop position/limit-switch feedback.
"""
import rclpy
from rclpy.node import Node


class LiftControlNode(Node):
    def __init__(self):
        super().__init__('amr_lift')
        # TODO: amr_msgs/LiftCommand publisher, amr_msgs/LiftState subscriber.


def main(args=None):
    rclpy.init(args=args)
    node = LiftControlNode()
    try:
        rclpy.spin(node)
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
