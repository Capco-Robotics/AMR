// Emergency stop.
//
// First thing on the home screen, above the menu, because an operator
// reaching for it is not going to navigate to it first.
//
// It is a latch, not a momentary button. Pressing it makes the gateway refuse
// every frame that can move the robot -- teleop, goals, paths, map building --
// and hold a zero twist on /cmd_vel until it is explicitly released. Engaging
// asks for nothing: a stop you have to confirm is not a stop, and the cost of
// an accidental press is one release. Releasing does ask, because that is the
// direction that can hurt someone.
//
// It is a *software* stop and it says so on the button. It covers every path
// this stack has to the motors (Nav2, teleop, and the Pico's drive latch), but
// it depends on the network, the RPi and the firmware all still working. It is
// not a substitute for a physical cut-off, and the "not sent" case below is
// loud for exactly that reason.
import { sendMessage } from "./ws_client.js";
import { notifyError, notifyInfo } from "./notice.js";

const IDLE_HINT =
    "Cuts drive power and cancels whatever the AMR is doing.";

const ENGAGED_HINT =
    "Stopped. The AMR refuses drive and navigation commands until this is "
    + "released.";

let button = null;
let hint = null;

let engaged = false;

// Overrides the hint for one render, for things that are true right now
// rather than true of the state -- "waiting for the AMR to confirm".
let detail = "";

export function initEstopPanel() {

    button = document.getElementById("estop-btn");
    hint = document.getElementById("estop-status");

    if (!button) {
        return;
    }

    button.addEventListener("click", onPress);

    render();
}

function onPress() {

    if (!engaged) {
        send(true);
        return;
    }

    const confirmed = window.confirm(
        "Release the emergency stop?\n\n"
        + "The AMR will accept drive and navigation commands again. Check "
        + "that the area around it is clear first."
    );

    if (confirmed) {
        send(false);
    }
}

function send(engage) {

    const sent = sendMessage({
        type: "estop",
        engage: engage,
    });

    if (!sent) {

        // Failing silently here would be the worst outcome in the app: the
        // operator has pressed stop, has no reason to think it did not land,
        // and the robot is still driving.
        notifyError(
            engage
                ? "EMERGENCY STOP NOT SENT — no connection to the AMR. "
                  + "Use the physical cut-off."
                : "Not sent — no connection to the AMR."
        );

        return;
    }

    if (engage) {
        // Optimistic, so the button changes under the operator's finger
        // rather than after a round trip. The gateway's estop_state (and the
        // estop field on every heartbeat) is what confirms or corrects it.
        setEstopEngaged(true, "Sent — waiting for the AMR to confirm");
    }
}

/**
 * Set the latch as reported by the gateway. Deliberately quiet: this is also
 * the once-a-second heartbeat path, and announcing on it would repeat the
 * same notice forever. handleEstopFrame() is the one that announces.
 */
export function setEstopEngaged(next, message = "") {

    engaged = Boolean(next);
    detail = message;

    render();
}

export function handleEstopFrame(frame) {

    const was = engaged;

    setEstopEngaged(frame.engaged);

    // A refusal the gateway wants to explain -- a command sent while the stop
    // was engaged. That is the message worth showing, not the state change.
    if (frame.message) {
        notifyError(frame.message);
        return;
    }

    // Only on a real transition. An operator who pressed the button here has
    // already flipped `was` optimistically, so this fires for stops engaged
    // from somewhere else -- another console, or a future physical button.
    if (engaged && !was) {
        notifyError("Emergency stop engaged — the AMR is stopped");
    } else if (!engaged && was) {
        notifyInfo("Emergency stop released");
    }
}

function render() {

    if (!button) {
        return;
    }

    button.classList.toggle("estop-engaged", engaged);
    button.setAttribute("aria-pressed", engaged ? "true" : "false");

    button.textContent = engaged
        ? "RELEASE STOP"
        : "EMERGENCY STOP";

    if (hint) {

        hint.textContent =
            detail || (engaged ? ENGAGED_HINT : IDLE_HINT);

        hint.classList.toggle("estop-status-engaged", engaged);
    }
}
