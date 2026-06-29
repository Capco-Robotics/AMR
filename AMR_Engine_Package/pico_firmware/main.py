"""Pico firmware entry point. Flashed onto the Pico; runs on boot.

Core 0: serial comms loop (decode RPi commands, drive motor_driver/signal_io,
read encoder_reader, feed the watchdog) and the hardware WDT.
Core 1: actuator_control's lift position PID loop (started via .start()).
"""
import time

import comms_protocol
import config
from actuator_control import ActuatorControl
from encoder_reader import EncoderReader
from motor_driver import MotorDriver
from signal_io import SignalIO
from watchdog import Watchdog


def main():
    motor_driver = MotorDriver()
    encoder_reader = EncoderReader()
    actuator_control = ActuatorControl()
    signal_io = SignalIO()
    watchdog = Watchdog(motor_driver, actuator_control, signal_io)

    actuator_control.start()

    # TODO: open the UART/USB serial port at config.SERIAL_BAUDRATE.

    while True:
        watchdog.feed_hardware_wdt()
        watchdog.check_heartbeat()
        # TODO: read available serial lines, comms_protocol.decode() each,
        # dispatch CMD_* to motor_driver/actuator_control/signal_io and call
        # watchdog.on_rpi_message(); periodically send TEL_* telemetry
        # (encoder_reader.read_ticks(), actuator_control.get_state(), etc)
        # via comms_protocol.encode().
        time.sleep_ms(10)


if __name__ == '__main__':
    main()
