"""Geometry for operator-drawn paths.

ROS-free on purpose, like keepout_zones.py: the maths here decides how the
robot is asked to sit at every waypoint, which is worth being able to test
without a graph, Nav2, or a map.
"""

import math


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
