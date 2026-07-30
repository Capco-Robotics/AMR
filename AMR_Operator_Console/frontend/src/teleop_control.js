// Goes through ws_client's sendMessage rather than holding a socket: the
// client reconnects, and a captured socket would be the dead one from before
// the drop -- teleop would look bound but silently stop driving.
import { sendMessage } from "./ws_client.js";
import { onScreenChange } from "./view.js";

const DRIVE_LINEAR_SPEED = 0.4;
const DRIVE_ANGULAR_SPEED = 1.0;

const RC_SCREEN = "rc";

const _active = new Set();

// W/A/S/D used to drive the robot from anywhere in the console, which meant
// typing "wasd" into a zone or path name also drove it across the floor.
// Keys are live only on the Remote Control screen.
let _keysEnabled = false;

/** True when the keystroke is someone typing, not someone driving. */
function _isTyping(event) {

    const node = event.target;

    if (!node) {
        return false;
    }

    const tag = (node.tagName || "").toLowerCase();

    return tag === "input" || tag === "textarea" || node.isContentEditable;
}

function _computeDriveFrame(keys) {
    let linear = 0.0;
    let angular = 0.0;

    if (keys.has("w")) {
        linear += DRIVE_LINEAR_SPEED;
    }

    if (keys.has("s")) {
        linear -= DRIVE_LINEAR_SPEED;
    }

    if (keys.has("a")) {
        angular += DRIVE_ANGULAR_SPEED;
    }

    if (keys.has("d")) {
        angular -= DRIVE_ANGULAR_SPEED;
    }

    return {
        type: "drive",
        linear,
        angular,
    };
}

function _sendFrame(keys) {

    sendMessage(
        _computeDriveFrame(keys)
    );
}

// Binds document-level listeners and starts the send loop. Call once: a
// second call would stack a duplicate interval and duplicate key handlers.
export function initTeleop() {

    onScreenChange((screen) => {

        _keysEnabled = screen === RC_SCREEN;

        // Leaving the screen mid-press would otherwise leave the key latched
        // and the robot driving with nothing on screen to stop it.
        if (!_keysEnabled) {
            _active.clear();
        }

    });

    document.addEventListener("keydown", (event) => {

        if (!_keysEnabled || _isTyping(event)) {
            return;
        }

        const key = event.key.toLowerCase();

        if (["w", "a", "s", "d"].includes(key)) {

            event.preventDefault();

            _active.add(key);
        }
    });

    document.addEventListener("keyup", (event) => {

        // Deliberately not gated on _keysEnabled: a key pressed on the RC
        // screen must still release if the screen changed while it was held.
        if (_isTyping(event)) {
            return;
        }

        const key = event.key.toLowerCase();

        if (["w", "a", "s", "d"].includes(key)) {

            event.preventDefault();

            _active.delete(key);
        }
    });

    // A tab-away with a key held is the other way to latch it on.
    window.addEventListener("blur", () => _active.clear());

    setInterval(() => {

        _sendFrame(_active);

    }, 100);
}

export function initTeleopButtons(padElement) {

    const buttons = padElement.querySelectorAll("[data-key]");

    buttons.forEach((button) => {

        const key = button.dataset.key;

        button.addEventListener("mousedown", () => {
            
            _active.add(key);
        });

        button.addEventListener("touchstart", (event) => {

            event.preventDefault();
            _active.add(key);
        });
        button.addEventListener("mouseup", () => {
            _active.delete(key);
        });

        button.addEventListener("mouseleave", () => {
            _active.delete(key);
        });

        button.addEventListener("touchend", () => {
            _active.delete(key);
        });

        button.addEventListener("touchcancel", () => {
            _active.delete(key);
        });

    });

}