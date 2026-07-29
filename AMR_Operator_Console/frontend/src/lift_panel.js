let socket = null;

let liftState = {
    position: 0,
    target: 0,
    moving: false,
    current: [0, 0],
    limit_upper: false,
    limit_lower: false,
    overload: false,
    fault: false
};


function connect() {

    socket = new WebSocket(
        "ws://localhost:8765"
    );


    socket.onopen = () => {
        console.log(
            "Lift panel websocket connected"
        );
    };


    socket.onmessage = (event) => {

        try {

            const frame = JSON.parse(
                event.data
            );


            if (
                frame.type === "lift"
            ) {

                updateLift(frame);
            }


        } catch(err) {

            console.error(
                "Lift frame error:",
                err
            );
        }

    };


    socket.onclose = () => {

        console.log(
            "Lift websocket closed"
        );

        setTimeout(
            connect,
            2000
        );
    };

}



function sendCommand(action, target=null) {

    if (
        !socket ||
        socket.readyState !== WebSocket.OPEN
    ) {

        return;
    }


    const msg = {

        type: "lift_cmd",

        action: action

    };


    if(target !== null){

        msg.target = target;

    }


    socket.send(
        JSON.stringify(msg)
    );

}




function updateLift(frame){

    liftState = frame;


    const position =
        document.getElementById(
            "lift-position"
        );


    const bar =
        document.getElementById(
            "lift-position-bar"
        );


    const currentA =
        document.getElementById(
            "lift-current-a"
        );


    const currentB =
        document.getElementById(
            "lift-current-b"
        );


    const fault =
        document.getElementById(
            "lift-fault"
        );


    const slider =
        document.getElementById(
            "lift-target"
        );



    if(position){

        position.innerText =
            frame.position.toFixed(2);

    }


    if(bar){

        bar.style.width =
            `${frame.position * 100}%`;

    }



    if(currentA){

        currentA.innerText =
            frame.current[0].toFixed(2)
            + " A";

    }



    if(currentB){

        currentB.innerText =
            frame.current[1].toFixed(2)
            + " A";

    }



    if(slider){

        slider.value =
            frame.target;

    }



    const faultActive =
        frame.fault ||
        frame.overload;



    if(fault){

        if(faultActive){

            fault.innerText =
                "LIFT FAULT";

            fault.classList.add(
                "active"
            );

        }
        else{

            fault.innerText =
                "OK";

            fault.classList.remove(
                "active"
            );

        }

    }



    updateButtons(
        faultActive
    );

}




function updateButtons(disabled){

    [
        "lift-up",
        "lift-down",
        "lift-stop"
    ].forEach(id=>{

        const btn =
            document.getElementById(id);


        if(btn){

            btn.disabled =
                disabled;

        }

    });

}




function initLiftPanel(){

    const up =
        document.getElementById(
            "lift-up"
        );


    const down =
        document.getElementById(
            "lift-down"
        );


    const stop =
        document.getElementById(
            "lift-stop"
        );


    const slider =
        document.getElementById(
            "lift-target"
        );



    if(up){

        up.onclick = () =>
            sendCommand(
                "raise"
            );

    }



    if(down){

        down.onclick = () =>
            sendCommand(
                "lower"
            );

    }



    if(stop){

        stop.onclick = () =>
            sendCommand(
                "stop"
            );

    }



    if(slider){

        slider.onchange = () => {

            sendCommand(
                "target",
                Number(
                    slider.value
                )
            );

        };

    }



    connect();

}



document.addEventListener(
    "DOMContentLoaded",
    initLiftPanel
);