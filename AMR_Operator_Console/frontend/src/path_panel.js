import { sendMessage } from "./ws_client.js";
import {
    loadPath,
    getCleanPath
} from "./path_draw.js";
let pathList = null;
let pathName = null;
let toast = null;

let loadedPaths = {};

export function initPathPanel() {

    pathList = document.getElementById("path-list");
    pathName = document.getElementById("path-name");

    document
        .getElementById("save-path-btn")
        .addEventListener("click", savePath);

    document
        .getElementById("refresh-path-btn")
        .addEventListener("click", refreshPaths);


    toast = document.getElementById("toast");

    if (!toast) {

        toast = document.createElement("div");
        toast.id = "toast";

        document.body.appendChild(toast);

    }


    refreshPaths();

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



function refreshPaths(){

    sendMessage({

        type:"path_list"

    });

}



function drawPathList(paths){

    pathList.innerHTML="";


    paths.forEach(name=>{


        const row=document.createElement("div");

        row.className="path-item";


        const label=document.createElement("span");

        label.innerText=name;



        const loadBtn=document.createElement("button");

        loadBtn.innerText="Load";

        loadBtn.onclick=()=>{

            sendMessage({

                type:"path_load",

                name:name

            });

        };



        const runBtn=document.createElement("button");

        runBtn.innerText="Run";

        runBtn.onclick=()=>{

            runPath(name);

        };



        const deleteBtn=document.createElement("button");

        deleteBtn.innerText="Delete";

        deleteBtn.onclick=()=>{

            sendMessage({

                type:"path_delete",

                name:name

            });

        };



        row.appendChild(label);
        row.appendChild(loadBtn);
        row.appendChild(runBtn);
        row.appendChild(deleteBtn);


        pathList.appendChild(row);


    });


}



function runPath(name){

    const points = loadedPaths[name];


    if(!points){

        showToast(
            "Load path first",
            false
        );

        return;

    }


    sendMessage({

        type:"nav_path",

        points:points

    });


}



function getCurrentPath(){

    return getCleanPath();

}


function handleFrame(frame){


    switch(frame.type){


        case "path_list":

            drawPathList(frame.paths);

            break;



        case "path_data":

            loadedPaths[frame.name]=frame.points;

            loadPath(frame.points);

            showToast(
                "Path Loaded",
                true
            );

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



function showToast(message,success){

    toast.innerText=message;


    toast.className =
        success ?
        "toast-success":
        "toast-error";


    toast.style.display="block";


    setTimeout(()=>{

        toast.style.display="none";

    },2500);

}



window.pathPanelHandler = handleFrame;
