"""Converts encoder ticks from the Pico bridge into /odom + the odom->base_link tf."""

import math

import rclpy
from rclpy.node import Node

from geometry_msgs.msg import TransformStamped
from nav_msgs.msg import Odometry
from tf2_ros import TransformBroadcaster
from tf_transformations import quaternion_from_euler

from amr_msgs.msg import EncoderTicks

from amr_navigation_move.diff_drive_kinematics import (
    ticks_to_pose_delta,
)

# TODO: from amr_msgs.srv import ResetOdometry


class OdometryNode(Node):
    def __init__(self):
        super().__init__("odometry")

    # Robot pose in global frame
        self.x = 0.0
        self.y = 0.0
        self.theta = 0.0

    # Store previous callback time
        self.last_time = self.get_clock().now()

    # Publisher: /odom
        self.odom_pub = self.create_publisher(
            Odometry,
            "/odom",
            10,
        )

    # TF Broadcaster
        self.tf_broadcaster = TransformBroadcaster(self)

    # Subscriber: /encoder_ticks
        self.encoder_sub = self.create_subscription(
            EncoderTicks,
            "/encoder_ticks",
            self._on_encoder_ticks,
            10,
        )

        self.get_logger().info("Odometry Node Started")

    # TODO: implement callback and uncomment
    # self.create_service(
    #     ResetOdometry,
    #     "reset_odometry",
    #     self._handle_reset_odometry,
    # )

    def _on_encoder_ticks(self, msg: EncoderTicks):
        """Handle incoming encoder tick updates."""

        # Time since previous encoder update
        current_time = self.get_clock().now()
        dt = (current_time - self.last_time).nanoseconds / 1e9
        self.last_time = current_time

        # Convert encoder ticks into local robot motion
        dx, dy, dtheta = ticks_to_pose_delta(
            msg.left_ticks,
            msg.right_ticks,
            dt,
        )

        # Update robot heading
        self.theta += dtheta

        # Convert local robot motion to global frame
        global_dx = (
            dx * math.cos(self.theta)
            - dy * math.sin(self.theta)
        )

        global_dy = (
            dx * math.sin(self.theta)
            + dy * math.cos(self.theta)
        )

        # Update global pose
        self.x += global_dx
        self.y += global_dy


        # Convert heading to quaternion
        qx, qy, qz, qw = quaternion_from_euler(
            0.0,
            0.0,
            self.theta,
        )

        # Create odometry message
        odom = Odometry()

        odom.header.stamp = current_time.to_msg()
        odom.header.frame_id = "odom"
        odom.child_frame_id = "base_link"

        odom.pose.pose.position.x = self.x
        odom.pose.pose.position.y = self.y
        odom.pose.pose.position.z = 0.0

        odom.pose.pose.orientation.x = qx
        odom.pose.pose.orientation.y = qy
        odom.pose.pose.orientation.z = qz
        odom.pose.pose.orientation.w = qw

        self.odom_pub.publish(odom)


        # Broadcast odom -> base_link transform
        transform = TransformStamped()

        transform.header.stamp = current_time.to_msg()
        transform.header.frame_id = "odom"
        transform.child_frame_id = "base_link"

        transform.transform.translation.x = self.x
        transform.transform.translation.y = self.y
        transform.transform.translation.z = 0.0

        transform.transform.rotation.x = qx
        transform.transform.rotation.y = qy
        transform.transform.rotation.z = qz
        transform.transform.rotation.w = qw

        self.tf_broadcaster.sendTransform(transform)    
    
    
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
