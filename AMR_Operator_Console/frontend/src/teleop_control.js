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

function _sendFrame(socket, keys) {

    if (socket.readyState !== WebSocket.OPEN) {
        return;
    }

    const frame = _computeDriveFrame(keys);

    socket.send(
        JSON.stringify(frame)
    );
}

export function initTeleop(socket) {


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

        _sendFrame(socket, _active);

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