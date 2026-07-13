import base64

from amr_command.map_encoder import encode_occupancy_grid


class DummyPosition:
    x = 0.0
    y = 0.0


class DummyOrigin:
    position = DummyPosition()


class DummyInfo:
    width = 2
    height = 2
    resolution = 0.1
    origin = DummyOrigin()


class DummyGrid:
    info = DummyInfo()
    data = [
        0,
        100,
        -1,
        0,
    ]


def test_encode_occupancy_grid():
    frame = encode_occupancy_grid(DummyGrid())

    assert frame["width"] == 2
    assert frame["height"] == 2
    assert frame["resolution"] == 0.1

    assert frame["origin"]["x"] == 0.0
    assert frame["origin"]["y"] == 0.0

    png = base64.b64decode(frame["image"])

    assert png.startswith(b"\x89PNG")