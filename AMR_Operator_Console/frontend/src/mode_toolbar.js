// Binds the three map-tool toggles to the renderer's exclusive mode.
//
// The tools no longer live together on one toolbar -- each belongs to the
// screen that uses it (Trace New on Zones, Draw on New Path, Send to a Point
// on Home). view.js arms the right mode when a screen opens; these buttons
// let the operator turn it off, or turn it back on after a save.
//
// The buttons are only a view of the mode, so anything else that changes it
// (finishing a trace, switching screens, hitting Redraw) lights the correct
// one without needing to know this module exists.
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

export function initModeToolbar() {

    BUTTONS.forEach(([id, mode]) => {

        const button = document.getElementById(id);

        if (!button) {
            return;
        }

        button.addEventListener("click", () => {

            // Tapping the armed tool disarms it, so the operator can read the
            // map without a stray tap sending the robot somewhere.
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

    });

}
