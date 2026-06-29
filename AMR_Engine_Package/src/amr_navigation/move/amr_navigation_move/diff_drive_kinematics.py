"""Differential-drive kinematics shared by drive_controller_node and odometry_node.

Calibration constants (wheel radius, track width, ticks-per-revolution) live
here as tunable Python config rather than in Pico firmware, so they can be
adjusted without reflashing.
"""

WHEEL_RADIUS_M = 0.0
TRACK_WIDTH_M = 0.0
TICKS_PER_REV = 0


def twist_to_wheel_speeds(linear: float, angular: float) -> tuple[float, float]:
    """Convert (linear, angular) cmd_vel into (left_speed, right_speed)."""
    raise NotImplementedError


def ticks_to_pose_delta(left_ticks: int, right_ticks: int, dt_s: float):
    """Convert delta encoder ticks over dt_s into a pose delta for odometry."""
    raise NotImplementedError
