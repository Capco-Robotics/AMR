// Sends through ws_client rather than a captured socket, which would be the
// stale pre-drop one after a reconnect.
import { sendMessage } from "./ws_client.js";
import { showToast } from "./notice.js";

let mapListContainer = null;
let mapNameInput = null;
let modeIndicator = null;

// Binds the panel's DOM once. Deliberately does NOT pull the map list -- the
// socket is not necessarily open yet at bind time, and re-binding on every
// (re)connect would stack duplicate click listeners on Save/Refresh. ws_client
// calls refreshMaps() on open instead.
export function initMapPanel() {

    mapListContainer = document.getElementById("map-list");
    mapNameInput = document.getElementById("map-name");
    modeIndicator = document.getElementById("slam-mode");

    document
        .getElementById("save-map-btn")
        .addEventListener("click", saveMap);

    document
        .getElementById("refresh-map-btn")
        .addEventListener("click", refreshMaps);
}

function saveMap() {

    const name = mapNameInput.value.trim();

    if (!/^[a-zA-Z0-9_-]+$/.test(name)) {

        showToast(
            "Map name must be letters, numbers, dashes or underscores",
            false,
        );

        return;
    }

    sendMessage({

        type: "map_save",

        name: name,

    });
}

export function refreshMaps() {

    sendMessage({

        type: "map_list"

    });
}

export function handleMapFrame(frame) {

    switch(frame.type){

        case "map_list":

            drawMapList(frame.maps);

            break;

        case "map_op_result":

            if(frame.ok){

                showToast("Operation Successful", true);

                refreshMaps();

            }

            else{

                showToast(frame.error, false);

            }

            break;

        case "slam_mode":

            modeIndicator.textContent = frame.mode;

            modeIndicator.dataset.mode = frame.mode;

            break;

    }

}

function drawMapList(maps){

    mapListContainer.innerHTML = "";

    if (maps.length === 0) {

        const empty = document.createElement("p");

        empty.className = "empty-hint";
        empty.textContent = "No saved maps yet.";

        mapListContainer.appendChild(empty);

        return;

    }

    maps.forEach(name=>{

        const row = document.createElement("div");

        row.className = "list-row";

        const label = document.createElement("span");

        label.className = "list-label";
        label.textContent = name;

        const btn = document.createElement("button");

        btn.className = "btn btn-small";
        btn.textContent = "Load";

        btn.onclick = ()=>{

            sendMessage({

                type:"map_load",

                name:name

            });

        };

        row.appendChild(label);

        row.appendChild(btn);

        mapListContainer.appendChild(row);

    });

}