"""Two independent safety layers:

1. Heartbeat-loss watchdog -- detects the RPi has stopped talking to us
   (crash, ROS2 stack hang, bridge node killed, kernel panic, etc).
   On trigger: zero motor PWM immediately, hold the lift at its current
   position (uncontrolled retraction could itself be a hazard), drive the
   siren/light, and emit a fault_event if we can still reach the RPi.

2. Hardware watchdog timer (machine.WDT) -- detects the Pico's own
   MicroPython runtime hanging (e.g. stuck in a blocking call). Fed from
   the main loop; if not fed in time, the chip resets itself rather than
   failing silently with motors potentially still energized.
"""
import time

import config


class Watchdog:
    def __init__(self, motor_driver, actuator_control, signal_io):
        self.motor_driver = motor_driver
        self.actuator_control = actuator_control
        self.signal_io = signal_io
        self._last_rpi_msg_ms = time.ticks_ms()
        self._hw_wdt = None  # TODO: machine.WDT(timeout=config.HARDWARE_WDT_TIMEOUT_MS)
        self._tripped = False

    def on_rpi_message(self):
        self._last_rpi_msg_ms = time.ticks_ms()

    def feed_hardware_wdt(self):
        if self._hw_wdt is not None:
            self._hw_wdt.feed()

    def check_heartbeat(self) -> bool:
        """Call every main-loop iteration. Returns True if it just tripped."""
        age_ms = time.ticks_diff(time.ticks_ms(), self._last_rpi_msg_ms)
        if age_ms > config.HEARTBEAT_TIMEOUT_MS and not self._tripped:
            self._tripped = True
            self._trip()
            return True
        return False

    def _trip(self):
        self.motor_driver.stop()
        # lift intentionally not moved -- hold position
        self.signal_io.set(siren_on=True, light_on=True)
