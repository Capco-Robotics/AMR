let ws = null;

let mapListContainer = null;
let mapNameInput = null;
let modeIndicator = null;
let toast = null;

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

    toast = document.getElementById("toast");

    if (!toast) {

        toast = document.createElement("div");

        toast.id = "toast";

        document.body.appendChild(toast);

    }
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

                showToast("Operation Successful", true);

                refreshMaps();

            }

            else{

                showToast(frame.error, false);

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

function showToast(message, success) {

    toast.innerText = message;

    toast.className = success
        ? "toast-success"
        : "toast-error";

    toast.style.display = "block";

    setTimeout(() => {

        toast.style.display = "none";

    }, 2500);

}