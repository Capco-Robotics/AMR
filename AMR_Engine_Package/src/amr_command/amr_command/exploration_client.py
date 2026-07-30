"""Drives the map builder: amr_navigation_explore's ExploreArea action.

The same shape, and the same constraints, as path_executor.py. Everything here
is called from the websocket thread's asyncio loop, so nothing may block --
a blocking wait freezes every connected console, not just the one that pressed
Start. Readiness is checked with the non-blocking `server_is_ready()` and every
outcome comes back later as an `explore_status` frame.

One exploration runs at a time. The explorer node enforces that too (it
rejects a second goal), but holding the goal handle here is what lets Stop
work and what stops the console from showing two overlapping runs.
"""

import math

from action_msgs.msg import GoalStatus

from rclpy.action import ActionClient

from amr_msgs.action import ExploreArea


# Terminal action states -> what the console should show. Note that a run the
# operator stopped, and one that hit its time limit, both come back as
# SUCCEEDED with success=False in the result: the node reserves ABORTED for a
# genuine fault, so that a normal Stop does not look like a crash.
_TERMINAL_STATES = {
    GoalStatus.STATUS_SUCCEEDED: "finished",
    GoalStatus.STATUS_CANCELED: "canceled",
    GoalStatus.STATUS_ABORTED: "aborted",
}

# Feedback arrives twice a second; that is already the rate an operator can
# read, so it is forwarded as-is rather than decimated again.


class ExplorationClient:

    def __init__(self, node, status_callback, on_complete=None):

        self._node = node

        # Called with a dict to broadcast. Injected rather than reaching into
        # the websocket server, so this class stays free of asyncio.
        self._status_callback = status_callback

        # Called as on_complete(success) when a run ends, so the gateway can
        # do whatever the operator asked for afterwards -- saving the map.
        self._on_complete = on_complete

        self._client = ActionClient(
            node,
            ExploreArea,
            "explore_area",
        )

        self._goal_handle = None
        self._running = False

        # Last feedback seen, so a console that connects mid-run gets the
        # current picture instead of an empty panel until the next frame.
        self._last_status = {
            "type": "explore_status",
            "state": "idle",
            "message": "",
            "running": False,
        }

    def is_running(self):
        return self._running

    def last_status(self):
        return dict(self._last_status)

    def _status(self, state, message="", **extra):

        frame = {
            "type": "explore_status",
            "state": state,
            "message": message,
            "running": self._running,
        }

        frame.update(extra)

        self._last_status = frame

        self._status_callback(frame)

    def start(self, max_duration_sec=0.0, min_frontier_size=0.0,
              return_to_start=True):
        """Ask the explorer to map the area. Returns True if the goal was sent."""

        if self._running:
            self._status(
                "rejected",
                "Already building a map",
            )
            return False

        if not self._client.server_is_ready():
            self._node.get_logger().error(
                "explore_area action server not available"
            )
            self._status(
                "unavailable",
                "The map builder is not running (explore_area unavailable)",
            )
            return False

        goal = ExploreArea.Goal()

        # A non-finite value here reaches the node as a nonsense limit that
        # either never fires or fires immediately, so clamp rather than trust.
        goal.max_duration_sec = (
            float(max_duration_sec)
            if math.isfinite(max_duration_sec) and max_duration_sec > 0.0
            else 0.0
        )

        goal.min_frontier_size = (
            float(min_frontier_size)
            if math.isfinite(min_frontier_size) and min_frontier_size > 0.0
            else 0.0
        )

        goal.return_to_start = bool(return_to_start)

        # Set before the goal is accepted: a second explore_start arriving in
        # the gap between send and acceptance would otherwise sail through the
        # guard above and leave two runs fighting over one robot.
        self._running = True

        future = self._client.send_goal_async(
            goal,
            feedback_callback=self._feedback_callback,
        )

        future.add_done_callback(self._goal_response_callback)

        self._node.get_logger().info("Map building requested")

        self._status("sent", "Starting the map builder")

        return True

    def _goal_response_callback(self, future):

        try:
            goal_handle = future.result()
        except Exception as e:
            self._node.get_logger().error(f"Explore goal failed: {e}")
            self._running = False
            self._goal_handle = None
            self._status("rejected", str(e))
            return

        if not goal_handle.accepted:
            self._node.get_logger().error("Explore goal rejected")
            self._running = False
            self._goal_handle = None
            self._status("rejected", "The map builder refused to start")
            return

        self._goal_handle = goal_handle

        self._node.get_logger().info("Map building accepted")

        self._status("accepted", "Building the map")

        result_future = goal_handle.get_result_async()
        result_future.add_done_callback(self._result_callback)

    def _feedback_callback(self, feedback_message):

        feedback = feedback_message.feedback

        extra = {
            "frontiers_remaining": int(feedback.frontiers_remaining),
            "frontiers_visited": int(feedback.frontiers_visited),
            "explored_area_m2": round(float(feedback.explored_area_m2), 2),
            "percent_explored": round(float(feedback.percent_explored), 1),
            "elapsed_sec": round(float(feedback.elapsed_sec), 1),
        }

        # (0, 0) is the node's "no target" sentinel rather than a real place to
        # drive to, so it must not be drawn on the map as one.
        if feedback.target_x != 0.0 or feedback.target_y != 0.0:

            extra["target"] = [
                round(float(feedback.target_x), 3),
                round(float(feedback.target_y), 3),
            ]

            extra["distance_to_target"] = round(
                float(feedback.distance_to_target), 2
            )

        self._status(
            feedback.state or "exploring",
            feedback.message,
            **extra,
        )

    def _result_callback(self, future):

        self._goal_handle = None
        self._running = False

        try:
            response = future.result()
        except Exception as e:
            self._node.get_logger().error(f"Explore result failed: {e}")
            self._status("aborted", str(e))
            self._notify_complete(False)
            return

        result = response.result

        state = _TERMINAL_STATES.get(
            response.status,
            "unknown",
        )

        # A finished run that did not finish the job -- stopped, or out of time
        # -- is reported as "stopped" rather than "complete", so the console
        # does not tell the operator the building is mapped when it is not.
        if state == "finished":
            state = "complete" if result.success else "stopped"

        message = result.message or f"Map building {state}"

        if state == "complete":
            self._node.get_logger().info(f"Map building complete: {message}")
        else:
            self._node.get_logger().warning(f"Map building {state}: {message}")

        self._status(
            state,
            message,
            frontiers_visited=int(result.frontiers_visited),
            explored_area_m2=round(float(result.explored_area_m2), 2),
            duration_sec=round(float(result.duration_sec), 1),
        )

        self._notify_complete(state == "complete")

    def _notify_complete(self, success):

        if self._on_complete is None:
            return

        try:
            self._on_complete(success)
        except Exception as e:
            self._node.get_logger().error(
                f"Post-exploration step failed: {e}"
            )

    def stop(self, reason="Stopped by the operator"):

        if self._goal_handle is None:

            # Covers both "never started" and "sent but not yet accepted".
            # Clearing the flag in the second case matters: without it a
            # rejected-then-stopped sequence would leave the console with a
            # Start button that refuses forever.
            self._running = False

            self._status("idle", "The map builder is not running")

            return False

        self._goal_handle.cancel_goal_async()

        self._node.get_logger().info("Map building cancel requested")

        self._status("canceling", reason)

        return True
