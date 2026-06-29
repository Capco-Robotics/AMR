"""Converts encoder ticks from the Pico bridge into /odom + the odom->base_link tf."""
import rclpy
from rclpy.node import Node


class OdometryNode(Node):
    def __init__(self):
        super().__init__('odometry')
        # TODO: amr_msgs/EncoderTicks subscriber, nav_msgs/Odometry publisher,
        # tf2_ros.TransformBroadcaster, using diff_drive_kinematics.


def main(args=None):
    rclpy.init(args=args)
    node = OdometryNode()
    try:
        rclpy.spin(node)
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
