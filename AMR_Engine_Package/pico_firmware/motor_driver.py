"""PWM + direction control for the drive motors, via the single motor driver."""
import config


class MotorDriver:
    def __init__(self):
        # TODO: machine.PWM on MOTOR_LEFT_PWM_PIN/MOTOR_RIGHT_PWM_PIN,
        # machine.Pin on the *_DIR_PIN outputs.
        pass

    def set_speeds(self, left_speed: float, right_speed: float):
        raise NotImplementedError

    def stop(self):
        raise NotImplementedError
