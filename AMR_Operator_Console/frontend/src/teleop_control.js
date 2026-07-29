// Goes through ws_client's sendMessage rather than holding a socket: the
// client reconnects, and a captured socket would be the dead one from before
// the drop -- teleop would look bound but silently stop driving.
import { sendMessage } from "./ws_client.js";

const DRIVE_LINEAR_SPEED = 0.4;
const DRIVE_ANGULAR_SPEED = 1.0;

const _active = new Set();

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


    document.addEventListener("keydown", (event) => {

        const key = event.key.toLowerCase();

        if (["w", "a", "s", "d"].includes(key)) {

            event.preventDefault();

            _active.add(key);
        }
    });

    document.addEventListener("keyup", (event) => {

        const key = event.key.toLowerCase();

        if (["w", "a", "s", "d"].includes(key)) {

            event.preventDefault();

            _active.delete(key);
        }
    });

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