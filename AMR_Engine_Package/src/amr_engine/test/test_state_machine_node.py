import pytest

import rclpy

from diagnostic_msgs.msg import DiagnosticArray, DiagnosticStatus

from amr_engine.state_machine_node import (
    StateMachineNode,
    IDLE,
    ERROR,
)


def create_fault(name):
    status = DiagnosticStatus()
    status.name = name
    status.level = DiagnosticStatus.ERROR

    msg = DiagnosticArray()
    msg.status = [status]

    return msg


@pytest.fixture
def node():
    rclpy.init()

    node = StateMachineNode()

    yield node

    node.destroy_node()
    rclpy.shutdown()


def test_initial_state(node):
    assert node.state == IDLE


def test_fault_moves_to_error(node):

    msg = create_fault("MOTOR_FAULT")

    node._diagnostics_callback(msg)

    assert node.state == ERROR
    assert node.fault_latched is True


def test_error_latch_acknowledge(node):

    msg = create_fault("BATTERY_FAULT")

    node._diagnostics_callback(msg)

    assert node.state == ERROR

    response = type("Response", (), {})()
    response.success = False

    node._handle_acknowledge_fault(
        None,
        response,
    )

    assert node.state == IDLE
    assert node.fault_latched is False