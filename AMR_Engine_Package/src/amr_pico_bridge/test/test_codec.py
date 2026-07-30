import json

from amr_pico_bridge import protocol_codec


def test_encode_decode_lift():

    message = {
        "type": protocol_codec.CMD_LIFT,
        "seq": 1,
        "ts": 123.45,
        "target_position": 0.7,
    }

    encoded = protocol_codec.encode(message)

    decoded = protocol_codec.decode(encoded)

    assert decoded == message


def test_encode_decode_drive():

    message = {
        "type": protocol_codec.CMD_DRIVE,
        "seq": 5,
        "ts": 10.0,
        "left": 1.0,
        "right": 1.2,
    }

    encoded = protocol_codec.encode(message)

    decoded = protocol_codec.decode(encoded)

    assert decoded == message
