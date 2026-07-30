"""Frontier detection on an occupancy grid.

A *frontier* is the boundary between mapped free space and the unknown: a
driveable cell with an unmapped neighbour. Driving to one and looking around
converts unknown into known, so repeatedly picking the best frontier and
driving to it maps a building without anyone steering.

Everything here is plain Python over the flat `OccupancyGrid.data` array, with
no ROS and no numpy -- the same choice `keepout_zones.py` and `map_encoder.py`
made, and it keeps this module importable by a unit test that does not need a
ROS graph. The algorithms are O(cells): one breadth-first sweep over free space
finds the frontiers, measures how far away they are, and rules out the ones
that are walled off, all in the same pass.

Two decisions worth knowing about:

  * **Distance is measured through free space, not straight-line.** A frontier
    on the far side of a wall is not "2 m away" in any sense the robot cares
    about, and a sealed-off room is not reachable at all. Both fall out of a
    BFS seeded at the robot: unreached frontiers are discarded, and the step
    count to the ones that were reached is a usable travel estimate. It counts
    diagonal steps as one, so it underestimates a zig-zag route by up to ~30%.
    That is fine for *ranking* candidates, which is all it is used for -- Nav2
    plans the actual route.

  * **The goal is a real cell on the frontier, not the centroid.** The centroid
    of a curved frontier can land inside a wall or in the unknown behind it,
    and a goal there is unreachable. The cell nearest the centroid that the
    robot can actually fit in is used instead.
"""

import math
from collections import deque


# OccupancyGrid conventions: -1 is unmapped, 0..100 is a probability.
_UNKNOWN_CELL = -1

# Cell classes used internally.
FREE = 0
OCCUPIED = 1
UNKNOWN = 2

# 8-connected neighbourhood, used for both the free-space sweep and for
# grouping frontier cells into one frontier.
_NEIGHBOURS_8 = (
    (-1, -1), (0, -1), (1, -1),
    (-1, 0), (1, 0),
    (-1, 1), (0, 1), (1, 1),
)

# 4-connected, used to decide "is this free cell touching the unknown". A
# diagonal touch is a corner clip rather than an opening to drive through, and
# counting it produces frontiers strung along every wall the lidar grazed.
_NEIGHBOURS_4 = (
    (0, -1), (-1, 0), (1, 0), (0, 1),
)

# How far from the robot to look for somewhere to start the sweep, when the
# robot's own cell is not free (it sits on an unmapped cell at startup, and a
# stale scan can briefly paint its cell as occupied).
_MAX_SEED_SEARCH_CELLS = 40


class Frontier:
    """One reachable frontier, with everything needed to rank and drive to it."""

    __slots__ = (
        "goal",
        "centroid",
        "size_m",
        "distance_m",
        "cell_count",
        "score",
    )

    def __init__(self, goal, centroid, size_m, distance_m, cell_count, score):
        # World-frame metres. `goal` is a cell the robot fits in; `centroid` is
        # the frontier's middle, which is only used for display.
        self.goal = goal
        self.centroid = centroid
        self.size_m = size_m
        self.distance_m = distance_m
        self.cell_count = cell_count
        self.score = score

    def __repr__(self):
        return (
            f"Frontier(goal=({self.goal[0]:.2f}, {self.goal[1]:.2f}), "
            f"size={self.size_m:.2f} m, distance={self.distance_m:.2f} m, "
            f"score={self.score:.2f})"
        )


class Grid:
    """An OccupancyGrid's geometry plus its cells classified once.

    Classifying up front costs one pass and saves re-deciding "is 65 a wall"
    at every one of the several million neighbour lookups the sweep does.
    """

    def __init__(self, data, width, height, resolution,
                 origin_x, origin_y, occupied_threshold=50):

        self.width = int(width)
        self.height = int(height)
        self.resolution = float(resolution)
        self.origin_x = float(origin_x)
        self.origin_y = float(origin_y)

        cells = bytearray(self.width * self.height)

        for i, value in enumerate(data):

            if value == _UNKNOWN_CELL or value < 0:
                cells[i] = UNKNOWN
            elif value >= occupied_threshold:
                cells[i] = OCCUPIED
            else:
                cells[i] = FREE

        self.cells = cells

    def in_bounds(self, col, row):
        return 0 <= col < self.width and 0 <= row < self.height

    def at(self, col, row):
        return self.cells[row * self.width + col]

    def world_to_cell(self, x, y):
        """Cell containing world (x, y), or None if it is off the grid."""

        col = int(math.floor((x - self.origin_x) / self.resolution))
        row = int(math.floor((y - self.origin_y) / self.resolution))

        if not self.in_bounds(col, row):
            return None

        return (col, row)

    def cell_to_world(self, col, row):
        """Centre of a cell, in world metres."""

        return (
            self.origin_x + (col + 0.5) * self.resolution,
            self.origin_y + (row + 0.5) * self.resolution,
        )

    def counts(self):
        """(free, occupied, unknown) cell counts."""

        free = 0
        occupied = 0

        for cell in self.cells:
            if cell == FREE:
                free += 1
            elif cell == OCCUPIED:
                occupied += 1

        return (free, occupied, len(self.cells) - free - occupied)


def _seed_cell(grid, robot_xy):
    """A free cell to start the sweep from, at or near the robot.

    The robot's own cell is usually free, but not always: before the first
    scan is integrated it is unmapped, and a grazing return can mark it
    occupied for an update or two. Rather than reporting "nothing to explore"
    in either case, spiral outwards for the nearest free cell.
    """

    start = grid.world_to_cell(robot_xy[0], robot_xy[1])

    if start is None:
        return None

    if grid.at(*start) == FREE:
        return start

    col0, row0 = start

    for radius in range(1, _MAX_SEED_SEARCH_CELLS + 1):

        # Perimeter of the square at this radius only -- the interior was
        # covered by the previous iterations.
        for d in range(-radius, radius + 1):

            for col, row in (
                (col0 + d, row0 - radius),
                (col0 + d, row0 + radius),
                (col0 - radius, row0 + d),
                (col0 + radius, row0 + d),
            ):

                if grid.in_bounds(col, row) and grid.at(col, row) == FREE:
                    return (col, row)

    return None


def _has_clearance(grid, col, row, radius_cells):
    """True when no wall sits within `radius_cells` of this cell.

    A frontier cell can be one cell from a wall; the robot is not a point, so
    sending it there produces a goal Nav2 immediately aborts. Checking a square
    window is marginally stricter than the robot's real circular footprint,
    which errs towards goals that actually work.
    """

    if radius_cells <= 0:
        return True

    for row_offset in range(-radius_cells, radius_cells + 1):

        row_index = row + row_offset

        if row_index < 0 or row_index >= grid.height:
            # Off the edge of the map is unknown, not wall -- the map grows.
            continue

        base = row_index * grid.width

        low = max(0, col - radius_cells)
        high = min(grid.width - 1, col + radius_cells)

        for col_index in range(low, high + 1):

            if grid.cells[base + col_index] == OCCUPIED:
                return False

    return True


def _blacklisted(x, y, blacklist, radius_m):
    """True when (x, y) is near somewhere that already failed."""

    for bx, by in blacklist:
        if math.hypot(x - bx, y - by) <= radius_m:
            return True

    return False


def _pick_goal(grid, group, distance, radius_cells, min_distance_cells,
               blacklist, blacklist_radius_m, keepout, keepout_threshold):
    """Best drivable cell on one frontier, or None if it has none.

    `group` arrives sorted nearest-to-centroid, so the first cell that passes
    every check is the most central one the robot can use. When every usable
    cell is nearer than `min_distance_cells` the farthest of them is returned
    instead of nothing -- see min_goal_distance_m in search().

    Returns (world_xy, distance_in_cells) or None.
    """

    width = grid.width

    nearest_fallback = None

    for col, row in group:

        index = row * width + col

        if keepout is not None and keepout[index] >= keepout_threshold:
            continue

        if not _has_clearance(grid, col, row, radius_cells):
            continue

        x, y = grid.cell_to_world(col, row)

        if blacklist and _blacklisted(x, y, blacklist, blacklist_radius_m):
            continue

        if distance[index] < min_distance_cells:

            if (
                nearest_fallback is None
                or distance[index] > nearest_fallback[1]
            ):
                nearest_fallback = ((x, y), distance[index])

            continue

        return ((x, y), distance[index])

    return nearest_fallback


def search(grid, robot_xy,
           min_frontier_size_m=0.35,
           robot_radius_m=0.30,
           preferred_radius_m=None,
           min_goal_distance_m=0.0,
           size_saturation_m=0.0,
           blacklist=(),
           blacklist_radius_m=0.5,
           distance_weight=1.0,
           size_weight=2.0,
           keepout=None,
           keepout_threshold=50):
    """Reachable frontiers on `grid`, best first.

    `keepout`, when given, is a filter mask sharing the grid's geometry (the
    one the command gateway publishes for Nav2). Frontiers inside a keep-out
    zone are dropped rather than driven to and aborted -- the operator marked
    that area off limits, so the unknown behind it is meant to stay unknown.

    `min_goal_distance_m` keeps the goal far enough away to be worth driving
    to. Early in a run the explored area is one blob and its whole boundary is
    a single frontier that starts a few centimetres from the robot; without
    this the nearest point on it is chosen, the robot is already within arrival
    tolerance of it, and nothing ever moves. When every cell on a frontier is
    nearer than this the closest thing to a real goal -- the farthest cell on
    it -- is used anyway, and the caller decides whether that is worth driving
    to.

    `robot_radius_m` is the clearance a goal must have; `preferred_radius_m`,
    when larger, is the clearance it should have if any cell on the frontier
    can offer it. Defaults to `robot_radius_m`, i.e. one tier.

    `size_saturation_m` caps how much frontier length counts towards the
    score. 0 disables the cap, which lets one large frontier outrank every
    nearby one no matter how far away it is.

    Returns (frontiers, stats).
    """

    stats = {
        "free_cells": 0,
        "occupied_cells": 0,
        "unknown_cells": 0,
        "total_cells": len(grid.cells),
        "explored_area_m2": 0.0,
        "percent_explored": 0.0,
        "frontier_cells": 0,
        "reachable_cells": 0,
    }

    free_cells, occupied_cells, unknown_cells = grid.counts()

    cell_area = grid.resolution * grid.resolution

    stats["free_cells"] = free_cells
    stats["occupied_cells"] = occupied_cells
    stats["unknown_cells"] = unknown_cells
    stats["explored_area_m2"] = free_cells * cell_area

    if stats["total_cells"]:
        stats["percent_explored"] = (
            100.0 * (free_cells + occupied_cells) / stats["total_cells"]
        )

    seed = _seed_cell(grid, robot_xy)

    if seed is None:
        # No free cell anywhere near the robot: either no map yet, or the
        # robot is off the edge of the one we have. Nothing to say about
        # frontiers, and claiming "none left" would end the run.
        return ([], stats)

    width = grid.width
    height = grid.height
    cells = grid.cells

    # Step count from the seed, in cells. -1 means not reached.
    distance = [-1] * (width * height)

    # Frontier cells found during the sweep, in discovery order.
    frontier_cells = []
    is_frontier = bytearray(width * height)

    seed_index = seed[1] * width + seed[0]
    distance[seed_index] = 0

    queue = deque([seed])

    while queue:

        col, row = queue.popleft()

        index = row * width + col
        next_distance = distance[index] + 1

        touches_unknown = False

        for dcol, drow in _NEIGHBOURS_4:

            ncol = col + dcol
            nrow = row + drow

            if ncol < 0 or ncol >= width or nrow < 0 or nrow >= height:
                continue

            if cells[nrow * width + ncol] == UNKNOWN:
                touches_unknown = True
                break

        if touches_unknown:
            is_frontier[index] = 1
            frontier_cells.append((col, row))

        for dcol, drow in _NEIGHBOURS_8:

            ncol = col + dcol
            nrow = row + drow

            if ncol < 0 or ncol >= width or nrow < 0 or nrow >= height:
                continue

            nindex = nrow * width + ncol

            if distance[nindex] != -1:
                continue

            # The sweep travels through free space only. That is what makes
            # an enclosed room's frontiers stay unreached, and therefore
            # excluded, instead of being offered as goals Nav2 cannot plan to.
            if cells[nindex] != FREE:
                continue

            distance[nindex] = next_distance
            queue.append((ncol, nrow))

    stats["frontier_cells"] = len(frontier_cells)
    stats["reachable_cells"] = sum(1 for d in distance if d != -1)

    if not frontier_cells:
        return ([], stats)

    radius_cells = int(math.ceil(robot_radius_m / grid.resolution))

    preferred_cells = radius_cells

    if preferred_radius_m is not None and preferred_radius_m > robot_radius_m:
        preferred_cells = int(math.ceil(preferred_radius_m / grid.resolution))

    frontiers = []

    grouped = bytearray(width * height)

    for cell in frontier_cells:

        start_index = cell[1] * width + cell[0]

        if grouped[start_index]:
            continue

        # Flood the connected run of frontier cells this one belongs to. One
        # doorway's worth of unknown is one frontier, however many cells wide.
        group = []

        grouped[start_index] = 1
        group_queue = deque([cell])

        while group_queue:

            col, row = group_queue.popleft()
            group.append((col, row))

            for dcol, drow in _NEIGHBOURS_8:

                ncol = col + dcol
                nrow = row + drow

                if ncol < 0 or ncol >= width or nrow < 0 or nrow >= height:
                    continue

                nindex = nrow * width + ncol

                if grouped[nindex] or not is_frontier[nindex]:
                    continue

                grouped[nindex] = 1
                group_queue.append((ncol, nrow))

        # A frontier's "size" is how much unknown it fronts, so cell count
        # times cell width -- a 2 m doorway and a 10 cm gap behind a table leg
        # are worth very different detours.
        size_m = len(group) * grid.resolution

        if size_m < min_frontier_size_m:
            continue

        sum_x = 0.0
        sum_y = 0.0

        for col, row in group:
            x, y = grid.cell_to_world(col, row)
            sum_x += x
            sum_y += y

        centroid = (sum_x / len(group), sum_y / len(group))

        # Nearest-to-centroid first, so the goal lands in the middle of the
        # opening where there is room, not at the end where it is pinched.
        group.sort(
            key=lambda c: (
                (grid.origin_x + (c[0] + 0.5) * grid.resolution - centroid[0]) ** 2
                + (grid.origin_y + (c[1] + 0.5) * grid.resolution - centroid[1]) ** 2
            )
        )

        min_distance_cells = min_goal_distance_m / grid.resolution

        # Roomy first, tight only if there is no alternative. A goal that
        # merely fits the robot can sit inside Nav2's inflation layer, where
        # the controller crawls and the robot ends up scraping along a wall
        # for minutes. Asking for a comfortable berth first, and settling for
        # a merely-passable one only when the whole frontier is tight, keeps
        # the usual case fast without dropping narrow frontiers entirely.
        picked = _pick_goal(
            grid, group, distance, preferred_cells, min_distance_cells,
            blacklist, blacklist_radius_m, keepout, keepout_threshold,
        )

        if picked is None and preferred_cells > radius_cells:
            picked = _pick_goal(
                grid, group, distance, radius_cells, min_distance_cells,
                blacklist, blacklist_radius_m, keepout, keepout_threshold,
            )

        if picked is None:
            # Every cell on this frontier is blacklisted, inside a keep-out
            # zone, or too tight for the robot. Nothing here to drive to.
            continue

        goal, goal_distance_cells = picked

        distance_m = goal_distance_cells * grid.resolution

        # Close beats far; big beats small, but only up to a point.
        #
        # Frontier "size" is the length of the boundary, and early in a run
        # that is the entire perimeter of the explored bubble -- tens of
        # metres. Scored raw it swamped the distance term completely, so the
        # robot would drive past unexplored space right beside it to reach a
        # nominally larger frontier across the building. Saturating the size
        # reflects what is actually on offer: the robot can only reveal what
        # fits in one sensor sweep, so a 10 m frontier is not worth five times
        # the detour of a 2 m one. Past the saturation point the choice comes
        # down to distance, which is what makes it explore its surroundings
        # before setting off across the map.
        effective_size_m = (
            min(size_m, size_saturation_m)
            if size_saturation_m > 0.0
            else size_m
        )

        score = size_weight * effective_size_m - distance_weight * distance_m

        frontiers.append(
            Frontier(
                goal=goal,
                centroid=centroid,
                size_m=size_m,
                distance_m=distance_m,
                cell_count=len(group),
                score=score,
            )
        )

    frontiers.sort(key=lambda f: f.score, reverse=True)

    return (frontiers, stats)
