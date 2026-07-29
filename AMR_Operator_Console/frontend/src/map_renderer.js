// Renders the SLAM occupancy grid (sent by amr_command's map_encoder as a
// PNG/compact image) plus a robot-pose marker, onto the <canvas> 2D context.
import { websocket } from "./ws_client.js";
const canvas = document.getElementById("map-canvas");
const ctx = canvas.getContext("2d");

let mapImage = null;

let latestMapFrame = null;

let goalMode = false;

let goalMarker = null;

let planPoints = [];

// The stroke the operator is drawing right now, as [x, y, theta] world
// points. Painted as an overlay so the drag has visible feedback.
let drawStroke = [];

let drawMode = false;

export function setGoalMode(enabled) {

    goalMode = enabled;

    updateCursor();
}

export function setDrawMode(enabled) {

    drawMode = enabled;

    updateCursor();
}

function updateCursor() {

    canvas.style.cursor =
        (goalMode || drawMode) ? "crosshair" : "default";
}

export function setDrawStroke(points) {

    drawStroke = points || [];

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

    // The canvas is resized to the map's pixel dimensions but laid out by CSS,
    // so client coords have to be scaled back into canvas space first.
    const pixelX =
        (clientX - rect.left) * (canvas.width / rect.width);

    const pixelY =
        (clientY - rect.top) * (canvas.height / rect.height);

    return {
        x:
            latestMapFrame.origin.x +
            pixelX * latestMapFrame.resolution,
        y:
            latestMapFrame.origin.y +
            (canvas.height - pixelY) * latestMapFrame.resolution,
        pixelX: pixelX,
        pixelY: pixelY,
    };
}

function worldToPixel(worldX, worldY) {

    const resolution = latestMapFrame.resolution;

    return {
        x: (worldX - latestMapFrame.origin.x) / resolution,
        y:
            canvas.height -
            ((worldY - latestMapFrame.origin.y) / resolution),
    };
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

    // Task 6: Resize canvas only when map size changes
    if (
        canvas.width !== mapFrame.width ||
        canvas.height !== mapFrame.height
    ) {
        canvas.width = mapFrame.width;
        canvas.height = mapFrame.height;
    }

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
    ctx.drawImage(mapImage, 0, 0);
    ctx.restore();

    // Task 7: Draw robot marker. A map can arrive before the first odom frame,
    // so treat the pose as optional -- the overlays below still need painting.
    if (mapFrame.pose) {

        const robot = worldToPixel(mapFrame.pose.x, mapFrame.pose.y);

        const yaw = mapFrame.pose.yaw || 0;

        // Robot body
        ctx.beginPath();
        ctx.arc(robot.x, robot.y, 5, 0, Math.PI * 2);
        ctx.fillStyle = "red";
        ctx.fill();

        // Heading line
        const lineLength = 15;

        ctx.beginPath();
        ctx.moveTo(robot.x, robot.y);
        ctx.lineTo(
            robot.x + Math.cos(yaw) * lineLength,
            robot.y - Math.sin(yaw) * lineLength,
        );
        ctx.strokeStyle = "red";
        ctx.lineWidth = 2;
        ctx.stroke();

    }

    // Nav2's computed plan.
    strokePolyline(planPoints, "cyan", 3);

    // The operator's in-progress / simplified freehand stroke.
    strokePolyline(drawStroke, "orange", 2);

    if (goalMarker) {

        ctx.beginPath();

        ctx.arc(
            goalMarker.x,
            goalMarker.y,
            6,
            0,
            Math.PI * 2
        );

        ctx.fillStyle = "lime";

        ctx.fill();

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

canvas.addEventListener("click", (event) => {

    // Draw mode owns the pointer while it is active; without this guard the
    // click that ends a stroke would also fire off a one-shot nav_goal.
    if (!goalMode || drawMode) {
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

