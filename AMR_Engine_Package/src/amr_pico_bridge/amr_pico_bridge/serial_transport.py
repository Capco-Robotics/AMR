"""Owns the physical serial port to the Pico.

Reads newline-delimited frames in a background thread and buffers them in
a bounded queue; callers drain it via poll_lines() (or block on
read_line()) and decode elsewhere (see protocol_codec). write() sends
outgoing frames.

The reader thread is not auto-restarted if it dies (bad read, port
unplugged) or if a line is truncated by a mid-frame read timeout -
callers should watch the connected/last_error properties.
"""
import logging
import queue
import threading
from typing import List, Optional

import serial

logger = logging.getLogger(__name__)

_RX_QUEUE_MAXSIZE = 1000

class SerialTransport:
    def __init__(self, port: str, baudrate: int = 115200):
        self.port = port
        self.baudrate = baudrate

        self._serial = None
        self._rx_queue = queue.Queue(maxsize=_RX_QUEUE_MAXSIZE)

        self._stop_event = threading.Event()
        self._reader_thread = None
        self._last_error = None

        self._write_lock = threading.Lock()

    @property
    def connected(self) -> bool:
        return (
            self._serial is not None
            and self._serial.is_open
            and self._reader_thread is not None
            and self._reader_thread.is_alive()
        )

    @property
    def last_error(self) -> Optional[Exception]:
        return self._last_error

    def open(self):
        if self._reader_thread is not None and self._reader_thread.is_alive():
            raise RuntimeError("Serial port is already open")

        self._serial = serial.Serial(
            port=self.port,
            baudrate=self.baudrate,
            timeout=0.1,
        )

        self._last_error = None
        self._stop_event.clear()

        self._reader_thread = threading.Thread(
            target=self._reader_thread_body,
            daemon=True,
        )

        self._reader_thread.start()

    def _reader_thread_body(self):
        while not self._stop_event.is_set():
            try:
                line = self._serial.readline()
            except Exception as exc:
                logger.exception("Serial reader thread stopped due to a read error")
                self._last_error = exc
                break

            if not line:
                continue

            if not line.endswith(b'\n'):
                logger.warning(
                    "Dropping incomplete serial line (read timed out mid-frame): %r",
                    line,
                )
                continue

            try:
                self._rx_queue.put_nowait(line)
            except queue.Full:
                try:
                    self._rx_queue.get_nowait()
                except queue.Empty:
                    pass
                self._rx_queue.put_nowait(line)

    def close(self):
        self._stop_event.set()

        if self._reader_thread is not None:
            self._reader_thread.join()

        if self._serial is not None and self._serial.is_open:
            self._serial.close()

    def write(self, data: bytes):
        if self._serial is None or not self._serial.is_open:
            raise RuntimeError("Serial port is not open")

        with self._write_lock:
            self._serial.write(data)

    def read_line(self) -> bytes:
        return self._rx_queue.get()

    def poll_lines(self) -> List[bytes]:
        lines = []

        while True:
            try:
                lines.append(self._rx_queue.get_nowait())
            except queue.Empty:
                break

        return lines
