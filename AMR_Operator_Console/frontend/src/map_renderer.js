// Renders the SLAM occupancy grid (sent by amr_command's map_encoder as a
// PNG/compact image) plus a robot-pose marker, onto the <canvas> 2D context.

const canvas = document.getElementById('map-canvas');
const ctx = canvas.getContext('2d');

export function renderMap(mapFrame) {
  // TODO: draw mapFrame.image onto ctx, overlay mapFrame.pose marker.
}
