"""Differential-drive kinematics shared by drive_controller_node and odometry_node.

Calibration constants (wheel radius, track width, ticks-per-revolution) live
here as tunable Python config rather than in Pico firmware, so they can be
adjusted without reflashing.
"""

import math
# Robot calibration constants
WHEEL_RADIUS_M = 0.127      # 10 inch diameter wheel -> radius = 5 inch = 0.127 m
TRACK_WIDTH_M = 0.800       # Distance between left & right wheel centers (meters)
TICKS_PER_REV = 4096        # AS5600 12-bit absolute encoder

def twist_to_wheel_speeds(linear: float, angular: float) -> tuple[float, float]:
    """
    Convert robot linear and angular velocity into left and right wheel speeds.

    Args:
        linear (float): Linear velocity (m/s)
        angular (float): Angular velocity (rad/s)

    Returns:
        tuple(left_speed, right_speed): Wheel speeds in m/s
    """

    left_speed = linear - (angular * TRACK_WIDTH_M / 2.0)
    right_speed = linear + (angular * TRACK_WIDTH_M / 2.0)

    return left_speed, right_speed


def ticks_to_pose_delta(left_ticks: int, right_ticks: int, dt_s: float):
    """Convert delta encoder ticks over dt_s into a pose delta for odometry."""

    wheel_circumference = 2 * math.pi * WHEEL_RADIUS_M
    left_distance = (left_ticks / TICKS_PER_REV) * wheel_circumference
    right_distance = (right_ticks / TICKS_PER_REV) * wheel_circumference

    center_distance = (left_distance + right_distance) / 2.0
    dtheta = (right_distance - left_distance) / TRACK_WIDTH_M

    dx = center_distance * math.cos(dtheta / 2.0)
    dy = center_distance * math.sin(dtheta / 2.0)

    
    return dx, dy, dtheta
