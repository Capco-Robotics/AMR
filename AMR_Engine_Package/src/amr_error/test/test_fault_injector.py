from amr_error.fault_pattern_table import (
    FAULT_PATTERN_TABLE,
    NO_FAULT_PATTERN,
    FAIL_SAFE_PATTERN,
    PATTERN_NONE,
    PATTERN_RED_FLASH,
    PATTERN_YELLOW_FLASH,
    PATTERN_EMERGENCY,
)


def test_no_fault():
    assert NO_FAULT_PATTERN["siren_on"] is False
    assert NO_FAULT_PATTERN["light_on"] is False
    assert NO_FAULT_PATTERN["pattern_id"] == PATTERN_NONE


def test_battery_low():
    pattern = FAULT_PATTERN_TABLE["BATTERY_LOW"]

    assert pattern["siren_on"] is False
    assert pattern["light_on"] is True
    assert pattern["pattern_id"] == PATTERN_YELLOW_FLASH


def test_motor_fault():
    pattern = FAULT_PATTERN_TABLE["MOTOR_FAULT"]

    assert pattern["siren_on"] is True
    assert pattern["light_on"] is True
    assert pattern["pattern_id"] == PATTERN_RED_FLASH


def test_emergency_stop():
    pattern = FAULT_PATTERN_TABLE["EMERGENCY_STOP"]

    assert pattern["siren_on"] is True
    assert pattern["light_on"] is True
    assert pattern["pattern_id"] == PATTERN_EMERGENCY


def test_unknown_fault():
    pattern = FAULT_PATTERN_TABLE.get(
        "UNKNOWN_FAULT",
        FAIL_SAFE_PATTERN,
    )

    assert pattern["siren_on"] is True
    assert pattern["light_on"] is True
    assert pattern["pattern_id"] == PATTERN_EMERGENCY