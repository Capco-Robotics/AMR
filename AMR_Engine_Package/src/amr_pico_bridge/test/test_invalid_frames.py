import pytest
from amr_pico_bridge import protocol_codec


def test_truncated_json():
    with pytest.raises(Exception):
        protocol_codec.decode(b'{"type":"lift_state"')


def test_missing_type():
    with pytest.raises(ValueError):
        protocol_codec.decode(b'{"seq":1}')


def test_missing_seq():
    with pytest.raises(ValueError):
        protocol_codec.decode(b'{"type":"lift_state"}')


def test_wrong_type_type():
    with pytest.raises(ValueError):
        protocol_codec.decode(b'{"type":123,"seq":1}')


def test_wrong_seq_type():
    with pytest.raises(ValueError):
        protocol_codec.decode(b'{"type":"lift_state","seq":"1"}')
