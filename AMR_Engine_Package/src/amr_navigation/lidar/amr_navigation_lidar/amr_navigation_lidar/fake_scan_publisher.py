import math
import random

import rclpy
from rclpy.node import Node

from sensor_msgs.msg import LaserScan


class FakeScanPublisher(Node):

    def __init__(self):
        super().__init__("fake_scan_publisher")

        self.declare_parameter("scan_topic", "/scan")
        self.declare_parameter("frame_id", "laser_front_left")
        self.declare_parameter("mount_x", 0.0)
        self.declare_parameter("mount_y", 0.0)
        self.declare_parameter("mount_yaw", 0.0)

        self.scan_topic = self.get_parameter("scan_topic").value
        self.frame_id = self.get_parameter("frame_id").value
        self.mount_x = self.get_parameter("mount_x").value
        self.mount_y = self.get_parameter("mount_y").value
        self.mount_yaw = self.get_parameter("mount_yaw").value

        self.publisher = self.create_publisher(
            LaserScan,
            self.scan_topic,
            10,
        )

        self.timer = self.create_timer(0.1, self.publish_scan)

        self.get_logger().info(
            f"Fake Scan Publisher Started (scan_topic={self.scan_topic}, "
            f"frame_id={self.frame_id}, mount=({self.mount_x}, {self.mount_y}, {self.mount_yaw}))"
        )

    def publish_scan(self):
        scan = LaserScan()

        now = self.get_clock().now().to_msg()

        scan.header.stamp = now
        scan.header.frame_id = self.frame_id

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
            world_angle = angle + self.mount_yaw

            cos_a = math.cos(world_angle)
            sin_a = math.sin(world_angle)

            distances = []

            if cos_a > 0:
                distances.append((2.0 - self.mount_x) / cos_a)
            elif cos_a < 0:
                distances.append((-2.0 - self.mount_x) / cos_a)

            if sin_a > 0:
                distances.append((2.0 - self.mount_y) / sin_a)
            elif sin_a < 0:
                distances.append((-2.0 - self.mount_y) / sin_a)

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