// Map Builder: hand the robot an unmapped area and let it map itself.
//
// The screen is deliberately two buttons and a readout. Everything that
// decides *where* to go lives in amr_navigation_explore; the operator's only
// real choices are whether to come home afterwards and what to call the
// finished map, so those are the only controls here.
//
// Progress is reported honestly: "frontiers left" is the number of unexplored
// openings the robot can still see, and it goes *up* when it discovers a new
// room. That is not a bug in the readout, so the bar is labelled coverage
// rather than dressed up as a countdown to completion.
import { sendMessage } from "./ws_client.js";
import { notifyError, notifySuccess, showToast } from "./notice.js";
import { setExploreTarget } from "./map_renderer.js";

let stateValue = null;
let detailValue = null;
let progressFill = null;
let progressLabel = null;
let areaValue = null;
let frontiersValue = null;
let elapsedValue = null;
let mapNameInput = null;
let returnCheckbox = null;
let startButton = null;
let stopButton = null;

// explore_status states the gateway sends. `stopped` is a run that ended
// without finishing the job -- cancelled, or out of time.
const STATE_LABELS = {
    idle: "Idle",
    sent: "Starting",
    accepted: "Starting",
    waiting_for_map: "Waiting for the map",
    exploring: "Exploring",
    driving: "Driving to a frontier",
    settling: "Looking around",
    returning: "Returning to start",
    canceling: "Stopping",
    canceled: "Stopped",
    stopped: "Stopped early",
    complete: "Map complete",
    aborted: "Failed",
    rejected: "Refused",
    unavailable: "Explorer unavailable",
    unknown: "Unknown",
};

// States where nothing is running any more, whatever the reason.
const FINISHED_STATES = [
    "idle",
    "canceled",
    "stopped",
    "complete",
    "aborted",
    "rejected",
    "unavailable",
];

const FAILED_STATES = [
    "aborted",
    "rejected",
    "unavailable",
];

export function initExplorePanel() {

    stateValue = document.getElementById("explore-state");
    detailValue = document.getElementById("explore-detail");
    progressFill = document.getElementById("explore-progress-fill");
    progressLabel = document.getElementById("explore-progress-label");
    areaValue = document.getElementById("explore-area");
    frontiersValue = document.getElementById("explore-frontiers");
    elapsedValue = document.getElementById("explore-elapsed");
    mapNameInput = document.getElementById("explore-map-name");
    returnCheckbox = document.getElementById("explore-return");
    startButton = document.getElementById("explore-start-btn");
    stopButton = document.getElementById("explore-stop-btn");

    if (startButton) {
        startButton.addEventListener("click", startExploring);
    }

    if (stopButton) {
        stopButton.addEventListener("click", stopExploring);
    }

    setRunning(false);
}

function startExploring() {

    const name = mapNameInput ? mapNameInput.value.trim() : "";

    // Checked here as well as in the gateway so a typo costs a toast rather
    // than a run that maps the whole building and then fails to save it.
    if (name && !/^[a-zA-Z0-9_-]+$/.test(name)) {

        showToast(
            "Map name must be letters, numbers, dashes or underscores",
            false,
        );

        return;
    }

    sendMessage({

        type: "explore_start",

        save_as: name || null,

        return_to_start: returnCheckbox ? returnCheckbox.checked : true,

        // 0 means "the gateway's own ceiling", which is what stops an
        // unattended run from going until the battery dies.
        max_duration_sec: 0,

    });

    // Optimistic, so the button stops inviting a second press during the
    // round trip. The first status frame corrects it either way.
    setRunning(true);

    if (stateValue) {
        stateValue.textContent = "Starting";
    }
}

function stopExploring() {

    sendMessage({ type: "explore_stop" });
}

/** Ask the gateway where a run that started without us has got to. */
export function refreshExploration() {

    sendMessage({ type: "explore_status_request" });
}

function setRunning(running) {

    if (startButton) {
        startButton.disabled = running;
    }

    if (stopButton) {
        stopButton.disabled = !running;
    }

    // The name and the return trip are read when the run starts, so changing
    // them mid-run would show settings that are not the ones in force.
    if (mapNameInput) {
        mapNameInput.disabled = running;
    }

    if (returnCheckbox) {
        returnCheckbox.disabled = running;
    }
}

function formatDuration(seconds) {

    if (typeof seconds !== "number" || !isFinite(seconds)) {
        return "--";
    }

    const total = Math.max(0, Math.round(seconds));

    const minutes = Math.floor(total / 60);

    return minutes
        ? `${minutes}m ${String(total % 60).padStart(2, "0")}s`
        : `${total}s`;
}

export function handleExploreFrame(frame) {

    if (frame.type !== "explore_status") {
        return;
    }

    const state = frame.state || "unknown";
    const label = STATE_LABELS[state] || state;

    const finished = FINISHED_STATES.includes(state);
    const failed = FAILED_STATES.includes(state);

    // `running` is the gateway's own view of whether a goal is live; trust it
    // over the state name, which can lag by a frame.
    setRunning(
        typeof frame.running === "boolean" ? frame.running : !finished
    );

    if (stateValue) {
        stateValue.textContent = label;
        stateValue.className = failed
            ? "status-value status-error"
            : "status-value";
    }

    if (detailValue) {

        const detail = [];

        if (typeof frame.distance_to_target === "number") {
            detail.push(`${frame.distance_to_target.toFixed(1)} m to target`);
        }

        if (frame.message) {
            detail.push(frame.message);
        }

        detailValue.textContent = detail.join(" — ");
    }

    if (areaValue && typeof frame.explored_area_m2 === "number") {
        areaValue.textContent = `${frame.explored_area_m2.toFixed(1)} m²`;
    }

    if (frontiersValue && typeof frame.frontiers_remaining === "number") {
        frontiersValue.textContent = String(frame.frontiers_remaining);
    }

    if (elapsedValue) {

        const seconds =
            typeof frame.elapsed_sec === "number"
                ? frame.elapsed_sec
                : frame.duration_sec;

        if (typeof seconds === "number") {
            elapsedValue.textContent = formatDuration(seconds);
        }
    }

    if (progressFill && typeof frame.percent_explored === "number") {

        const percent = Math.max(0, Math.min(100, frame.percent_explored));

        progressFill.style.width = `${percent}%`;

        if (progressLabel) {
            progressLabel.textContent = `${percent.toFixed(0)}% known`;
        }
    }

    // Draw where it is heading, so the map explains the robot's behaviour
    // rather than the robot appearing to wander.
    setExploreTarget(
        frame.running && Array.isArray(frame.target) ? frame.target : null
    );

    // A finish is an event the operator may not be watching the panel for.
    if (state === "complete") {
        notifySuccess(frame.message || "Map complete");
    } else if (failed) {
        notifyError(frame.message || `Map builder: ${label.toLowerCase()}`);
    }
}
