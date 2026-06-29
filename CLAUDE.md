# AMR

Autonomous mobile robot: Raspberry Pi (Linux, ROS2, Python) + Raspberry Pi
Pico (no OS, MicroPython) for real-time I/O. Differential drive (2 motors,
1 driver, 2 quadrature encoders), a closed-loop linear-actuator lift, an
audio siren + visual light for error signaling, a BMS, and SLAM
Toolbox/Nav2 for navigation.

## Repo layout

- `AMR_Engine_Package/` — everything that runs on the robot.
  - `src/` — a colcon ROS2 workspace (ament_python packages, see below).
  - `pico_firmware/` — plain MicroPython, flashed onto the Pico. Not a ROS2
    package.
- `AMR_Operator_Console/frontend/` — browser dashboard (map, battery,
  lift/fault status). Connects to `amr_command`'s websocket, which runs on
  the RPi as part of `AMR_Engine_Package`.

## ROS2 packages (`AMR_Engine_Package/src/`)

| Package | Responsibility |
|---|---|
| `amr_msgs` | Shared `.msg` interfaces (rosidl/ament_cmake) used across the packages below. |
| `amr_pico_bridge` | Owns the serial link to the Pico; the only package that touches that port. Translates the wire protocol (see below) to/from ROS2 topics. |
| `amr_navigation/move` (`amr_navigation_move`) | `cmd_vel` → per-wheel setpoints (kinematics/calibration live here, not on the Pico), and odometry (encoder ticks → `/odom` + tf). |
| `amr_navigation/map` (`amr_navigation_map`) | Config + launch only — SLAM Toolbox and Nav2. No custom nodes. |
| `amr_navigation/imu` (`amr_navigation_imu`) | Placeholder — empty config/launch, no nodes yet. Reserved in case IMU-based localization is used instead of (or alongside) SLAM Toolbox. |
| `amr_lift` | Decides lift target height and tracks reported state. PWM/limit-switch/PID logic itself is on the Pico. |
| `amr_error` | Decides what fault means what siren/light pattern. GPIO drive itself is on the Pico. |
| `amr_charging` | BMS telemetry. The BMS talks directly to the RPi over its own UART/I2C, not through the Pico. |
| `amr_command` | External-facing gateway: arbitrates commands from the operator console (and future input sources), forwards decisions to `amr_engine`, streams live telemetry out over a websocket. |
| `amr_engine` | Coordinator. `amr_engine.launch.py` loads/initializes every package (the literal "load packages" entry point). `amr_engine.py` is a thin executable wrapping `state_machine_node.py`, the supervisor (IDLE/NAVIGATING/LIFTING/ERROR) that aggregates diagnostics across the stack. |

## Pico vs RPi split

Pico owns anything needing tight timing/GPIO-level real-time control,
independent of whether the RPi is alive: motor PWM, PIO-driven encoder
counting, lift PWM + limit switches + position PID (the lift needs
arbitrary intermediate positions, so its PID loop runs on the Pico's
**second core** via MicroPython `_thread`, separate from the motor/encoder/
serial-comms loop on core 0), siren/light GPIO, and a two-layer fail-safe:
heartbeat-loss watchdog (RPi stopped talking → stop motors, hold lift,
trigger siren/light) plus a hardware WDT (Pico's own runtime hangs → chip
self-resets). See `pico_firmware/watchdog.py`.

RPi owns anything that needs "thinking": SLAM Toolbox, Nav2, odometry math,
BMS protocol parsing, the supervisor state machine, command arbitration,
and the dashboard gateway.

## Wire protocol (RPi ↔ Pico)

Newline-delimited JSON over one shared serial port, owned by
`amr_pico_bridge` on the RPi side and mirrored in `pico_firmware/
comms_protocol.py` on the Pico side. Every message has `type` + `seq` (+`ts`).

- RPi → Pico: `heartbeat`, `drive_cmd`, `lift_cmd`, `signal_cmd`, `estop_cmd`.
- Pico → RPi: `encoder_ticks`, `lift_state`, `signal_state`, `pico_status`,
  `fault_event`.

## Conventions

- Spaces in conceptual names become underscores in folder/package names
  (e.g. "AMR Engine Package" → `AMR_Engine_Package`).
- `amr_navigation/move`, `amr_navigation/map`, and `amr_navigation/imu` are
  separate colcon packages (`amr_navigation_move`, `amr_navigation_map`,
  `amr_navigation_imu`) nested under one directory — colcon discovers
  `package.xml` recursively, so this is valid and keeps the Navigation =
  Move + Map + IMU grouping visible in the tree.
