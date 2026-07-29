#!/usr/bin/env python3

"""Scores Nav2 path following against the scenarios in path_eval_scenarios.yaml.

Run with Nav2 up (ros2 launch amr_navigation_map nav2_sim.launch.py):

    ros2 run amr_navigation_map path_eval.py

Exits non-zero if any scenario fails, so it can gate a tuning change.
"""

import math
import os
import time
import yaml
import sys

from ament_index_python.packages import get_package_share_directory

import rclpy
from rclpy.node import Node
from rclpy.action import ActionClient

# How long to wait for Nav2's action server before giving up. Without a
# timeout wait_for_server() blocks forever and the harness looks hung.
SERVER_WAIT_SEC = 10.0

# Budget for driving back to a scenario's start pose before it is scored.
RESET_TIMEOUT_SEC = 90.0

# How long to let a cancel settle before moving on. Starting the next
# scenario while the robot is still coasting corrupts its first samples.
CANCEL_TIMEOUT_SEC = 10.0

# Close enough to a scenario's first pose to call the reset done.
RESET_TOLERANCE_M = 0.25

from geometry_msgs.msg import PoseStamped
from nav_msgs.msg import Odometry
from nav2_msgs.action import NavigateThroughPoses
from action_msgs.msg import GoalStatus


def yaw_to_quaternion(yaw):
    from geometry_msgs.msg import Quaternion

    q = Quaternion()
    q.x = 0.0
    q.y = 0.0
    q.z = math.sin(yaw / 2.0)
    q.w = math.cos(yaw / 2.0)
    return q


class PathEvaluator(Node):

    def __init__(self):

        super().__init__("path_eval")

        self.client = ActionClient(
            self,
            NavigateThroughPoses,
            "/navigate_through_poses"
        )

        self.odom_sub = self.create_subscription(
            Odometry,
            "/odom",
            self.odom_callback,
            10
        )

        self.current_pose = None
        self.actual_path = []

        # Odometry is always tracked, but only recorded into actual_path
        # while a scored run is in progress -- the drive back to a scenario's
        # start pose must not be scored against that scenario's path.
        self.collecting = False

        self.goal_done = False
        self.goal_success = False

        self.feedback_remaining = None
        self.feedback_distance = None

        self.goal_handle = None
        self.result_future = None

        # The YAML installs to share/, while this script installs to
        # lib/. Deriving the config path from __file__ therefore looked in
        # <install>/lib/config/ and raised FileNotFoundError under ros2 run;
        # it only ever worked when executed from the source tree.
        scenario_file = os.path.join(
            get_package_share_directory("amr_navigation_map"),
            "config",
            "path_eval_scenarios.yaml",
        )

        with open(scenario_file, "r") as f:
            self.scenarios = yaml.safe_load(f)

    def odom_callback(self, msg):

        x = msg.pose.pose.position.x
        y = msg.pose.pose.position.y

        self.current_pose = (x, y)

        if self.collecting:
            self.actual_path.append((x, y))

    def build_pose(self, x, y, yaw):

        pose = PoseStamped()

        pose.header.frame_id = "map"
        pose.header.stamp = self.get_clock().now().to_msg()

        pose.pose.position.x = float(x)
        pose.pose.position.y = float(y)
        pose.pose.position.z = 0.0

        pose.pose.orientation = yaw_to_quaternion(yaw)

        return pose

    def load_goal(self, scenario):

        poses = []

        for point in scenario["poses"]:

            poses.append(
                self.build_pose(
                    point["x"],
                    point["y"],
                    point.get("yaw", 0.0)
                )
            )

        return poses

    def feedback_callback(self, feedback_msg):

        fb = feedback_msg.feedback

        self.feedback_remaining = fb.number_of_poses_remaining
        self.feedback_distance = fb.distance_remaining

        self.get_logger().info(
            f"Remaining={self.feedback_remaining} "
            f"Distance={self.feedback_distance:.2f}"
        )
    def send_goal(self, poses):

        goal = NavigateThroughPoses.Goal()
        goal.poses = poses

        self.goal_done = False
        self.goal_success = False
        self.goal_handle = None

        self.actual_path = []

        # wait_for_server() with no timeout blocks forever, so with Nav2 down
        # the harness hung silently instead of reporting anything.
        if not self.client.wait_for_server(timeout_sec=SERVER_WAIT_SEC):

            self.get_logger().error(
                "navigate_through_poses server not available after "
                f"{SERVER_WAIT_SEC:.0f}s -- is Nav2 running?"
            )

            self.goal_done = True
            self.goal_success = False

            return False

        future = self.client.send_goal_async(
            goal,
            feedback_callback=self.feedback_callback
        )

        future.add_done_callback(self.goal_response_callback)

        return True

    def spin_until_done(self, timeout):
        """Spin until the active goal finishes. True if it finished in time."""

        start = time.time()

        while rclpy.ok():

            rclpy.spin_once(self, timeout_sec=0.1)

            if self.goal_done:
                return True

            if time.time() - start > timeout:
                return False

        return False

    def cancel_active_goal(self):
        """Cancel whatever is running and wait for the robot to give up.

        On a timeout the harness previously just moved on, leaving the
        previous goal still executing -- so the next scenario was scored
        while the robot was still driving the last one.
        """

        if self.goal_handle is None:
            return

        self.get_logger().warning("Cancelling active goal")

        cancel_future = self.goal_handle.cancel_goal_async()

        start = time.time()

        while rclpy.ok():

            rclpy.spin_once(self, timeout_sec=0.1)

            if cancel_future.done() and self.goal_done:
                break

            if time.time() - start > CANCEL_TIMEOUT_SEC:

                self.get_logger().error(
                    "Goal did not acknowledge cancellation"
                )

                break

        self.goal_handle = None

    def reset_to_start(self, scenario):
        """Drive to the scenario's first pose before scoring begins.

        There is no odometry reset service (see the TODO in odometry_node),
        so the robot cannot be teleported. Instead each scenario starts by
        navigating to its own declared start pose as a separate, unscored
        goal. Without this the robot began every scenario wherever the
        previous one ended, and that transit leg was scored against the new
        scenario's path -- which made results depend on scenario order.
        """

        first = scenario["poses"][0]

        target = (float(first["x"]), float(first["y"]))

        if (
            self.current_pose is not None
            and self.distance(self.current_pose, target) <= RESET_TOLERANCE_M
        ):
            return True

        self.get_logger().info(
            f"Repositioning to start pose {target}"
        )

        self.collecting = False

        pose = self.build_pose(
            first["x"],
            first["y"],
            first.get("yaw", 0.0),
        )

        if not self.send_goal([pose]):
            return False

        if not self.spin_until_done(RESET_TIMEOUT_SEC):

            self.get_logger().error("Repositioning timed out")

            self.cancel_active_goal()

            return False

        return self.goal_success

    def goal_response_callback(self, future):

        self.goal_handle = future.result()

        if not self.goal_handle.accepted:

            self.get_logger().error("Goal rejected")

            # Nothing to cancel later; a rejected handle is not cancellable.
            self.goal_handle = None

            self.goal_done = True
            self.goal_success = False
            return

        self.get_logger().info("Goal accepted")

        self.result_future = (
            self.goal_handle.get_result_async()
        )

        self.result_future.add_done_callback(
            self.result_callback
        )

    def result_callback(self, future):

        result = future.result()

        status = result.status

        self.goal_done = True

        self.goal_success = (
            status == GoalStatus.STATUS_SUCCEEDED
        )

        self.get_logger().info(
            f"Result status = {status}"
        )

    def distance(self, a, b):

        return math.sqrt(
            (a[0] - b[0]) ** 2 +
            (a[1] - b[1]) ** 2
        )

    def point_to_segment_distance(
        self,
        point,
        start,
        end
    ):

        px, py = point
        x1, y1 = start
        x2, y2 = end

        dx = x2 - x1
        dy = y2 - y1

        if dx == 0.0 and dy == 0.0:
            return self.distance(point, start)

        t = (
            ((px - x1) * dx) +
            ((py - y1) * dy)
        ) / (
            dx * dx + dy * dy
        )

        t = max(0.0, min(1.0, t))

        proj_x = x1 + t * dx
        proj_y = y1 + t * dy

        return self.distance(
            point,
            (proj_x, proj_y)
        )

    def compute_cross_track_error(
        self,
        commanded,
        actual
    ):

        if len(actual) == 0:
            return 0.0, 0.0

        # One commanded pose gives no segment to measure against, so every
        # sample would score as infinitely far away.
        if len(commanded) < 2:
            return 0.0, 0.0

        errors = []

        for point in actual:

            best = float("inf")

            for i in range(
                len(commanded) - 1
            ):

                start = commanded[i]
                end = commanded[i + 1]

                d = self.point_to_segment_distance(
                    point,
                    start,
                    end
                )

                if d < best:
                    best = d

            errors.append(best)

        mean_error = (
            sum(errors) / len(errors)
        )

        max_error = max(errors)

        return mean_error, max_error
    def run_scenario(self, name, scenario):

        self.get_logger().info(f"Running scenario: {name}")

        commanded = []

        for p in scenario["poses"]:
            commanded.append((p["x"], p["y"]))

        if not self.reset_to_start(scenario):

            self.get_logger().error(
                f"Could not reach the start pose for {name}; scoring it as "
                "a failure rather than against the wrong starting point"
            )

            return {
                "completed": False,
                "mean_error": float("nan"),
                "max_error": float("nan"),
                "time": 0.0,
                "passed": False,
            }

        poses = self.load_goal(scenario)

        timeout = scenario.get("timeout", 120)

        start_time = time.time()

        self.collecting = True

        try:

            if not self.send_goal(poses):
                elapsed = time.time() - start_time
            else:
                if not self.spin_until_done(timeout):

                    self.get_logger().error("Scenario timeout")

                    # Stop the robot before the next scenario is scored.
                    self.cancel_active_goal()

                    self.goal_success = False
                    self.goal_done = True

                elapsed = time.time() - start_time

        finally:

            self.collecting = False

        mean_error, max_error = (
            self.compute_cross_track_error(
                commanded,
                self.actual_path
            )
        )

        completed = self.goal_success

        pass_limit = scenario["max_cross_track"]

        passed = (
            completed
            and
            max_error <= pass_limit
        )

        return {
            "completed": completed,
            "mean_error": mean_error,
            "max_error": max_error,
            "time": elapsed,
            "passed": passed
        }

    def print_summary(
        self,
        results
    ):

        print()
        print("=" * 90)

        print(
            "{:<20} {:<10} {:<12} {:<12} {:<10} {:<8}".format(
                "Scenario",
                "Complete",
                "Mean(m)",
                "Max(m)",
                "Time(s)",
                "PASS"
            )
        )

        print("-" * 90)

        failed = False

        for name, r in results.items():

            if not r["passed"]:
                failed = True

            print(
                "{:<20} {:<10} {:<12.3f} {:<12.3f} {:<10.2f} {:<8}".format(
                    name,
                    str(r["completed"]),
                    r["mean_error"],
                    r["max_error"],
                    r["time"],
                    "PASS" if r["passed"] else "FAIL"
                )
            )

        print("=" * 90)

        return failed
    def run(self):

        results = {}

        for scenario in self.scenarios["scenarios"]:

            name = scenario["name"]

            results[name] = self.run_scenario(
                name,
                scenario
            )

        failed = self.print_summary(results)

        return failed


def main(args=None):

    rclpy.init(args=args)

    node = PathEvaluator()

    failed = False

    try:

        failed = node.run()

    except KeyboardInterrupt:

        print("\nInterrupted")

    finally:

        node.destroy_node()
        rclpy.shutdown()

    if failed:
        sys.exit(1)

    sys.exit(0)


if __name__ == "__main__":
    main()