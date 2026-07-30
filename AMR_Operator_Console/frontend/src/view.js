// Screen router.
//
// The console used to show every control at once, which meant an operator
// wanting to drive scrolled past two managers to reach the pad. Now one job
// is on screen at a time, with the map always visible above it, and the home
// screen is a menu of those jobs.
//
// Entering a screen arms the tool that screen is for -- opening "Keep-out
// Zones" and then having to press a second "draw" button is a tap that
// carries no information.
import {
    MODE_NONE,
    MODE_PATH,
    MODE_ZONE,
    setInteractionMode,
    setPreviewPath,
} from "./map_renderer.js";

export const HOME = "home";

const TITLES = {
    home: "AMR Console",
    explore: "Map Builder",
    zones: "Keep-out Zones",
    "path-new": "New Path",
    "path-run": "Run Path",
    rc: "Remote Control",
    maps: "Maps",
};

const HINTS = {
    home: "",
    explore: "The AMR maps the area by itself. Watch it on the map above.",
    zones: "Hold and drag on the map to trace a keep-out area.",
    "path-new": "Hold and drag on the map to draw a route.",
    "path-run": "Preview a saved path, then run it.",
    rc: "Driving stops automatically if something is too close.",
    maps: "",
};

// Which map tool each screen owns.
const MODES = {
    home: MODE_NONE,
    // Nothing to draw here -- the map is a view of what the robot is doing,
    // and an armed tool would turn a stray tap into a command mid-run.
    explore: MODE_NONE,
    zones: MODE_ZONE,
    "path-new": MODE_PATH,
    "path-run": MODE_NONE,
    rc: MODE_NONE,
    maps: MODE_NONE,
};

let current = HOME;

const listeners = [];

export function onScreenChange(listener) {
    listeners.push(listener);
}

export function currentScreen() {
    return current;
}

export function showScreen(name) {

    if (!TITLES[name]) {
        name = HOME;
    }

    current = name;

    document.querySelectorAll("[data-screen]").forEach((section) => {
        section.hidden = section.dataset.screen !== name;
    });

    const title = document.getElementById("screen-title");

    if (title) {
        title.textContent = TITLES[name];
    }

    const hint = document.getElementById("mode-hint");

    if (hint) {
        hint.textContent = HINTS[name] || "";
    }

    const back = document.getElementById("back-btn");

    if (back) {
        back.hidden = name === HOME;
    }

    setInteractionMode(MODES[name] ?? MODE_NONE);

    // A preview belongs to the Run Path screen; leaving it should not leave a
    // dangling purple line on the map.
    if (name !== "path-run") {
        setPreviewPath([]);
    }

    listeners.forEach((listener) => listener(name));

    // Coming back from a long list, the map is what the operator wants to see.
    window.scrollTo({ top: 0, behavior: "smooth" });
}

export function initViews() {

    document.querySelectorAll("[data-goto]").forEach((button) => {

        button.addEventListener("click", () => {
            showScreen(button.dataset.goto);
        });
    });

    const back = document.getElementById("back-btn");

    if (back) {
        back.addEventListener("click", () => showScreen(HOME));
    }

    showScreen(HOME);
}
