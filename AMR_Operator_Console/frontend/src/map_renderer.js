// Renders the SLAM occupancy grid (sent by amr_command's map_encoder as a
// PNG/compact image) plus a robot-pose marker, onto the <canvas> 2D context.
import { websocket } from "./ws_client.js";
const canvas = document.getElementById("map-canvas");
const ctx = canvas.getContext("2d");

let mapImage = null;

let latestMapFrame = null;

let goalMode = false;

let goalMarker = null;

export function setGoalMode(enabled) {

    goalMode = enabled;

    canvas.style.cursor =
        enabled ? "crosshair" : "default";
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

    mapImage = new Image();

    mapImage.onload = () => {

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

        // Task 7: Draw robot marker
        if (!mapFrame.pose) {
            return;
        }

        const resolution = mapFrame.resolution;

        const originX = mapFrame.origin.x;
        const originY = mapFrame.origin.y;

        const robotX =
            (mapFrame.pose.x - originX) / resolution;

        const robotY =
            canvas.height -
            ((mapFrame.pose.y - originY) / resolution);

        const yaw = mapFrame.pose.yaw || 0;

        // Robot body
        ctx.beginPath();
        ctx.arc(robotX, robotY, 5, 0, Math.PI * 2);
        ctx.fillStyle = "red";
        ctx.fill();

        // Heading line
        const lineLength = 15;

        const endX =
            robotX + Math.cos(yaw) * lineLength;

        const endY =
            robotY - Math.sin(yaw) * lineLength;

        ctx.beginPath();
        ctx.moveTo(robotX, robotY);
        ctx.lineTo(endX, endY);
        ctx.strokeStyle = "red";
        ctx.lineWidth = 2;
        ctx.stroke();

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
    };
    

    mapImage.src =
        `data:image/png;base64,${mapFrame.image}`;
}

canvas.addEventListener("click", (event) => {

    if (!goalMode || !latestMapFrame) {
        return;
    }

    const rect = canvas.getBoundingClientRect();

    const scaleX = canvas.width / rect.width;
    const scaleY = canvas.height / rect.height;

    const pixelX =
        (event.clientX - rect.left) * scaleX;

    const pixelY =
        (event.clientY - rect.top) * scaleY;

    const worldX =
        latestMapFrame.origin.x +
        pixelX * latestMapFrame.resolution;

    const worldY =
        latestMapFrame.origin.y +
        (canvas.height - pixelY) *
        latestMapFrame.resolution;

    goalMarker = {
        x: pixelX,
        y: pixelY,
    };

    if (websocket) {

        websocket.send(
            JSON.stringify({
                type: "nav_goal",
                x: worldX,
                y: worldY,
                theta: 0.0,
            })
        );

    }

    renderMap(latestMapFrame);

});