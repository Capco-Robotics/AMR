"""Pose-aware arena LiDAR simulator for the demo sim.

Replaces the earlier static box raycaster (PR #20). Instead of casting a
fixed box from a mount offset, this reads the robot's live pose from /odom
and ray-casts a virtual arena (walls + a couple of obstacles) from each
LiDAR's true world position -- so the scans *change as the robot drives*,
which is what lets SLAM actually build (and extend) a map.

It publishes three topics:

  /scan_front  (frame laser_front_left) -- front-left sensor, ~270 deg FoV
  /scan_rear   (frame laser_rear_right) -- rear-right sensor,  ~270 deg FoV
  /scan        (frame base_link)        -- MERGED 360 deg coverage, fed to
                                           SLAM Toolbox + Nav2

The two per-sensor scans each miss a ~90 deg wedge (the robot body occludes
the diagonally-opposite corner); together they cover the full circle, which
is what the merged /scan represents. This is the "Wave-2 scan merger" the
PR #20 description promised, folded into the sim so no extra node is needed.
"""

import math
import random

import rclpy
from rclpy.node import Node

from sensor_msgs.msg import LaserScan
from nav_msgs.msg import Odometry


# --- Scan geometry ---------------------------------------------------------
ANGLE_INCREMENT = math.radians(1.0)   # 1 deg beams
RANGE_MIN = 0.10
RANGE_MAX = 6.0                        # < arena length, so the map must be explored
NOISE_STD = 0.01
PUBLISH_PERIOD = 0.1                   # 10 Hz

# Per-sensor field of view (each misses a rear ~90 deg wedge).
SENSOR_HALF_FOV = math.radians(135.0)  # -> 270 deg arc

# LiDAR mounts on the chassis (metres, radians), matching amr_description's xacro.
FRONT_MOUNT = (0.4, 0.4, 0.0)
REAR_MOUNT = (-0.4, -0.4, math.pi)

# --- Virtual arena (odom frame; robot starts at 0,0) -----------------------
# Two rooms joined by a doorway, plus two obstacles. Room 2 sits beyond
# RANGE_MAX and behind the divider, so it only appears once you drive through.
#   segment = (x1, y1, x2, y2)
ARENA_WALLS = [
    # outer boundary: rectangle (-5,-4) .. (9,4)
    (-5.0, -4.0, 9.0, -4.0),   # bottom
    (9.0, -4.0, 9.0, 4.0),     # right
    (9.0, 4.0, -5.0, 4.0),     # top
    (-5.0, 4.0, -5.0, -4.0),   # left
    # divider at x=4 from y=-4 up to y=1  (doorway is y in [1, 4])
    (4.0, -4.0, 4.0, 1.0),
    # pillar in room 1 (a small square around (-2, 2))
    (-2.5, 1.5, -1.5, 1.5),
    (-1.5, 1.5, -1.5, 2.5),
    (-1.5, 2.5, -2.5, 2.5),
    (-2.5, 2.5, -2.5, 1.5),
    # box obstacle in room 2 (around (6.5, -1))
    (6.0, -1.5, 7.0, -1.5),
    (7.0, -1.5, 7.0, -0.5),
    (7.0, -0.5, 6.0, -0.5),
    (6.0, -0.5, 6.0, -1.5),
]


def _ray_segment_range(px, py, dx, dy, ax, ay, bx, by):
    """Distance from (px,py) along unit dir (dx,dy) to segment A-B, or None."""
    ex = bx - ax
    ey = by - ay

    det = ex * dy - dx * ey
    if abs(det) < 1e-9:
        return None  # parallel

    apx = ax - px
    apy = ay - py

    t = (ex * apy - ey * apx) / det   # distance along the ray
    u = (dx * apy - dy * apx) / det   # position along the segment

    if t >= 0.0 and 0.0 <= u <= 1.0:
        return t
    return None


class ArenaScanSim(Node):

    def __init__(self):
        super().__init__("arena_scan_sim")

        # Latest robot pose in the odom frame.
        self.robot_x = 0.0
        self.robot_y = 0.0
        self.robot_yaw = 0.0
        # Timestamp of the /odom sample the pose above came from. Scans MUST be
        # stamped with this (not "now"), so the odom->base_link tf SLAM looks up
        # at the scan time matches the pose the scan was actually cast from.
        # Otherwise, while turning, each scan lands a few degrees rotated and the
        # map smears into overlapping copies.
        self.robot_stamp = None

        self.odom_sub = self.create_subscription(
            Odometry,
            "/odom",
            self._on_odom,
            10,
        )

        self.pub_front = self.create_publisher(LaserScan, "/scan_front", 10)
        self.pub_rear = self.create_publisher(LaserScan, "/scan_rear", 10)
        self.pub_merged = self.create_publisher(LaserScan, "/scan", 10)

        self.timer = self.create_timer(PUBLISH_PERIOD, self._publish_all)

        self.get_logger().info(
            "Arena scan sim started -- pose-aware raycaster publishing "
            "/scan_front, /scan_rear and merged /scan"
        )

    def _on_odom(self, msg: Odometry):
        p = msg.pose.pose.position
        q = msg.pose.pose.orientation

        siny_cosp = 2.0 * (q.w * q.z + q.x * q.y)
        cosy_cosp = 1.0 - 2.0 * (q.y * q.y + q.z * q.z)

        self.robot_x = p.x
        self.robot_y = p.y
        self.robot_yaw = math.atan2(siny_cosp, cosy_cosp)
        self.robot_stamp = msg.header.stamp

    def _publish_all(self):
        if self.robot_stamp is None:
            return  # no odom yet -- wait so scans carry a matching pose timestamp

        rx, ry, ryaw = self.robot_x, self.robot_y, self.robot_yaw
        stamp = self.robot_stamp

        # Each sensor's world pose = robot pose + its rotated mount offset.
        for mount, frame_id, publisher, half_fov in (
            (FRONT_MOUNT, "laser_front_left", self.pub_front, SENSOR_HALF_FOV),
            (REAR_MOUNT, "laser_rear_right", self.pub_rear, SENSOR_HALF_FOV),
            # Merged scan: cast a full circle straight from the robot centre.
            ((0.0, 0.0, 0.0), "base_link", self.pub_merged, math.pi),
        ):
            mx, my, myaw = mount

            sensor_x = rx + math.cos(ryaw) * mx - math.sin(ryaw) * my
            sensor_y = ry + math.sin(ryaw) * mx + math.cos(ryaw) * my
            sensor_yaw = ryaw + myaw

            scan = self._cast_scan(sensor_x, sensor_y, sensor_yaw, half_fov, frame_id, stamp)
            publisher.publish(scan)

    def _cast_scan(self, sx, sy, syaw, half_fov, frame_id, stamp):
        scan = LaserScan()
        scan.header.stamp = stamp
        scan.header.frame_id = frame_id

        scan.angle_min = -half_fov
        scan.angle_max = half_fov
        scan.angle_increment = ANGLE_INCREMENT
        scan.time_increment = 0.0
        scan.scan_time = PUBLISH_PERIOD
        scan.range_min = RANGE_MIN
        scan.range_max = RANGE_MAX

        num_readings = int((scan.angle_max - scan.angle_min) / ANGLE_INCREMENT) + 1

        ranges = []
        for i in range(num_readings):
            beam = scan.angle_min + i * ANGLE_INCREMENT
            world_angle = syaw + beam
            dx = math.cos(world_angle)
            dy = math.sin(world_angle)

            nearest = None
            for (ax, ay, bx, by) in ARENA_WALLS:
                hit = _ray_segment_range(sx, sy, dx, dy, ax, ay, bx, by)
                if hit is not None and hit <= RANGE_MAX and (nearest is None or hit < nearest):
                    nearest = hit

            if nearest is None:
                # No wall within range -- a real LiDAR reports "no return", not a
                # false hit at max range. Using inf lets RViz/SLAM/costmaps treat
                # this beam as unknown instead of baking a phantom circular wall
                # into the map wherever the nearest real wall is farther than
                # RANGE_MAX (this arena is bigger than RANGE_MAX by design).
                ranges.append(float("inf"))
                continue

            nearest += random.gauss(0.0, NOISE_STD)
            nearest = max(RANGE_MIN, min(nearest, RANGE_MAX))
            ranges.append(nearest)

        scan.ranges = ranges
        scan.intensities = [100.0] * num_readings
        return scan


def main(args=None):
    rclpy.init(args=args)

    node = ArenaScanSim()

    try:
        rclpy.spin(node)
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == "__main__":
    main()
