// Freehand path drawing over the map canvas.
//
// The operator holds the pointer down and drags; every sample is converted
// straight to world metres so the stroke survives a canvas resize (the map
// canvas is resized to match each incoming map's pixel dimensions). On
// release the raw stroke is thinned with Ramer-Douglas-Peucker before it is
// offered to the backend as a path.
//
// Imported for its side effect: this is the upstream UMD build, which assigns
// `self.simplify` when it is loaded without a module loader. index.html never
// loaded it, so every endStroke() threw "window.simplify is not a function";
// importing it here ties the dependency to the one file that uses it, and
// module imports are resolved before this body runs.
import "./vendor/simplify.js";

import {
    MODE_PATH,
    canvasToWorld,
    isMode,
    onModeChange,
    setDrawStroke,
    setInteractionMode,
} from "./map_renderer.js";

// Raw pointer samples and the thinned result, both as [x, y, theta] world
// points -- the same shape the backend's path_save/nav_path frames expect.
let rawStroke = [];
let cleanStroke = [];

let drawing = false;

let epsilonSlider = null;

function currentEpsilon() {

    // The slider was previously ignored entirely: endStroke() passed a
    // hardcoded 0.10, so dragging it changed the readout and nothing else.
    if (!epsilonSlider) {
        return 0.10;
    }

    const value = parseFloat(epsilonSlider.value);

    return Number.isFinite(value) ? value : 0.10;
}

export function beginStroke(point) {

    rawStroke = [point];

}

export function appendPoint(point) {

    rawStroke.push(point);

}

export function endStroke() {

    if (rawStroke.length < 2) {

        cleanStroke = rawStroke;

        return;

    }

    // simplify() reads p.x / p.y off each point, so it silently returned the
    // endpoints unchanged when handed raw [x, y, theta] arrays -- every
    // coordinate read as undefined. Convert in, convert back out.
    const simplified = window.simplify(
        rawStroke.map(p => ({ x: p[0], y: p[1] })),
        currentEpsilon(),
        true,
    );

    cleanStroke = simplified.map(p => [p.x, p.y, 0.0]);

}

export function clear() {

    rawStroke = [];
    cleanStroke = [];

    setDrawStroke([]);

}

export function loadPath(points) {

    cleanStroke = points;
    rawStroke = points;

    setDrawStroke(cleanStroke);

}

export function getCleanPath() {

    return cleanStroke;

}

export function initPathDraw() {

    const canvas = document.getElementById("map-canvas");

    epsilonSlider = document.getElementById("epsilon-slider");

    const epsilonValue = document.getElementById("epsilon-value");

    // #draw-controls is hidden by default: Send Path / Redraw / Clear / Stop
    // and the epsilon slider only mean anything while the path tool is live.
    const drawControls = document.getElementById("draw-controls");

    if (!canvas) {
        return;
    }

    // The toolbar owns which tool is selected; this just follows it, so a
    // mode change from anywhere (Redraw, or arming the zone tool) leaves the
    // controls in the right state.
    onModeChange((mode) => {

        if (drawControls) {
            drawControls.classList.toggle("visible", mode === MODE_PATH);
        }

        if (mode !== MODE_PATH) {
            drawing = false;
        }

    });

    if (epsilonSlider && epsilonValue) {

        const showEpsilon = () => {
            epsilonValue.innerText =
                `${currentEpsilon().toFixed(2)} m`;
        };

        epsilonSlider.addEventListener("input", () => {

            showEpsilon();

            // Re-thin the stroke we already have, so the slider is a live
            // preview of what "Send Path" would actually transmit.
            if (rawStroke.length >= 2) {
                endStroke();
                setDrawStroke(cleanStroke);
            }

        });

        showEpsilon();

    }

    // Pointer events (not mouse events) so a stylus or touch drag works too.
    canvas.addEventListener("pointerdown", (event) => {

        if (!isMode(MODE_PATH)) {
            return;
        }

        const world = canvasToWorld(event.clientX, event.clientY);

        if (!world) {
            return;
        }

        drawing = true;

        // Keep receiving moves even if the pointer leaves the canvas, and
        // guarantee a pointerup we can end the stroke on.
        canvas.setPointerCapture(event.pointerId);

        beginStroke([world.x, world.y, 0.0]);

        setDrawStroke(rawStroke);

        event.preventDefault();

    });

    canvas.addEventListener("pointermove", (event) => {

        if (!drawing) {
            return;
        }

        const world = canvasToWorld(event.clientX, event.clientY);

        if (!world) {
            return;
        }

        appendPoint([world.x, world.y, 0.0]);

        setDrawStroke(rawStroke);

    });

    function finishStroke(event) {

        if (!drawing) {
            return;
        }

        drawing = false;

        if (canvas.hasPointerCapture(event.pointerId)) {
            canvas.releasePointerCapture(event.pointerId);
        }

        endStroke();

        setDrawStroke(cleanStroke);

    }

    canvas.addEventListener("pointerup", finishStroke);
    canvas.addEventListener("pointercancel", finishStroke);

    const redrawButton = document.getElementById("redraw-path-btn");

    if (redrawButton) {

        redrawButton.addEventListener("click", () => {

            clear();

            setInteractionMode(MODE_PATH);

        });

    }

    const clearButton = document.getElementById("clear-path-btn");

    if (clearButton) {
        clearButton.addEventListener("click", clear);
    }

}
