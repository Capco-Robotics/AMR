// Renders the SLAM occupancy grid (sent by amr_command's map_encoder as a
// PNG/compact image) plus a robot-pose marker, onto the <canvas> 2D context.

const canvas = document.getElementById("map-canvas");
const ctx = canvas.getContext("2d");

let mapImage = null;

export function renderMap(mapFrame) {

    // Task 5: Safe initialization
    if (!mapFrame || !mapFrame.image) {
        return;
    }

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

        // Draw occupancy map
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        ctx.drawImage(mapImage, 0, 0);

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
    };

    mapImage.src =
        `data:image/png;base64,${mapFrame.image}`;
}