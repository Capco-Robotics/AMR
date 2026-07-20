import math
import random

import rclpy
from rclpy.node import Node

from sensor_msgs.msg import LaserScan


class FakeScanPublisher(Node):

    def __init__(self):
        super().__init__("fake_scan_publisher")

        self.publisher = self.create_publisher(
            LaserScan,
            "/scan",
            10,
        )

        self.timer = self.create_timer(0.1, self.publish_scan)

        self.get_logger().info("Fake Scan Publisher Started")

    def publish_scan(self):
        scan = LaserScan()

        now = self.get_clock().now().to_msg()

        scan.header.stamp = now
        scan.header.frame_id = "laser_front_left"

        scan.angle_min = -math.pi
        scan.angle_max = math.pi
        scan.angle_increment = math.radians(1.0)

        scan.time_increment = 0.0
        scan.scan_time = 0.1

        scan.range_min = 0.10
        scan.range_max = 4.00

        num_readings = int(
            (scan.angle_max - scan.angle_min) / scan.angle_increment
        ) + 1

        ranges = []

        for i in range(num_readings):

            angle = scan.angle_min + i * scan.angle_increment

            cos_a = math.cos(angle)
            sin_a = math.sin(angle)

            distances = []

            if cos_a > 0:
                distances.append(2.0 / cos_a)
            elif cos_a < 0:
                distances.append(-2.0 / cos_a)

            if sin_a > 0:
                distances.append(2.0 / sin_a)
            elif sin_a < 0:
                distances.append(-2.0 / sin_a)

            distance = min(distances)

            distance += random.gauss(0.0, 0.02)
            distance = max(scan.range_min, min(distance, scan.range_max))

            r = random.random()

            if r < 0.01:
                distance = float("nan")
            elif r < 0.03:
                distance = scan.range_max

            ranges.append(distance)

        scan.ranges = ranges
        scan.intensities = [100.0] * num_readings

        self.publisher.publish(scan)


def main(args=None):
    rclpy.init(args=args)

    node = FakeScanPublisher()

    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()


if __name__ == "__main__":
    main()