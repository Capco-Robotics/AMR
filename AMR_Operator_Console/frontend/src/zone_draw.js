// Freehand tracing of keep-out zones over the map canvas.
//
// Same interaction as path drawing -- hold and drag -- because it is the only
// gesture that works identically with a mouse, a stylus and a finger. On
// release the loop is closed automatically and thinned with RDP: an operator
// tracing a rectangle by hand produces a few hundred samples, and the gateway
// caps a zone at 200 vertices (nothing is gained by shipping the noise).
//
// Imported for its side effect, exactly as path_draw does: the UMD build
// assigns `self.simplify` when loaded without a module loader.
import "./vendor/simplify.js";

import {
    MODE_ZONE,
    canvasToWorld,
    isMode,
    setZoneDraft,
} from "./map_renderer.js";

// Zone outlines carry no useful detail below this, and every retained vertex
// costs rasterisation work on the robot. Deliberately coarser than the path
// epsilon, which the operator can tune because path shape is the whole point.
const ZONE_EPSILON_M = 0.12;

const MIN_ZONE_VERTICES = 3;

let rawStroke = [];

let draftPolygon = [];

let drawing = false;

export function getDraft() {
    return draftPolygon;
}

export function clearDraft() {

    rawStroke = [];
    draftPolygon = [];

    setZoneDraft([]);

}

function finish() {

    if (rawStroke.length < MIN_ZONE_VERTICES) {

        // Not enough of a gesture to enclose anything. Drop it rather than
        // leaving a degenerate two-point "zone" the gateway would reject.
        clearDraft();

        return;

    }

    const simplified = window.simplify(
        rawStroke.map((p) => ({ x: p[0], y: p[1] })),
        ZONE_EPSILON_M,
        true,
    );

    let polygon = simplified.map((p) => [p.x, p.y]);

    // RDP keeps both endpoints, so a closed-looking trace ends with a vertex
    // almost on top of its first one. The polygon is implicitly closed by the
    // renderer and the rasteriser, so that duplicate is just a zero-length
    // edge.
    if (polygon.length > MIN_ZONE_VERTICES) {

        const first = polygon[0];
        const last = polygon[polygon.length - 1];

        const dx = first[0] - last[0];
        const dy = first[1] - last[1];

        if (Math.hypot(dx, dy) < ZONE_EPSILON_M) {
            polygon.pop();
        }

    }

    if (polygon.length < MIN_ZONE_VERTICES) {
        clearDraft();
        return;
    }

    draftPolygon = polygon;

    setZoneDraft(draftPolygon);

}

export function initZoneDraw() {

    const canvas = document.getElementById("map-canvas");

    if (!canvas) {
        return;
    }

    canvas.addEventListener("pointerdown", (event) => {

        if (!isMode(MODE_ZONE)) {
            return;
        }

        const world = canvasToWorld(event.clientX, event.clientY);

        if (!world) {
            return;
        }

        drawing = true;

        // Keep receiving moves even if the pointer leaves the canvas, and
        // guarantee a pointerup we can close the loop on.
        canvas.setPointerCapture(event.pointerId);

        rawStroke = [[world.x, world.y]];
        draftPolygon = [];

        setZoneDraft(rawStroke);

        event.preventDefault();

    });

    canvas.addEventListener("pointermove", (event) => {

        if (!drawing || !isMode(MODE_ZONE)) {
            return;
        }

        const world = canvasToWorld(event.clientX, event.clientY);

        if (!world) {
            return;
        }

        rawStroke.push([world.x, world.y]);

        setZoneDraft(rawStroke);

    });

    function endStroke(event) {

        if (!drawing) {
            return;
        }

        drawing = false;

        if (canvas.hasPointerCapture(event.pointerId)) {
            canvas.releasePointerCapture(event.pointerId);
        }

        finish();

    }

    canvas.addEventListener("pointerup", endStroke);
    canvas.addEventListener("pointercancel", endStroke);

}
