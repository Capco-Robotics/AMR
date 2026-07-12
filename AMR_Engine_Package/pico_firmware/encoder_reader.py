# pico_firmware/encoder_reader.py

"""AS5600 absolute magnetic encoder reader for both wheels.

Each AS5600 has a fixed I2C address (0x36), so left and right encoders sit on
separate I2C buses (I2C0 and I2C1). The chip outputs a 12-bit raw angle
(0–4095 per full revolution); read_ticks() tracks the previous angle and
returns the signed delta since the last call, handling the 0/4095 wrap-around.
"""
from machine import I2C, Pin
import config

_AS5600_RAW_ANGLE_REG = 0x0C  # 2 bytes: [3:0] high nibble + [7:0] low byte
_HALF_RANGE = 2048             # wrap threshold: > half-turn means opposite direction


def _read_angle(i2c: I2C) -> int:
    # Read 2 bytes starting from the raw angle register
    data = i2c.readfrom_mem(config.AS5600_ADDR, _AS5600_RAW_ANGLE_REG, 2)
    # Combine high and low byte to get the 12-bit value (0-4095)
    return ((data[0] & 0x0F) << 8) | data[1]


class EncoderReader:
    def __init__(self):
        # Initialize I2C Bus 0 for the Left Encoder
        self._i2c_left = I2C(
            config.ENCODER_LEFT_I2C_ID,
            scl=Pin(config.ENCODER_LEFT_SCL_PIN),
            sda=Pin(config.ENCODER_LEFT_SDA_PIN),
            freq=config.ENCODER_I2C_FREQ,
        )
        
        # Initialize I2C Bus 1 for the Right Encoder
        self._i2c_right = I2C(
            config.ENCODER_RIGHT_I2C_ID,
            scl=Pin(config.ENCODER_RIGHT_SCL_PIN),
            sda=Pin(config.ENCODER_RIGHT_SDA_PIN),
            freq=config.ENCODER_I2C_FREQ,
        )
        
        # Establish the baseline angles for the first read_ticks() calculation
        self._prev_left = _read_angle(self._i2c_left)
        self._prev_right = _read_angle(self._i2c_right)
        self._left_ticks = 0
        self._right_ticks = 0

    def read_ticks(self) -> tuple[int, int]:
        """Returns (left_ticks, right_ticks) accumulated since the last call.

        One tick == 1/4096 of a full revolution. Sign reflects direction.
        """
        cur_left = _read_angle(self._i2c_left)
        cur_right = _read_angle(self._i2c_right)

        delta_left = cur_left - self._prev_left
        delta_right = cur_right - self._prev_right

        # Correct for 0/4095 wrap-around.
        if delta_left > _HALF_RANGE:
            delta_left -= 4096
        elif delta_left < -_HALF_RANGE:
            delta_left += 4096

        if delta_right > _HALF_RANGE:
            delta_right -= 4096
        elif delta_right < -_HALF_RANGE:
            delta_right += 4096

        # Store the current baseline for next calculation
        
        # Store the current baseline for next calculation
        self._prev_left = cur_left
        self._prev_right = cur_right

        self._left_ticks += delta_left
        self._right_ticks += delta_right

        return (self._left_ticks, self._right_ticks)