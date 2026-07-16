import rclpy
from rclpy.node import Node
from diagnostic_msgs.msg import DiagnosticArray
from diagnostic_msgs.msg import DiagnosticStatus
from amr_msgs.msg import SignalCommand

from .fault_pattern_table import (
    FAULT_PATTERN_TABLE,
    NO_FAULT_PATTERN,
    FAIL_SAFE_PATTERN,
)


class SignalSystemNode(Node):

    def __init__(self):
        super().__init__("amr_error")

        # Publisher
        self.publisher = self.create_publisher(
            SignalCommand,
            "/signal_command",
            10,
        )

        # Subscriber
        self.subscription = self.create_subscription(
            DiagnosticArray,
            "/diagnostics",
            self.diagnostic_callback,
            10,
        )

        self.get_logger().info("Signal System Node Started")

    def diagnostic_callback(self, msg):

        # Default pattern
        pattern = NO_FAULT_PATTERN
        active_fault = None

        # Emergency Stop always has highest priority
        for status in msg.status:
            if (
                status.level != DiagnosticStatus.OK
                and status.name == "EMERGENCY_STOP"
            ):
                active_fault = status.name
                break

        # Otherwise choose the first active fault
        if active_fault is None:
            for status in msg.status:
                if status.level != DiagnosticStatus.OK:
                    active_fault = status.name
                    break

        # Select signal pattern
        if active_fault is None:
            pattern = NO_FAULT_PATTERN

        elif active_fault in FAULT_PATTERN_TABLE:
            pattern = FAULT_PATTERN_TABLE[active_fault]

        else:
            pattern = FAIL_SAFE_PATTERN

        # Publish signal command
        command = SignalCommand()
        command.header.stamp = self.get_clock().now().to_msg()
        command.siren_on = pattern["siren_on"]
        command.light_on = pattern["light_on"]
        command.pattern_id = pattern["pattern_id"]

        self.publisher.publish(command)


def main(args=None):
    rclpy.init(args=args)

    node = SignalSystemNode()

    try:
        rclpy.spin(node)
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == "__main__":
    main()