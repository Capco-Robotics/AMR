"""Frontier detection, checked on hand-built grids.

frontier_search is deliberately free of ROS, so these run under plain pytest
with no graph, no Nav2 and no map server:

    python3 -m pytest src/amr_navigation/explore/test/test_frontier_search.py
"""

import os
import sys

import pytest

sys.path.insert(
    0,
    os.path.join(os.path.dirname(__file__), ".."),
)

from amr_navigation_explore import frontier_search  # noqa: E402


FREE = 0
WALL = 100
UNKNOWN = -1

RESOLUTION = 0.1


def build(rows, resolution=RESOLUTION, origin=(0.0, 0.0)):
    """Grid from a picture, bottom row first.

    '.' free, '#' wall, '?' unknown -- so a test reads as the map it describes.
    """

    symbols = {".": FREE, "#": WALL, "?": UNKNOWN}

    data = []

    for row in rows:
        for char in row:
            data.append(symbols[char])

    return frontier_search.Grid(
        data,
        len(rows[0]),
        len(rows),
        resolution,
        origin[0],
        origin[1],
    )


def test_fully_known_grid_has_no_frontiers():

    grid = build([
        "#####",
        "#...#",
        "#...#",
        "#...#",
        "#####",
    ])

    frontiers, stats = frontier_search.search(
        grid, (0.25, 0.25), min_frontier_size_m=0.0, robot_radius_m=0.0
    )

    assert frontiers == []
    assert stats["unknown_cells"] == 0


def test_finds_the_open_edge():

    # Free space along the bottom, unknown above it: one frontier, the full
    # width of the opening.
    grid = build([
        ".....",
        ".....",
        "?????",
        "?????",
    ])

    frontiers, _ = frontier_search.search(
        grid, (0.25, 0.05), min_frontier_size_m=0.0, robot_radius_m=0.0
    )

    assert len(frontiers) == 1

    # Row 1 is the only free row touching the unknown, so the goal sits there.
    assert frontiers[0].cell_count == 5
    assert frontiers[0].goal[1] == pytest.approx(0.15)


def test_walled_off_unknown_is_not_a_frontier():

    # The unknown on the right is real, but a wall separates it from the free
    # space the robot is in. Nothing here is reachable, so nothing is offered.
    grid = build([
        "..#??",
        "..#??",
        "..#??",
    ])

    frontiers, stats = frontier_search.search(
        grid, (0.05, 0.05), min_frontier_size_m=0.0, robot_radius_m=0.0
    )

    assert stats["unknown_cells"] == 6
    assert frontiers == []


def test_unreachable_room_is_excluded():

    # Two pockets of free space, each touching unknown, with no way between
    # them. Only the one the robot is standing in should be offered.
    grid = build([
        "..#..",
        "..#..",
        "??#??",
    ])

    frontiers, _ = frontier_search.search(
        grid, (0.05, 0.15), min_frontier_size_m=0.0, robot_radius_m=0.0
    )

    assert len(frontiers) == 1
    assert frontiers[0].goal[0] < 0.2


def test_small_frontiers_are_filtered_out():

    # A single-cell gap of unknown: 0.1 m of frontier on a 0.1 m grid.
    grid = build([
        "#####",
        "#...#",
        "#.#.#",
        "#...#",
        "##?##",
    ])

    kept, _ = frontier_search.search(
        grid, (0.25, 0.25), min_frontier_size_m=0.0, robot_radius_m=0.0
    )

    dropped, _ = frontier_search.search(
        grid, (0.25, 0.25), min_frontier_size_m=0.5, robot_radius_m=0.0
    )

    assert len(kept) == 1
    assert dropped == []


def test_bigger_and_closer_scores_higher():

    # A wide opening two cells away and a narrow one at the far end. The wide
    # one wins on both counts, so it must come first.
    grid = build([
        "?????????????",
        ".............",
        ".............",
        "????.........",
        "............?",
    ])

    frontiers, _ = frontier_search.search(
        grid,
        (0.05, 0.15),
        min_frontier_size_m=0.0,
        robot_radius_m=0.0,
    )

    assert len(frontiers) >= 2
    assert frontiers[0].size_m >= frontiers[1].size_m
    assert frontiers[0].score >= frontiers[1].score


def test_a_gap_too_narrow_for_the_robot_is_skipped():

    # One free cell poking into a wall, with unknown beyond it. Worth going to
    # for a robot that is a point; impossible for one 0.5 m across.
    grid = build([
        "#########",
        "#.......#",
        "#.......#",
        "#.......#",
        "#.......#",
        "###.#####",
        "###?#####",
    ])

    reachable, _ = frontier_search.search(
        grid, (0.15, 0.15), min_frontier_size_m=0.0, robot_radius_m=0.0
    )

    too_tight, _ = frontier_search.search(
        grid, (0.15, 0.15), min_frontier_size_m=0.0, robot_radius_m=0.25
    )

    assert len(reachable) == 1
    assert too_tight == []


def test_goal_moves_off_the_centroid_to_keep_clearance():

    # A wide frontier along the top, with a pillar two rows below its middle.
    # The centroid is the natural goal and is exactly where the robot does not
    # fit, so the goal has to slide along the frontier until it does.
    grid = build([
        "#####################",
        "#...................#",
        "#...................#",
        "#...................#",
        "#...................#",
        "#.......###.........#",
        "#...................#",
        "#...................#",
        "#???????????????????#",
    ])

    point_robot, _ = frontier_search.search(
        grid, (0.15, 0.15), min_frontier_size_m=0.0, robot_radius_m=0.0
    )

    real_robot, _ = frontier_search.search(
        grid, (0.15, 0.15), min_frontier_size_m=0.0, robot_radius_m=0.25
    )

    assert len(point_robot) == 1
    assert len(real_robot) == 1

    # A point robot goes to the middle of the opening...
    assert point_robot[0].goal[0] == pytest.approx(1.05)

    # ...a real one to the nearest part of it that clears the pillar and the
    # side walls by 0.25 m.
    assert real_robot[0].goal[0] == pytest.approx(1.45)


def test_size_saturation_prefers_the_near_frontier():

    # A one-cell opening right beside the robot, and a nine-cell one at the
    # far end of the room. Unsaturated, raw frontier length swamps the
    # distance term and the robot drives the length of the map past
    # unexplored space at its feet. Saturated, the near one wins.
    grid = build([
        "#####################",
        "#...................#",
        "#...................#",
        "#?#########?????????#",
    ])

    unsaturated, _ = frontier_search.search(
        grid,
        (0.15, 0.15),
        min_frontier_size_m=0.0,
        robot_radius_m=0.0,
        size_saturation_m=0.0,
    )

    saturated, _ = frontier_search.search(
        grid,
        (0.15, 0.15),
        min_frontier_size_m=0.0,
        robot_radius_m=0.0,
        size_saturation_m=0.15,
    )

    assert len(unsaturated) == 2
    assert len(saturated) == 2

    # Unsaturated: the big distant frontier outranks the one underfoot.
    assert unsaturated[0].size_m == pytest.approx(0.9)
    assert unsaturated[0].distance_m > 1.0

    # Saturated: extra width stops paying for extra distance, so the near
    # one is dealt with first.
    assert saturated[0].size_m == pytest.approx(0.1)
    assert saturated[0].distance_m < unsaturated[0].distance_m


def test_preferred_clearance_is_used_when_available():

    # A wide-open room whose frontier runs along the top. A goal that merely
    # fits the robot could sit one cell off the side wall; asking for a
    # roomier berth first moves it away, and the tight requirement is only
    # fallen back to when nothing roomier exists.
    grid = build([
        "#####################",
        "#...................#",
        "#...................#",
        "#...................#",
        "#...................#",
        "#.......###.........#",
        "#...................#",
        "#...................#",
        "#???????????????????#",
    ])

    tight, _ = frontier_search.search(
        grid, (0.15, 0.15), min_frontier_size_m=0.0, robot_radius_m=0.05
    )

    roomy, _ = frontier_search.search(
        grid,
        (0.15, 0.15),
        min_frontier_size_m=0.0,
        robot_radius_m=0.05,
        preferred_radius_m=0.25,
    )

    # The tight requirement puts the goal at the centroid, beside the pillar.
    assert tight[0].goal[0] == pytest.approx(1.05)

    # The preferred one moves it clear of both the pillar and the side walls.
    assert roomy[0].goal[0] == pytest.approx(1.45)


def test_falls_back_to_minimum_clearance_when_nothing_is_roomier():

    # The only way on is a one-cell gap. Insisting on the preferred clearance
    # would drop this frontier and declare the map finished with a whole room
    # unexplored, so the minimum has to be accepted.
    grid = build([
        "#########",
        "#.......#",
        "#.......#",
        "#.......#",
        "#.......#",
        "###.#####",
        "###?#####",
    ])

    frontiers, _ = frontier_search.search(
        grid,
        (0.15, 0.15),
        min_frontier_size_m=0.0,
        robot_radius_m=0.0,
        preferred_radius_m=0.25,
    )

    assert len(frontiers) == 1
    assert frontiers[0].goal == pytest.approx((0.35, 0.55))


def test_goal_is_pushed_away_from_the_robot():

    # The robot stands next to a long frontier. The nearest point on it is
    # under the robot's own arrival tolerance, so driving there would count as
    # arriving without moving -- and the same frontier would be picked again on
    # the next search, forever. The goal has to be further along.
    grid = build([
        "?????????????????????",
        ".....................",
        ".....................",
        ".....................",
    ])

    nearest, _ = frontier_search.search(
        grid,
        (1.05, 0.25),
        min_frontier_size_m=0.0,
        robot_radius_m=0.0,
    )

    pushed, _ = frontier_search.search(
        grid,
        (1.05, 0.25),
        min_frontier_size_m=0.0,
        robot_radius_m=0.0,
        min_goal_distance_m=0.75,
    )

    assert len(nearest) == 1
    assert len(pushed) == 1

    assert nearest[0].distance_m < 0.75
    assert pushed[0].distance_m >= 0.75


def test_a_frontier_entirely_underfoot_still_yields_a_goal():

    # Every cell of this frontier is inside min_goal_distance. Returning
    # nothing would end the run early, so the farthest cell is offered and the
    # caller decides whether it is worth driving to.
    grid = build([
        "??",
        "..",
        "..",
    ])

    frontiers, _ = frontier_search.search(
        grid,
        (0.05, 0.05),
        min_frontier_size_m=0.0,
        robot_radius_m=0.0,
        min_goal_distance_m=5.0,
    )

    assert len(frontiers) == 1


def test_blacklisted_frontier_is_skipped():

    grid = build([
        ".....",
        ".....",
        "?????",
    ])

    frontiers, _ = frontier_search.search(
        grid, (0.25, 0.05), min_frontier_size_m=0.0, robot_radius_m=0.0
    )

    target = frontiers[0].goal

    again, _ = frontier_search.search(
        grid,
        (0.25, 0.05),
        min_frontier_size_m=0.0,
        robot_radius_m=0.0,
        blacklist=[target],
        blacklist_radius_m=0.15,
    )

    # The frontier is still there, but the goal has moved off the blacklisted
    # spot rather than the whole frontier disappearing.
    assert len(again) == 1
    assert again[0].goal != target


def test_keepout_mask_blocks_a_frontier():

    grid = build([
        ".....",
        ".....",
        "?????",
    ])

    # Block the entire row the frontier sits on.
    mask = [0] * 15

    for col in range(5):
        mask[1 * 5 + col] = 100

    frontiers, _ = frontier_search.search(
        grid,
        (0.25, 0.05),
        min_frontier_size_m=0.0,
        robot_radius_m=0.0,
        keepout=mask,
    )

    assert frontiers == []


def test_robot_on_an_unknown_cell_still_finds_frontiers():

    # At startup the robot's own cell is often not yet mapped. Reporting "no
    # frontiers" there would end a run before it began.
    grid = build([
        ".....",
        "..?..",
        ".....",
        "?????",
    ])

    frontiers, _ = frontier_search.search(
        grid, (0.25, 0.15), min_frontier_size_m=0.0, robot_radius_m=0.0
    )

    assert len(frontiers) >= 1


def test_stats_report_explored_area():

    grid = build([
        "..##",
        "..??",
    ])

    _, stats = frontier_search.search(
        grid, (0.05, 0.05), min_frontier_size_m=0.0, robot_radius_m=0.0
    )

    assert stats["free_cells"] == 4
    assert stats["occupied_cells"] == 2
    assert stats["unknown_cells"] == 2

    # Free cells only: walls are mapped, but they are not floor.
    assert stats["explored_area_m2"] == pytest.approx(4 * RESOLUTION ** 2)
    assert stats["percent_explored"] == pytest.approx(75.0)
