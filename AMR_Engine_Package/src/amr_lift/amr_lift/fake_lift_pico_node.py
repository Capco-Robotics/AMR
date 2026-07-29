import rclpy
from rclpy.node import Node

from amr_msgs.msg import LiftCommand, LiftState


class FakeLiftPicoNode(Node):

    def __init__(self):
        super().__init__("fake_lift_pico")

        # Placeholder travel range
        self.min_position = 0.0
        self.declare_parameter(
            "max_position",
            1.0
        )

        self.max_position = (
            self.get_parameter(
                "max_position"
            ).value
        )

        self.current_position = 0.0
        self.target_position = 0.0

        # Dual actuators
        self.actuator_position = [0.0, 0.0]
        self.actuator_current = [0.0, 0.0]

        # Simulation parameters
        self.declare_parameter("load", 0.0)
        self.declare_parameter("stall", False)
        self.declare_parameter("slant_bias", 0.0)
        self.declare_parameter("slant_tolerance", 0.05)
        self.declare_parameter("nominal_rate", 0.02)
        self.declare_parameter("idle_current", 0.2)
        self.declare_parameter("moving_current", 1.0)
        self.declare_parameter("stall_current", 8.0)


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

        load = self.get_parameter("load").value
        stall = self.get_parameter("stall").value
        slant_bias = self.get_parameter("slant_bias").value
        step = self.get_parameter("nominal_rate").value
        idle_current = self.get_parameter("idle_current").value
        moving_current = self.get_parameter("moving_current").value
        stall_current = self.get_parameter("stall_current").value

        for i in range(2):

            target = self.target_position

            if i == 1:
                target += slant_bias

            target = max(
                self.min_position,
                min(target, self.max_position)
            )

            if not stall:

                if self.actuator_position[i] < target:
                    self.actuator_position[i] = min(
                        self.actuator_position[i] + step,
                        target
                    )

                elif self.actuator_position[i] > target:
                    self.actuator_position[i] = max(
                        self.actuator_position[i] - step,
                        target
                    )

        self.current_position = (
            self.actuator_position[0]
            + self.actuator_position[1]
        ) / 2.0

        for i in range(2):

            moving = abs(
                self.actuator_position[i] - self.target_position
            ) > 0.001

            current = idle_current

            if moving:
                current = moving_current + load

            if stall:
                current = stall_current

            at_lower = (
                self.actuator_position[i] <= self.min_position
            )

            at_upper = (
                self.actuator_position[i] >= self.max_position
            )

            trying_up = target > self.actuator_position[i]

            trying_down = target < self.actuator_position[i]

            if stall:
                current = stall_current

            elif (trying_up and at_upper) or (
                trying_down and at_lower
            ):
                current = stall_current

            elif moving:
                current = moving_current + load

            else:
                current = idle_current

            self.actuator_current[i] = current

        slant = abs(
            self.actuator_position[0]
            - self.actuator_position[1]
        )

        level_fault = (
            slant >
            self.get_parameter(
                "slant_tolerance"
            ).value
        )           

        state = LiftState()

        state.position = self.current_position

        state.limit_lower = (
            self.current_position <= self.min_position
        )

        state.limit_upper = (
            self.current_position >= self.max_position
        )

        state.actuator_position = self.actuator_position

        state.actuator_current = self.actuator_current

        state.level_fault = level_fault

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