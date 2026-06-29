"""Polls the BMS over its own UART/I2C link and publishes sensor_msgs/BatteryState."""
import rclpy
from rclpy.node import Node


class BmsNode(Node):
    def __init__(self):
        super().__init__('amr_charging')
        # TODO: open BMS link (separate from the Pico serial port), poll via
        # bms_protocol, publish sensor_msgs/BatteryState and low-battery/fault events.


def main(args=None):
    rclpy.init(args=args)
    node = BmsNode()
    try:
        rclpy.spin(node)
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
