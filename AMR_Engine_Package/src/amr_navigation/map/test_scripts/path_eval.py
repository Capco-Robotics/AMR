#!/usr/bin/env python3

import math
import time
import yaml
import sys
from pathlib import Path

import rclpy
from rclpy.node import Node
from rclpy.action import ActionClient

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

        self.goal_done = False
        self.goal_success = False

        self.feedback_remaining = None
        self.feedback_distance = None

        self.goal_handle = None
        self.result_future = None

        scenario_file = (
            Path(__file__).resolve().parent.parent
            / "config"
            / "path_eval_scenarios.yaml"
        )

        with open(scenario_file, "r") as f:
            self.scenarios = yaml.safe_load(f)

    def odom_callback(self, msg):

        x = msg.pose.pose.position.x
        y = msg.pose.pose.position.y

        self.current_pose = (x, y)

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

        self.actual_path = []

        self.client.wait_for_server()

        future = self.client.send_goal_async(
            goal,
            feedback_callback=self.feedback_callback
        )

        future.add_done_callback(self.goal_response_callback)

    def goal_response_callback(self, future):

        self.goal_handle = future.result()

        if not self.goal_handle.accepted:

            self.get_logger().error("Goal rejected")

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

        poses = self.load_goal(scenario)

        start_time = time.time()

        self.send_goal(poses)

        timeout = scenario.get("timeout", 120)

        while rclpy.ok():

            rclpy.spin_once(self, timeout_sec=0.1)

            if self.goal_done:
                break

            if time.time() - start_time > timeout:

                self.get_logger().error(
                    "Scenario timeout"
                )

                self.goal_success = False
                self.goal_done = True
                break

        elapsed = time.time() - start_time

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