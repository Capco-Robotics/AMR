# pico_firmware/main.py

"""Pico firmware entry point. Flashed onto the Pico; runs on boot.

Core 0: serial comms loop (decode RPi commands, drive motor_driver/signal_io,
read encoder_reader, feed the watchdog) and the hardware WDT.
Core 1: actuator_control's lift position PID loop (started via .start()).
"""
import time
import machine
import json

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

    # 1. Open the UART serial port
    # Adjust Tx/Rx pins if using custom GPIOs (e.g., tx=machine.Pin(0), rx=machine.Pin(1))
    uart = machine.UART(config.SERIAL_UART_ID, baudrate=config.SERIAL_BAUDRATE)
    
    # Track time for periodic telemetry transmission (every 50ms)
    last_telemetry_ms = time.ticks_ms()
    
    # Internal string buffer for tracking streaming serial data chunks
    serial_buffer = ""

    while True:
        # Feed the hardware watchdog timer & check incoming heartbeat health
        watchdog.feed_hardware_wdt()
        watchdog.check_heartbeat()

        # 2. Read available incoming serial data
        if uart.any():
            # Read all characters waiting in the hardware queue
            incoming_bytes = uart.read()
            if incoming_bytes:
                # Decode bytes safely to string characters
                serial_buffer += incoming_bytes.decode('utf-8', 'ignore')

        # 3. Process complete messages separated by newlines
        while "\n" in serial_buffer:
            line, serial_buffer = serial_buffer.split("\n", 1)
            line = line.strip()
            
            if not line:
                continue
                
            try:
                # Parse incoming string chunk to structural JSON message
                msg = json.loads(line)
                msg_type = msg.get("type")
                
                # Signal the watchdog that the Raspberry Pi is successfully alive
                watchdog.on_rpi_message()

                # Dispatch structural message targets
                if msg_type == "drive_cmd":
                  if not watchdog.is_tripped():
                   left_spd = float(msg.get("left", 0.0))
                   right_spd = float(msg.get("right", 0.0))
                   motor_driver.set_speeds(left_spd, right_spd)
                    
                elif msg_type == "heartbeat":
                    # Handled implicitly above by watchdog.on_rpi_message()
                    pass
                    
                elif msg_type == "estop_cmd":
                    motor_driver.stop()
                    
            except (ValueError, KeyError, TypeError):
                # Safely catch JSON formatting corruptions or missing keys without crashing firmware
                pass

        # 4. Periodically broadcast encoder data over telemetry every 50ms
        current_time = time.ticks_ms()
        if time.ticks_diff(current_time, last_telemetry_ms) >= config.TELEMETRY_INTERVAL_MS:
            # Gather fresh metrics from hardware
         left_ticks, right_ticks = encoder_reader.read_ticks()

         telemetry_payload = {
          "type": "encoder_ticks",
          "left_ticks": left_ticks,
          "right_ticks": right_ticks,
          "dt_ms": config.TELEMETRY_INTERVAL_MS,
}
            
            # Send serialized frame over UART pipeline followed by a trailing newline
         telemetry_str = json.dumps(telemetry_payload) + "\n"
         uart.write(telemetry_str.encode('utf-8'))
            
            # Reset timer mark
         last_telemetry_ms = current_time

        # Yield execution minimally to keep processing light and clear
        time.sleep_ms(1)
        
if __name__ == '__main__':
    main()