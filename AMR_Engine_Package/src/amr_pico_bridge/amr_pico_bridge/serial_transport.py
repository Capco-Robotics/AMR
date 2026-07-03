"""Owns the physical serial port to the Pico.

Stub: real implementation should open the port (e.g. via pyserial),
read newline-delimited frames in a background thread, and hand decoded
dicts to a callback, plus expose a write() for outgoing frames.
"""
import queue
import threading

import serial

class SerialTransport:
    def __init__(self, port: str, baudrate: int = 115200):
     self.port = port
     self.baudrate = baudrate

     self._serial = None
     self._rx_queue = queue.Queue()

     self._stop_event = threading.Event()
     self._reader_thread = None

     self._write_lock = threading.Lock()

    def open(self):
     self._serial = serial.Serial(
        port=self.port,
        baudrate=self.baudrate,
        timeout=0.1,
    )

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

            if line:
                self._rx_queue.put(line)

        except Exception:
            break

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