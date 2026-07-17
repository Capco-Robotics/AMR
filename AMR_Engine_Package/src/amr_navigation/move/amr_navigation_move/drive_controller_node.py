"""Converts /cmd_vel into per-wheel setpoints and forwards them to the Pico bridge."""

import rclpy
from rclpy.node import Node

from geometry_msgs.msg import Twist
from amr_msgs.msg import WheelSetpoints

from amr_navigation_move.diff_drive_kinematics import (
    twist_to_wheel_speeds,
    MAX_WHEEL_SPEED_MPS,
)
# TODO: from amr_msgs.srv import SetDriveLimits


class DriveControllerNode(Node):
    def __init__(self):
        super().__init__("drive_controller")

        # Publisher for wheel speed setpoints
        self.wheel_pub = self.create_publisher(
            WheelSetpoints,
            "/wheel_setpoints",
            10,
        )

        # Subscriber for robot velocity commands
        self.create_subscription(
            Twist,
            "/cmd_vel",
            self._on_cmd_vel,
            10,
        )

        # TODO: implement callback and uncomment
        # self.create_service(SetDriveLimits, 'set_drive_limits', self._handle_set_drive_limits)

    def _on_cmd_vel(self, msg: Twist):
        """
        Receive cmd_vel, convert it to left/right wheel speeds,
        and publish WheelSetpoints.
        """

        linear = msg.linear.x
        angular = msg.angular.z

        left_speed, right_speed = twist_to_wheel_speeds(
            linear,
            angular,
        )
        left_speed = max(-1.0, min(1.0, left_speed / MAX_WHEEL_SPEED_MPS))
        right_speed = max(-1.0, min(1.0, right_speed / MAX_WHEEL_SPEED_MPS))
        wheel_msg = WheelSetpoints()

        wheel_msg.header.stamp = self.get_clock().now().to_msg()
        wheel_msg.header.frame_id = "base_link"

        wheel_msg.left_speed = float(left_speed)
        wheel_msg.right_speed = float(right_speed)

        self.wheel_pub.publish(wheel_msg)


def main(args=None):
    rclpy.init(args=args)
    node = DriveControllerNode()
    try:
        rclpy.spin(node)
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == "__main__":
    main()