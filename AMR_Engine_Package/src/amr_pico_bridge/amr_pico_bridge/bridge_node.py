"""Bridges the Pico serial protocol to ROS2 topics.

Subscribes to command topics from amr_navigation/move, amr_lift, and
amr_error, forwards them to the Pico as protocol_codec messages, and
republishes Pico telemetry (encoder_ticks, lift_state, signal_state,
pico_status, fault_event) as amr_msgs topics.
"""
import rclpy
from rclpy.node import Node

from amr_pico_bridge import protocol_codec
from amr_pico_bridge.serial_transport import SerialTransport


class PicoBridgeNode(Node):
    def __init__(self):
        super().__init__('amr_pico_bridge')
        self.declare_parameter('serial_port', '/dev/ttyACM0')
        self.declare_parameter('baudrate', 115200)
        self.transport = SerialTransport(
            self.get_parameter('serial_port').value,
            self.get_parameter('baudrate').value,
        )
        # TODO: wire up amr_msgs publishers/subscribers and the
        # heartbeat timer once the transport is implemented.


def main(args=None):
    rclpy.init(args=args)
    node = PicoBridgeNode()
    try:
        rclpy.spin(node)
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
