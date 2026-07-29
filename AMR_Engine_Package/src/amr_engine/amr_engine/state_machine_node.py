"""Robot-wide supervisor state machine."""

import rclpy

from rclpy.node import Node
from rclpy.action import ActionClient
from rclpy.qos import qos_profile_action_status_default
from action_msgs.msg import GoalStatusArray

from std_msgs.msg import String
from diagnostic_msgs.msg import DiagnosticArray, DiagnosticStatus

from amr_msgs.action import MoveLift
from amr_msgs.msg import LiftState
from amr_msgs.srv import GetRobotState, AcknowledgeFault

from amr_engine.diagnostics_aggregator import DiagnosticsAggregator


IDLE = "IDLE"
NAVIGATING = "NAVIGATING"
LIFTING = "LIFTING"
ERROR = "ERROR"


class StateMachineNode(Node):

    def __init__(self):
        super().__init__("amr_engine")

        self.state = IDLE
        self.fault_latched = False

        self.diagnostics = DiagnosticsAggregator()

        self.lift_goal_handle = None

        # Publishers
        self.state_pub = self.create_publisher(
            String,
            "/robot_state",
            10,
        )

        # Subscribers
        self.create_subscription(
            DiagnosticArray,
            "/diagnostics",
            self._diagnostics_callback,
            10,
        )

        self.create_subscription(
            LiftState,
            "/lift_state",
            self._lift_state_callback,
            10,
        )
        self.create_subscription(
            GoalStatusArray,
            "/move_lift/_action/status",
            self._lift_status_callback,
            qos_profile_action_status_default,
        )

        # Action Client
        self.move_lift_client = ActionClient(
            self,
            MoveLift,
            "/move_lift",
        )

        # Services
        self.create_service(
            GetRobotState,
            "/get_robot_state",
            self._handle_get_robot_state,
        )

        self.create_service(
            AcknowledgeFault,
            "/acknowledge_fault",
            self._handle_acknowledge_fault,
        )

        self.timer = self.create_timer(
            1.0,
            self._publish_state,
        )

        self.get_logger().info("State Machine Node Started")

    def _publish_state(self):

        if self.diagnostics.has_active_fault():
            self.state = ERROR
            self.fault_latched = True

        msg = String()
        msg.data = self.state
        self.state_pub.publish(msg)

    def _diagnostics_callback(self, msg):

        self.diagnostics.update(
            "diagnostics",
            msg,
        )

        if self.diagnostics.has_active_fault():
            self.state = ERROR
            self.fault_latched = True

    def _lift_state_callback(self, msg):
        pass

    def _lift_status_callback(self, msg):

        if not msg.status_list:
            return

        status = msg.status_list[-1].status

        if status in (
            1,  # ACCEPTED
            2,  # EXECUTING
        ):
            if not self.fault_latched:
                self.state = LIFTING

        elif status == 4:  # SUCCEEDED
            if not self.fault_latched:
                self.state = IDLE

        elif status == 5:  # CANCELED
            if not self.fault_latched:
                self.state = IDLE

        elif status == 6:  # ABORTED
            self.state = ERROR
            self.fault_latched = True

    def send_lift_goal(self, target):

        if self.fault_latched:
            self.get_logger().warn(
                "Cannot lift, robot in ERROR state"
            )
            return

        if not self.move_lift_client.wait_for_server(
            timeout_sec=2.0
        ):
            self.get_logger().error(
                "MoveLift action server not available"
            )
            return

        goal = MoveLift.Goal()
        goal.target_position = target

        

        future = self.move_lift_client.send_goal_async(
            goal,
        )

        future.add_done_callback(
            self._lift_goal_response_callback
        )

    def _lift_goal_response_callback(self, future):

        self.lift_goal_handle = future.result()

        if not self.lift_goal_handle.accepted:
            self.state = ERROR
            self.fault_latched = True
            return

        result_future = (
            self.lift_goal_handle.get_result_async()
        )

        result_future.add_done_callback(
            self._lift_result_callback
        )

    def _lift_result_callback(self, future):

        result = future.result().result

        if result.success:
            self.state = IDLE
        else:
            self.state = ERROR
            self.fault_latched = True

    def _handle_get_robot_state(
        self,
        request,
        response,
    ):
        response.state = self.state

        response.active_faults = list(
            self.diagnostics._latest_by_source.keys()
        )

        return response

    def _handle_acknowledge_fault(
        self,
        request,
        response,
    ):

        self.fault_latched = False
        self.state = IDLE

        response.success = True

        return response


def main(args=None):

    rclpy.init(args=args)

    node = StateMachineNode()

    try:
        rclpy.spin(node)

    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == "__main__":
    main()