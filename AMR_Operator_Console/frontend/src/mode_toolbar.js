// Owns the map's tool selection: Set Goal / Draw Path / Draw Zone.
//
// Selection is exclusive and lives in map_renderer, so the buttons here are
// only a view of it -- anything else that changes the mode (finishing a zone,
// hitting Redraw) lights the right button without having to know about the
// toolbar.
import {
    MODE_GOAL,
    MODE_NONE,
    MODE_PATH,
    MODE_ZONE,
    getInteractionMode,
    onModeChange,
    setInteractionMode,
} from "./map_renderer.js";

const BUTTONS = [
    ["goal-toggle", MODE_GOAL],
    ["draw-toggle", MODE_PATH],
    ["zone-toggle", MODE_ZONE],
];

const HINTS = {
    [MODE_NONE]: "Pick a tool to interact with the map.",
    [MODE_GOAL]: "Tap the map to send the AMR to a single goal.",
    [MODE_PATH]: "Hold and drag to draw a path, then Send Path.",
    [MODE_ZONE]: "Hold and drag to trace a keep-out zone, then name and save it.",
};

export function initModeToolbar() {

    const hint = document.getElementById("mode-hint");

    BUTTONS.forEach(([id, mode]) => {

        const button = document.getElementById(id);

        if (!button) {
            return;
        }

        button.addEventListener("click", () => {

            // Tapping the live tool turns it off, so the operator can pan or
            // read the map without arming anything.
            setInteractionMode(
                getInteractionMode() === mode ? MODE_NONE : mode
            );

        });

    });

    onModeChange((mode) => {

        BUTTONS.forEach(([id, buttonMode]) => {

            const button = document.getElementById(id);

            if (button) {
                button.classList.toggle("active", mode === buttonMode);
            }

        });

        if (hint) {
            hint.textContent = HINTS[mode] || HINTS[MODE_NONE];
        }

    });

    if (hint) {
        hint.textContent = HINTS[MODE_NONE];
    }

}
