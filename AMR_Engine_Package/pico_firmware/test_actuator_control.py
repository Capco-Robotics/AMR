import threading
import types
import sys


class FakePWM:
    def __init__(self, pin):
        self.pin = pin
        self.frequency = 0
        self.duty = 0

    def freq(self, value):
        self.frequency = value

    def duty_u16(self, value):
        self.duty = value


class FakePin:
    OUT = 0
    IN = 1

    def __init__(self, *args, **kwargs):
        self._value = 0

    def value(self, value=None):
        if value is None:
            return self._value

        self._value = value


class FakeADC:
    def __init__(self, *args, **kwargs):
        self._value = 0

    def read_u16(self):
        return self._value


fake_machine = types.SimpleNamespace(
    PWM=FakePWM,
    Pin=FakePin,
    ADC=FakeADC,
)

sys.modules["machine"] = fake_machine


class FakeThreadModule:
    @staticmethod
    def allocate_lock():
        return threading.Lock()

    @staticmethod
    def start_new_thread(function, args):
        function(*args)


sys.modules["_thread"] = FakeThreadModule


class FakeTimeModule:
    @staticmethod
    def ticks_ms():
        return 0

    @staticmethod
    def ticks_diff(a, b):
        return a - b

    @staticmethod
    def sleep_ms(value):
        pass


sys.modules["time"] = FakeTimeModule

import time

import actuator_control


def test_import():
    controller = actuator_control.ActuatorControl()

    assert controller is not None
    assert controller.target_position is None


def test_set_target():
    controller = actuator_control.ActuatorControl()

    controller.set_target(0.75)

    assert controller.target_position == 0.75


def test_get_state():
    controller = actuator_control.ActuatorControl()

    state = controller.get_state()

    assert "position" in state
    assert "actuator_position" in state
    assert "actuator_current" in state
    assert "limit_upper" in state
    assert "limit_lower" in state
    assert "level_fault" in state


def test_stop():
    controller = actuator_control.ActuatorControl()

    controller.pwm.duty_u16(5000)
    controller.stop()

    assert controller.pwm.duty == 0
