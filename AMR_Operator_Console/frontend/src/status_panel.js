// Renders lift state and active fault/signal status pushed from
// amr_lift / amr_error via amr_command.

import { connect } from "./ws_client.js";
import { renderMap } from './map_renderer.js';
import { renderBattery } from './battery_panel.js';

const panel = document.getElementById('status-panel');

function renderStatus(statusFrame) {
  // TODO: panel.textContent = JSON.stringify(statusFrame), etc.
}

connect((frame) => {

    switch (frame.type) {

        case "map":
            renderMap(frame);
            break;

        case "battery":
            renderBattery(frame);
            break;

        case "status":
            renderStatus(frame);
            break;

    }

});