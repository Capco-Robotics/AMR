"""Pin assignments and tunables for the Pico firmware. Fill in once wiring is finalized."""

# Motor driver (1 driver, 2 motors)
MOTOR_LEFT_PWM_PIN = 2
MOTOR_LEFT_DIR_PIN = 3
MOTOR_RIGHT_PWM_PIN = 4
MOTOR_RIGHT_DIR_PIN = 5

# AS5600 absolute magnetic encoders (2x, I2C-backed, address 0x36 each)
# Left encoder on I2C0, right encoder on I2C1 (separate buses, same chip address).
ENCODER_LEFT_I2C_ID = 0   # machine.I2C(0, ...)
ENCODER_LEFT_SDA_PIN = 8   # GP8
ENCODER_LEFT_SCL_PIN = 9   # GP9
ENCODER_RIGHT_I2C_ID = 1
ENCODER_RIGHT_SDA_PIN = 10  # GP10
ENCODER_RIGHT_SCL_PIN = 11  # GP11
ENCODER_I2C_FREQ = 400_000
AS5600_ADDR = 0x36

# Linear actuator (lift) -- closed-loop, position feedback + PID on core 1
LIFT_PWM_PIN = 24
LIFT_DIR_PIN = 25
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
SERIAL_UART_ID = 0
SERIAL_BAUDRATE = 115200
TELEMETRY_INTERVAL_MS = 50
HEARTBEAT_TIMEOUT_MS = 500
HARDWARE_WDT_TIMEOUT_MS = 8000

