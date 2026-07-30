"""Linear actuator (lift) control: PWM/direction drive, limit switches, and
a closed-loop position PID since the lift must reach arbitrary intermediate
heights (not just full-up/full-down).

Runs the PID loop on the Pico's second core via _thread, so it doesn't
compete with the motor/encoder/serial-comms loop on core 0.
"""

import _thread
import time
import machine

import config


class ActuatorControl:
    def __init__(self):
        self.target_position = None
        self._lock = _thread.allocate_lock()
        # TODO: machine.PWM/Pin for LIFT_PWM_PIN/LIFT_DIR_PIN, machine.ADC
        # for LIFT_POSITION_FEEDBACK_PIN, machine.Pin irq() for the limit
        # switches (always honored, even mid-PID-loop, as a hard stop).
        self.current_position = 0.0
        self.level_fault = False

        self.limit_upper = False
        self.limit_lower = False

        self._upper_latched = False
        self._lower_latched = False

        self._last_target_ms = None

        lift_pwm_pin = machine.Pin(config.LIFT_PWM_PIN)
        self.pwm = machine.PWM(lift_pwm_pin)
        self.pwm.freq(config.LIFT_PWM_FREQUENCY)

        self.direction = machine.Pin(
            config.LIFT_DIR_PIN,
            machine.Pin.OUT,
        )

        self.position_adc = machine.ADC(machine.Pin(config.LIFT_POSITION_FEEDBACK_PIN))

        self.integral_error = 0.0
        self.previous_error = 0.0

        self._last_direction = 0

        self.stop()

        self.upper_limit_switch = machine.Pin(
            config.LIFT_LIMIT_UPPER_PIN,
            machine.Pin.IN,
        )

        self.lower_limit_switch = machine.Pin(
            config.LIFT_LIMIT_LOWER_PIN,
            machine.Pin.IN,
        )

    def start(self):
        _thread.start_new_thread(self._pid_loop, ())

    def set_target(self, position: float):
        with self._lock:
            self.target_position = position
            self._last_target_ms = time.ticks_ms()

    def stop(self):
        self.pwm.duty_u16(0)
        self.direction.value(0)

    def get_state(self) -> dict:
        with self._lock:

            position = self.current_position
            limit_upper = self.limit_upper
            limit_lower = self.limit_lower
            level_fault = self.level_fault

        return {
            "position": position,
            "actuator_position": [position, position],
            "actuator_current": [0.0, 0.0],
            "limit_upper": limit_upper,
            "limit_lower": limit_lower,
            "level_fault": level_fault,
        }

    def _pid_loop(self):
        while True:
            current_time = time.ticks_ms()

            with self._lock:
                target = self.target_position
                last_target_ms = self._last_target_ms

            # Fail-safe: hold current position if target is missing.
            if target is None:
                with self._lock:
                    self.target_position = self.current_position
                    target = self.current_position
                    self._last_target_ms = current_time

            # Fail-safe: stale target.
            if (
                last_target_ms is not None
                and time.ticks_diff(
                    current_time,
                    last_target_ms,
                )
                > config.LIFT_TARGET_TIMEOUT_MS
            ):
                with self._lock:
                    self.target_position = self.current_position
                    target = self.current_position
                    self._last_target_ms = current_time

            position = self.position_adc.read_u16() / config.LIFT_MAX_PWM

            upper_limit = bool(self.upper_limit_switch.value())

            lower_limit = bool(self.lower_limit_switch.value())

            with self._lock:
                self.limit_upper = upper_limit
                self.limit_lower = lower_limit

            if upper_limit:
                self._upper_latched = True

            if lower_limit:
                self._lower_latched = True

            with self._lock:
                self.current_position = position

            error = target - position

            self.integral_error += error

            derivative = error - self.previous_error

            self.previous_error = error

            output = (
                config.LIFT_PID_KP * error
                + config.LIFT_PID_KI * self.integral_error
                + config.LIFT_PID_KD * derivative
            )

            output = max(
                -1.0,
                min(1.0, output),
            )

            direction = 0

            if output > 0:
                direction = 1
            elif output < 0:
                direction = -1

            if self._upper_latched and direction > 0:
                self.stop()
                time.sleep_ms(config.LIFT_CONTROL_INTERVAL_MS)
                continue

            if self._lower_latched and direction < 0:
                self.stop()
                time.sleep_ms(config.LIFT_CONTROL_INTERVAL_MS)
                continue

            if direction < 0:
                self._upper_latched = False

            if direction > 0:
                self._lower_latched = False

            if abs(error) < config.LIFT_POSITION_TOLERANCE:
                self.stop()
            else:
                self.direction.value(1 if direction > 0 else 0)

                duty = int(abs(output) * config.LIFT_MAX_PWM)

                self.pwm.duty_u16(duty)

            self._last_direction = direction

            time.sleep_ms(config.LIFT_CONTROL_INTERVAL_MS)
