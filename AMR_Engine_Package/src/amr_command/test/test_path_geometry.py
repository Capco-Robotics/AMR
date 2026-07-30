"""Waypoint headings for operator-drawn paths.

path_geometry is ROS-free, so these run under plain pytest:

    python3 -m pytest src/amr_command/test/test_path_geometry.py
"""

import math
import os
import sys

import pytest

sys.path.insert(
    0,
    os.path.join(os.path.dirname(__file__), ".."),
)

from amr_command.path_geometry import (  # noqa: E402
    drop_points_behind,
    travel_headings,
)


def test_heading_follows_the_direction_of_travel():

    # Due east, then due north. The console sends 0.0 for both, which would
    # ask the robot to face east at the corner it is meant to turn north at.
    points = [
        [0.0, 0.0, 0.0],
        [1.0, 0.0, 0.0],
        [1.0, 1.0, 0.0],
    ]

    headings = travel_headings(points)

    assert headings[0] == pytest.approx(0.0)
    assert headings[1] == pytest.approx(math.pi / 2)

    # The last pose keeps the heading it arrived on -- there is no segment
    # leaving it to derive one from.
    assert headings[2] == pytest.approx(math.pi / 2)


def test_the_saved_paths_bug_case():

    # The real path that made the robot spin: every heading 0.0, but the route
    # turns north and then south. Every waypoint must end up pointing along
    # its own segment, and none of the turning ones may stay at 0.0.
    points = [
        [-2.78, -1.33, 0.0],
        [1.47, -1.40, 0.0],
        [1.15, 2.02, 0.0],
        [4.41, 2.50, 0.0],
        [5.61, -2.31, 0.0],
    ]

    headings = travel_headings(points)

    assert len(headings) == len(points)

    for i in range(len(points) - 1):

        expected = math.atan2(
            points[i + 1][1] - points[i][1],
            points[i + 1][0] - points[i][0],
        )

        assert headings[i] == pytest.approx(expected)

    # The leg heading north and the leg heading south must not both be "face
    # due east", which is what the stored 0.0 said.
    assert headings[1] > 1.0
    assert headings[3] < -1.0


def test_repeated_points_do_not_become_due_east():

    # atan2(0, 0) is 0.0, which is precisely the heading this code exists to
    # avoid inventing. A duplicated point takes the next real direction.
    points = [
        [0.0, 0.0, 0.0],
        [0.0, 0.0, 0.0],
        [0.0, 2.0, 0.0],
    ]

    headings = travel_headings(points)

    assert headings[0] == pytest.approx(math.pi / 2)
    assert headings[1] == pytest.approx(math.pi / 2)
    assert headings[2] == pytest.approx(math.pi / 2)


def test_single_point_keeps_its_supplied_heading():

    # Nothing to derive from, so an explicitly requested orientation stands.
    assert travel_headings([[1.0, 2.0, 1.234]]) == pytest.approx([1.234])


def test_a_path_of_identical_points_falls_back():

    headings = travel_headings([
        [1.0, 1.0, 0.5],
        [1.0, 1.0, 0.5],
    ])

    assert headings == pytest.approx([0.5, 0.5])


def test_empty_path():
    assert travel_headings([]) == []


# --- drop_points_behind ---------------------------------------------------


def test_the_spinning_bug_case():

    # The run that spun on the spot: the same saved path as above, with the
    # robot parked where it actually was -- 1.5 m along the first leg, having
    # already driven that far. Asking it back to the route's start makes the
    # planner produce a hairpin through the robot's own position, which DWB
    # answers with an endless rotation.
    points = [
        [-2.78, -1.33, 0.0],
        [1.47, -1.40, 0.0],
        [1.15, 2.02, 0.0],
        [4.41, 2.50, 0.0],
        [5.61, -2.31, 0.0],
    ]

    trimmed = drop_points_behind(points, -1.3, -1.4, 0.5)

    # The first waypoint is behind the robot and goes; the route it still has
    # to drive is untouched.
    assert trimmed == points[1:]


def test_a_route_starting_far_away_is_left_alone():

    # Driving out to a route that starts across the room is a normal request,
    # and no hairpin comes of it -- the whole path stands.
    points = [
        [5.0, 5.0, 0.0],
        [6.0, 5.0, 0.0],
        [7.0, 5.0, 0.0],
    ]

    assert drop_points_behind(points, 0.0, 0.0, 0.5) is points


def test_only_the_first_leg_within_radius_counts():

    # A route that loops back past the robot near its end must not have its
    # middle thrown away: the leg the robot is on is the *first* one it is
    # close to, not the last.
    points = [
        [0.0, 0.0, 0.0],
        [4.0, 0.0, 0.0],
        [4.0, 0.2, 0.0],
        [0.0, 0.2, 0.0],
    ]

    trimmed = drop_points_behind(points, 2.0, 0.0, 0.5)

    assert trimmed == points[1:]


def test_standing_on_the_last_leg_keeps_the_final_waypoint():

    # Whatever else it drops, this must never return an empty path -- an
    # empty NavigateThroughPoses goal is not a run at all.
    points = [
        [0.0, 0.0, 0.0],
        [2.0, 0.0, 0.0],
    ]

    trimmed = drop_points_behind(points, 1.0, 0.0, 0.5)

    assert trimmed == [[2.0, 0.0, 0.0]]


def test_a_waypoint_just_reached_is_left_for_nav2():

    # Standing at the start of a leg is not being past it. Dropping here is
    # what would make this unsafe to run on a timer: every waypoint reached
    # would take the next one with it, and the route would unravel one leg at
    # a time. Nav2's own RemovePassedGoals retires a waypoint this close.
    points = [
        [0.0, 0.0, 0.0],
        [3.0, 0.0, 0.0],
        [3.0, 3.0, 0.0],
    ]

    assert drop_points_behind(points, 0.1, 0.05, 0.5) is points

    # ...and a leg's worth of driving later, it goes.
    assert drop_points_behind(points, 1.5, 0.05, 0.5) == points[1:]


def test_a_single_point_path_is_never_trimmed():

    points = [[1.0, 1.0, 0.0]]

    assert drop_points_behind(points, 1.0, 1.0, 0.5) is points
