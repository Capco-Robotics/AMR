"""Drives an operator-drawn path through Nav2's NavigateThroughPoses action.

Everything here is called from the websocket thread's asyncio loop (that is
where the gateway dispatches inbound frames), so nothing in this module is
allowed to block: a blocking wait stalls the loop and freezes every connected
console, not just the one that sent the frame. Readiness is therefore checked
with the non-blocking `server_is_ready()`, and every outcome is reported back
asynchronously as a `path_status` frame.
"""

import math
import time

from action_msgs.msg import GoalStatus

from rclpy.action import ActionClient

from geometry_msgs.msg import PoseStamped

from nav2_msgs.action import NavigateThroughPoses

from amr_command.path_geometry import travel_headings


# Terminal action states -> what the operator console should show.
_TERMINAL_STATES = {
    GoalStatus.STATUS_SUCCEEDED: ("succeeded", "Path complete"),
    GoalStatus.STATUS_CANCELED: ("canceled", "Path canceled"),
    GoalStatus.STATUS_ABORTED: ("aborted", "Nav2 aborted the path"),
}

# Nav2 publishes NavigateThroughPoses feedback faster than an operator can
# read it; one frame every half second is plenty and keeps the socket quiet.
_FEEDBACK_INTERVAL_SEC = 0.5


class PathExecutor:

    def __init__(self, node, status_callback):
        self._node = node

        # Called with a dict to be broadcast to the console. Injected rather
        # than reaching into the websocket server, so this class stays free of
        # asyncio and is testable on its own.
        self._status_callback = status_callback

        self._client = ActionClient(
            node,
            NavigateThroughPoses,
            "navigate_through_poses",
        )

        self._goal_handle = None
        self._last_feedback_time = 0.0

        # Every goal gets a number, and its callbacks carry that number.
        #
        # Superseding a path leaves the old goal's result callback still in
        # flight. That callback used to clear _goal_handle unconditionally --
        # so a moment after a second Run, the handle of the goal that was
        # actually driving was wiped, Stop reported "No path is running", and
        # the robot could not be stopped at all while the console still showed
        # it running. Stale callbacks are now ignored instead.
        self._generation = 0

        # True between handing a goal to the action client and hearing whether
        # it was accepted. Stop has to work in that window too, or a fast
        # Run-then-Stop leaves a goal nobody holds a handle to.
        self._pending = False

    def _status(self, state, message="", **extra):
        frame = {
            "type": "path_status",
            "state": state,
            "message": message,
        }
        frame.update(extra)

        self._status_callback(frame)

    def send_path(self, waypoints):
        """Send validated [x, y, theta] waypoints to Nav2.

        Returns True if the goal was handed to the action client. The real
        outcome arrives later as path_status frames.
        """

        # Non-blocking. The original wait_for_server(timeout_sec=5.0) ran on
        # the websocket loop, so with Nav2 down every console froze for five
        # seconds on each attempt.
        if not self._client.server_is_ready():
            self._node.get_logger().error(
                "NavigateThroughPoses action server not available"
            )
            self._status(
                "unavailable",
                "Nav2 is not running (navigate_through_poses unavailable)",
            )
            return False

        # A second path while one is running would otherwise leave the first
        # goal handle orphaned and uncancellable.
        if self._goal_handle is not None or self._pending:
            self.cancel_path(reason="Superseded by a new path")

        # Past this point the old goal's callbacks are stale and will be
        # ignored, so they cannot clear the handle this new goal is about to
        # install.
        self._generation += 1
        generation = self._generation

        self._goal_handle = None
        self._pending = True

        goal = NavigateThroughPoses.Goal()

        goal.poses = []

        # The heading that comes in is ignored, deliberately -- see
        # path_geometry.travel_headings(). The console sends 0.0 for every
        # point of a freehand route, and Nav2 enforces that as a goal
        # orientation at every waypoint, which makes the robot stop and spin
        # at each one instead of driving through.
        headings = travel_headings(waypoints)

        for (x, y, _), theta in zip(waypoints, headings):

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

        self._last_feedback_time = 0.0

        future = self._client.send_goal_async(
            goal,
            feedback_callback=(
                lambda message: self._feedback_callback(message, generation)
            ),
        )

        future.add_done_callback(
            lambda f: self._goal_response_callback(f, generation)
        )

        self._node.get_logger().info(
            f"Sent path with {len(goal.poses)} poses"
        )

        self._status(
            "sent",
            f"Sent {len(goal.poses)} waypoints to Nav2",
            poses=len(goal.poses),
        )

        return True

    def _goal_response_callback(self, future, generation):

        stale = generation != self._generation

        try:
            goal_handle = future.result()
        except Exception as e:

            if stale:
                return

            self._node.get_logger().error(f"Path goal failed: {e}")
            self._goal_handle = None
            self._pending = False
            self._status("rejected", str(e))
            return

        if stale:

            # Superseded or stopped while this goal was still being accepted.
            # Nobody is going to hold this handle, so cancel it here or it
            # drives on with no way to reach it.
            if goal_handle.accepted:

                self._node.get_logger().info(
                    "Cancelling a path goal that was superseded before it "
                    "was accepted"
                )

                goal_handle.cancel_goal_async()

            return

        self._pending = False

        if not goal_handle.accepted:
            self._node.get_logger().error("Path goal rejected")
            self._goal_handle = None
            self._status("rejected", "Nav2 rejected the path")
            return

        self._goal_handle = goal_handle

        self._node.get_logger().info("Path goal accepted")
        self._status("accepted", "Nav2 accepted the path")

        result_future = goal_handle.get_result_async()
        result_future.add_done_callback(
            lambda f: self._result_callback(f, generation)
        )

    def _feedback_callback(self, feedback_message, generation):

        # Feedback from a superseded goal would otherwise keep overwriting the
        # console's status with the old run's progress.
        if generation != self._generation:
            return

        now = time.monotonic()

        if (now - self._last_feedback_time) < _FEEDBACK_INTERVAL_SEC:
            return

        self._last_feedback_time = now

        feedback = feedback_message.feedback

        self._status(
            "executing",
            "Following path",
            poses_remaining=int(feedback.number_of_poses_remaining),
            distance_remaining=round(float(feedback.distance_remaining), 3),
            recoveries=int(feedback.number_of_recoveries),
        )

    def _result_callback(self, future, generation):

        # The whole point of the generation guard: this used to clear the
        # handle of whichever goal was current, including one that had just
        # replaced this finished goal.
        if generation != self._generation:
            return

        self._goal_handle = None
        self._pending = False

        try:
            response = future.result()
        except Exception as e:
            self._node.get_logger().error(f"Path result failed: {e}")
            self._status("aborted", str(e))
            return

        # response.result is an empty message for this action -- all the
        # outcome information lives in response.status. Logging only .result
        # reported an aborted run as a success.
        state, message = _TERMINAL_STATES.get(
            response.status,
            ("unknown", f"Navigation ended with status {response.status}"),
        )

        if state == "succeeded":
            self._node.get_logger().info(f"Navigation {state}")
        else:
            self._node.get_logger().warning(f"Navigation {state}: {message}")

        self._status(state, message)

    def cancel_path(self, reason="Cancel requested by operator"):

        if self._goal_handle is None:

            if not self._pending:
                self._status("idle", "No path is running")
                return False

            # Sent but not yet accepted. Retiring the generation makes the
            # response callback cancel it the moment it arrives, so Stop works
            # even in that window instead of silently doing nothing.
            self._generation += 1
            self._pending = False

            self._node.get_logger().info(
                "Navigation cancel requested before the goal was accepted"
            )

            self._status("canceling", reason)

            return True

        self._goal_handle.cancel_goal_async()

        self._node.get_logger().info("Navigation cancel requested")
        self._status("canceling", reason)

        return True
