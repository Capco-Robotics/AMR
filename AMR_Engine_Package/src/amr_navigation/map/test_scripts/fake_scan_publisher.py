#!/usr/bin/env python3
import math
import random

import rclpy
from rclpy.node import Node
from sensor_msgs.msg import LaserScan


class FakeScanPublisher(Node):

    def __init__(self):
        super().__init__('fake_scan_publisher')

        self.declare_parameter('noise', False)

        self.noise = self.get_parameter('noise').value

        self.publisher = self.create_publisher(
            LaserScan,
            '/scan',
            10
        )

        self.timer = self.create_timer(
            0.1,
            self.publish_scan
        )

    def publish_scan(self):

        msg = LaserScan()

        msg.header.stamp = self.get_clock().now().to_msg()
        msg.header.frame_id = "laser"

        msg.angle_min = -math.pi
        msg.angle_max = math.pi
        msg.angle_increment = math.pi / 180

        msg.range_min = 0.05
        msg.range_max = 12.0

        ranges = []

        for _ in range(360):
            distance = 5.0

            if self.noise:
                distance += random.uniform(-0.05, 0.05)

            ranges.append(distance)

        msg.ranges = ranges

        self.publisher.publish(msg)


def main(args=None):
    rclpy.init(args=args)

    node = FakeScanPublisher()

    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
