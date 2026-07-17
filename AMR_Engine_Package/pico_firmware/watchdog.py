# pico_firmware/watchdog.py

"""
Two independent safety layers:

1. Heartbeat-loss watchdog -- detects the RPi has stopped talking to us
   (crash, ROS2 stack hang, bridge node killed, kernel panic, etc).
   On trigger: zero motor PWM immediately, hold the lift at its current
   position, drive the siren/light, and emit a fault_event if possible.

2. Hardware watchdog timer (machine.WDT) -- detects the Pico's own
   MicroPython runtime hanging. Fed from the main loop; if not fed in
   time, the chip resets itself.
"""

import time
import machine
import config


class Watchdog:
    def __init__(self, motor_driver, actuator_control, signal_io):
        self.motor_driver = motor_driver
        self.actuator_control = actuator_control
        self.signal_io = signal_io

        self._last_rpi_msg_ms = time.ticks_ms()
        self._tripped = False

        # Hardware watchdog
        self._hw_wdt = machine.WDT(
            timeout=config.HARDWARE_WDT_TIMEOUT_MS
        )

    def on_rpi_message(self):
        """Called when a valid heartbeat is received."""
        self._last_rpi_msg_ms = time.ticks_ms()

        # Clear watchdog trip once heartbeats resume.
        if self._tripped:
            self._tripped = False

            try:
                self.signal_io.set(
                    siren_on=False,
                    light_on=False,
                )
            except Exception:
                pass

    def feed_hardware_wdt(self):
        if self._hw_wdt is not None:
            self._hw_wdt.feed()

    def check_heartbeat(self) -> bool:
        """Call every main-loop iteration."""
        age_ms = time.ticks_diff(
            time.ticks_ms(),
            self._last_rpi_msg_ms,
        )

        if age_ms > config.HEARTBEAT_TIMEOUT_MS and not self._tripped:
            self._tripped = True
            self._trip()
            return True

        return False

    def _trip(self):
        """
        Never suppress a motor stop failure.
        If stopping the motors fails, let the exception propagate.
        The hardware watchdog is the final safety backstop.
        """
        self.motor_driver.stop()

        # Lift intentionally not moved.
        try:
            self.signal_io.set(
                siren_on=True,
                light_on=True,
            )
        except Exception:
            pass

    def is_tripped(self):
        return self._tripped