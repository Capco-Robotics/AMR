import { sendMessage } from "./ws_client.js";
import { notifyError, showToast } from "./notice.js";
import { setPreviewPath } from "./map_renderer.js";
import {
    loadPath,
    getCleanPath
} from "./path_draw.js";
let pathList = null;
let pathName = null;
let pathStatus = null;

let loadedPaths = {};

// Set when Run was pressed on a path whose points we do not have yet, so the
// path_data reply knows to drive it rather than just preview it. Previously
// Run on a fresh page just said "Load path first", which made the button look
// broken -- the operator had no reason to know Load was a prerequisite.
let pendingRun = null;

export function initPathPanel() {

    pathList = document.getElementById("path-list");
    pathName = document.getElementById("path-name");
    pathStatus = document.getElementById("path-status");

    document
        .getElementById("save-path-btn")
        .addEventListener("click", savePath);

    document
        .getElementById("refresh-path-btn")
        .addEventListener("click", refreshPaths);

    const stopButton = document.getElementById("stop-path-btn");

    if (stopButton) {
        stopButton.addEventListener("click", cancelPath);
    }

}


function savePath() {

    const name = pathName.value.trim();


    if (!/^[a-zA-Z0-9_-]+$/.test(name)) {

        showToast("Invalid path name", false);
        return;

    }


    sendMessage({

        type:"path_save",

        name:name,

        points:getCurrentPath()

    });

}



export function refreshPaths(){

    sendMessage({

        type:"path_list"

    });

}


// The gateway's only way of being told to abandon a running path.
export function cancelPath(){

    sendMessage({

        type:"nav_path_cancel"

    });

}


// path_status frames arrive from the gateway for every stage of a Nav2 run:
// sent -> accepted -> executing (repeating) -> succeeded/aborted/canceled,
// plus rejected/unavailable when the path never starts.
const PATH_STATE_LABELS = {
    sent: "Sent",
    accepted: "Accepted",
    executing: "Running",
    canceling: "Cancelling",
    canceled: "Cancelled",
    succeeded: "Complete",
    aborted: "Aborted",
    rejected: "Rejected",
    unavailable: "Nav2 unavailable",
    idle: "Idle",
};

const PATH_STATE_FAILED = [
    "aborted",
    "rejected",
    "unavailable",
];

export function renderPathStatus(frame){

    if(!pathStatus){
        return;
    }


    const label =
        PATH_STATE_LABELS[frame.state] || frame.state || "Unknown";


    const detail = [];

    if(typeof frame.poses_remaining === "number"){
        detail.push(`${frame.poses_remaining} poses left`);
    }

    if(typeof frame.distance_remaining === "number"){
        detail.push(`${frame.distance_remaining.toFixed(2)} m left`);
    }

    if(detail.length === 0 && frame.message){
        detail.push(frame.message);
    }


    pathStatus.textContent =
        detail.length
            ? `${label} — ${detail.join(", ")}`
            : label;


    const failed = PATH_STATE_FAILED.includes(frame.state);


    pathStatus.className =
        failed ? "status-value status-error" : "status-value";


    // A refusal is an event, not a state. Turning this line red said nothing
    // to an operator looking at the map -- and on the Run Path screen the
    // line is not even visible from the other screens. Announce it instead.
    if(failed){

        notifyError(
            frame.message || `Path ${label.toLowerCase()}`
        );

    }

}



function drawPathList(paths){

    pathList.innerHTML="";


    if(paths.length === 0){

        const empty = document.createElement("p");

        empty.className = "empty-hint";
        empty.textContent = "No saved paths yet.";

        pathList.appendChild(empty);

        return;

    }


    paths.forEach(name=>{


        const row=document.createElement("div");

        row.className="list-row";


        const label=document.createElement("span");

        label.className="list-label";
        label.textContent=name;



        const previewBtn=document.createElement("button");

        previewBtn.className="btn btn-small";
        previewBtn.textContent="Preview";

        previewBtn.onclick=()=>{

            const points = loadedPaths[name];

            if (points) {
                setPreviewPath(points);
                return;
            }

            sendMessage({

                type:"path_load",

                name:name

            });

        };



        const runBtn=document.createElement("button");

        runBtn.className="btn btn-primary btn-small";
        runBtn.textContent="Run";

        runBtn.onclick=()=>{

            runPath(name);

        };



        const deleteBtn=document.createElement("button");

        deleteBtn.className="btn btn-danger btn-small";
        deleteBtn.textContent="Delete";

        deleteBtn.onclick=()=>{

            sendMessage({

                type:"path_delete",

                name:name

            });

        };



        row.appendChild(label);
        row.appendChild(previewBtn);
        row.appendChild(runBtn);
        row.appendChild(deleteBtn);


        pathList.appendChild(row);


    });


}



function runPath(name){

    const points = loadedPaths[name];


    if(!points){

        // Fetch it, then drive it, instead of making the operator press
        // Preview first and guess that that was the missing step.
        pendingRun = name;

        sendMessage({

            type:"path_load",

            name:name

        });

        return;

    }


    setPreviewPath(points);


    sendMessage({

        type:"nav_path",

        points:points

    });


}



function getCurrentPath(){

    return getCleanPath();

}


export function handlePathFrame(frame){


    switch(frame.type){


        case "path_list":

            drawPathList(frame.paths);

            break;



        case "path_data":

            loadedPaths[frame.name]=frame.points;

            loadPath(frame.points);

            setPreviewPath(frame.points);

            if(pendingRun === frame.name){

                pendingRun = null;

                sendMessage({
                    type:"nav_path",
                    points:frame.points,
                });

            } else {

                showToast(`Previewing "${frame.name}"`, true);

            }

            break;



        case "path_op_result":


            if(frame.ok){

                showToast(
                    "Operation Successful",
                    true
                );

                refreshPaths();

            }

            else{

                showToast(
                    frame.error,
                    false
                );

            }


            break;

    }

}
