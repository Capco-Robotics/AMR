"""Encodes nav_msgs/OccupancyGrid into a compact format for the websocket
(e.g. PNG) instead of shipping the raw int8 array to the browser.
"""


def encode_occupancy_grid(grid) -> bytes:
    raise NotImplementedError
