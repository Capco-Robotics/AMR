"""Operator-drawn keep-out zones: storage, geometry, and mask rasterisation.

A zone is a closed polygon in map-frame metres, drawn on the console. Two
things consume it:

  * Nav2, via a `KeepoutFilter` costmap filter. The filter wants an
    OccupancyGrid "filter mask" (100 inside a zone, 0 outside) plus a
    CostmapFilterInfo describing how to read it. `rasterise()` produces the
    former; the gateway publishes both on latched topics, which is exactly
    what nav2's costmap_filter_info_server + map_server pair would do -- doing
    it in-process instead means a zone edit takes effect immediately, with no
    PGM round-trip and no extra lifecycle nodes to sequence.

  * The gateway itself, to refuse a drawn path that would cross a zone
    (`path_violations()`). Nav2 would already plan around a keep-out, but a
    path sent through NavigateThroughPoses is a list of *goal poses* -- a pose
    dropped inside a zone is unreachable and the run dies partway with an
    opaque abort. Rejecting it up front gives the operator a real message.

No numpy: the rest of this package is dependency-light pure Python (see
map_encoder's hand-rolled PNG writer), and the algorithms below are O(cells)
rather than O(cells x vertices), which is fast enough for the grid sizes a
warehouse map produces.
"""

import json
import math
import os


# Filter-mask cell values. The KeepoutFilter reads these through
# `space = data * multiplier + base`; with the multiplier/base the gateway
# advertises, 100 is what marks a cell as blocked.
MASK_BLOCKED = 100
MASK_FREE = 0

# A polygon needs three corners to enclose anything, and an operator tracing a
# zone with a finger produces far fewer points than a freehand path.
MIN_ZONE_VERTICES = 3
MAX_ZONE_VERTICES = 200
MAX_ZONES = 50


def point_in_polygon(x, y, polygon):
    """Even-odd ray cast. Points exactly on an edge are not guaranteed."""

    inside = False

    count = len(polygon)

    for i in range(count):

        x1, y1 = polygon[i]
        x2, y2 = polygon[(i + 1) % count]

        # Half-open vertical span, so a vertex shared by two edges is counted
        # once rather than twice (which would flip `inside` back and forth).
        if (y1 > y) != (y2 > y):

            t = (y - y1) / (y2 - y1)

            if x < x1 + t * (x2 - x1):
                inside = not inside

    return inside


def _segments_cross(p1, p2, p3, p4):
    """True when segment p1-p2 properly crosses segment p3-p4."""

    def orientation(a, b, c):

        value = (
            (b[1] - a[1]) * (c[0] - b[0])
            - (b[0] - a[0]) * (c[1] - b[1])
        )

        if abs(value) < 1e-12:
            return 0

        return 1 if value > 0 else 2

    o1 = orientation(p1, p2, p3)
    o2 = orientation(p1, p2, p4)
    o3 = orientation(p3, p4, p1)
    o4 = orientation(p3, p4, p2)

    if o1 != o2 and o3 != o4:
        return True

    # Collinear overlap. Rare in practice (an operator would have to trace a
    # path exactly along a zone edge) but it is still a crossing.
    def on_segment(a, b, c):
        return (
            min(a[0], b[0]) - 1e-9 <= c[0] <= max(a[0], b[0]) + 1e-9
            and min(a[1], b[1]) - 1e-9 <= c[1] <= max(a[1], b[1]) + 1e-9
        )

    if o1 == 0 and on_segment(p1, p2, p3):
        return True
    if o2 == 0 and on_segment(p1, p2, p4):
        return True
    if o3 == 0 and on_segment(p3, p4, p1):
        return True
    if o4 == 0 and on_segment(p3, p4, p2):
        return True

    return False


def segment_hits_polygon(start, end, polygon):
    """True when the segment enters `polygon` at any point.

    Both the "an endpoint is inside" and "the segment cuts across" cases
    matter: a path can tunnel straight through a zone with both of its
    waypoints outside it.
    """

    if point_in_polygon(start[0], start[1], polygon):
        return True

    if point_in_polygon(end[0], end[1], polygon):
        return True

    count = len(polygon)

    for i in range(count):

        edge_start = polygon[i]
        edge_end = polygon[(i + 1) % count]

        if _segments_cross(start, end, edge_start, edge_end):
            return True

    return False


def validate_polygon(polygon):
    """Return None when usable, else an operator-facing reason why not."""

    if not isinstance(polygon, list):
        return "Invalid polygon"

    if len(polygon) < MIN_ZONE_VERTICES:
        return f"A zone needs at least {MIN_ZONE_VERTICES} points"

    if len(polygon) > MAX_ZONE_VERTICES:
        return f"A zone cannot exceed {MAX_ZONE_VERTICES} points"

    for vertex in polygon:

        if not isinstance(vertex, list) or len(vertex) != 2:
            return "Invalid polygon point format"

        # Same guard as the path validator: bool is an int subclass, and
        # json.load happily returns NaN/Infinity for non-standard JSON.
        for value in vertex:

            if isinstance(value, bool):
                return "Invalid polygon point value"

            if not isinstance(value, (int, float)):
                return "Invalid polygon point value"

            if not math.isfinite(value):
                return "Invalid polygon point value"

    return None


def _dilate(mask, width, height, radius_cells):
    """Grow every blocked cell by `radius_cells` in place, via prefix sums.

    Nav2 applies costmap *filters* after the layer stack, so the inflation
    layer never sees keep-out cells -- without this the planner is free to
    graze a zone with the robot's body while keeping its centre outside.
    Growing the mask by the footprint's inscribed radius restores the margin.

    Two separable passes over a binary mask: a window contains a blocked cell
    exactly when its prefix-sum delta is non-zero. That makes this O(cells)
    rather than O(cells x window), and gives a square (Chebyshev) dilation --
    marginally more conservative at the diagonals than a true disc, which errs
    in the safe direction.
    """

    if radius_cells <= 0:
        return mask

    # Horizontal pass.
    out = bytearray(width * height)

    for row in range(height):

        base = row * width

        prefix = [0] * (width + 1)

        for col in range(width):
            prefix[col + 1] = prefix[col] + mask[base + col]

        for col in range(width):

            low = max(0, col - radius_cells)
            high = min(width, col + radius_cells + 1)

            out[base + col] = 1 if (prefix[high] - prefix[low]) else 0

    # Vertical pass over the horizontal result.
    result = bytearray(width * height)

    for col in range(width):

        prefix = [0] * (height + 1)

        for row in range(height):
            prefix[row + 1] = prefix[row] + out[row * width + col]

        for row in range(height):

            low = max(0, row - radius_cells)
            high = min(height, row + radius_cells + 1)

            result[row * width + col] = (
                1 if (prefix[high] - prefix[low]) else 0
            )

    return result


def rasterise(polygons, width, height, resolution, origin_x, origin_y,
              margin_m=0.0):
    """Render zone polygons into OccupancyGrid `data`, bottom-up row-major.

    Returns a list of int8 sized width*height, matching the geometry of the
    map the zones were drawn on.
    """

    mask = bytearray(width * height)

    if width <= 0 or height <= 0 or resolution <= 0:
        return [MASK_FREE] * max(0, width * height)

    for polygon in polygons:

        if len(polygon) < MIN_ZONE_VERTICES:
            continue

        # Only sweep the rows the polygon actually spans.
        ys = [vertex[1] for vertex in polygon]

        first_row = int((min(ys) - origin_y) / resolution) - 1
        last_row = int((max(ys) - origin_y) / resolution) + 1

        first_row = max(0, first_row)
        last_row = min(height - 1, last_row)

        count = len(polygon)

        for row in range(first_row, last_row + 1):

            # Cell centre, so a cell is blocked when its middle is inside the
            # zone rather than when a corner clips it.
            y = origin_y + (row + 0.5) * resolution

            crossings = []

            for i in range(count):

                x1, y1 = polygon[i]
                x2, y2 = polygon[(i + 1) % count]

                if (y1 > y) != (y2 > y):

                    t = (y - y1) / (y2 - y1)

                    crossings.append(x1 + t * (x2 - x1))

            if not crossings:
                continue

            crossings.sort()

            base = row * width

            # Even-odd: fill between consecutive crossing pairs.
            for i in range(0, len(crossings) - 1, 2):

                span_start = (crossings[i] - origin_x) / resolution - 0.5
                span_end = (crossings[i + 1] - origin_x) / resolution - 0.5

                col_start = max(0, int(math.ceil(span_start)))
                col_end = min(width - 1, int(math.floor(span_end)))

                for col in range(col_start, col_end + 1):
                    mask[base + col] = 1

    if margin_m > 0.0:
        mask = _dilate(
            mask,
            width,
            height,
            int(math.ceil(margin_m / resolution)),
        )

    return [MASK_BLOCKED if cell else MASK_FREE for cell in mask]


class ZoneStore:
    """Named keep-out polygons, persisted as one JSON file.

    Zones are global rather than per-map: the gateway has no reliable notion
    of "the current map" (slam_toolbox can be mapping fresh, or have had a
    posegraph deserialised into it), and a site's no-go areas are a property
    of the site. Zones are stored in map-frame metres, so they stay put as
    long as the map frame does.
    """

    def __init__(self, directory, filename="zones.json"):

        self.directory = directory
        self.filepath = os.path.join(directory, filename)

        # name -> [[x, y], ...]
        self._zones = {}

        os.makedirs(directory, exist_ok=True)

        self.load()

    def load(self):

        if not os.path.exists(self.filepath):
            return

        try:

            with open(self.filepath) as handle:
                data = json.load(handle)

            zones = {}

            for name, polygon in (data.get("zones") or {}).items():

                # A hand-edited or truncated file should cost us the bad zone,
                # not every zone -- and never a mask that silently omits a
                # no-go area the operator believes is still enforced.
                if validate_polygon(polygon) is None:
                    zones[name] = [[float(x), float(y)] for x, y in polygon]

            self._zones = zones

        except Exception:
            # Caller logs; an unreadable store must not stop the gateway from
            # coming up, but it must also not look like "no zones defined".
            raise

    def save(self):

        with open(self.filepath, "w") as handle:

            json.dump(
                {"zones": self._zones},
                handle,
            )

    def names(self):
        return sorted(self._zones)

    def polygons(self):
        return list(self._zones.values())

    def as_list(self):
        """Wire form: a list of {name, polygon}, stable order."""

        return [
            {"name": name, "polygon": self._zones[name]}
            for name in sorted(self._zones)
        ]

    def add(self, name, polygon):
        """Returns None on success, else an operator-facing error."""

        error = validate_polygon(polygon)

        if error is not None:
            return error

        if name not in self._zones and len(self._zones) >= MAX_ZONES:
            return f"Cannot store more than {MAX_ZONES} zones"

        self._zones[name] = [[float(x), float(y)] for x, y in polygon]

        self.save()

        return None

    def delete(self, name):

        if name not in self._zones:
            return "Zone does not exist"

        del self._zones[name]

        self.save()

        return None

    def clear(self):

        self._zones = {}

        self.save()

    def path_violations(self, points):
        """Names of zones an [x, y, theta] path would enter.

        Checked segment by segment, so a path that steps straight over a
        narrow zone is caught even though neither waypoint is inside it.
        """

        hit = []

        for name in sorted(self._zones):

            polygon = self._zones[name]

            if len(points) == 1:

                if point_in_polygon(points[0][0], points[0][1], polygon):
                    hit.append(name)

                continue

            for i in range(len(points) - 1):

                start = (points[i][0], points[i][1])
                end = (points[i + 1][0], points[i + 1][1])

                if segment_hits_polygon(start, end, polygon):
                    hit.append(name)
                    break

        return hit
