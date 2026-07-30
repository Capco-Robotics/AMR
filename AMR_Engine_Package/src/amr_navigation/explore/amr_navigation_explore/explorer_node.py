"""Autonomous map building: drive to the nearest worthwhile unknown, repeat.

Exposes one action, `explore_area` (amr_msgs/ExploreArea). While a goal is
active this node picks the best frontier on the live SLAM map (see
`frontier_search.py`), drives to it through Nav2's `navigate_to_pose`, and
picks again -- until no frontier is left, the operator cancels, or the time
limit runs out. SLAM Toolbox is what actually builds the map; this node only
decides where to stand.

Threading
---------

The action's execute callback is a long-running loop, so this node is spun on
a MultiThreadedExecutor with every callback in one reentrant group. That lets
map updates, TF, and the Nav2 client's own callbacks keep arriving while the
loop is inside a sleep -- on the default single-threaded executor the loop
would starve the very subscriptions it is waiting on, and the map it planned
against would never change.

`_lock` guards the handful of fields written from subscription callbacks and
read from the loop. Everything else belongs to whichever thread made it.

Why not m-explore / nav2_wfd
----------------------------

Both are external packages that would have to be installed on every robot and
every developer's machine. The frontier maths is ~300 lines of grid walking,
this stack already hand-rolls that kind of thing (`keepout_zones.py`,
`map_encoder.py`), and doing it here means exploration honours the operator's
keep-out zones -- which an off-the-shelf explorer has no way to know about.
"""

import math
import threading
import time

import rclpy

from rclpy.action import ActionClient, ActionServer, CancelResponse, GoalResponse
from rclpy.callback_groups import ReentrantCallbackGroup
from rclpy.duration import Duration
from rclpy.executors import MultiThreadedExecutor
from rclpy.node import Node
from rclpy.qos import (
    DurabilityPolicy,
    HistoryPolicy,
    QoSProfile,
    ReliabilityPolicy,
)

from action_msgs.msg import GoalStatus

from geometry_msgs.msg import Pose, PoseArray
from nav_msgs.msg import OccupancyGrid, Odometry

from nav2_msgs.action import NavigateToPose

import tf2_ros

from amr_msgs.action import ExploreArea

from amr_navigation_explore import frontier_search


# How often the loop wakes up. Short enough to notice a finished Nav2 goal
# promptly, long enough not to spin a core.
_TICK_SEC = 0.2

# Feedback rate. Nav2's own feedback is faster than an operator can read.
_FEEDBACK_INTERVAL_SEC = 0.5

# Nav2 goal states this node tracks, kept separate from the action's own
# GoalStatus so a goal we abandoned mid-flight can be told apart from one that
# reached a terminal state on its own.
_NAV_IDLE = "idle"
_NAV_PENDING = "pending"
_NAV_ACTIVE = "active"
_NAV_SUCCEEDED = "succeeded"
_NAV_FAILED = "failed"
_NAV_CANCELED = "canceled"


class ExplorerNode(Node):

    def __init__(self):
        super().__init__("amr_explorer")

        callbacks = ReentrantCallbackGroup()

        # --- tuning ------------------------------------------------------
        #
        # Defaults suit the differential-drive AMR on a 5 cm SLAM grid. The
        # two worth revisiting per site are min_frontier_size (how small an
        # unexplored gap is worth a trip) and robot_radius (how much room a
        # goal needs), which together decide whether exploration finishes
        # tidily or keeps chasing slivers behind furniture.

        self.declare_parameter("min_frontier_size", 0.35)

        # Clearance a goal must have at minimum. Under nav2_params.yaml's
        # 0.45 m inflation radius on purpose, so a genuinely narrow frontier
        # is still reachable rather than dropped.
        self.declare_parameter("robot_radius", 0.30)

        # ...and the clearance a goal gets when the frontier can offer it,
        # which is almost always. Matched to the costmap's inflation radius:
        # inside that band Nav2 charges a steep cost, the controller crawls,
        # and an unattended robot ends up grinding along a wall for minutes
        # instead of exploring. Only frontiers where nothing is this roomy
        # fall back to robot_radius.
        self.declare_parameter("preferred_clearance", 0.45)

        # Frontier ranking: worth going to when it is big, worth skipping when
        # it is far. See frontier_search.search().
        self.declare_parameter("size_weight", 2.0)
        self.declare_parameter("distance_weight", 1.0)

        # How much frontier length is worth counting. A frontier is scored on
        # how much unknown it fronts, but that is the *perimeter* of unexplored
        # space, which early on is the whole edge of the map -- tens of metres,
        # against a distance term of a few. Unsaturated, the robot drove past
        # unexplored space at its feet to reach a nominally bigger frontier
        # across the building. Roughly one sensor sweep's worth, since that is
        # all it can actually reveal on arrival.
        self.declare_parameter("size_saturation", 3.0)

        # How often to re-run the search while already driving somewhere. The
        # search is O(cells) pure Python, so on a large map this is the most
        # expensive thing the node does -- 2 s keeps it well clear of the
        # executor while still reacting to a frontier that got mapped by a
        # passing glance.
        self.declare_parameter("replan_interval_sec", 2.0)

        # After arriving, give SLAM a moment to integrate the scans taken from
        # the new spot before deciding where to go next. Without this the
        # search runs on a map that does not yet include what the robot is
        # looking at, and it turns straight back around.
        self.declare_parameter("settle_time_sec", 2.0)

        # Nav2 can spend a long time recovering rather than admitting defeat.
        # Every progress_timeout_sec the robot has to have closed at least
        # min_progress_distance of the gap to its target, or the frontier is
        # treated as unreachable and another is chosen.
        #
        # Measured per window rather than "has it improved at all since last
        # time": a robot scraping along a wall gains a few centimetres every
        # tick, which resets an improvement-based timer forever. It was
        # observed covering 0.5 m in 28 s and never timing out.
        self.declare_parameter("progress_timeout_sec", 30.0)
        self.declare_parameter("min_progress_distance", 1.0)

        # A failed frontier and everything within this radius is skipped for
        # the rest of the run. Wide enough that the next pick is a genuinely
        # different place rather than the cell next door.
        self.declare_parameter("blacklist_radius", 0.6)

        # How far the frontier being driven to is allowed to move before the
        # trip is abandoned and a new one chosen. It moves constantly: every
        # search picks a fresh cell on a boundary that is itself retreating as
        # the robot maps it. Testing this at the blacklist radius made the
        # robot re-target every couple of seconds and skitter between opposite
        # ends of the building; at 1.5 m it follows a frontier until that
        # frontier is genuinely gone.
        self.declare_parameter("target_reuse_radius", 1.5)

        # A frontier the robot got this close to counts as visited even if
        # Nav2 reports otherwise -- the point was to look, and it has looked.
        self.declare_parameter("goal_tolerance", 0.40)

        # ...which is exactly why a goal cannot be chosen inside that radius.
        # At the start of a run the explored area is one blob whose entire
        # boundary is a single frontier beginning centimetres from the robot;
        # picking the nearest point on it means arriving without moving,
        # forever. Comfortably above goal_tolerance so the two cannot meet.
        self.declare_parameter("min_goal_distance", 0.75)

        # Zero frontiers once can just mean the map has not caught up. Requiring
        # a few consecutive empty searches avoids declaring the building mapped
        # because one scan arrived late.
        self.declare_parameter("empty_confirmations", 3)

        self.declare_parameter("occupied_threshold", 50)

        self.declare_parameter("global_frame", "map")
        self.declare_parameter("robot_base_frame", "base_link")

        self._reload_parameters()

        # --- state shared with subscription callbacks --------------------

        self._lock = threading.Lock()

        self._map = None
        self._keepout = None
        self._odom_pose = None

        # --- exploration state (loop thread only) ------------------------

        self._nav_state = _NAV_IDLE
        self._nav_goal_handle = None

        # Every Nav2 goal gets a number, and its callbacks carry that number.
        # Cancelling a goal to chase a better frontier leaves its result
        # callback still in flight; without this the late "canceled" would be
        # applied to the goal that replaced it.
        self._nav_generation = 0

        self._target = None
        self._target_started_at = 0.0
        self._target_size_m = 0.0
        self._best_distance = math.inf
        self._last_progress_at = 0.0

        self._blacklist = []
        self._frontiers_visited = 0

        # --- ROS interfaces ----------------------------------------------

        self.tf_buffer = tf2_ros.Buffer()
        self.tf_listener = tf2_ros.TransformListener(self.tf_buffer, self)

        self.create_subscription(
            OccupancyGrid,
            "/map",
            self._map_callback,
            10,
            callback_group=callbacks,
        )

        # The gateway publishes the keep-out mask latched, so a subscriber that
        # comes up later still receives the current one. Matching durability
        # here is what makes that work -- with volatile QoS this node would
        # only ever see zones edited after it started.
        latched = QoSProfile(
            depth=1,
            history=HistoryPolicy.KEEP_LAST,
            reliability=ReliabilityPolicy.RELIABLE,
            durability=DurabilityPolicy.TRANSIENT_LOCAL,
        )

        self.create_subscription(
            OccupancyGrid,
            "/keepout_filter_mask",
            self._keepout_callback,
            latched,
            callback_group=callbacks,
        )

        # Fallback pose source for a rig with no map->odom transform yet.
        self.create_subscription(
            Odometry,
            "/odom",
            self._odom_callback,
            10,
            callback_group=callbacks,
        )

        # Frontier candidates, for RViz. PoseArray rather than a MarkerArray
        # so nothing has to depend on visualization_msgs to see them.
        self.frontier_pub = self.create_publisher(
            PoseArray,
            "/explore/frontiers",
            10,
        )

        self.nav_client = ActionClient(
            self,
            NavigateToPose,
            "navigate_to_pose",
            callback_group=callbacks,
        )

        self.action_server = ActionServer(
            self,
            ExploreArea,
            "explore_area",
            execute_callback=self._execute,
            goal_callback=self._on_goal_request,
            cancel_callback=self._on_cancel_request,
            callback_group=callbacks,
        )

        self._exploring = False

        self.get_logger().info("ExplorerNode ready (action: explore_area)")

    # ---- parameters -----------------------------------------------------

    def _reload_parameters(self):
        """Snapshot every parameter into a plain attribute.

        Read once per run rather than per tick: a parameter changed halfway
        through an exploration would otherwise silently alter the ranking the
        run started with.
        """

        get = self.get_parameter

        self.min_frontier_size = float(get("min_frontier_size").value)
        self.robot_radius = float(get("robot_radius").value)
        self.preferred_clearance = float(get("preferred_clearance").value)
        self.size_weight = float(get("size_weight").value)
        self.distance_weight = float(get("distance_weight").value)
        self.size_saturation = float(get("size_saturation").value)
        self.replan_interval_sec = float(get("replan_interval_sec").value)
        self.settle_time_sec = float(get("settle_time_sec").value)
        self.progress_timeout_sec = float(get("progress_timeout_sec").value)
        self.min_progress_distance = float(get("min_progress_distance").value)
        self.blacklist_radius = float(get("blacklist_radius").value)
        self.target_reuse_radius = float(get("target_reuse_radius").value)
        self.goal_tolerance = float(get("goal_tolerance").value)
        self.min_goal_distance = float(get("min_goal_distance").value)
        self.empty_confirmations = int(get("empty_confirmations").value)
        self.occupied_threshold = int(get("occupied_threshold").value)
        self.global_frame = str(get("global_frame").value)
        self.robot_base_frame = str(get("robot_base_frame").value)

    # ---- subscriptions --------------------------------------------------

    def _map_callback(self, msg):
        with self._lock:
            self._map = msg

    def _keepout_callback(self, msg):
        with self._lock:
            self._keepout = msg

    def _odom_callback(self, msg):

        pose = msg.pose.pose

        q = pose.orientation

        yaw = math.atan2(
            2.0 * (q.w * q.z + q.x * q.y),
            1.0 - 2.0 * (q.y * q.y + q.z * q.z),
        )

        with self._lock:
            self._odom_pose = (pose.position.x, pose.position.y, yaw)

    def _robot_pose(self):
        """(x, y, yaw) in the map frame, or None.

        TF first: SLAM corrects the robot's map-frame position by moving
        map->odom, so raw odometry drifts away from the map the frontiers were
        found on. Odometry is only the fallback for a rig where SLAM has not
        published a transform yet, where the two frames coincide anyway.
        """

        try:

            transform = self.tf_buffer.lookup_transform(
                self.global_frame,
                self.robot_base_frame,
                rclpy.time.Time(),
                timeout=Duration(seconds=0.2),
            )

            translation = transform.transform.translation
            q = transform.transform.rotation

            yaw = math.atan2(
                2.0 * (q.w * q.z + q.x * q.y),
                1.0 - 2.0 * (q.y * q.y + q.z * q.z),
            )

            return (translation.x, translation.y, yaw)

        except Exception:

            with self._lock:
                return self._odom_pose

    # ---- action plumbing ------------------------------------------------

    def _on_goal_request(self, goal_request):
        """One exploration at a time.

        Accepting a second would leave two loops fighting over the same Nav2
        client, each cancelling the other's goals.
        """

        if self._exploring:
            self.get_logger().warning(
                "Rejected explore goal: already exploring"
            )
            return GoalResponse.REJECT

        return GoalResponse.ACCEPT

    def _on_cancel_request(self, goal_handle):
        return CancelResponse.ACCEPT

    # ---- the run --------------------------------------------------------

    def _execute(self, goal_handle):

        request = goal_handle.request

        self._exploring = True
        self._reload_parameters()

        # A goal-supplied override wins over the parameter, but only for this
        # run -- 0 means "whatever the node is configured with".
        if request.min_frontier_size > 0.0:
            self.min_frontier_size = float(request.min_frontier_size)

        self._blacklist = []
        self._frontiers_visited = 0
        self._target = None
        self._target_size_m = 0.0
        self._nav_state = _NAV_IDLE
        self._nav_goal_handle = None

        started_at = time.monotonic()

        last_feedback_at = 0.0
        last_search_at = 0.0
        settle_until = 0.0

        empty_searches = 0

        frontiers = []
        stats = {}

        start_pose = self._robot_pose()

        self.get_logger().info(
            "Exploration started "
            f"(min_frontier_size={self.min_frontier_size:.2f} m, "
            f"return_to_start={request.return_to_start}, "
            f"max_duration={request.max_duration_sec:.0f} s)"
        )

        state = "waiting_for_map"
        message = "Waiting for the map"

        outcome = None

        try:

            while rclpy.ok():

                now = time.monotonic()
                elapsed = now - started_at

                # --- operator cancelled -------------------------------
                if goal_handle.is_cancel_requested:
                    outcome = ("canceled", "Stopped by the operator")
                    break

                # --- time limit ---------------------------------------
                if (
                    request.max_duration_sec > 0.0
                    and elapsed >= request.max_duration_sec
                ):
                    outcome = (
                        "timeout",
                        f"Stopped after the {request.max_duration_sec:.0f} s limit",
                    )
                    break

                grid, keepout = self._snapshot_grid()
                pose = self._robot_pose()

                if grid is None or pose is None:

                    state = "waiting_for_map"
                    message = (
                        "Waiting for the map"
                        if grid is None
                        else "Waiting for the robot's position"
                    )

                    last_feedback_at = self._maybe_feedback(
                        goal_handle, state, message, frontiers, stats,
                        elapsed, last_feedback_at,
                    )

                    time.sleep(_TICK_SEC)
                    continue

                # --- watch the goal Nav2 is currently driving to -------

                if self._nav_state in (_NAV_PENDING, _NAV_ACTIVE):

                    reached = self._check_arrival(pose)

                    if reached:
                        settle_until = now + self.settle_time_sec

                    else:
                        self._check_progress(pose, now)

                elif self._nav_state == _NAV_SUCCEEDED:

                    self._frontiers_visited += 1
                    self.get_logger().info("Reached frontier")

                    self._clear_target()
                    settle_until = now + self.settle_time_sec

                elif self._nav_state in (_NAV_FAILED, _NAV_CANCELED):

                    if self._nav_state == _NAV_FAILED and self._target:

                        # Nav2 could not get there. Something the map does not
                        # show is in the way, so stop offering that spot.
                        self._blacklist.append(self._target)

                        self.get_logger().warning(
                            "Nav2 could not reach "
                            f"({self._target[0]:.2f}, {self._target[1]:.2f}) "
                            "-- blacklisted"
                        )

                    self._clear_target()

                # --- pick somewhere to go -----------------------------

                due = (now - last_search_at) >= self.replan_interval_sec

                if due and now >= settle_until:

                    last_search_at = now

                    frontiers, stats = frontier_search.search(
                        grid,
                        (pose[0], pose[1]),
                        min_frontier_size_m=self.min_frontier_size,
                        robot_radius_m=self.robot_radius,
                        preferred_radius_m=self.preferred_clearance,
                        min_goal_distance_m=self.min_goal_distance,
                        size_saturation_m=self.size_saturation,
                        blacklist=self._blacklist,
                        blacklist_radius_m=self.blacklist_radius,
                        distance_weight=self.distance_weight,
                        size_weight=self.size_weight,
                        keepout=keepout,
                        keepout_threshold=self.occupied_threshold,
                    )

                    self._publish_frontiers(frontiers)

                    if frontiers:

                        empty_searches = 0

                        if self._target is None:

                            self._send_nav_goal(frontiers[0], pose)

                        elif self._target_is_stale(frontiers):

                            # What we were driving to has been mapped from
                            # somewhere else (a passing glance down a corridor
                            # does this constantly). Finishing the trip would
                            # just park the robot in explored space -- and the
                            # frontier is gone, which is the whole point, so it
                            # counts as one dealt with.
                            self.get_logger().info(
                                "Target already mapped -- switching frontier"
                            )

                            self._frontiers_visited += 1

                            self._cancel_nav_goal()
                            self._send_nav_goal(frontiers[0], pose)

                    else:

                        empty_searches += 1

                        if empty_searches >= self.empty_confirmations:
                            outcome = ("complete", "Nothing left to explore")
                            break

                # Derived every tick from what is actually true now. Setting
                # these only where a goal is sent left the console showing the
                # first frontier's description for the whole run.
                state, message = self._describe(frontiers, empty_searches)

                last_feedback_at = self._maybe_feedback(
                    goal_handle, state, message, frontiers, stats,
                    elapsed, last_feedback_at,
                )

                time.sleep(_TICK_SEC)

            else:
                # rclpy shut down under us.
                outcome = ("canceled", "Node is shutting down")

        finally:
            self._cancel_nav_goal()

        # --- wrap up -----------------------------------------------------

        reason, message = outcome or ("canceled", "Exploration ended")

        if (
            reason == "complete"
            and request.return_to_start
            and start_pose is not None
            and rclpy.ok()
            and not goal_handle.is_cancel_requested
        ):
            self._return_to_start(goal_handle, start_pose, started_at, stats)

        self._publish_frontiers([])
        self._exploring = False

        result = ExploreArea.Result()

        result.success = reason == "complete"
        result.message = message
        result.frontiers_visited = self._frontiers_visited
        result.explored_area_m2 = float(stats.get("explored_area_m2", 0.0))
        result.duration_sec = float(time.monotonic() - started_at)

        if goal_handle.is_cancel_requested:
            goal_handle.canceled()
        elif result.success:
            goal_handle.succeed()
        else:
            # "Stopped early" is not a crash: the operator asked for it, or
            # the clock ran out. Abort would make the console shout about a
            # failure that did not happen, so a cancel-shaped end is reported
            # as one and only a genuine fault aborts.
            if reason == "failed":
                goal_handle.abort()
            else:
                goal_handle.succeed()

        self.get_logger().info(
            f"Exploration finished: {message} "
            f"({self._frontiers_visited} frontiers, "
            f"{result.explored_area_m2:.1f} m2, {result.duration_sec:.0f} s)"
        )

        return result

    # ---- map snapshot ---------------------------------------------------

    def _snapshot_grid(self):
        """Classify the latest map, plus an aligned keep-out mask if there is one."""

        with self._lock:
            map_msg = self._map
            keepout_msg = self._keepout

        if map_msg is None:
            return (None, None)

        info = map_msg.info

        if info.width == 0 or info.height == 0 or info.resolution <= 0.0:
            return (None, None)

        grid = frontier_search.Grid(
            map_msg.data,
            info.width,
            info.height,
            info.resolution,
            info.origin.position.x,
            info.origin.position.y,
            occupied_threshold=self.occupied_threshold,
        )

        keepout = None

        if keepout_msg is not None:

            k = keepout_msg.info

            # The gateway rasterises the mask onto the map's own geometry, so
            # these normally match. They briefly do not while a growing SLAM
            # map re-origins itself; using a misaligned mask would put the
            # no-go areas metres from where the operator drew them, so skip it
            # for the tick or two until the gateway republishes.
            aligned = (
                k.width == info.width
                and k.height == info.height
                and abs(k.resolution - info.resolution) < 1e-6
                and abs(k.origin.position.x - info.origin.position.x) < 1e-6
                and abs(k.origin.position.y - info.origin.position.y) < 1e-6
            )

            if aligned:
                keepout = keepout_msg.data

        return (grid, keepout)

    # ---- Nav2 goals -----------------------------------------------------

    def _send_nav_goal(self, frontier, pose):

        if not self.nav_client.server_is_ready():
            self.get_logger().warning(
                "navigate_to_pose is not available -- waiting"
            )
            return False

        x, y = frontier.goal

        # The search keeps goals clear of the robot, but it falls back to the
        # farthest cell on a frontier when the whole thing is underfoot. Such
        # a goal would be "reached" the instant it was sent, and picked again
        # on the next search, and again. Blacklisting it costs one frontier
        # the robot is standing on anyway, and the run keeps moving.
        if math.hypot(x - pose[0], y - pose[1]) <= self.goal_tolerance:

            self.get_logger().info(
                f"Frontier at ({x:.2f}, {y:.2f}) is already underfoot "
                "-- skipping it"
            )

            self._blacklist.append((float(x), float(y)))

            return False

        goal = NavigateToPose.Goal()

        goal.pose.header.frame_id = self.global_frame
        goal.pose.header.stamp = self.get_clock().now().to_msg()

        goal.pose.pose.position.x = float(x)
        goal.pose.pose.position.y = float(y)

        # Face the frontier on arrival, so the lidar sweeps the unknown the
        # trip was for rather than whatever happens to be behind the robot.
        yaw = math.atan2(y - pose[1], x - pose[0])

        goal.pose.pose.orientation.z = math.sin(yaw / 2.0)
        goal.pose.pose.orientation.w = math.cos(yaw / 2.0)

        self._nav_generation += 1
        generation = self._nav_generation

        self._target = (float(x), float(y))
        self._target_started_at = time.monotonic()
        self._target_size_m = float(frontier.size_m)
        self._best_distance = math.hypot(x - pose[0], y - pose[1])
        self._last_progress_at = time.monotonic()

        self._nav_state = _NAV_PENDING

        future = self.nav_client.send_goal_async(goal)

        future.add_done_callback(
            lambda f: self._nav_goal_response(f, generation)
        )

        self.get_logger().info(
            f"Heading for frontier at ({x:.2f}, {y:.2f}): "
            f"{frontier.size_m:.2f} m wide, {frontier.distance_m:.2f} m away"
        )

        return True

    def _nav_goal_response(self, future, generation):

        if generation != self._nav_generation:
            return

        try:
            goal_handle = future.result()
        except Exception as e:
            self.get_logger().error(f"Nav2 goal failed: {e}")
            self._nav_state = _NAV_FAILED
            return

        if not goal_handle.accepted:
            self.get_logger().warning("Nav2 rejected the frontier goal")
            self._nav_state = _NAV_FAILED
            return

        self._nav_goal_handle = goal_handle
        self._nav_state = _NAV_ACTIVE

        result_future = goal_handle.get_result_async()

        result_future.add_done_callback(
            lambda f: self._nav_result(f, generation)
        )

    def _nav_result(self, future, generation):

        if generation != self._nav_generation:
            # Belongs to a goal we already moved on from.
            return

        self._nav_goal_handle = None

        try:
            status = future.result().status
        except Exception as e:
            self.get_logger().error(f"Nav2 result failed: {e}")
            self._nav_state = _NAV_FAILED
            return

        if status == GoalStatus.STATUS_SUCCEEDED:
            self._nav_state = _NAV_SUCCEEDED
        elif status == GoalStatus.STATUS_CANCELED:
            self._nav_state = _NAV_CANCELED
        else:
            self._nav_state = _NAV_FAILED

    def _cancel_nav_goal(self):

        handle = self._nav_goal_handle

        # Bumping the generation first makes every callback still in flight for
        # this goal a no-op, so a late result cannot resurrect a target the
        # loop has already given up on.
        self._nav_generation += 1

        self._nav_goal_handle = None
        self._nav_state = _NAV_IDLE
        self._target = None
        self._target_size_m = 0.0

        if handle is not None:
            try:
                handle.cancel_goal_async()
            except Exception as e:
                self.get_logger().warning(f"Nav2 cancel failed: {e}")

    def _clear_target(self):
        self._nav_state = _NAV_IDLE
        self._nav_goal_handle = None
        self._target = None
        self._target_size_m = 0.0

    def _check_arrival(self, pose):
        """True when the robot is close enough to call the frontier visited.

        Nav2's own goal checker is stricter than exploration needs. The point
        of the trip is to see what is behind the frontier, and the lidar has
        done that from within tolerance -- waiting for a precise pose costs a
        slow final approach at every single frontier.
        """

        if self._target is None:
            return False

        distance = math.hypot(
            self._target[0] - pose[0],
            self._target[1] - pose[1],
        )

        if distance > self.goal_tolerance:
            return False

        self.get_logger().info(
            f"Within {distance:.2f} m of the frontier -- close enough"
        )

        self._frontiers_visited += 1
        self._cancel_nav_goal()

        return True

    def _check_progress(self, pose, now):
        """Give up on a frontier the robot is not meaningfully closing on.

        Judged over a whole window: at the end of every progress_timeout_sec,
        the gap must have shrunk by min_progress_distance. Asking instead
        whether it improved *since the last check* lets a robot grinding along
        a wall reset the timer forever on a centimetre a tick.
        """

        if self._target is None or self.progress_timeout_sec <= 0.0:
            return

        distance = math.hypot(
            self._target[0] - pose[0],
            self._target[1] - pose[1],
        )

        elapsed = now - self._last_progress_at

        if elapsed < self.progress_timeout_sec:
            return

        closed = self._best_distance - distance

        if closed >= self.min_progress_distance:

            # Good enough. Start a fresh window from where it is now.
            self._best_distance = distance
            self._last_progress_at = now

            return

        self.get_logger().warning(
            f"Only closed {closed:.2f} m towards ({self._target[0]:.2f}, "
            f"{self._target[1]:.2f}) in {elapsed:.0f} s "
            "-- blacklisted"
        )

        self._blacklist.append(self._target)
        self._cancel_nav_goal()

    def _describe(self, frontiers, empty_searches):
        """What the console should say the robot is doing, right now."""

        if self._target is not None:

            if self._target_size_m > 0.0:
                return (
                    "driving",
                    f"Driving to a {self._target_size_m:.1f} m frontier",
                )

            return ("driving", "Driving to a frontier")

        if empty_searches:
            return ("settling", "No frontier found -- confirming")

        if frontiers:
            return ("exploring", "Choosing where to go next")

        return ("exploring", "Looking for somewhere to explore")

    def _target_is_stale(self, frontiers):
        """True when the current target is no longer on any frontier.

        Driving down a corridor maps the rooms either side of it in passing,
        which routinely erases the frontier the robot set out for. Carrying on
        would park it in fully-explored space.
        """

        if self._target is None:
            return False

        for frontier in frontiers:

            if math.hypot(
                frontier.goal[0] - self._target[0],
                frontier.goal[1] - self._target[1],
            ) <= self.target_reuse_radius:
                return False

        return True

    # ---- returning home -------------------------------------------------

    def _return_to_start(self, goal_handle, start_pose, started_at, stats):

        self.get_logger().info("Exploration complete -- returning to start")

        if not self.nav_client.server_is_ready():
            self.get_logger().warning(
                "navigate_to_pose unavailable -- skipping the return trip"
            )
            return

        goal = NavigateToPose.Goal()

        goal.pose.header.frame_id = self.global_frame
        goal.pose.header.stamp = self.get_clock().now().to_msg()

        goal.pose.pose.position.x = float(start_pose[0])
        goal.pose.pose.position.y = float(start_pose[1])

        goal.pose.pose.orientation.z = math.sin(start_pose[2] / 2.0)
        goal.pose.pose.orientation.w = math.cos(start_pose[2] / 2.0)

        self._nav_generation += 1
        generation = self._nav_generation

        self._nav_state = _NAV_PENDING
        self._target = (float(start_pose[0]), float(start_pose[1]))

        future = self.nav_client.send_goal_async(goal)

        future.add_done_callback(
            lambda f: self._nav_goal_response(f, generation)
        )

        last_feedback_at = 0.0

        # The return trip is a courtesy, not the job -- it must not be able to
        # hang the action, so it gets its own bounded wait rather than the
        # main loop's open-ended one.
        deadline = time.monotonic() + 120.0

        while rclpy.ok() and time.monotonic() < deadline:

            if goal_handle.is_cancel_requested:
                break

            if self._nav_state in (_NAV_SUCCEEDED, _NAV_FAILED, _NAV_CANCELED):
                break

            last_feedback_at = self._maybe_feedback(
                goal_handle,
                "returning",
                "Returning to the starting point",
                [],
                stats,
                time.monotonic() - started_at,
                last_feedback_at,
            )

            time.sleep(_TICK_SEC)

        self._cancel_nav_goal()

    # ---- feedback -------------------------------------------------------

    def _maybe_feedback(self, goal_handle, state, message, frontiers, stats,
                        elapsed, last_feedback_at):

        now = time.monotonic()

        if (now - last_feedback_at) < _FEEDBACK_INTERVAL_SEC:
            return last_feedback_at

        feedback = ExploreArea.Feedback()

        feedback.state = state
        feedback.message = message
        feedback.frontiers_remaining = len(frontiers)
        feedback.frontiers_visited = self._frontiers_visited
        feedback.explored_area_m2 = float(stats.get("explored_area_m2", 0.0))
        feedback.percent_explored = float(stats.get("percent_explored", 0.0))
        feedback.elapsed_sec = float(elapsed)

        if self._target is not None:

            feedback.target_x = float(self._target[0])
            feedback.target_y = float(self._target[1])

            pose = self._robot_pose()

            if pose is not None:
                feedback.distance_to_target = float(
                    math.hypot(
                        self._target[0] - pose[0],
                        self._target[1] - pose[1],
                    )
                )

        goal_handle.publish_feedback(feedback)

        return now

    def _publish_frontiers(self, frontiers):

        message = PoseArray()

        message.header.frame_id = self.global_frame
        message.header.stamp = self.get_clock().now().to_msg()

        for frontier in frontiers:

            pose = Pose()

            pose.position.x = float(frontier.goal[0])
            pose.position.y = float(frontier.goal[1])
            pose.orientation.w = 1.0

            message.poses.append(pose)

        self.frontier_pub.publish(message)


def main(args=None):

    rclpy.init(args=args)

    node = ExplorerNode()

    # The action's execute callback blocks for the whole run, so the map and
    # TF callbacks it depends on need a thread of their own. See the module
    # docstring.
    executor = MultiThreadedExecutor()

    try:
        rclpy.spin(node, executor=executor)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()

        if rclpy.ok():
            rclpy.shutdown()


if __name__ == "__main__":
    main()
