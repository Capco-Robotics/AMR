// Renders lift state and active fault/signal status pushed from
// amr_lift / amr_error via amr_command.

import { connect } from "./ws_client.js";
import { renderMap } from './map_renderer.js';
import { renderBattery } from './battery_panel.js';

const panel = document.getElementById('status-panel');

const robots = new Map();
let selectedRobot = null;


function updateRobotSelector() {

    let selector = document.getElementById("robot-selector");

    if (!selector) {
        selector = document.createElement("select");
        selector.id = "robot-selector";

        panel.prepend(selector);

        selector.onchange = () => {
            selectedRobot = selector.value;
            console.log("Selected robot:", selectedRobot);
        };
    }

    selector.innerHTML = "";

    robots.forEach((_, robotId) => {

        const option = document.createElement("option");
        option.value = robotId;
        option.textContent = robotId;

        selector.appendChild(option);

    });

    if (!selectedRobot && robots.size > 0) {
        selectedRobot = robots.keys().next().value;
        selector.value = selectedRobot;
    }
    if (selectedRobot) {
    selector.value = selectedRobot;
}

}


function renderStatus(statusFrame) {

    if (selectedRobot !== statusFrame.robot_id) {
        return;
    }

    console.log(
        "Status:",
        statusFrame
    );

}


connect((frame) => {

    if (!frame.robot_id || frame.v !== 1) {
        console.warn("Invalid frame:", frame);
        return;
    }


    robots.set(
        frame.robot_id,
        frame
    );


    updateRobotSelector();


    switch (frame.type) {

        case "map":
            if (selectedRobot === frame.robot_id) {
                renderMap(frame);
            }
            break;


        case "battery":
            if (selectedRobot === frame.robot_id) {
                renderBattery(frame);
            }
            break;


        case "status":
            renderStatus(frame);
            break;

    }

});