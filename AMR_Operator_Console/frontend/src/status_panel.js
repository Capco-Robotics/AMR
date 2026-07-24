// Renders lift state and active fault/signal status pushed from
// amr_lift / amr_error via amr_command.

import {
    renderMap,
    updatePlan,
} from "./map_renderer.js";
import { renderBattery } from './battery_panel.js';

const panel = document.getElementById('status-panel');

export function renderStatus(statusFrame) {
  // TODO: panel.textContent = JSON.stringify(statusFrame), etc.
}

