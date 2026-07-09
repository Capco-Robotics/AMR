"""Bridges the Pico serial protocol to ROS2 topics.

Subscribes to command topics from amr_navigation/move, amr_lift, and
amr_error, forwards them to the Pico as protocol_codec messages, and
republishes Pico telemetry (encoder_ticks, lift_state, signal_state,
pico_status, fault_event) as amr_msgs topics.
"""
import time

import rclpy
from rclpy.node import Node

from amr_msgs.msg import WheelSetpoints, EncoderTicks, PicoStatus

from amr_pico_bridge import protocol_codec
from amr_pico_bridge.serial_transport import SerialTransport

# TODO: from amr_msgs.srv import GetPicoStatus, TriggerEstop


class PicoBridgeNode(Node):
    def __init__(self):
        super().__init__('amr_pico_bridge')
        self.declare_parameter('serial_port', '/dev/ttyACM0')
        self.declare_parameter('baudrate', 115200)
        self.transport = SerialTransport(
            self.get_parameter('serial_port').value,
            self.get_parameter('baudrate').value,
        )
        self.transport.open()
        self._seq = 0
        self._rx_seq = None
        self._link_connected = True

        self.encoder_pub = self.create_publisher(
            EncoderTicks,
            "/encoder_ticks",
            10,
        )

        self.status_pub = self.create_publisher(
            PicoStatus,
            "/pico_status",
            10,
        )

        self.create_subscription(
            WheelSetpoints,
            "/wheel_setpoints",
            self._on_wheel_setpoints,
            10,
        )

        self.heartbeat_timer = self.create_timer(
            0.1,
            self._send_heartbeat,
        )

        self.rx_timer = self.create_timer(
            0.01,
            self._drain_rx,
        )

    def _on_wheel_setpoints(self, msg: WheelSetpoints):
        self._seq += 1

        message = {
            "type": protocol_codec.CMD_DRIVE,
            "seq": self._seq,
            "ts": time.time(),
            "left": max(-1.0, min(1.0, msg.left_speed)),
            "right": max(-1.0, min(1.0, msg.right_speed)),
        }

        self.transport.write(protocol_codec.encode(message))

    def _send_heartbeat(self):
        if not self.transport.connected:
            if self._link_connected:
                self.get_logger().error(
                    f"Serial link to Pico lost: {self.transport.last_error}"
                )
                self._link_connected = False
            return

        self._seq += 1

        message = {
            "type": protocol_codec.CMD_HEARTBEAT,
            "seq": self._seq,
            "ts": time.time(),
        }

        self.transport.write(protocol_codec.encode(message))
        # TODO: implement callbacks and uncomment
        # self.create_service(GetPicoStatus, 'get_pico_status', self._handle_get_pico_status)
        # self.create_service(TriggerEstop, 'trigger_estop', self._handle_trigger_estop)

    def _drain_rx(self):
        for line in self.transport.poll_lines():
            self._on_serial_line(line)

    def _on_serial_line(self, line: bytes):
        try:
            message = protocol_codec.decode(line)
        except Exception:
            self.get_logger().warning(f"Failed to decode serial line: {line!r}")
            return

        seq = message.get("seq")

        if seq is not None:
            if self._rx_seq is not None and seq != self._rx_seq + 1:
                self.get_logger().warning(
                    f"Gap in Pico seq: expected {self._rx_seq + 1}, got {seq}"
                )

            self._rx_seq = seq

        msg_type = message.get("type")

        if msg_type == protocol_codec.TEL_ENCODER_TICKS:
            msg = EncoderTicks()
            msg.left_ticks = message.get("left_ticks", 0)
            msg.right_ticks = message.get("right_ticks", 0)
            msg.dt_ms = message.get("dt_ms", 0)

            self.encoder_pub.publish(msg)
        elif msg_type == protocol_codec.TEL_PICO_STATUS:
            msg = PicoStatus()
            msg.uptime_ms = message.get("uptime_ms", 0)
            msg.last_rpi_msg_age_ms = message.get("last_rpi_msg_age_ms", 0)
            msg.watchdog_resets = message.get("watchdog_resets", 0)
            msg.free_mem_bytes = message.get("free_mem_bytes", 0)

            self.status_pub.publish(msg)


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
