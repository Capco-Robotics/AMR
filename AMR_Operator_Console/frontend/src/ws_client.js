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
    handlePathFrame,
    refreshPaths,
    renderPathStatus,
} from "./path_panel.js";
import {
    initZonePanel,
    handleZoneFrame,
    refreshZones,
} from "./zone_panel.js";
import { initZoneDraw } from "./zone_draw.js";
import { initModeToolbar } from "./mode_toolbar.js";
import { initPanels } from "./panels.js";
import { renderMap, updatePlan } from "./map_renderer.js";


// Follow whatever host served the page, rather than a hardcoded localhost.
// The console is meant to be opened from a tablet or phone on the same
// network as the robot, and there "localhost" is the phone -- the socket
// would try to reach a gateway on the handset and never connect.
// `?gateway=host[:port]` overrides, for serving the page from somewhere
// other than the robot.
const GATEWAY_PORT = 8765;

function gatewayUrl() {

    const override =
        new URLSearchParams(window.location.search).get("gateway");

    if (override) {
        return override.includes(":")
            ? `ws://${override}`
            : `ws://${override}:${GATEWAY_PORT}`;
    }

    // Opened as a file:// URL there is no host to inherit, so fall back.
    const host = window.location.hostname || "localhost";

    return `ws://${host}:${GATEWAY_PORT}`;
}

const WS_URL = gatewayUrl();

// Backing off avoids hammering a robot that is still booting, while staying
// responsive to a gateway that only blipped.
const RECONNECT_MIN_MS = 1000;
const RECONNECT_MAX_MS = 10000;

export let websocket = null;

let reconnectDelayMs = RECONNECT_MIN_MS;

let reconnectTimer = null;

export function connect(onMessage) {
  const socket = new WebSocket(WS_URL);
  socket.onmessage = (event) => onMessage(JSON.parse(event.data));
  return socket;
}

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


function setConnectionState(state, label) {

    const pill = document.getElementById("connection-pill");

    if (!pill) {
        return;
    }

    pill.dataset.state = state;
    pill.textContent = label;

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

            handlePathFrame(data);

            break;

        case "zone_list":
        case "zone_op_result":

            handleZoneFrame(data);

            break;

    }

}


function openSocket() {

    setConnectionState("connecting", "Connecting");

    websocket = connect(handleTelemetryFrame);

    window.wsClient = websocket;

    websocket.onopen = () => {

        console.log("Connected to AMR websocket");

        setConnectionState("online", "Connected");

        reconnectDelayMs = RECONNECT_MIN_MS;

        // Only the list pulls belong here -- they need an open socket, and
        // they are repeated on every reconnect so a console that was offline
        // while zones or maps changed does not keep showing stale ones.
        refreshMaps();
        refreshPaths();
        refreshZones();

    };

    websocket.onclose = () => {

        setConnectionState("offline", "Disconnected");

        scheduleReconnect();

    };

    websocket.onerror = () => {

        // onerror is always followed by onclose, which owns the retry.
        setConnectionState("offline", "Disconnected");

    };

}


function scheduleReconnect() {

    if (reconnectTimer) {
        return;
    }

    reconnectTimer = setTimeout(() => {

        reconnectTimer = null;

        openSocket();

    }, reconnectDelayMs);

    reconnectDelayMs = Math.min(
        reconnectDelayMs * 2,
        RECONNECT_MAX_MS,
    );

}


// Bind panel DOM once, not per connection. Re-binding on every open would
// stack duplicate listeners -- which is exactly what reconnecting now does.
initTeleop();

initTeleopButtons(
    document.getElementById("teleop-pad")
);

initMapPanel();
initPathPanel();
initPathDraw();
initZonePanel();
initZoneDraw();
initModeToolbar();
initPanels();

openSocket();


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
