import rclpy
from rclpy.node import Node
import math
from amr_msgs.msg import WheelSetpoints, EncoderTicks

WHEEL_RADIUS_M = 0.127
TICKS_PER_REV = 4096


class FakePicoNode(Node):
    def __init__(self):
        super().__init__("fake_pico_node")
        # Latest wheel speeds (m/s)
        self.left_speed = 0.0
        self.right_speed = 0.0

        # Running encoder tick counts
        self.left_ticks = 0
        self.right_ticks = 0

        # Publisher
        self.encoder_pub = self.create_publisher(
            EncoderTicks,
            "/encoder_ticks",
            10,
        )

        # Subscriber
        self.create_subscription(
            WheelSetpoints,
            "/wheel_setpoints",
            self._on_wheel_setpoints,
            10,
        )

        # 50 ms update loop
        self.timer = self.create_timer(
            0.05,
            self._timer_callback,
        )

    def _on_wheel_setpoints(self, msg: WheelSetpoints):
        """Store the latest wheel speed commands."""

        self.left_speed = msg.left_speed
        self.right_speed = msg.right_speed

    def _timer_callback(self):
        dt = 0.05

        # Distance travelled by each wheel
        left_distance = self.left_speed * dt
        right_distance = self.right_speed * dt

        wheel_circumference = 2 * math.pi * WHEEL_RADIUS_M

        # Convert distance to encoder tick increments
        left_delta_ticks = int(
            (left_distance / wheel_circumference) * TICKS_PER_REV
        )
        right_delta_ticks = int(
            (right_distance / wheel_circumference) * TICKS_PER_REV
        )

        # Accumulate absolute encoder ticks
        self.left_ticks += left_delta_ticks
        self.right_ticks += right_delta_ticks

        # Publish encoder message
        msg = EncoderTicks()
        msg.left_ticks = self.left_ticks
        msg.right_ticks = self.right_ticks
        msg.dt_ms = 50

        self.encoder_pub.publish(msg)

    
def main(args=None):
    rclpy.init(args=args)

    node = FakePicoNode()

    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()


if __name__ == "__main__":
    main()