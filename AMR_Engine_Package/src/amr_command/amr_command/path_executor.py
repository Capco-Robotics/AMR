import math

from rclpy.action import ActionClient

from geometry_msgs.msg import PoseStamped

from nav2_msgs.action import NavigateThroughPoses

class PathExecutor:

    def __init__(self, node):
        self._node = node

        self._client = ActionClient(
            node,
            NavigateThroughPoses,
            "navigate_through_poses",
        )

        self._goal_handle = None

    def send_path(self, waypoints):

        if not self._client.wait_for_server(timeout_sec=5.0):
            self._node.get_logger().error(
                "NavigateThroughPoses action server not available"
            )
            return

        goal = NavigateThroughPoses.Goal()

        goal.poses = []

        for x, y, theta in waypoints:

            pose = PoseStamped()

            pose.header.frame_id = "map"
            pose.header.stamp = self._node.get_clock().now().to_msg()

            pose.pose.position.x = float(x)
            pose.pose.position.y = float(y)
            pose.pose.position.z = 0.0

            half_theta = float(theta) / 2.0

            pose.pose.orientation.x = 0.0
            pose.pose.orientation.y = 0.0
            pose.pose.orientation.z = math.sin(half_theta)
            pose.pose.orientation.w = math.cos(half_theta)

            goal.poses.append(pose)

        future = self._client.send_goal_async(goal)

        future.add_done_callback(
            self._goal_response_callback
        )

        self._node.get_logger().info(
            f"Sent path with {len(goal.poses)} poses"
        )

    def _goal_response_callback(self, future):

        self._goal_handle = future.result()

        if not self._goal_handle.accepted:
            self._node.get_logger().error(
                "Path goal rejected"
            )
            return

        self._node.get_logger().info(
            "Path goal accepted"
        )

        result_future = self._goal_handle.get_result_async()
        result_future.add_done_callback(
            self._result_callback
        )

    def _result_callback(self, future):

        result = future.result().result

        self._node.get_logger().info(
            f"Navigation completed: {result}"
        )

        self._goal_handle = None

    def cancel_path(self):

        if self._goal_handle is not None:
            self._goal_handle.cancel_goal_async()

            self._node.get_logger().info(
                "Navigation cancel requested"
            )