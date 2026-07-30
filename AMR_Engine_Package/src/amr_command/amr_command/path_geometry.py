"""Geometry for operator-drawn paths.

ROS-free on purpose, like keepout_zones.py: the maths here decides how the
robot is asked to sit at every waypoint, which is worth being able to test
without a graph, Nav2, or a map.
"""

import math


def _closest_point_on_segment(px, py, ax, ay, bx, by):
    """How far (px,py) is from segment A-B, and how far along A-B that lands.

    Returns (distance, travelled), both in metres: `travelled` is measured
    from A, so 0.0 means the closest point is A itself and the segment's own
    length means it is B.
    """

    ex = bx - ax
    ey = by - ay

    length_sq = ex * ex + ey * ey

    if length_sq < 1e-12:
        # Degenerate segment: A and B are the same point.
        return math.hypot(px - ax, py - ay), 0.0

    t = ((px - ax) * ex + (py - ay) * ey) / length_sq
    t = max(0.0, min(1.0, t))

    return (
        math.hypot(px - (ax + t * ex), py - (ay + t * ey)),
        t * math.sqrt(length_sq),
    )


def drop_points_behind(points, robot_x, robot_y, radius):
    """Drop leading waypoints the robot has provably already driven past.

    NavigateThroughPoses has to visit every pose it is given, and Nav2 only
    forgets one when the robot comes within half a metre of it
    (RemovePassedGoals). A waypoint the robot went past any wider than that is
    a trap: every replan from then on produces a hairpin -- back down the leg
    to the waypoint, a U-turn, then the same ground again forwards.

    A hairpin is what breaks DWB. Both legs occupy the same cells of a 3 m
    local costmap, so PathDist and PathAlign score the outbound and return
    directions identically, while GoalDist -- which only sees the end of the
    pruned local plan, out ahead on the return leg -- pulls the other way. The
    best-scoring trajectory becomes a pure rotation, every cycle, and the
    robot turns circles on the spot instead of driving. Nav2's progress
    checker does not rescue it either: spinning wobbles the base further than
    `required_movement_radius`, so the stall reads as progress and the run
    never times out.

    Two ordinary things put the robot past a waypoint by more than Nav2's half
    metre. It starts already standing on the route, because the operator drew
    over the map from wherever it happened to be; and it cuts corners, because
    DWB follows the plan by scoring trajectories against it rather than
    tracking it exactly. Both are why this has to be re-checked *during* a run
    and not only when one is sent.

    `radius` is how close to a leg the robot has to be for that leg to count
    as one it is driving. Only the *first* such leg is considered, so a route
    that loops back past the robot later on keeps its middle. The robot also
    has to have travelled further than `radius` along that leg, which is what
    makes this safe to run continuously: immediately after a waypoint is
    dropped the robot sits at the start of the next leg, and nothing more is
    dropped until it has actually driven along it.

    Returns the trimmed list (the same point objects), or `points` unchanged
    when there is nothing to drop -- including when the robot is nowhere near
    the route, since driving out to a distant route's start is a normal thing
    to ask for and no hairpin comes of it.
    """

    if len(points) < 2:
        return points

    for i in range(len(points) - 1):

        distance, travelled = _closest_point_on_segment(
            robot_x,
            robot_y,
            points[i][0],
            points[i][1],
            points[i + 1][0],
            points[i + 1][1],
        )

        if distance > radius:
            continue

        if travelled <= radius:
            # On this leg, but not yet far enough along it to have left the
            # waypoint behind. Nav2's own RemovePassedGoals covers the rest.
            return points

        # Everything up to and including the start of this leg is behind the
        # robot. points[i + 1] onwards always leaves at least one waypoint,
        # because i stops at len(points) - 2.
        return points[i + 1:]

    return points


def travel_headings(points):
    """Yaw for each waypoint, taken from the direction of travel.

    A freehand path is a *route*, not a list of orientations. The console has
    no way to express "face this way at point 3" -- it sends 0.0 for every
    point, because a finger drawn across a map says nothing about heading.

    Nav2 does not read it that way. NavigateThroughPoses treats each point as
    a goal *pose*, and the goal checker enforces `yaw_goal_tolerance` (0.15 rad
    in nav2_params.yaml) at every one of them. A route running north with 0.0
    in its heading field therefore asks the robot to arrive at each waypoint
    and then pirouette to face due east before the waypoint counts as reached.
    On a differential drive that in-place rotation oscillates, and the robot
    spins on the spot instead of following the route.

    Pointing each pose along the segment leaving it means the required
    orientation is the one the robot naturally arrives in, so it drives
    through the waypoints instead of stopping to turn at each.

    The last pose has no segment leaving it, so it keeps the heading of the
    one arriving -- the robot finishes facing the way it was travelling, which
    is the only defensible guess when the operator never specified one.

    Returns a list of floats, one per point.
    """

    count = len(points)

    if count == 0:
        return []

    if count == 1:
        # Nothing to derive a direction from; honour whatever was sent.
        return [float(points[0][2])]

    headings = [None] * count

    for i in range(count - 1):

        dx = points[i + 1][0] - points[i][0]
        dy = points[i + 1][1] - points[i][1]

        # A repeated point has no direction. Left as None and filled below,
        # rather than becoming atan2(0, 0) == 0.0 -- which is exactly the due
        # east this function exists to stop the robot turning to.
        if math.hypot(dx, dy) > 1e-6:
            headings[i] = math.atan2(dy, dx)

    # Fill gaps from the next segment that does have a direction, walking
    # backwards so a run of duplicated points adopts the heading of the move
    # that eventually leaves them.
    next_known = None

    for i in range(count - 2, -1, -1):

        if headings[i] is None:
            headings[i] = next_known
        else:
            next_known = headings[i]

    headings[count - 1] = headings[count - 2]

    # Every point identical: no direction exists anywhere in the path.
    fallback = float(points[0][2])

    return [
        fallback if heading is None else float(heading)
        for heading in headings
    ]
