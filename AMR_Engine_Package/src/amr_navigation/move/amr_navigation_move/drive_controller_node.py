"""Converts /cmd_vel into per-wheel setpoints and forwards them to the Pico bridge."""
import rclpy
from rclpy.node import Node

# TODO: from amr_msgs.srv import SetDriveLimits


class DriveControllerNode(Node):
    def __init__(self):
        super().__init__('drive_controller')
        # TODO: geometry_msgs/Twist subscriber on /cmd_vel, amr_msgs/WheelSetpoints
        # publisher to amr_pico_bridge, using diff_drive_kinematics.

        # TODO: implement callback and uncomment
        # self.create_service(SetDriveLimits, 'set_drive_limits', self._handle_set_drive_limits)


def main(args=None):
    rclpy.init(args=args)
    node = DriveControllerNode()
    try:
        rclpy.spin(node)
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
