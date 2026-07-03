"""Robot-wide supervisor: IDLE / NAVIGATING / LIFTING / ERROR state machine.

Aggregates diagnostics from every subsystem (via DiagnosticsAggregator),
decides overall robot state, and triggers amr_error on faults.
"""
import rclpy
from rclpy.node import Node

from amr_engine.diagnostics_aggregator import DiagnosticsAggregator

# TODO: from amr_msgs.srv import GetRobotState, AcknowledgeFault
# TODO: from amr_msgs.action import NavigateToGoal, MoveLift
# TODO: from rclpy.action import ActionServer, ActionClient

IDLE = 'IDLE'
NAVIGATING = 'NAVIGATING'
LIFTING = 'LIFTING'
ERROR = 'ERROR'


class StateMachineNode(Node):
    def __init__(self):
        super().__init__('amr_engine')
        self.diagnostics = DiagnosticsAggregator()
        self.state = IDLE
        # TODO: diagnostic_msgs/DiagnosticArray subscribers from each
        # subsystem, amr_msgs/SignalCommand publisher for fault handoff to
        # amr_error, state transition logic.

        # TODO: implement callbacks/clients and uncomment
        # self.create_service(GetRobotState, 'get_robot_state', self._handle_get_robot_state)
        # self.create_service(AcknowledgeFault, 'acknowledge_fault', self._handle_acknowledge_fault)
        # self._navigate_server = ActionServer(self, NavigateToGoal, 'navigate_to_goal', self._execute_navigate_to_goal)
        # self._move_lift_client = ActionClient(self, MoveLift, 'move_lift')


def main(args=None):
    rclpy.init(args=args)
    node = StateMachineNode()
    try:
        rclpy.spin(node)
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
