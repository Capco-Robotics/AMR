import rclpy
from rclpy.node import Node

from amr_msgs.msg import LiftCommand, LiftState


class FakeLiftPicoNode(Node):

    def __init__(self):
        super().__init__("fake_lift_pico")

        # Placeholder travel range
        self.min_position = 0.0
        self.max_position = 1.0

        self.current_position = 0.0
        self.target_position = 0.0

        # Receive lift commands
        self.command_sub = self.create_subscription(
            LiftCommand,
            "lift_command",
            self.command_callback,
            10
        )

        # Publish lift state
        self.state_pub = self.create_publisher(
            LiftState,
            "lift_state",
            10
        )

        # Update at 10 Hz
        self.timer = self.create_timer(
            0.1,
            self.update_lift
        )

    def command_callback(self, msg):
        self.target_position = max(
            self.min_position,
            min(msg.target_position, self.max_position)
        )

    def update_lift(self):

        step = 0.02

        if self.current_position < self.target_position:
            self.current_position = min(
                self.current_position + step,
                self.target_position
            )

        elif self.current_position > self.target_position:
            self.current_position = max(
                self.current_position - step,
                self.target_position
            )

        state = LiftState()

        state.position = self.current_position

        state.limit_lower = (
            self.current_position <= self.min_position
        )

        state.limit_upper = (
            self.current_position >= self.max_position
        )

        self.state_pub.publish(state)


def main(args=None):
    rclpy.init(args=args)

    node = FakeLiftPicoNode()

    try:
        rclpy.spin(node)
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == "__main__":
    main()