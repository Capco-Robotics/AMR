"""
Fault to signal-pattern mapping.

This module contains only the mapping table.
It is intentionally ROS-independent so it can be unit-tested easily.
"""

PATTERN_NONE = 0
PATTERN_RED_FLASH = 1
PATTERN_YELLOW_FLASH = 2
PATTERN_EMERGENCY = 3


NO_FAULT_PATTERN = {
    "siren_on": False,
    "light_on": False,
    "pattern_id": PATTERN_NONE,
}


FAIL_SAFE_PATTERN = {
    "siren_on": True,
    "light_on": True,
    "pattern_id": PATTERN_EMERGENCY,
}


FAULT_PATTERN_TABLE = {

    "BATTERY_LOW": {
        "siren_on": False,
        "light_on": True,
        "pattern_id": PATTERN_YELLOW_FLASH,
    },

    "MOTOR_FAULT": {
        "siren_on": True,
        "light_on": True,
        "pattern_id": PATTERN_RED_FLASH,
    },

    "EMERGENCY_STOP": {
        "siren_on": True,
        "light_on": True,
        "pattern_id": PATTERN_EMERGENCY,
    },
}