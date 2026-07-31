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
        return int(simulated_actuator.position * 65535)


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
        return simulation.current_time_ms

    @staticmethod
    def ticks_diff(a, b):
        return a - b

    @staticmethod
    def sleep_ms(value):
        simulation.current_time_ms += value
        simulation.iteration += 1

        if hasattr(actuator_control, "ActuatorControl"):
            controller = getattr(
                actuator_control,
                "_active_controller",
                None,
            )

            if controller is not None:
                simulated_actuator.step(
                    controller.pwm,
                    controller.direction,
                )

        if (
            simulation.max_iterations
            and simulation.iteration >= simulation.max_iterations
        ):
            raise LoopExit()


sys.modules["time"] = FakeTimeModule


import time


class LoopExit(Exception):
    pass


class SimulationState:
    def __init__(self):
        self.position = 0.0
        self.current_time_ms = 0
        self.max_iterations = 0
        self.iteration = 0

    def reset(self):
        self.position = 0.0
        self.current_time_ms = 0
        self.iteration = 0
        self.max_iterations = 0


simulation = SimulationState()


class SimulatedActuator:
    def step(self, pwm, direction):
        velocity = pwm.duty / 65535.0

        if direction.value():
            self.position += velocity * 0.02
        else:
            self.position -= velocity * 0.02

        self.position = max(0.0, min(1.0, self.position))

    @property
    def position(self):
        return simulation.position

    @position.setter
    def position(self, value):
        simulation.position = value


simulated_actuator = SimulatedActuator()


import actuator_control


def make_controller():
    simulation.reset()

    controller = actuator_control.ActuatorControl()

    actuator_control._active_controller = controller

    return controller


def test_import():
    controller = make_controller()

    assert controller is not None
    assert controller.target_position is None


def test_set_target():
    controller = make_controller()

    controller.set_target(0.75)

    assert controller.target_position == 0.75


def test_get_state():
    controller = make_controller()

    state = controller.get_state()

    assert "position" in state
    assert "actuator_position" in state
    assert "actuator_current" in state
    assert "limit_upper" in state
    assert "limit_lower" in state
    assert "level_fault" in state


def test_stop():
    controller = make_controller()

    controller.pwm.duty_u16(5000)

    controller.stop()

    assert controller.pwm.duty == 0


def test_pid_converges_to_target():
    controller = make_controller()

    simulation.max_iterations = 200

    controller.set_target(0.75)

    try:
        controller._pid_loop()
    except LoopExit:
        pass

    assert abs(simulated_actuator.position - 0.75) < 0.05
    assert abs(controller.current_position - 0.75) < 0.05


def run_pid_for_iterations(controller, iterations):
    simulation.max_iterations = iterations

    try:
        controller._pid_loop()
    except LoopExit:
        pass


def test_upper_limit_switch_latch_behavior():
    controller = make_controller()

    simulated_actuator.position = 0.8

    controller.set_target(0.9)

    controller.upper_limit_switch.value(1)

    run_pid_for_iterations(controller, 20)

    assert controller.pwm.duty == 0
    assert controller._upper_latched is True

    controller.upper_limit_switch.value(0)

    controller.set_target(0.2)

    run_pid_for_iterations(controller, 20)

    assert controller._upper_latched is False


def test_stale_target_holds_position():
    controller = make_controller()

    simulated_actuator.position = 0.55
    controller.current_position = 0.55

    controller.set_target(0.90)

    simulation.current_time_ms += actuator_control.config.LIFT_TARGET_TIMEOUT_MS + 1

    run_pid_for_iterations(controller, 5)

    assert abs(controller.target_position - 0.55) < 0.01
    assert controller.pwm.duty == 0


def test_thread_safety():
    controller = make_controller()

    failures = []

    def writer():
        try:
            for i in range(500):
                controller.set_target(i / 500.0)
        except Exception as exc:
            failures.append(exc)

    def reader():
        try:
            for _ in range(500):
                state = controller.get_state()

                assert "position" in state
                assert "actuator_position" in state
                assert "actuator_current" in state
        except Exception as exc:
            failures.append(exc)

    thread_a = threading.Thread(target=writer)
    thread_b = threading.Thread(target=reader)

    thread_a.start()
    thread_b.start()

    thread_a.join()
    thread_b.join()

    assert not failures
