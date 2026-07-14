"""
Signal System Node

This node listens for diagnostic messages and converts active faults into
SignalCommand messages.

Fault Clear Policy:
-------------------
The signal is cleared immediately once there are no active faults.
No manual acknowledge is required.

Fail-safe Behaviour:
--------------------
If an unknown/unmapped fault is received, the node enables both siren and
light using the emergency pattern.
"""

import rclpy
from rclpy.node import Node

from diagnostic_msgs.msg import DiagnosticArray
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

        # Default: no fault
        pattern = NO_FAULT_PATTERN
        # Empty diagnostics
        if len(msg.status) == 0:
           command = SignalCommand()

           command.header.stamp = self.get_clock().now().to_msg()
           command.siren_on = NO_FAULT_PATTERN["siren_on"]
           command.light_on = NO_FAULT_PATTERN["light_on"]
           command.pattern_id = NO_FAULT_PATTERN["pattern_id"]

           self.publisher.publish(command)
           return

        active_fault = None

        # Find first active fault
        for status in msg.status:

            if status.level > 0:
                active_fault = status.name
                break

        # No active fault
        if active_fault is None:
            pattern = NO_FAULT_PATTERN

        elif active_fault in FAULT_PATTERN_TABLE:
            pattern = FAULT_PATTERN_TABLE[active_fault]

        else:
            pattern = FAIL_SAFE_PATTERN


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