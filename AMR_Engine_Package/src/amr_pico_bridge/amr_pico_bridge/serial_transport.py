"""Owns the physical serial port to the Pico.

Stub: real implementation should open the port (e.g. via pyserial),
read newline-delimited frames in a background thread, and hand decoded
dicts to a callback, plus expose a write() for outgoing frames.
"""


class SerialTransport:
    def __init__(self, port: str, baudrate: int = 115200):
        self.port = port
        self.baudrate = baudrate

    def open(self):
        raise NotImplementedError

    def close(self):
        raise NotImplementedError

    def write(self, data: bytes):
        raise NotImplementedError

    def read_line(self) -> bytes:
        raise NotImplementedError
