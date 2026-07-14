const canvas = document.getElementById("map-canvas");
const ctx = canvas.getContext("2d");


let mapImage = null;


export function renderMap(mapFrame) {

    console.log("renderMap called");


    // Task 5: Defensive initialization
    if (!mapFrame || !mapFrame.image) {

        console.log("Map data unavailable");

        return;
    }


    // Task 6: Dynamic canvas resize
    if (
    canvas.width !== mapFrame.width ||
    canvas.height !== mapFrame.height
) {

    canvas.width = mapFrame.width;
    canvas.height = mapFrame.height;

    // Display size (visual scaling)
    canvas.style.width = "500px";
    canvas.style.height = "500px";

    console.log(
        "Canvas resized:",
        mapFrame.width,
        mapFrame.height
    );
}


    mapImage = new Image();


    mapImage.onload = () => {

        console.log("IMAGE LOADED");


        // Draw occupancy map
        ctx.clearRect(
            0,
            0,
            canvas.width,
            canvas.height
        );


        ctx.drawImage(
            mapImage,
            0,
            0,
            canvas.width,
            canvas.height
        );


        console.log("IMAGE DRAWN");


        // Task 7: Robot position marker

        if (!mapFrame.pose) {

            console.log("No pose data");

            return;
        }


        const resolution = mapFrame.resolution;
        const origin = mapFrame.origin;


        const robotX =
            (mapFrame.pose.x - origin.x)
            / resolution;


        const robotY =
            (
                mapFrame.pose.y - origin.y
            ) / resolution;


        console.log(
            "Robot pixel:",
            robotX,
            robotY
        );


        // Robot dot

        ctx.beginPath();

        ctx.arc(
            robotX,
            robotY,
            5,
            0,
            2 * Math.PI
        );

        ctx.fillStyle = "red";

        ctx.fill();



        // Direction line

        const yaw =
            mapFrame.pose.yaw || 0;


        ctx.beginPath();

        ctx.moveTo(
            robotX,
            robotY
        );


        ctx.lineTo(
            robotX + Math.cos(yaw) * 20,
            robotY - Math.sin(yaw) * 20
        );


        ctx.strokeStyle = "red";

        ctx.lineWidth = 2;

        ctx.stroke();


    };


    console.log("SETTING IMAGE SRC");


    mapImage.src =
        `data:image/png;base64,${mapFrame.image}`;

}