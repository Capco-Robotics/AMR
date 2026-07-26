# AMR WebSocket Protocol

## Overview

AMR WebSocket communication uses a JSON based protocol.

Each message uses a common envelope structure:

```json
{
  "robot_id": "amr-01",
  "v": 1,
  "type": "message_type"
}
```

## Frame Envelope

| Field | Description |
|---|---|
| robot_id | Unique robot identifier |
| v | Protocol version |
| type | Message type |

---

## Hello Frame

Gateway sends a hello message when a WebSocket client connects.

Example:

```json
{
  "robot_id": "amr-01",
  "v": 1,
  "type": "hello",
  "capabilities": [
    "drive",
    "map"
  ]
}
```

---

## Supported Message Types

### Map Frame

Used for sending map information.

```json
{
  "robot_id": "amr-01",
  "v": 1,
  "type": "map",
  "data": {}
}
```

---

### Battery Frame

Used for battery status updates.

```json
{
  "robot_id": "amr-01",
  "v": 1,
  "type": "battery",
  "data": {}
}
```

---

### Status Frame

Used for robot status information.

```json
{
  "robot_id": "amr-01",
  "v": 1,
  "type": "status",
  "data": {}
}
```

---

### Drive Frame

Used for manual operator commands.

Example:

```json
{
  "robot_id": "amr-01",
  "v": 1,
  "type": "drive",
  "linear": 0.2,
  "angular": 0.0
}
```

---

### Navigation Goal Frame

Used for sending a navigation goal to the selected robot.

Example:

```json
{
  "robot_id": "amr-01",
  "v": 1,
  "type": "nav_goal",
  "x": 2.5,
  "y": 1.2,
  "theta": 0.0
}
```

---

## Validation Rules

Gateway validates all incoming frames.

Frame is rejected if:

- `robot_id` is missing
- `v` is missing
- unsupported protocol version is received

---

## Multi Robot Support

Operator Console supports multiple AMRs.

Robot registry format:

```
robot_id -> latest received frame
```

Example:

```
amr-01 -> map, battery, status
amr-02 -> map, battery, status
```

Only the **selected robot** receives operator commands (`drive`, `nav_goal`).

---

## WebSocket Flow

1. Client connects to Gateway.
2. Gateway sends a `hello` frame.
3. Client registers the robot using `robot_id`.
4. Operator selects a robot from the console.
5. Incoming telemetry is filtered by the selected `robot_id`.
6. Outgoing commands (`drive`, `nav_goal`) are stamped with the selected `robot_id`.
7. Gateway routes commands to the correct robot.

---

## Protocol Version

Current protocol version:

```
v = 1
```

Future protocol changes should increment the protocol version number.