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
    blocked: "#dc2626",
    explore: "#0d9488",
};

let latestMapFrame = null;

// Horizontal runs of like cells, in grid coordinates: {row, from, to}.
// Rebuilt only when a new map arrives, not on every repaint.
let wallRuns = [];
let freeRuns = [];

// Denoised occupancy as one cell per entry, kept so the console can warn
// about a path crossing a wall while it is still being drawn. The gateway
// re-checks against the real map before anything is driven -- this is the
// fast advisory copy, not the authority.
let occupancy = null;
let occupancyWidth = 0;
let occupancyHeight = 0;

let goalMarker = null;
let planPoints = [];
let drawStroke = [];
let previewPath = [];
let zones = [];
let zoneDraft = [];

// Where the map builder is currently driving, as [x, y] in map metres, or
// null. Without it an unattended run looks like the robot wandering off.
let exploreTarget = null;

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

/** The frontier the map builder is heading for, or null when it is idle. */
export function setExploreTarget(point) {

    const next =
        Array.isArray(point) && point.length >= 2 ? point : null;

    // Feedback arrives twice a second and the target only changes every few
    // frontiers, so repainting on every frame would redraw the whole map for
    // nothing.
    const same =
        (next === null && exploreTarget === null) ||
        (next &&
            exploreTarget &&
            next[0] === exploreTarget[0] &&
            next[1] === exploreTarget[1]);

    if (same) {
        return;
    }

    exploreTarget = next;

    repaint();
}

export function hasMap() {
    return latestMapFrame !== null;
}

/**
 * Move the robot marker, without touching the map underneath it.
 *
 * The pose used to arrive only as a field on the map frame, and slam_toolbox
 * republishes the map every two seconds -- so the marker jumped between
 * positions two seconds apart while RViz, reading tf at 20 Hz, showed it
 * gliding. Under teleop that read as the console being broken. The gateway now
 * streams a `pose` frame ten times a second and this applies it.
 */
export function updateRobotPose(frame) {

    if (!latestMapFrame) {
        // Nothing to draw on yet. The next map frame carries a pose of its
        // own, so nothing is lost by dropping this one.
        return;
    }

    latestMapFrame.pose = {
        x: frame.x,
        y: frame.y,
        yaw: frame.yaw,
    };

    requestRepaint();
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

    // map_encoder walks the OccupancyGrid's data array in order and writes
    // PNG rows in that same order, so PNG row N *is* grid row N. There is no
    // flip to undo here -- paintRuns already puts grid row 0 at the bottom of
    // the canvas, which is where world -y belongs. Reading (height-1-row)
    // here as well double-flipped it and mirrored the whole map vertically
    // against RViz.
    const wall = new Uint8Array(width * height);
    const free = new Uint8Array(width * height);

    for (let i = 0; i < width * height; i += 1) {
        const value = data[i * 4];
        if (value <= OCCUPIED_MAX) wall[i] = 1;
        else if (value >= FREE_MIN) free[i] = 1;
    }

    denoise(wall, width, height);

    occupancy = wall;
    occupancyWidth = width;
    occupancyHeight = height;

    wallRuns = runsOf(wall, width, height);
    freeRuns = runsOf(free, width, height);
}

/**
 * Drop isolated occupied cells.
 *
 * A live SLAM map is speckled with one-cell hits from scan noise and from
 * cells only ever seen at a glancing angle. Painted as-is they read as grit
 * scattered around every wall -- the "jittery pixels" that made the map look
 * unfinished. A cell with almost no occupied neighbours is not a wall, so it
 * is not drawn as one. Two neighbours is enough to keep genuine thin walls
 * and corners, which always have a neighbour along their length.
 */
function denoise(cells, width, height) {

    const keep = new Uint8Array(cells);

    for (let row = 0; row < height; row += 1) {
        for (let col = 0; col < width; col += 1) {

            const i = row * width + col;

            if (!cells[i]) {
                continue;
            }

            let neighbours = 0;

            for (let dy = -1; dy <= 1; dy += 1) {
                for (let dx = -1; dx <= 1; dx += 1) {

                    if (dx === 0 && dy === 0) continue;

                    const y = row + dy;
                    const x = col + dx;

                    if (y < 0 || y >= height || x < 0 || x >= width) continue;

                    neighbours += cells[y * width + x];
                }
            }

            if (neighbours < 2) {
                keep[i] = 0;
            }
        }
    }

    cells.set(keep);
}

/** Merge horizontally adjacent set cells into {row, from, to} spans. */
function runsOf(cells, width, height) {

    const runs = [];

    for (let row = 0; row < height; row += 1) {

        let from = -1;

        for (let col = 0; col <= width; col += 1) {

            const set = col < width && cells[row * width + col];

            if (set) {
                if (from < 0) from = col;
            } else if (from >= 0) {
                runs.push({ row, from, to: col });
                from = -1;
            }
        }
    }

    return runs;
}

/**
 * True when any part of the stroke lies on a wall.
 *
 * Advisory only, and deliberately cheaper and looser than the gateway's
 * check: no inflation, and sampled at one cell rather than half. It exists to
 * colour the line while the operator drags, not to decide anything. The
 * gateway re-checks against the real map with the robot's clearance before
 * any of it is driven.
 */
export function strokeCrossesWall(points) {

    if (!occupancy || !points || points.length === 0) {
        return false;
    }

    const step = latestMapFrame.resolution;

    for (let i = 0; i < points.length; i += 1) {

        if (isOccupiedAt(points[i][0], points[i][1])) {
            return true;
        }

        if (i + 1 >= points.length) {
            break;
        }

        const [x0, y0] = points[i];
        const [x1, y1] = points[i + 1];

        const length = Math.hypot(x1 - x0, y1 - y0);
        const steps = Math.floor(length / step);

        for (let s = 1; s <= steps; s += 1) {

            const t = (s * step) / length;

            if (isOccupiedAt(x0 + (x1 - x0) * t, y0 + (y1 - y0) * t)) {
                return true;
            }
        }
    }

    return false;
}

/** True when world (x, y) falls on an occupied cell. */
export function isOccupiedAt(worldX, worldY) {

    if (!occupancy || !latestMapFrame) {
        return false;
    }

    const col = Math.floor(
        (worldX - latestMapFrame.origin.x) / latestMapFrame.resolution
    );
    const row = Math.floor(
        (worldY - latestMapFrame.origin.y) / latestMapFrame.resolution
    );

    if (col < 0 || col >= occupancyWidth) return false;
    if (row < 0 || row >= occupancyHeight) return false;

    return occupancy[row * occupancyWidth + col] === 1;
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

// Pose frames arrive faster than the display refreshes, and each repaint
// redraws every wall run. Coalescing to one repaint per animation frame keeps
// a 10 Hz pose stream from doing 10 full redraws a second on a phone.
let repaintQueued = false;

function requestRepaint() {

    if (repaintQueued) {
        return;
    }

    repaintQueued = true;

    requestAnimationFrame(() => {
        repaintQueued = false;
        repaint();
    });
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

    // Colour the operator's own stroke by whether it is drivable, so the
    // problem is visible while drawing rather than only on refusal.
    strokePolyline(
        drawStroke,
        strokeCrossesWall(drawStroke) ? COLOURS.blocked : COLOURS.stroke,
        3 * dpr,
    );

    if (goalMarker) {

        ctx.beginPath();
        ctx.arc(goalMarker.x, goalMarker.y, 7 * dpr, 0, Math.PI * 2);
        ctx.fillStyle = COLOURS.goal;
        ctx.fill();
        ctx.strokeStyle = "#ffffff";
        ctx.lineWidth = 2 * dpr;
        ctx.stroke();
    }

    if (exploreTarget) {
        paintExploreTarget(exploreTarget, dpr);
    }

    if (latestMapFrame.pose) {
        paintRobot(latestMapFrame.pose, dpr);
    }
}

/**
 * The frontier the map builder is driving to.
 *
 * An open ring rather than a filled dot, so it reads differently from the
 * operator's own green goal marker at a glance -- this one is the robot's
 * choice, not the operator's -- and so the unexplored edge underneath it stays
 * visible through the middle.
 */
function paintExploreTarget(target, dpr) {

    const pixel = worldToPixel(target[0], target[1]);

    ctx.strokeStyle = "#ffffff";
    ctx.lineWidth = 5 * dpr;

    ctx.beginPath();
    ctx.arc(pixel.x, pixel.y, 9 * dpr, 0, Math.PI * 2);
    ctx.stroke();

    ctx.strokeStyle = COLOURS.explore;
    ctx.lineWidth = 2.5 * dpr;

    ctx.beginPath();
    ctx.arc(pixel.x, pixel.y, 9 * dpr, 0, Math.PI * 2);
    ctx.stroke();

    ctx.beginPath();
    ctx.arc(pixel.x, pixel.y, 2.5 * dpr, 0, Math.PI * 2);
    ctx.fillStyle = COLOURS.explore;
    ctx.fill();
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
