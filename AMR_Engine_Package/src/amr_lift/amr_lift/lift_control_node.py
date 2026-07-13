"""Decides the lift's target height and tracks its reported state.

Publishes amr_msgs/LiftCommand to amr_pico_bridge and subscribes to
amr_msgs/LiftState for the Pico's closed-loop position/limit-switch feedback.
"""

import time

import rclpy
from rclpy.action import ActionServer
from rclpy.node import Node

from amr_msgs.action import MoveLift
from amr_msgs.msg import LiftCommand, LiftState
from amr_msgs.srv import SetLiftTarget


class LiftControlNode(Node):

    def __init__(self):
        super().__init__("amr_lift")

        # Current lift state
        self.current_position = 0.0
        self.limit_upper = False
        self.limit_lower = False

        # Publisher
        self.command_pub = self.create_publisher(
            LiftCommand,
            "lift_command",
            10,
        )

        # Subscriber
        self.state_sub = self.create_subscription(
            LiftState,
            "lift_state",
            self._lift_state_callback,
            10,
        )

        # Service
        self.create_service(
            SetLiftTarget,
            "set_lift_target",
            self._handle_set_lift_target,
        )

        # Action Server
        self._move_lift_server = ActionServer(
            self,
            MoveLift,
            "move_lift",
            self._execute_move_lift,
        )

        self.get_logger().info("Lift Control Node Started")

    def _lift_state_callback(self, msg):
        self.current_position = msg.position
        self.limit_upper = msg.limit_upper
        self.limit_lower = msg.limit_lower

    def _handle_set_lift_target(self, request, response):
        command = LiftCommand()
        command.target_position = request.target_position

        self.command_pub.publish(command)

        self.get_logger().info(
            f"Service request: target={request.target_position:.2f}"
        )

        response.accepted = True
        return response

    def _execute_move_lift(self, goal_handle):

        target = goal_handle.request.target_position
        self.get_logger().info(
            f"Execute callback started. Target={target:.2f}"
        )

        command = LiftCommand()
        command.target_position = target
        self.command_pub.publish(command)

        self.get_logger().info(
            f"Action goal received: target={target:.2f}"
        )

        feedback = MoveLift.Feedback()

        while abs(self.current_position - target) > 0.01:
            
            self.get_logger().info(
                f"Current Position={self.current_position:.2f}, Target={target:.2f}"
            )

            feedback.current_position = self.current_position
            feedback.limit_upper = self.limit_upper
            feedback.limit_lower = self.limit_lower

            goal_handle.publish_feedback(feedback)

            time.sleep(0.1)

        goal_handle.succeed()

        result = MoveLift.Result()
        result.success = True
        result.final_position = self.current_position

        return result


def main(args=None):
    rclpy.init(args=args)

    node = LiftControlNode()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == "__main__":
    main()