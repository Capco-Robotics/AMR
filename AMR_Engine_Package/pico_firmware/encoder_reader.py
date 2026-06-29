"""Quadrature encoder tick counting for both wheels.

Must use rp2.PIO state machines for the actual edge-counting, not a
pure-Python irq() callback -- GC pauses in MicroPython's interpreter make
raw quadrature decode in an ISR unreliable above a few hundred ticks/sec.
The main loop just reads the PIO-accumulated counts.
"""


class EncoderReader:
    def __init__(self):
        # TODO: two rp2.PIO state machines (left/right), one per encoder,
        # decoding quadrature edges in hardware.
        pass

    def read_ticks(self) -> tuple[int, int]:
        """Returns (left_ticks, right_ticks) since the last read."""
        raise NotImplementedError
