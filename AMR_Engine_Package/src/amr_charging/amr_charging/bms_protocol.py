"""BMS-specific protocol parser (e.g. Daly/JBD UART query/response framing).

Fill in once the actual BMS model is chosen -- these units each have their
own framing/checksum, so this stays separate from the Pico wire protocol.
"""


def parse_frame(raw: bytes) -> dict:
    raise NotImplementedError
