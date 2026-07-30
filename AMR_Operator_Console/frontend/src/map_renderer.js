// Draws the SLAM occupancy grid and everything layered on it: the robot, the
// Nav2 plan, the operator's freehand path, a previewed saved path, and
// keep-out zones.
//
// The map is NOT drawn by blitting the PNG the gateway sends. That PNG is one
// pixel per grid cell, and scaling it up to fill a laptop card turned every
// wall into a ragged staircase of 4 px blocks. Instead the PNG is decoded
// once into cell data, occupied cells are merged into horizontal runs, and
// those runs are filled *and* stroked with round joins -- which renders a
// two-cell-thick wall as one solid, continuous line at any zoom.
import { websocket } from "./ws_client.js";

const canvas = document.getElementById("map-canvas");
const ctx = canvas.getContext("2d");

// Grayscale values map_encoder emits, and the midpoints we classify against.
const GRAY_OCCUPIED = 0;
const GRAY_UNKNOWN = 205;
const GRAY_FREE = 254;

const OCCUPIED_MAX = 100;   // <= this is a wall
const FREE_MIN = 230;       // >= this is open floor; between the two: unknown

const COLOURS = {
    free: "#ffffff",
    unknown: "#e9edf2",
    wall: "#33405a",
    plan: "#2563eb",
    stroke: "#f59e0b",
    preview: "#7c3aed",
    zone: "#ef4444",
    zoneFill: "rgba(239, 68, 68, 0.22)",
    zoneDraftFill: "rgba(239, 68, 68, 0.12)",
    goal: "#16a34a",
    robot: "#1f2937",
};

let latestMapFrame = null;

// Horizontal runs of like cells, in grid coordinates: {row, from, to}.
// Rebuilt only when a new map arrives, not on every repaint.
let wallRuns = [];
let freeRuns = [];

let goalMarker = null;
let planPoints = [];
let drawStroke = [];
let previewPath = [];
let zones = [];
let zoneDraft = [];

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

export function onModeChange(listener) {
    modeListeners.push(listener);
}

export function setInteractionMode(mode) {

    interactionMode = mode;

    canvas.style.cursor = mode === MODE_NONE ? "default" : "crosshair";

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

/** A saved path shown without being driven, for the Run Path screen. */
export function setPreviewPath(points) {
    previewPath = points || [];
    repaint();
}

export function hasMap() {
    return latestMapFrame !== null;
}

export function updatePlan(planFrame) {

    planPoints = planFrame.points || [];

    if (planPoints.length === 0) {
        goalMarker = null;
    }

    repaint();
}

// ---- coordinates --------------------------------------------------------

/** Canvas pixels per grid cell. */
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

export function canvasToWorld(clientX, clientY) {

    if (!latestMapFrame) {
        return null;
    }

    const rect = canvas.getBoundingClientRect();

    if (!rect.width || !rect.height) {
        return null;
    }

    const pixelX = (clientX - rect.left) * (canvas.width / rect.width);
    const pixelY = (clientY - rect.top) * (canvas.height / rect.height);

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

function resizeBackingStore() {

    if (!latestMapFrame || !latestMapFrame.width) {
        return false;
    }

    const wrap = canvas.parentElement;

    if (wrap) {

        wrap.style.aspectRatio =
            `${latestMapFrame.width} / ${latestMapFrame.height}`;

        // The stylesheet caps map height by bounding its *width* through this
        // ratio; capping height directly would squash the box out of the
        // aspect ratio the canvas fills, and the pointer maths assumes one
        // uniform scale on both axes.
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

// ---- map decoding -------------------------------------------------------

const decoder = document.createElement("canvas");
const decoderCtx = decoder.getContext("2d", { willReadFrequently: true });

/**
 * Turn the decoded map image into horizontal runs of wall and of free space.
 *
 * Runs rather than per-cell rects: a 400x400 map is 160k cells, and painting
 * each one as its own rectangle every frame is both slow and what produced
 * the visible seams between neighbouring cells. A row of wall becomes one
 * rectangle, which fills as a single unbroken block.
 */
function extractRuns(image, width, height) {

    decoder.width = width;
    decoder.height = height;

    decoderCtx.clearRect(0, 0, width, height);
    decoderCtx.drawImage(image, 0, 0);

    const data = decoderCtx.getImageData(0, 0, width, height).data;

    const walls = [];
    const free = [];

    for (let row = 0; row < height; row += 1) {

        // The encoder ships OccupancyGrid rows bottom-up, and PNG row 0 is
        // the top, so image row (height-1-row) is grid row `row`.
        const imageRow = height - 1 - row;

        let wallFrom = -1;
        let freeFrom = -1;

        for (let col = 0; col <= width; col += 1) {

            let isWall = false;
            let isFree = false;

            if (col < width) {
                const value = data[(imageRow * width + col) * 4];
                isWall = value <= OCCUPIED_MAX;
                isFree = value >= FREE_MIN;
            }

            if (isWall) {
                if (wallFrom < 0) wallFrom = col;
            } else if (wallFrom >= 0) {
                walls.push({ row, from: wallFrom, to: col });
                wallFrom = -1;
            }

            if (isFree) {
                if (freeFrom < 0) freeFrom = col;
            } else if (freeFrom >= 0) {
                free.push({ row, from: freeFrom, to: col });
                freeFrom = -1;
            }
        }
    }

    wallRuns = walls;
    freeRuns = free;
}

export function renderMap(mapFrame) {

    if (!mapFrame || !mapFrame.image) {
        return;
    }

    latestMapFrame = mapFrame;

    resizeBackingStore();

    const image = new Image();

    image.onload = () => {

        extractRuns(image, mapFrame.width, mapFrame.height);

        repaint();
    };

    image.src = `data:image/png;base64,${mapFrame.image}`;
}

// ---- painting -----------------------------------------------------------

function paintRuns(runs, scale, colour) {

    ctx.fillStyle = colour;
    ctx.beginPath();

    runs.forEach((run) => {

        const x = run.from * scale;
        const width = (run.to - run.from) * scale;

        // Grid row 0 is the bottom of the world, canvas y grows downward.
        const y = canvas.height - (run.row + 1) * scale;

        // +1 device pixel of overlap closes the hairline seams that
        // sub-pixel run boundaries leave between adjacent rows.
        ctx.rect(x, y, width + 1, scale + 1);
    });

    ctx.fill();
}

function repaint() {

    if (!latestMapFrame) {
        return;
    }

    const scale = cellScale();
    const dpr = window.devicePixelRatio || 1;

    // Unknown space is the backdrop; free and occupied are painted onto it.
    ctx.fillStyle = COLOURS.unknown;
    ctx.fillRect(0, 0, canvas.width, canvas.height);

    paintRuns(freeRuns, scale, COLOURS.free);

    // Fill *and* stroke: the stroke with a round join is what turns a
    // staircase of cells into one continuous wall, and thickens a
    // single-cell wall enough to read at a glance.
    ctx.fillStyle = COLOURS.wall;
    ctx.strokeStyle = COLOURS.wall;
    ctx.lineWidth = Math.max(1.5 * dpr, scale * 0.75);
    ctx.lineJoin = "round";
    ctx.lineCap = "round";

    ctx.beginPath();

    wallRuns.forEach((run) => {

        const x = run.from * scale;
        const width = (run.to - run.from) * scale;
        const y = canvas.height - (run.row + 1) * scale;

        ctx.rect(x, y, width, scale);
    });

    ctx.fill();
    ctx.stroke();

    zones.forEach((zone) => paintZone(zone.polygon, zone.name, false, dpr));

    if (zoneDraft.length > 0) {
        paintZone(zoneDraft, null, true, dpr);
    }

    strokePolyline(previewPath, COLOURS.preview, 3 * dpr, [8 * dpr, 5 * dpr]);
    strokePolyline(planPoints, COLOURS.plan, 3 * dpr);
    strokePolyline(drawStroke, COLOURS.stroke, 3 * dpr);

    if (goalMarker) {

        ctx.beginPath();
        ctx.arc(goalMarker.x, goalMarker.y, 7 * dpr, 0, Math.PI * 2);
        ctx.fillStyle = COLOURS.goal;
        ctx.fill();
        ctx.strokeStyle = "#ffffff";
        ctx.lineWidth = 2 * dpr;
        ctx.stroke();
    }

    if (latestMapFrame.pose) {
        paintRobot(latestMapFrame.pose, dpr);
    }
}

function paintRobot(pose, dpr) {

    const robot = worldToPixel(pose.x, pose.y);
    const yaw = pose.yaw || 0;

    const radius = 9 * dpr;

    // Body and heading arrow are one filled shape with a white outline, so
    // the marker reads the same over white floor and over a dark wall.
    ctx.beginPath();
    ctx.moveTo(
        robot.x + Math.cos(yaw) * radius * 2.4,
        robot.y - Math.sin(yaw) * radius * 2.4,
    );
    ctx.lineTo(
        robot.x + Math.cos(yaw + 2.3) * radius * 1.35,
        robot.y - Math.sin(yaw + 2.3) * radius * 1.35,
    );
    ctx.lineTo(
        robot.x + Math.cos(yaw - 2.3) * radius * 1.35,
        robot.y - Math.sin(yaw - 2.3) * radius * 1.35,
    );
    ctx.closePath();

    ctx.lineWidth = 3 * dpr;
    ctx.lineJoin = "round";
    ctx.strokeStyle = "#ffffff";
    ctx.stroke();

    ctx.fillStyle = COLOURS.robot;
    ctx.fill();

    ctx.beginPath();
    ctx.arc(robot.x, robot.y, radius * 0.55, 0, Math.PI * 2);
    ctx.fillStyle = "#ffffff";
    ctx.fill();
}

function paintZone(polygon, name, isDraft, dpr) {

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

    // A draft stays open -- the operator is still tracing it. A stored zone
    // is the closed area Nav2 is actually enforcing.
    if (!isDraft) {
        ctx.closePath();
    }

    if (polygon.length >= 3) {
        ctx.fillStyle = isDraft ? COLOURS.zoneDraftFill : COLOURS.zoneFill;
        ctx.fill();
    }

    ctx.strokeStyle = COLOURS.zone;
    ctx.lineWidth = 2.5 * dpr;
    ctx.lineJoin = "round";

    if (isDraft) {
        ctx.setLineDash([7 * dpr, 5 * dpr]);
    }

    ctx.stroke();
    ctx.setLineDash([]);

    if (name) {

        const anchor = worldToPixel(polygon[0][0], polygon[0][1]);

        const x = anchor.x + 7 * dpr;
        const y = anchor.y - 7 * dpr;

        ctx.font = `600 ${13 * dpr}px system-ui, sans-serif`;

        ctx.lineWidth = 3 * dpr;
        ctx.strokeStyle = "#ffffff";
        ctx.strokeText(name, x, y);

        ctx.fillStyle = "#b91c1c";
        ctx.fillText(name, x, y);
    }
}

function strokePolyline(points, colour, width, dash) {

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
    ctx.lineJoin = "round";
    ctx.lineCap = "round";

    if (dash) {
        ctx.setLineDash(dash);
    }

    ctx.stroke();
    ctx.setLineDash([]);
}

window.addEventListener("resize", () => {

    resizeBackingStore();

    repaint();
});

canvas.addEventListener("click", (event) => {

    if (!isMode(MODE_GOAL)) {
        return;
    }

    const world = canvasToWorld(event.clientX, event.clientY);

    if (!world) {
        return;
    }

    goalMarker = { x: world.pixelX, y: world.pixelY };

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
