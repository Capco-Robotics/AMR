// Renders the SLAM occupancy grid (sent by amr_command's map_encoder as a
// PNG/compact image) plus a robot-pose marker, the Nav2 plan, the operator's
// freehand path, and any keep-out zones, onto the <canvas> 2D context.
import { websocket } from "./ws_client.js";

const canvas = document.getElementById("map-canvas");
const ctx = canvas.getContext("2d");

let mapImage = null;

let latestMapFrame = null;

let goalMarker = null;

let planPoints = [];

// The stroke the operator is drawing right now, as [x, y, theta] world
// points. Painted as an overlay so the drag has visible feedback.
let drawStroke = [];

// Saved keep-out zones from the gateway, as {name, polygon} in world metres,
// plus the polygon being traced right now.
let zones = [];

let zoneDraft = [];

// Exactly one pointer tool can be live at a time. This used to be two
// independent booleans (goalMode, drawMode) that had to be manually guarded
// against each other -- a third tool made that untenable, and the guard was
// already leaking (ending a path stroke could also fire off a nav_goal).
export const MODE_NONE = "none";
export const MODE_GOAL = "goal";
export const MODE_PATH = "path";
export const MODE_ZONE = "zone";

let interactionMode = MODE_NONE;

const modeListeners = [];

export function getInteractionMode() {
    return interactionMode;
}

export function isMode(mode) {
    return interactionMode === mode;
}

/** Register a callback fired whenever the active tool changes. */
export function onModeChange(listener) {
    modeListeners.push(listener);
}

export function setInteractionMode(mode) {

    interactionMode = mode;

    canvas.style.cursor =
        mode === MODE_NONE ? "default" : "crosshair";

    modeListeners.forEach((listener) => listener(mode));

    repaint();
}

export function setDrawStroke(points) {

    drawStroke = points || [];

    repaint();
}

export function setZones(nextZones) {

    zones = nextZones || [];

    repaint();
}

export function getZones() {
    return zones;
}

export function setZoneDraft(polygon) {

    zoneDraft = polygon || [];

    repaint();
}

/**
 * Convert a pointer event's client coordinates to world metres, using the
 * latest map's origin/resolution. Returns null when no map has arrived yet
 * (there is no frame of reference to convert into).
 */
export function canvasToWorld(clientX, clientY) {

    if (!latestMapFrame) {
        return null;
    }

    const rect = canvas.getBoundingClientRect();

    if (!rect.width || !rect.height) {
        return null;
    }

    // Client coords -> backing-store coords (the element is laid out by CSS
    // and the backing store is scaled by the device pixel ratio).
    const pixelX =
        (clientX - rect.left) * (canvas.width / rect.width);

    const pixelY =
        (clientY - rect.top) * (canvas.height / rect.height);

    // ...then backing-store coords -> map cells -> world metres.
    const scale = cellScale();

    return {
        x:
            latestMapFrame.origin.x +
            (pixelX / scale) * latestMapFrame.resolution,
        y:
            latestMapFrame.origin.y +
            ((canvas.height - pixelY) / scale) * latestMapFrame.resolution,
        pixelX: pixelX,
        pixelY: pixelY,
    };
}

/**
 * Canvas pixels per map cell.
 *
 * The backing store is sized to the *display*, not to the occupancy grid (see
 * resizeBackingStore), so the map is scaled up on draw and every overlay is
 * drawn at its natural pixel size. Sizing the backing store to the grid
 * instead -- a few hundred px stretched across a desktop card -- meant lines
 * and labels were rendered tiny and then magnified into a blur.
 */
function cellScale() {

    if (!latestMapFrame || !latestMapFrame.width) {
        return 1;
    }

    return canvas.width / latestMapFrame.width;
}

function worldToPixel(worldX, worldY) {

    const resolution = latestMapFrame.resolution;
    const scale = cellScale();

    return {
        x: ((worldX - latestMapFrame.origin.x) / resolution) * scale,
        y:
            canvas.height -
            (((worldY - latestMapFrame.origin.y) / resolution) * scale),
    };
}

/**
 * Match the backing store to the element's on-screen size (times the device
 * pixel ratio, so it is sharp on a retina tablet). The wrapper carries the
 * map's aspect ratio, which keeps the element box a fixed shape and stops
 * this from feeding back into layout.
 */
function resizeBackingStore() {

    if (!latestMapFrame || !latestMapFrame.width) {
        return false;
    }

    const wrap = canvas.parentElement;

    if (wrap) {

        wrap.style.aspectRatio =
            `${latestMapFrame.width} / ${latestMapFrame.height}`;

        // The stylesheet caps the map's height by bounding its *width* with
        // this ratio. Capping the height directly would squash the box out of
        // the aspect ratio the canvas fills, and the world-to-pixel maths
        // assumes one uniform scale for both axes.
        wrap.style.setProperty(
            "--map-aspect",
            String(latestMapFrame.width / latestMapFrame.height),
        );

    }

    const cssWidth = canvas.clientWidth;
    const cssHeight = canvas.clientHeight;

    if (!cssWidth || !cssHeight) {
        return false;
    }

    const dpr = window.devicePixelRatio || 1;

    const width = Math.round(cssWidth * dpr);
    const height = Math.round(cssHeight * dpr);

    if (canvas.width === width && canvas.height === height) {
        return false;
    }

    canvas.width = width;
    canvas.height = height;

    return true;
}

export function hasMap() {
    return latestMapFrame !== null;
}

export function updatePlan(planFrame) {

    planPoints = planFrame.points || [];

    if (
        planPoints.length === 0
    ) {
        goalMarker = null;
    }

    repaint();

}

export function renderMap(mapFrame) {

    // Task 5: Safe initialization
    if (!mapFrame || !mapFrame.image) {
        return;
    }
    latestMapFrame = mapFrame;

    // The backing store follows the element, not the grid; this only needs to
    // run here because a new map can change the aspect ratio.
    resizeBackingStore();

    const image = new Image();

    // Decode off the critical path, then hand the finished bitmap to repaint.
    // Everything that actually paints lives in repaint() so that overlays (the
    // in-progress stroke, the goal marker) can be redrawn at pointer rate
    // without re-decoding the map PNG each time.
    image.onload = () => {

        mapImage = image;

        repaint();

    };

    image.src =
        `data:image/png;base64,${mapFrame.image}`;
}

function repaint() {

    if (!mapImage || !latestMapFrame) {
        return;
    }

    const mapFrame = latestMapFrame;

    // Overlay sizes are in device pixels, so they have to follow the DPR the
    // backing store was built at or they come out hairline on a retina panel.
    const scale = window.devicePixelRatio || 1;

    // Draw occupancy map.
    // A ROS OccupancyGrid is row-major BOTTOM-UP: grid row 0 is the lowest
    // world y, with y increasing upward. The encoder ships those rows in the
    // same order, but PNG/canvas row 0 is the TOP -- so drawing it as-is
    // renders the map upside-down relative to the robot-pose math below
    // (which correctly treats world +y as up). Flip vertically on draw so the
    // map, the marker, and RViz all agree. (Root cause is really the encoder
    // emitting bottom-up rows; if that is ever fixed, remove this flip.)
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    ctx.save();
    ctx.translate(0, canvas.height);
    ctx.scale(1, -1);

    // Occupancy grids are chunky by nature; interpolating them on the way up
    // to display resolution just makes the walls mushy.
    ctx.imageSmoothingEnabled = false;

    ctx.drawImage(mapImage, 0, 0, canvas.width, canvas.height);
    ctx.restore();

    // Keep-out zones sit directly on the map, under every other overlay --
    // they are terrain, not something the operator is steering.
    zones.forEach((zone) => paintZone(zone.polygon, zone.name, false, scale));

    if (zoneDraft.length > 0) {
        paintZone(zoneDraft, null, true, scale);
    }

    // Task 7: Draw robot marker. A map can arrive before the first odom frame,
    // so treat the pose as optional -- the overlays below still need painting.
    if (mapFrame.pose) {

        const robot = worldToPixel(mapFrame.pose.x, mapFrame.pose.y);

        const yaw = mapFrame.pose.yaw || 0;

        // Robot body
        ctx.beginPath();
        ctx.arc(robot.x, robot.y, 6 * scale, 0, Math.PI * 2);
        ctx.fillStyle = "#f87171";
        ctx.fill();
        ctx.strokeStyle = "#7f1d1d";
        ctx.lineWidth = 2 * scale;
        ctx.stroke();

        // Heading line
        const lineLength = 18 * scale;

        ctx.beginPath();
        ctx.moveTo(robot.x, robot.y);
        ctx.lineTo(
            robot.x + Math.cos(yaw) * lineLength,
            robot.y - Math.sin(yaw) * lineLength,
        );
        ctx.strokeStyle = "#f87171";
        ctx.lineWidth = 2.5 * scale;
        ctx.stroke();

    }

    // Nav2's computed plan.
    strokePolyline(planPoints, "#22d3ee", 2.5 * scale);

    // The operator's in-progress / simplified freehand stroke.
    strokePolyline(drawStroke, "#fb923c", 2.5 * scale);

    if (goalMarker) {

        ctx.beginPath();

        ctx.arc(
            goalMarker.x,
            goalMarker.y,
            6 * scale,
            0,
            Math.PI * 2
        );

        ctx.fillStyle = "#4ade80";

        ctx.fill();

    }

}

function paintZone(polygon, name, isDraft, scale) {

    if (!polygon || polygon.length === 0) {
        return;
    }

    ctx.beginPath();

    polygon.forEach((vertex, i) => {

        const pixel = worldToPixel(vertex[0], vertex[1]);

        if (i === 0) {
            ctx.moveTo(pixel.x, pixel.y);
        } else {
            ctx.lineTo(pixel.x, pixel.y);
        }

    });

    // A draft is shown open (the operator is still tracing it); a stored zone
    // is the closed area Nav2 is actually enforcing.
    if (!isDraft) {
        ctx.closePath();
    }

    if (polygon.length >= 3) {
        ctx.fillStyle = isDraft
            ? "rgba(239, 68, 68, 0.18)"
            : "rgba(239, 68, 68, 0.30)";
        ctx.fill();
    }

    ctx.strokeStyle = isDraft ? "#fca5a5" : "#ef4444";
    ctx.lineWidth = 2 * scale;

    if (isDraft) {
        ctx.setLineDash([6 * scale, 4 * scale]);
    }

    ctx.stroke();
    ctx.setLineDash([]);

    if (name) {

        const anchor = worldToPixel(polygon[0][0], polygon[0][1]);

        const x = anchor.x + 6 * scale;
        const y = anchor.y - 6 * scale;

        ctx.font = `600 ${13 * scale}px system-ui, sans-serif`;

        // The label sits on top of the zone's own red fill and whatever the
        // map has underneath it, so it needs its own contrast rather than
        // relying on either.
        ctx.lineWidth = 3 * scale;
        ctx.strokeStyle = "rgba(9, 12, 18, 0.85)";
        ctx.strokeText(name, x, y);

        ctx.fillStyle = "#fee2e2";
        ctx.fillText(name, x, y);

    }

}

function strokePolyline(points, colour, width) {

    if (!points || points.length === 0) {
        return;
    }

    ctx.beginPath();

    points.forEach((point, i) => {

        const pixel = worldToPixel(point[0], point[1]);

        if (i === 0) {
            ctx.moveTo(pixel.x, pixel.y);
        } else {
            ctx.lineTo(pixel.x, pixel.y);
        }

    });

    ctx.strokeStyle = colour;
    ctx.lineWidth = width;
    ctx.stroke();

}

// The backing store tracks the element's on-screen size, so a window resize
// (or a tablet rotating) has to rebuild it -- otherwise the map is drawn at
// the old resolution and stretched.
window.addEventListener("resize", () => {

    resizeBackingStore();

    repaint();

});

canvas.addEventListener("click", (event) => {

    // One exclusive mode means no cross-tool guard is needed here any more.
    if (!isMode(MODE_GOAL)) {
        return;
    }

    const world = canvasToWorld(event.clientX, event.clientY);

    if (!world) {
        return;
    }

    goalMarker = {
        x: world.pixelX,
        y: world.pixelY,
    };

    if (websocket) {

        websocket.send(
            JSON.stringify({
                type: "nav_goal",
                x: world.x,
                y: world.y,
                theta: 0.0,
            })
        );

    }

    repaint();

});
