"""
Encodes nav_msgs/OccupancyGrid into a compact format for the websocket
(e.g. PNG) instead of shipping the raw int8 array to the browser.
"""

import base64
import struct
import zlib


_UNKNOWN_GRAY = 205
_FREE_GRAY = 254
_OCCUPIED_GRAY = 0


def _png_chunk(chunk_type: bytes, data: bytes) -> bytes:
    return (
        struct.pack(">I", len(data))
        + chunk_type
        + data
        + struct.pack(">I", zlib.crc32(chunk_type + data))
    )


def encode_grayscale_png(width: int, height: int, pixels: bytes) -> bytes:
    if len(pixels) != width * height:
        raise ValueError("pixels length must equal width * height")

    signature = b"\x89PNG\r\n\x1a\n"

    ihdr = struct.pack(
        ">IIBBBBB",
        width,
        height,
        8,      # bit depth
        0,      # grayscale
        0,      # compression
        0,      # filter
        0,      # interlace
    )

    raw = bytearray()

    for row in range(height):
        raw.append(0)
        start = row * width
        raw.extend(pixels[start:start + width])

    idat = zlib.compress(bytes(raw), level=6)

    return (
        signature
        + _png_chunk(b"IHDR", ihdr)
        + _png_chunk(b"IDAT", idat)
        + _png_chunk(b"IEND", b"")
    )


def grid_to_grayscale(data) -> bytes:
    out = bytearray(len(data))

    for i, cell in enumerate(data):
        if cell < 0:
            out[i] = _UNKNOWN_GRAY
        elif cell == 0:
            out[i] = _FREE_GRAY
        else:
            out[i] = _OCCUPIED_GRAY

    return bytes(out)


def encode_occupancy_grid(grid) -> dict:
    info = grid.info

    pixels = grid_to_grayscale(grid.data)
    png_bytes = encode_grayscale_png(
        info.width,
        info.height,
        pixels,
    )

    return {
        "image": base64.b64encode(png_bytes).decode("ascii"),
        "width": info.width,
        "height": info.height,
        "resolution": info.resolution,
        "origin": {
            "x": info.origin.position.x,
            "y": info.origin.position.y,
        },
    }