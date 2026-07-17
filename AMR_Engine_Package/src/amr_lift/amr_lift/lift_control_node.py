"""Decides the lift's target height and tracks its reported state.

Publishes amr_msgs/LiftCommand to amr_pico_bridge and subscribes to
amr_msgs/LiftState for the Pico's closed-loop position/limit-switch feedback.
"""

import time

import rclpy
from rclpy.action import ActionServer, CancelResponse
from rclpy.node import Node
from rclpy.callback_groups import ReentrantCallbackGroup

from rclpy.executors import MultiThreadedExecutor


from amr_msgs.action import MoveLift
from amr_msgs.msg import LiftCommand, LiftState
from amr_msgs.srv import SetLiftTarget


class LiftControlNode(Node):

    def __init__(self):
        super().__init__("amr_lift")

        self.callback_group = ReentrantCallbackGroup()
        self.MAX_POSITION = 1.0

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
            callback_group=self.callback_group,
        )

        # Service
        self.create_service(
            SetLiftTarget,
            "set_lift_target",
            self._handle_set_lift_target,
            callback_group=self.callback_group,
        )

        # Action Server
        self._move_lift_server = ActionServer(
            self,
            MoveLift,
            "move_lift",
            self._execute_move_lift,
            callback_group=self.callback_group,
            cancel_callback=self._cancel_callback,
        )

        self.get_logger().info("Lift Control Node Started")

    def _lift_state_callback(self, msg):
        self.current_position = msg.position
        self.limit_upper = msg.limit_upper
        self.limit_lower = msg.limit_lower

    def _handle_set_lift_target(self, request, response):

        if request.target_position < 0.0 or request.target_position > self.MAX_POSITION:
            self.get_logger().warn(
                f"Invalid target: {request.target_position:.2f}"
            )

            response.accepted = False
            return response

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

        if target < 0.0 or target > self.MAX_POSITION:
            self.get_logger().error(
                f"Invalid target position: {target:.2f}"
            )

            goal_handle.abort()

            result = MoveLift.Result()
            result.success = False
            result.final_position = self.current_position

            return result

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
        start_time = time.time()
        TIMEOUT = 10.0

        rate = self.create_rate(10)
        while abs(self.current_position - target) > 0.01:

            if time.time() - start_time > TIMEOUT:
                self.get_logger().error("Lift movement timed out")
                goal_handle.abort()

                result = MoveLift.Result()
                result.success = False
                result.final_position = self.current_position
                return result
            
            if self.limit_upper and target >= self.MAX_POSITION:
                self.get_logger().warn("Upper limit reached")
                goal_handle.abort()

                result = MoveLift.Result()
                result.success = False
                result.final_position = self.current_position
                return result

            if self.limit_lower and target <= 0.0:
                self.get_logger().warn("Lower limit reached")
                goal_handle.abort()

                result = MoveLift.Result()
                result.success = False
                result.final_position = self.current_position
                return result

            if goal_handle.is_cancel_requested:
                goal_handle.canceled()

                result = MoveLift.Result()
                result.success = False
                result.final_position = self.current_position

                return result

            self.get_logger().debug(
                f"Current Position={self.current_position:.2f}, Target={target:.2f}"
            )

            feedback.current_position = self.current_position
            feedback.limit_upper = self.limit_upper
            feedback.limit_lower = self.limit_lower

            goal_handle.publish_feedback(feedback)

            rate.sleep()

        goal_handle.succeed()

        result = MoveLift.Result()
        result.success = True
        result.final_position = self.current_position

        return result
    
    def _cancel_callback(self, cancel_request):
        self.get_logger().info("Cancel request received")
        return CancelResponse.ACCEPT

def main(args=None):
    rclpy.init(args=args)

    node = LiftControlNode()

    executor = MultiThreadedExecutor()
    executor.add_node(node)

    try:
        executor.spin()
    except KeyboardInterrupt:
        pass
    finally:
        executor.shutdown()
        node.destroy_node()
        rclpy.shutdown()