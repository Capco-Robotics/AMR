import math

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
        scan.header.frame_id = "laser"

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

        scan.ranges = [2.0] * num_readings
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