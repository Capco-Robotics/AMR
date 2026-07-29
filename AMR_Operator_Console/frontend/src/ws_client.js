// Connects to amr_command's websocket gateway on the RPi and dispatches
// incoming telemetry frames to whichever panel/renderer cares about them.
import { initTeleop } from "./teleop_control.js";
import { initTeleopButtons } from "./teleop_control.js";

import { renderBattery } from "./battery_panel.js";
import { renderStatus } from "./status_panel.js";

import {
    initMapPanel,
    handleMapFrame,
} from "./map_panel.js";
import {
    renderMap,
    setGoalMode,
    updatePlan,
} from "./map_renderer.js";


const WS_URL = 'ws://localhost:8765';

export function connect(onMessage) {
  const socket = new WebSocket(WS_URL);
  socket.onmessage = (event) => onMessage(JSON.parse(event.data));
  return socket;
}

export let websocket = null;


function handleTelemetryFrame(data) {

    switch (data.type) {

        case "map":
            renderMap(data);
            break;

        case "plan":
            updatePlan(data);
            break;

        case "battery":
            renderBattery(data);
            break;

        case "status":
            renderStatus(data);
            break;

        case "map_list":
        case "map_op_result":
        case "slam_mode":

            handleMapFrame(data);

            break;

    }

    console.log("Telemetry frame received:", data);

}

websocket = connect(handleTelemetryFrame);

initTeleop(websocket);

initTeleopButtons(
    document.getElementById("teleop-pad")
);

window.wsClient = websocket;


websocket.onopen = () => {

    console.log("Connected to AMR websocket");

    initMapPanel();

};

const goalButton =
    document.getElementById("goal-toggle");

goalButton.addEventListener("click", () => {

    goalButton.classList.toggle("active");

    setGoalMode(
        goalButton.classList.contains("active")
    );

});