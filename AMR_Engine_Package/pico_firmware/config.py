"""Pin assignments and tunables for the Pico firmware. Fill in once wiring is finalized."""

# Motor driver (1 driver, 2 motors)
MOTOR_LEFT_PWM_PIN = None
MOTOR_LEFT_DIR_PIN = None
MOTOR_RIGHT_PWM_PIN = None
MOTOR_RIGHT_DIR_PIN = None

# Quadrature encoders (2x, PIO-backed)
ENCODER_LEFT_A_PIN = None
ENCODER_LEFT_B_PIN = None
ENCODER_RIGHT_A_PIN = None
ENCODER_RIGHT_B_PIN = None

# Linear actuator (lift) -- closed-loop, position feedback + PID on core 1
LIFT_PWM_PIN = None
LIFT_DIR_PIN = None
LIFT_POSITION_FEEDBACK_PIN = None  # e.g. potentiometer ADC pin
LIFT_LIMIT_UPPER_PIN = None
LIFT_LIMIT_LOWER_PIN = None
LIFT_PID_KP = 0.0
LIFT_PID_KI = 0.0
LIFT_PID_KD = 0.0

# Siren + light
SIREN_PIN = None
LIGHT_PIN = None

# Comms / watchdog
SERIAL_BAUDRATE = 115200
HEARTBEAT_TIMEOUT_MS = 500
HARDWARE_WDT_TIMEOUT_MS = 8000
