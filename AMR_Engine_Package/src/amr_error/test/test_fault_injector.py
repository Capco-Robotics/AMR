import rclpy

from diagnostic_msgs.msg import DiagnosticArray, DiagnosticStatus

from amr_error.signal_system_node import SignalSystemNode


class FakePublisher:
    def __init__(self):
        self.last_msg = None

    def publish(self, msg):
        self.last_msg = msg


def create_status(name, level):
    status = DiagnosticStatus()
    status.name = name
    status.level = level
    return status


def setup_node():
    rclpy.init()

    node = SignalSystemNode()

    fake_pub = FakePublisher()
    node.publisher = fake_pub

    return node, fake_pub


def teardown_node(node):
    node.destroy_node()
    rclpy.shutdown()


def test_no_fault():

    node, pub = setup_node()

    msg = DiagnosticArray()
    msg.status = []

    node.diagnostic_callback(msg)

    assert pub.last_msg.siren_on is False
    assert pub.last_msg.light_on is False
    assert pub.last_msg.pattern_id == 0

    teardown_node(node)


def test_motor_fault():

    node, pub = setup_node()

    msg = DiagnosticArray()
    msg.status = [
        create_status("MOTOR_FAULT", DiagnosticStatus.ERROR)
    ]

    node.diagnostic_callback(msg)

    assert pub.last_msg.siren_on is True
    assert pub.last_msg.light_on is True
    assert pub.last_msg.pattern_id == 1

    teardown_node(node)


def test_battery_low():

    node, pub = setup_node()

    msg = DiagnosticArray()
    msg.status = [
        create_status("BATTERY_LOW", DiagnosticStatus.WARN)
    ]

    node.diagnostic_callback(msg)

    assert pub.last_msg.siren_on is False
    assert pub.last_msg.light_on is True
    assert pub.last_msg.pattern_id == 2

    teardown_node(node)


def test_emergency_stop():

    node, pub = setup_node()

    msg = DiagnosticArray()
    msg.status = [
        create_status("EMERGENCY_STOP", DiagnosticStatus.ERROR)
    ]

    node.diagnostic_callback(msg)

    assert pub.last_msg.siren_on is True
    assert pub.last_msg.light_on is True
    assert pub.last_msg.pattern_id == 3

    teardown_node(node)


def test_unknown_fault():

    node, pub = setup_node()

    msg = DiagnosticArray()
    msg.status = [
        create_status("SOME_NEW_FAULT", DiagnosticStatus.ERROR)
    ]

    node.diagnostic_callback(msg)

    assert pub.last_msg.siren_on is True
    assert pub.last_msg.light_on is True
    assert pub.last_msg.pattern_id == 3

    teardown_node(node)