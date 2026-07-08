# pico_firmware/motor_driver.py

import machine
import config

class MotorDriver:
    def __init__(self):
        # 1. Initialize Left Motor Pins
        left_pwm_pin = machine.Pin(config.LEFT_MOTOR_PWM)
        self.left_pwm = machine.PWM(left_pwm_pin)
        self.left_pwm.freq(20000)  # Set frequency to 20 kHz
        
        self.left_dir = machine.Pin(config.LEFT_MOTOR_DIR, machine.Pin.OUT)
        
        # 2. Initialize Right Motor Pins
        right_pwm_pin = machine.Pin(config.RIGHT_MOTOR_PWM)
        self.right_pwm = machine.PWM(right_pwm_pin)
        self.right_pwm.freq(20000)  # Set frequency to 20 kHz
        
        self.right_dir = machine.Pin(config.RIGHT_MOTOR_DIR, machine.Pin.OUT)
        
        # Ensure motors start completely stopped
        self.stop()

    def set_speeds(self, left_speed: float, right_speed: float):
        # --- Handle Left Motor ---
        # Clamp value to [-1.0, 1.0]
        left_speed = max(-1.0, min(1.0, left_speed))
        
        # Set Direction: Low (0) for forward (>= 0), High (1) for reverse (< 0)
        if left_speed >= 0:
            self.left_dir.value(0)
        else:
            self.left_dir.value(1)
            
        # Convert absolute speed to 16-bit PWM duty cycle (0 to 65535)
        left_duty = int(abs(left_speed) * 65535)
        self.left_pwm.duty_u16(left_duty)

        # --- Handle Right Motor ---
        # Clamp value to [-1.0, 1.0]
        right_speed = max(-1.0, min(1.0, right_speed))
        
        # Set Direction: Low (0) for forward (>= 0), High (1) for reverse (< 0)
        if right_speed >= 0:
            self.right_dir.value(0)
        else:
            self.right_dir.value(1)
            
        # Convert absolute speed to 16-bit PWM duty cycle
        right_duty = int(abs(right_speed) * 65535)
        self.right_pwm.duty_u16(right_duty)

    def stop(self):
        # Immediately set both PWM duty cycles to 0 (No ramp-down)
        self.left_pwm.duty_u16(0)
        self.right_pwm.duty_u16(0)
        
        # Optional: Force direction pins low as well
        self.left_dir.value(0)
        self.right_dir.value(0)