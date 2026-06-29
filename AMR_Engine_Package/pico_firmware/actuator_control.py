"""Linear actuator (lift) control: PWM/direction drive, limit switches, and
a closed-loop position PID since the lift must reach arbitrary intermediate
heights (not just full-up/full-down).

Runs the PID loop on the Pico's second core via _thread, so it doesn't
compete with the motor/encoder/serial-comms loop on core 0.
"""
import _thread

import config


class ActuatorControl:
    def __init__(self):
        self.target_position = None
        self._lock = _thread.allocate_lock()
        # TODO: machine.PWM/Pin for LIFT_PWM_PIN/LIFT_DIR_PIN, machine.ADC
        # for LIFT_POSITION_FEEDBACK_PIN, machine.Pin irq() for the limit
        # switches (always honored, even mid-PID-loop, as a hard stop).

    def start(self):
        _thread.start_new_thread(self._pid_loop, ())

    def set_target(self, position: float):
        with self._lock:
            self.target_position = position

    def get_state(self) -> dict:
        raise NotImplementedError

    def _pid_loop(self):
        raise NotImplementedError
