"""Wire protocol contract with the Pico, mirrored in pico_firmware/comms_protocol.py.

Newline-delimited JSON. Every message carries `type` and `seq`; commands
(RPi -> Pico) additionally carry `ts` as time.time(), telemetry (Pico -> RPi)
carries `ts` as the Pico's own ticks_ms().
"""
import json

# RPi -> Pico
CMD_HEARTBEAT = 'heartbeat'
CMD_DRIVE = 'drive_cmd'
CMD_LIFT = 'lift_cmd'
CMD_SIGNAL = 'signal_cmd'
CMD_ESTOP = 'estop_cmd'

# Pico -> RPi
TEL_ENCODER_TICKS = 'encoder_ticks'
TEL_LIFT_STATE = 'lift_state'
TEL_SIGNAL_STATE = 'signal_state'
TEL_PICO_STATUS = 'pico_status'
TEL_FAULT_EVENT = 'fault_event'


def encode(message: dict) -> bytes:
    return (json.dumps(message) + '\n').encode('utf-8')


def decode(line: bytes) -> dict:
    return json.loads(line.decode('utf-8').strip())
