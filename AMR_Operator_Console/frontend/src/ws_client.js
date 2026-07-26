// Connects to amr_command's websocket gateway on the RPi and dispatches
// incoming telemetry frames to whichever panel/renderer cares about them.

import { initTeleop } from "./teleop_control.js";
import { initTeleopButtons } from "./teleop_control.js";
import { setGoalMode } from "./map_renderer.js";

const WS_URL = "ws://localhost:8765";

export let websocket = null;

/*
 * Registry:
 * robot_id -> {
 *   socket,
 *   lastFrame
 * }
 */
export const robots = new Map();

export let selectedRobotId = null;

export function connect(onMessage) {
    const socket = new WebSocket(WS_URL);

    socket.onopen = () => {
        console.log("Connected to AMR websocket");
    };

    socket.onmessage = (event) => {
        const frame = JSON.parse(event.data);

        if (!frame.robot_id || frame.v !== 1) {
            console.warn("Ignoring invalid frame:", frame);
            return;
        }

        if (!robots.has(frame.robot_id)) {
            robots.set(frame.robot_id, {
                socket: socket,
                lastFrame: null,
            });
        }

        const robot = robots.get(frame.robot_id);

        robot.socket = socket;
        robot.lastFrame = frame;

        if (selectedRobotId === null) {
            selectedRobotId = frame.robot_id;
        }

        if (frame.robot_id !== selectedRobotId) {
            return;
        }

        onMessage(frame);
    };

    socket.onclose = () => {
        console.log("Disconnected from websocket");
    };

    socket.onerror = (err) => {
        console.error("WebSocket error:", err);
    };

    return socket;
}

function handleTelemetryFrame(frame) {
    const robot = robots.get(frame.robot_id);

    if (robot) {
        robot.lastFrame = frame;
    }

    const data = frame.data ?? frame;

    console.log(
        `[${frame.robot_id}]`,
        frame.type,
        data
    );
}

export function getKnownRobots() {
    return Array.from(robots.keys());
}

export function getSelectedRobot() {
    return selectedRobotId;
}

export function setSelectedRobot(robotId) {
    if (robots.has(robotId)) {
        selectedRobotId = robotId;
    }
}

export function getConnection(robotId) {
    return robots.get(robotId)?.socket ?? null;
}

websocket = connect(handleTelemetryFrame);

initTeleop(websocket);
initTeleopButtons(document.getElementById("teleop-pad"));

const goalButton = document.getElementById("goal-toggle");

goalButton.addEventListener("click", () => {
    goalButton.classList.toggle("active");

    setGoalMode(
        goalButton.classList.contains("active")
    );
});