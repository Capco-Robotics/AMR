# pico_firmware/main.py

"""Pico firmware entry point. Flashed onto the Pico; runs on boot.

Core 0: serial comms loop (decode RPi commands, drive motor_driver/signal_io,
read encoder_reader, feed the watchdog) and the hardware WDT.
Core 1: actuator_control's lift position PID loop (started via .start()).
"""

import json
import time
import machine

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
    watchdog = Watchdog(
        motor_driver,
        actuator_control,
        signal_io,
    )

    actuator_control.start()

    uart = machine.UART(
        config.SERIAL_UART_ID,
        baudrate=config.SERIAL_BAUDRATE,
    )

    last_telemetry_ms = time.ticks_ms()
    serial_buffer = ""

    # Latched by estop_cmd. Separate from the watchdog trip on purpose: that
    # one means "the RPi went quiet", this one means "the RPi is talking and
    # is telling us to stay stopped", and only the RPi clears it.
    #
    # Note this is still a software stop -- it depends on this firmware
    # running. A physical cut-off between the driver and the motors is the
    # only thing that survives a hung Pico; the hardware WDT in watchdog.py is
    # the nearest this stack gets.
    estop_engaged = False

    while True:
        # Feed hardware watchdog
        watchdog.feed_hardware_wdt()
        watchdog.check_heartbeat()

        # Read serial bytes
        if uart.any():
            incoming_bytes = uart.read()

            if incoming_bytes:
                serial_buffer += incoming_bytes.decode(
                    "utf-8",
                    "ignore",
                )

        # Process complete JSON lines
        while "\n" in serial_buffer:
            line, serial_buffer = serial_buffer.split("\n", 1)
            line = line.strip()

            if not line:
                continue

            try:
                msg = json.loads(line)
                msg_type = msg.get("type")

                if msg_type == "drive_cmd":

                    # Ignore drive commands while the watchdog is tripped or
                    # an e-stop is latched
                    if not watchdog.is_tripped() and not estop_engaged:
                        left_spd = float(msg.get("left", 0.0))
                        right_spd = float(msg.get("right", 0.0))

                        motor_driver.set_speeds(
                            left_spd,
                            right_spd,
                        )

                elif msg_type == "heartbeat":
                    # Only heartbeat clears the watchdog trip
                    watchdog.on_rpi_message()

                elif msg_type == "estop_cmd":

                    # Absent or malformed `engage` means engage. A truncated
                    # e-stop frame has to stop the robot, never release it.
                    estop_engaged = msg.get("engage", True) is not False

                    if estop_engaged:
                        motor_driver.stop()

            except (ValueError, KeyError, TypeError):
                # Ignore malformed packets
                pass

        # Send encoder telemetry every 50 ms
        current_time = time.ticks_ms()

        if (
            time.ticks_diff(
                current_time,
                last_telemetry_ms,
            )
            >= config.TELEMETRY_INTERVAL_MS
        ):

            left_ticks, right_ticks = encoder_reader.read_ticks()

            telemetry_payload = {
                "type": "encoder_ticks",
                "left_ticks": left_ticks,
                "right_ticks": right_ticks,
                "dt_ms": config.TELEMETRY_INTERVAL_MS,
            }

            telemetry_str = json.dumps(
                telemetry_payload
            ) + "\n"

            uart.write(
                telemetry_str.encode("utf-8")
            )

            last_telemetry_ms = current_time

        time.sleep_ms(1)


if __name__ == "__main__":
    main()