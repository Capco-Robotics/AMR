// Connects to amr_command's websocket gateway on the RPi and dispatches
// incoming telemetry frames to whichever panel/renderer cares about them.
import { initTeleop } from "./teleop_control.js";
import { initTeleopButtons } from "./teleop_control.js";

import { renderBattery } from "./battery_panel.js";
import { renderStatus } from "./status_panel.js";
import {
    getCleanPath,
    initPathDraw,
} from "./path_draw.js";

import {
    initMapPanel,
    handleMapFrame,
    refreshMaps,
} from "./map_panel.js";
import {
    initPathPanel,
    refreshPaths,
    renderPathStatus,
} from "./path_panel.js";
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

export function sendMessage(message)
{

    if(websocket === null)
    {
        return;
    }


    if(websocket.readyState !== WebSocket.OPEN)
    {
        return;
    }


    websocket.send(
        JSON.stringify(message)
    );

}


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

        // Nav2 path execution progress. This used to fall through to
        // renderStatus(), which is still an unimplemented stub, so the
        // "Path Status" readout never left "Idle".
        case "path_status":
            renderPathStatus(data);
            break;

        case "map_list":
        case "map_op_result":
        case "slam_mode":

            handleMapFrame(data);

            break;
        case "path_list":
        case "path_data":
        case "path_op_result":

            window.pathPanelHandler(data);

            break;

    }

}

websocket = connect(handleTelemetryFrame);

initTeleop(websocket);

initTeleopButtons(
    document.getElementById("teleop-pad")
);

window.wsClient = websocket;

// Bind panel DOM once, not per connection. Re-binding on every open would
// stack duplicate listeners the moment a reconnect is added.
initMapPanel(websocket);
initPathPanel();
initPathDraw();


websocket.onopen = () => {

    console.log("Connected to AMR websocket");

    // Only the list pulls belong here -- they need an open socket, and they
    // are safe to repeat if a reconnect is ever added.
    refreshMaps();
    refreshPaths();

};



const goalButton =
    document.getElementById("goal-toggle");

goalButton.addEventListener("click", () => {

    goalButton.classList.toggle("active");

    setGoalMode(
        goalButton.classList.contains("active")
    );

});

const sendPathButton =
    document.getElementById("send-path-btn");


if (sendPathButton) {

    sendPathButton.addEventListener(
        "click",
        () => {

            // getCleanPath() already returns wire-format [x, y, theta]
            // points. This used to re-map them as p.x/p.y, which produced a
            // list of [undefined, undefined, 0.0] the gateway rejected.
            const points = getCleanPath();

            if (points.length === 0) {
                return;
            }

            sendMessage({

                type: "nav_path",

                points: points

            });

        }
    );

}
