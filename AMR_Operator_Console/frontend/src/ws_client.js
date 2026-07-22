// Connects to amr_command's websocket gateway on the RPi and dispatches
// incoming telemetry frames to whichever panel/renderer cares about them.
import { initTeleop } from "./teleop_control.js";
import { initTeleopButtons } from "./teleop_control.js";
import { setGoalMode } from "./map_renderer.js";

const WS_URL = 'ws://localhost:8765';

export function connect(onMessage) {
  const socket = new WebSocket(WS_URL);
  socket.onmessage = (event) => onMessage(JSON.parse(event.data));
  return socket;
}

export let websocket = null;


function handleTelemetryFrame(data) {

    console.log("Telemetry frame received:", data);

}

websocket = connect(handleTelemetryFrame);

initTeleop(websocket);
initTeleopButtons(document.getElementById("teleop-pad"));

websocket.onopen = () => {
  console.log("Connected to AMR websocket");
};
const goalButton =
    document.getElementById("goal-toggle");

goalButton.addEventListener("click", () => {

    goalButton.classList.toggle("active");

    setGoalMode(
        goalButton.classList.contains("active")
    );

});