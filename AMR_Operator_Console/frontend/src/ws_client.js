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
import {
    initExplorePanel,
    handleExploreFrame,
    refreshExploration,
} from "./explore_panel.js";
import { initZoneDraw } from "./zone_draw.js";
import { initModeToolbar } from "./mode_toolbar.js";
import { initViews } from "./view.js";
import { notifyError, notifyInfo } from "./notice.js";
import { renderMap, updatePlan, updateRobotPose } from "./map_renderer.js";
import {
    handleEstopFrame,
    initEstopPanel,
    setEstopEngaged,
} from "./estop_panel.js";


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

// ---- link liveness -------------------------------------------------------
//
// "Connected" used to mean exactly one thing: the browser's WebSocket had
// reached OPEN and had not fired onclose. That is a claim about a TCP socket,
// not about the robot. A gateway that goes away without closing the
// connection -- Pi powered off, Wi-Fi dropped, robot driven out of range --
// leaves the socket in OPEN until the OS gives up retransmitting, which takes
// minutes. For all of that time the pill said "Connected", teleop frames went
// into a buffer that would never drain, and every panel sat on its last
// value. That is the bug this section exists for.
//
// The protocol's own ping/pong cannot help: RFC 6455 pings are answered by
// the browser and are invisible to JavaScript. So liveness is measured from
// ordinary application frames instead. The gateway sends a `heartbeat` every
// second, this client sends a `ping` and counts the `pong`, and silence is
// what "disconnected" is actually derived from.
//
// Note the pill now reports two separate things, because they fail
// separately: whether frames are arriving at all, and whether the gateway's
// ROS side is still spinning behind them. The websocket server runs on its
// own thread inside amr_command, so a wedged ROS executor leaves the socket
// perfectly healthy and the robot perfectly deaf.
const LINK_CHECK_MS = 500;

// Two thresholds rather than one. A brief Wi-Fi hiccup on a tablet should
// warn rather than flash "Disconnected" and tear down a socket that was about
// to recover; five seconds of nothing, against a one-second heartbeat, is not
// a hiccup.
const STALE_MS = 2500;
const DEAD_MS = 5000;

const PING_INTERVAL_MS = 2000;

const CONNECTION_STATES = {
    connecting: ["Connecting", "Opening a websocket to the AMR"],
    online: ["Connected", "The AMR is answering"],
    stale: ["No signal", "The socket is open but the AMR has gone quiet"],
    degraded: [
        "AMR stalled",
        "The gateway is answering but its ROS side has stopped running",
    ],
    offline: ["Disconnected", "No websocket to the AMR"],
};

export let websocket = null;

let reconnectDelayMs = RECONNECT_MIN_MS;

let reconnectTimer = null;

// When the last frame of any kind arrived. 0 means "nothing yet".
let lastFrameAt = 0;

// Whether the gateway's most recent heartbeat said its ROS side was alive. A
// gateway that sends no heartbeat at all has no opinion, so this stays true.
let rosOk = true;

export function connect(onMessage) {
  const socket = new WebSocket(WS_URL);
  socket.onmessage = (event) => onMessage(JSON.parse(event.data));
  return socket;
}

/** Send a frame. Returns false if there was no open socket to send it on. */
export function sendMessage(message)
{

    if(websocket === null)
    {
        return false;
    }


    if(websocket.readyState !== WebSocket.OPEN)
    {
        return false;
    }


    websocket.send(
        JSON.stringify(message)
    );


    return true;

}


function setConnectionState(state, detail) {

    const pill = document.getElementById("connection-pill");

    if (!pill) {
        return;
    }

    const [label, explanation] = CONNECTION_STATES[state] || [state, ""];

    pill.dataset.state = state;
    pill.textContent = label;

    // The pill has room for two words; the reason it is showing them goes in
    // the tooltip rather than being left for the operator to guess.
    pill.title = detail ? `${explanation} — ${detail}` : explanation;

}


/** Re-derive the pill from how long it has been since a frame arrived. */
function refreshLinkState() {

    if (websocket === null || websocket.readyState !== WebSocket.OPEN) {
        // Not open: openSocket/onclose own the pill in that case, and
        // overwriting it here would stamp on "Connecting".
        return;
    }

    const silentMs = Date.now() - lastFrameAt;

    if (silentMs > DEAD_MS) {

        setConnectionState(
            "offline",
            `nothing received for ${Math.round(silentMs / 1000)} s`,
        );

        // The browser still calls this socket OPEN, and will go on doing so
        // for minutes. Closing it by hand is what makes onclose fire and the
        // reconnect ladder start.
        try {
            websocket.close();
        } catch (error) {
            // Nothing to do about it -- onclose still owns the retry.
        }

        return;
    }

    if (silentMs > STALE_MS) {

        setConnectionState(
            "stale",
            `${(silentMs / 1000).toFixed(1)} s since the last frame`,
        );

        return;
    }

    setConnectionState(rosOk ? "online" : "degraded");
}


function applyHeartbeat(frame) {

    // An older gateway sends no heartbeat and therefore no ros_ok; absent
    // means "no opinion", not "stalled".
    rosOk = frame.ros_ok !== false;

    // The gateway's own view of the latch, which is the authoritative one --
    // this is what confirms an operator's press actually landed, and what
    // gets a console that connected mid-stop showing the right button.
    if (typeof frame.estop === "boolean") {
        setEstopEngaged(frame.estop);
    }

    refreshLinkState();
}


function handleTelemetryFrame(data) {

    // Any frame at all is proof the link is alive. The heartbeat exists so
    // that proof keeps arriving from a robot that is parked and quiet.
    lastFrameAt = Date.now();

    switch (data.type) {

        case "heartbeat":
            applyHeartbeat(data);
            break;

        // Nothing to do with the contents -- having arrived is the whole
        // message, and the timestamp above has already recorded that.
        case "pong":
            break;

        case "estop_state":
            handleEstopFrame(data);
            break;

        case "map":
            renderMap(data);
            break;

        // Robot position on its own, ~10 Hz. The map only arrives every two
        // seconds, so without this the marker teleports between poses that
        // far apart instead of moving.
        case "pose":
            updateRobotPose(data);
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

        // Autonomous map building progress, twice a second while it runs.
        case "explore_status":

            handleExploreFrame(data);

            break;

        // The gateway refused a teleop command because something is too close
        // in the direction of travel. It rate-limits these to one a second.
        case "drive_blocked":

            notifyError(data.message || "Drive blocked by an obstacle");

            break;

    }

}


function openSocket() {

    setConnectionState("connecting");

    // Held in a local as well, so every handler below can tell whether it
    // belongs to the socket that is currently live. A socket superseded while
    // it was still connecting -- which is exactly what the stale-link close
    // above produces -- would otherwise fire onclose a moment later and drag
    // the pill back to "Disconnected" over a healthy new connection.
    const socket = connect(handleTelemetryFrame);

    websocket = socket;

    window.wsClient = socket;

    socket.onopen = () => {

        if (socket !== websocket) {
            socket.close();
            return;
        }

        console.log("Connected to AMR websocket");

        // The gateway sends a heartbeat the moment a client connects, but not
        // until the round trip completes; without this the watchdog would
        // measure silence from whenever the last socket died.
        lastFrameAt = Date.now();
        rosOk = true;

        setConnectionState("online");

        reconnectDelayMs = RECONNECT_MIN_MS;

        // Only the list pulls belong here -- they need an open socket, and
        // they are repeated on every reconnect so a console that was offline
        // while zones or maps changed does not keep showing stale ones.
        refreshMaps();
        refreshPaths();
        refreshZones();

        // Not a list pull, but the same reasoning: a console that opened (or
        // reconnected) while the AMR was mapping itself must not show Idle
        // next to a robot that is visibly driving around.
        refreshExploration();

    };

    socket.onclose = () => {

        if (socket !== websocket) {
            return;
        }

        setConnectionState("offline");

        scheduleReconnect();

    };

    socket.onerror = () => {

        if (socket !== websocket) {
            return;
        }

        // onerror is always followed by onclose, which owns the retry.
        setConnectionState("offline");

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


/** Retry immediately instead of waiting out the backoff. */
function reconnectNow() {

    if (
        websocket !== null
        && (
            websocket.readyState === WebSocket.OPEN
            || websocket.readyState === WebSocket.CONNECTING
        )
    ) {
        return;
    }

    if (reconnectTimer) {
        clearTimeout(reconnectTimer);
        reconnectTimer = null;
    }

    reconnectDelayMs = RECONNECT_MIN_MS;

    openSocket();
}


// A tablet waking from sleep, or a Wi-Fi network that has just come back,
// should not sit at "Disconnected" for the rest of a ten-second backoff when
// the browser has already told us the situation changed.
window.addEventListener("online", reconnectNow);

document.addEventListener("visibilitychange", () => {

    if (document.visibilityState === "visible") {
        reconnectNow();
    }
});


// Bind panel DOM once, not per connection. Re-binding on every open would
// stack duplicate listeners -- which is exactly what reconnecting now does.
initTeleop();

initTeleopButtons(
    document.getElementById("teleop-pad")
);

initEstopPanel();
initMapPanel();
initPathPanel();
initPathDraw();
initZonePanel();
initZoneDraw();
initExplorePanel();
initModeToolbar();
initViews();

// Lift control is deliberately UI-only for now: amr_lift exists but nothing
// is wired from the console to it yet, and a button that silently does
// nothing is worse than one that says so.
[
    ["lift-raise-btn", "Raise"],
    ["lift-lower-btn", "Lower"],
].forEach(([id, action]) => {

    const button = document.getElementById(id);

    if (button) {
        button.addEventListener("click", () => {
            notifyInfo(`${action} load: not wired to amr_lift yet`);
        });
    }

});

openSocket();

// Both are harmless while disconnected: refreshLinkState returns early on a
// socket that is not open, and sendMessage no-ops.
setInterval(refreshLinkState, LINK_CHECK_MS);

setInterval(() => {

    // Not strictly needed while the gateway is sending heartbeats, but it is
    // the half of the check that tests the *outbound* direction -- a socket
    // can be half-open, and only a missing pong shows it.
    sendMessage({ type: "ping", ts: Date.now() });

}, PING_INTERVAL_MS);


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
