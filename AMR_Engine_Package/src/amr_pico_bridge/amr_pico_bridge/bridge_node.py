"""Bridges the Pico serial protocol to ROS2 topics.

Subscribes to command topics from amr_navigation/move, amr_lift, and
amr_error, forwards them to the Pico as protocol_codec messages, and
republishes Pico telemetry (encoder_ticks, lift_state, signal_state,
pico_status, fault_event) as amr_msgs topics.
"""

import time

import rclpy
from rclpy.node import Node
from rclpy.qos import (
    DurabilityPolicy,
    HistoryPolicy,
    QoSProfile,
    ReliabilityPolicy,
)

from amr_msgs.msg import WheelSetpoints, EncoderTicks, PicoStatus
from std_msgs.msg import Bool

from amr_pico_bridge import protocol_codec
from amr_pico_bridge.serial_transport import SerialTransport

# TODO: from amr_msgs.srv import GetPicoStatus


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

        # Set by /estop. This node is the only writer of drive_cmd, so
        # dropping the setpoint here is what makes "stopped" mean stopped
        # regardless of which node upstream is still publishing wheel
        # setpoints -- the gateway can only silence the publishers it knows
        # about.
        self._estopped = False

        # Ticks of _send_heartbeat since the stop was last repeated to the
        # Pico. See the repeat in _send_heartbeat for why it is repeated.
        self._estop_repeat = 0

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

        # Latched, matching amr_command's publisher: a bridge that restarts
        # while the stop is engaged has to come up refusing to drive rather
        # than forwarding the next setpoint that happens to arrive.
        self.create_subscription(
            Bool,
            "/estop",
            self._on_estop,
            QoSProfile(
                depth=1,
                history=HistoryPolicy.KEEP_LAST,
                reliability=ReliabilityPolicy.RELIABLE,
                durability=DurabilityPolicy.TRANSIENT_LOCAL,
            ),
        )

        # TODO: self.create_service(
        #     GetPicoStatus, 'get_pico_status', self._handle_get_pico_status)

        self.heartbeat_timer = self.create_timer(
            0.1,
            self._send_heartbeat,
        )

        self.rx_timer = self.create_timer(
            0.01,
            self._drain_rx,
        )

    def _on_wheel_setpoints(self, msg: WheelSetpoints):

        if self._estopped:
            return

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

        self._link_connected = True

        self._seq += 1

        message = {
            "type": protocol_codec.CMD_HEARTBEAT,
            "seq": self._seq,
            "ts": time.time(),
        }

        self.transport.write(protocol_codec.encode(message))

        # A Pico that reset itself (its hardware WDT fired) comes back with a
        # clear e-stop latch, and nothing else would ever tell it otherwise --
        # /estop is latched on the ROS side, but that only replays to new
        # subscribers, not to a microcontroller that rebooted. So the stop is
        # repeated about once a second for as long as it is engaged, rather
        # than sent once and trusted.
        if self._estopped:

            self._estop_repeat += 1

            if self._estop_repeat >= 10:
                self._estop_repeat = 0
                self._send_estop(True)

    def _on_estop(self, msg: Bool):

        engage = bool(msg.data)

        if engage == self._estopped:
            return

        self._estopped = engage
        self._estop_repeat = 0

        if engage:
            self.get_logger().error(
                "Emergency stop engaged -- drive commands to the Pico are "
                "being dropped"
            )
        else:
            self.get_logger().warning("Emergency stop released")

        self._send_estop(engage)

    def _send_estop(self, engage: bool):

        if not self.transport.connected:
            # Nothing useful to do here. The Pico's own heartbeat watchdog is
            # what covers a dead serial link: no heartbeat reaches it either,
            # so it trips and stops the motors on its own.
            return

        self._seq += 1

        message = {
            "type": protocol_codec.CMD_ESTOP,
            "seq": self._seq,
            "ts": time.time(),
            "engage": engage,
        }

        self.transport.write(protocol_codec.encode(message))

    def _drain_rx(self):
        for line in self.transport.poll_lines():
            self._on_serial_line(line)

    def _on_serial_line(self, line: bytes):
        try:
            message = protocol_codec.decode(line)
        except Exception:
            self.get_logger().warning(
                f"Failed to decode serial line: {line!r}"
            )
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

            required_fields = (
                "left_ticks",
                "right_ticks",
                "dt_ms",
            )

            missing = [
                field for field in required_fields
                if field not in message
            ]

            if missing:
                self.get_logger().warning(
                    f"Encoder telemetry missing fields: {missing}. "
                    f"Message: {message}"
                )
                return

            msg = EncoderTicks()
            msg.left_ticks = message["left_ticks"]
            msg.right_ticks = message["right_ticks"]
            msg.dt_ms = message["dt_ms"]

            self.encoder_pub.publish(msg)

        elif msg_type == protocol_codec.TEL_PICO_STATUS:

            msg = PicoStatus()

            msg.uptime_ms = message.get("uptime_ms", 0)
            msg.last_rpi_msg_age_ms = message.get(
                "last_rpi_msg_age_ms", 0
            )
            msg.watchdog_resets = message.get(
                "watchdog_resets", 0
            )
            msg.free_mem_bytes = message.get(
                "free_mem_bytes", 0
            )

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