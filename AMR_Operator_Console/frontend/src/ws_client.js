// Connects to amr_command's websocket gateway on the RPi and dispatches
// incoming telemetry frames to whichever panel/renderer cares about them.
import { initTeleop, initTeleopButtons } from "./teleop_control.js";
import { renderMap } from "./map_renderer.js";

const WS_URL = 'ws://localhost:8765';

export function connect(onMessage) {
  const socket = new WebSocket(WS_URL);
  socket.onmessage = (event) => onMessage(JSON.parse(event.data));
  return socket;
}
function handleTelemetryFrame(data) {
  console.log("Telemetry frame received:", data);

  if (data.type === "map") {
    renderMap(data);
  }
}
const socket = connect(handleTelemetryFrame);

initTeleop(socket);
initTeleopButtons(document.getElementById("teleop-pad"));

socket.onopen = () => {
  console.log("Connected to AMR websocket");
};