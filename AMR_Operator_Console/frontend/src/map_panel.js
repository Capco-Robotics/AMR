let ws = null;

let mapListContainer = null;
let mapNameInput = null;
let modeIndicator = null;

export function initMapPanel() {
    
    ws = window.wsClient;

    mapListContainer = document.getElementById("map-list");
    mapNameInput = document.getElementById("map-name");
    modeIndicator = document.getElementById("slam-mode");

    document
        .getElementById("save-map-btn")
        .addEventListener("click", saveMap);

    document
        .getElementById("refresh-map-btn")
        .addEventListener("click", refreshMaps);

    refreshMaps();
}

function saveMap() {

    const name = mapNameInput.value.trim();

    if (!/^[a-zA-Z0-9_-]+$/.test(name)) {

        alert("Invalid map name");

        return;
    }

    ws.send(JSON.stringify({

        type: "map_save",

        name: name,

    }));
}

function refreshMaps() {

    ws.send(JSON.stringify({

        type: "map_list"

    }));
}

export function handleMapFrame(frame) {

    switch(frame.type){

        case "map_list":

            drawMapList(frame.maps);

            break;

        case "map_op_result":

            if(frame.ok){

                alert("Operation Successful");

                refreshMaps();

            }

            else{

                alert(frame.error);

            }

            break;

        case "slam_mode":

            modeIndicator.innerText =
                "Mode : " + frame.mode;

            break;

    }

}

function drawMapList(maps){

    mapListContainer.innerHTML = "";

    maps.forEach(name=>{

        const row = document.createElement("div");

        row.className = "map-item";

        const label = document.createElement("span");

        label.innerText = name;

        const btn = document.createElement("button");

        btn.innerText = "Load";

        btn.onclick = ()=>{

            ws.send(JSON.stringify({

                type:"map_load",

                name:name

            }));

        };

        row.appendChild(label);

        row.appendChild(btn);

        mapListContainer.appendChild(row);

    });

}