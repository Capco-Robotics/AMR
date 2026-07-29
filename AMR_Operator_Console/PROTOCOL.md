# AMR WebSocket Protocol

> **Status: proposed, not implemented.**
>
> This document describes a multi-robot envelope (`robot_id` + `v`) that the
> gateway and the operator console do **not** implement today. Nothing in
> `amr_command` emits or reads `robot_id` or `v`, there is no robot registry,
> and there is no command routing — the console talks to exactly one gateway
> over one socket. Treat everything below marked *(proposed)* as a design
> sketch to argue about, not as a description of the running system.
>
> Sections marked *(implemented)* do describe the current wire format and are
> accurate as of the gateway in `amr_command/command_gateway_node.py`.

## Overview

The operator console and `amr_command` exchange JSON text frames over a single
websocket (`ws://<robot>:8765`).

**Every frame today is flat: `type` sits alongside the payload fields, and
there is no wrapper object.** An earlier draft of this document showed
telemetry as `{"type": ..., "data": {...}}`; no frame has ever been sent or
parsed in that shape, and the examples below have been corrected to match the
code.

### Current envelope *(implemented)*

```json
{
  "type": "message_type"
}
```

`type` is the only common field. Everything else is per-type and sits at the
top level.

### Proposed envelope *(proposed)*

```json
{
  "robot_id": "amr-01",
  "v": 1,
  "type": "message_type"
}
```

| Field | Description |
|---|---|
| robot_id | Unique robot identifier |
| v | Protocol version |
| type | Message type |

Adding these is backwards-compatible for the console (an unknown extra key is
ignored) but **not** for the gateway, which currently dispatches on `type`
alone.

---

## Hello Frame *(proposed)*

The gateway would send a hello frame when a client connects. It does not
today; a client's first frame is whatever telemetry happens to be broadcast
next.

```json
{
  "robot_id": "amr-01",
  "v": 1,
  "type": "hello",
  "capabilities": ["drive", "map"]
}
```

---

## Telemetry: gateway to console

### Map Frame *(implemented)*

Broadcast on every `/map` update. `image` is a base64 PNG of the occupancy
grid; `pose` is the latest odometry pose, or `null` before the first `/odom`
message.

```json
{
  "type": "map",
  "image": "iVBORw0KGgoAAAANSUhEUgAA...",
  "width": 189,
  "height": 161,
  "resolution": 0.05,
  "origin": {"x": -5.02, "y": -4.02},
  "pose": {"x": 0.0, "y": 0.0, "yaw": 0.0}
}
```

### Plan Frame *(implemented)*

The current Nav2 plan, decimated to every fifth pose. `points` are
`[x, y]` pairs in metres; an empty list means the plan was cleared.

```json
{
  "type": "plan",
  "points": [[0.0, 0.0], [0.5, 0.1]]
}
```

### SLAM Mode Frame *(implemented)*

```json
{
  "type": "slam_mode",
  "mode": "Mapping"
}
```

`mode` is `"Mapping"`, `"Localization"`, or `"Unknown"` when no slam_toolbox
node is reachable.

### Battery Frame *(proposed)*

There is no producer for this frame. `amr_charging` publishes BMS telemetry
into the ROS graph, but the gateway does not subscribe to it or forward it.

```json
{
  "type": "battery",
  "percent": 82,
  "voltage": 25.6,
  "charging": false
}
```

### Status Frame *(proposed)*

Also unproduced. `status_panel.js` has a `renderStatus()` stub with a TODO in
place of a body.

```json
{
  "type": "status",
  "state": "IDLE",
  "lift": "DOWN",
  "faults": []
}
```

---

## Commands: console to gateway

### Drive Frame *(implemented)*

Manual teleop. The gateway holds the last command for 500 ms and then stops,
so a client must repeat this frame to keep moving.

```json
{
  "type": "drive",
  "linear": 0.2,
  "angular": 0.0
}
```

### Navigation Goal Frame *(implemented)*

```json
{
  "type": "nav_goal",
  "x": 2.5,
  "y": 1.2,
  "theta": 0.0
}
```

Non-finite values are rejected.

---

## Map and path persistence *(implemented)*

These frames are the map and path managers in the console. Names must match
`[a-zA-Z0-9_-]+`.

| Console sends | Gateway replies |
|---|---|
| `{"type": "map_save", "name": "..."}` | `map_op_result` |
| `{"type": "map_load", "name": "..."}` | `map_op_result` |
| `{"type": "map_list"}` | `map_list` |
| `{"type": "path_save", "name": "...", "points": [...]}` | `path_op_result` |
| `{"type": "path_load", "name": "..."}` | `path_data` |
| `{"type": "path_list"}` | `path_list` |
| `{"type": "path_delete", "name": "..."}` | `path_op_result` |

Result frames are flat:

```json
{"type": "map_op_result", "ok": true, "error": ""}
{"type": "map_list", "maps": ["arena", "warehouse"]}
{"type": "path_list", "paths": ["loop_a"]}
{"type": "path_data", "name": "loop_a", "points": [[0.0, 0.0, 0.0]]}
```

Path points are `[x, y, theta]` arrays throughout. A path must have between
1 and 1000 points, and every value must be a finite number.

---

## Validation Rules

### Today *(implemented)*

The gateway dispatches on `type` and validates per-frame: names against the
character class above, path points for shape and finiteness, goals for
finiteness. Unknown `type` values are ignored silently. A frame missing
`type` is ignored.

### Proposed *(proposed)*

A frame would be rejected if:

- `robot_id` is missing
- `v` is missing
- an unsupported protocol version is received

Note that rejecting on a missing `robot_id` **before** reading `type` would
drop every frame the current console and gateway send, in both directions.
Any rollout of this envelope has to update both ends together, or accept
frames without `robot_id` during a transition.

---

## Multi Robot Support *(proposed)*

None of this exists. The console has one hardcoded `WS_URL` and no robot
selector.

Robot registry format:

```
robot_id -> latest received frame
```

Example:

```
amr-01 -> map, battery, status
amr-02 -> map, battery, status
```

Only the **selected robot** would receive operator commands (`drive`,
`nav_goal`).

If this is built, the selected-robot state must be a single source of truth.
A previous attempt kept the dropdown's value and the variable used to stamp
outbound commands as two unrelated variables, so selecting robot B and
pressing an arrow key drove robot A.

---

## WebSocket Flow *(proposed)*

1. Client connects to Gateway.
2. Gateway sends a `hello` frame.
3. Client registers the robot using `robot_id`.
4. Operator selects a robot from the console.
5. Incoming telemetry is filtered by the selected `robot_id`.
6. Outgoing commands (`drive`, `nav_goal`) are stamped with the selected `robot_id`.
7. Gateway routes commands to the correct robot.

The flow today is steps 1 and 5-without-filtering: connect, then receive every
frame the gateway broadcasts.

---

## Protocol Version *(proposed)*

```
v = 1
```

Future protocol changes should increment the protocol version number. Frames
today carry no version field, so the first implementation has to treat a
missing `v` as v0.
