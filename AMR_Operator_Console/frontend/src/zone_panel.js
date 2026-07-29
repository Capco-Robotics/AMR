// Keep-out zone manager: names the traced polygon, stores it on the robot,
// and lists what is currently being enforced.
//
// The list is authoritative from the gateway (zone_list), never from local
// state: a zone that only exists in the browser is a zone Nav2 is not
// enforcing, and showing it would be worse than showing nothing.
import { sendMessage } from "./ws_client.js";
import { showToast } from "./toast.js";
import { clearDraft, getDraft } from "./zone_draw.js";
import { setZones } from "./map_renderer.js";

let zoneList = null;
let zoneName = null;
let zoneCount = null;

export function initZonePanel() {

    zoneList = document.getElementById("zone-list");
    zoneName = document.getElementById("zone-name");
    zoneCount = document.getElementById("zone-count");

    const saveButton = document.getElementById("save-zone-btn");

    if (saveButton) {
        saveButton.addEventListener("click", saveZone);
    }

    const discardButton = document.getElementById("discard-zone-btn");

    if (discardButton) {

        discardButton.addEventListener("click", () => {

            clearDraft();

            showToast("Discarded the traced zone", true);

        });

    }

    const clearButton = document.getElementById("clear-zones-btn");

    if (clearButton) {

        clearButton.addEventListener("click", () => {

            // Deleting every no-go area at once is the one destructive action
            // on this panel, and an accidental tap on a touchscreen is cheap.
            const ok = window.confirm(
                "Delete every keep-out zone? The AMR will be free to drive " +
                "through all of them."
            );

            if (ok) {
                sendMessage({ type: "zone_clear" });
            }

        });

    }

    const refreshButton = document.getElementById("refresh-zones-btn");

    if (refreshButton) {
        refreshButton.addEventListener("click", refreshZones);
    }

}

export function refreshZones() {

    sendMessage({ type: "zone_list" });

}

function saveZone() {

    const polygon = getDraft();

    if (!polygon || polygon.length < 3) {

        showToast(
            "Trace a zone on the map first (hold and drag)",
            false,
        );

        return;

    }

    const name = zoneName ? zoneName.value.trim() : "";

    // Matches the gateway's _sanitize_map_name, so an invalid name is caught
    // here with a useful message rather than bouncing off the robot.
    if (!/^[a-zA-Z0-9_-]+$/.test(name)) {

        showToast(
            "Zone name must be letters, numbers, dashes or underscores",
            false,
        );

        return;

    }

    sendMessage({
        type: "zone_save",
        name: name,
        polygon: polygon,
    });

}

function drawZoneList(zones) {

    if (!zoneList) {
        return;
    }

    zoneList.innerHTML = "";

    if (zoneCount) {

        zoneCount.textContent =
            zones.length === 1 ? "1 zone" : `${zones.length} zones`;

    }

    if (zones.length === 0) {

        const empty = document.createElement("p");

        empty.className = "empty-hint";
        empty.textContent = "No keep-out zones. Trace one on the map.";

        zoneList.appendChild(empty);

        return;

    }

    zones.forEach((zone) => {

        const row = document.createElement("div");

        row.className = "list-row";

        const label = document.createElement("span");

        label.className = "list-label";
        label.textContent = zone.name;

        const meta = document.createElement("span");

        meta.className = "list-meta";
        meta.textContent = `${zone.polygon.length} pts`;

        const deleteButton = document.createElement("button");

        deleteButton.className = "btn btn-danger btn-small";
        deleteButton.textContent = "Delete";

        deleteButton.onclick = () => {

            sendMessage({
                type: "zone_delete",
                name: zone.name,
            });

        };

        row.appendChild(label);
        row.appendChild(meta);
        row.appendChild(deleteButton);

        zoneList.appendChild(row);

    });

}

export function handleZoneFrame(frame) {

    switch (frame.type) {

        case "zone_list":

            drawZoneList(frame.zones || []);

            // The map overlay and the list are the same data; painting from
            // the same frame keeps them from drifting apart.
            setZones(frame.zones || []);

            break;

        case "zone_op_result":

            if (frame.ok) {

                showToast("Keep-out zones updated", true);

                // The draft has been accepted and now belongs to the stored
                // set, so stop drawing it as a pending outline.
                clearDraft();

                if (zoneName) {
                    zoneName.value = "";
                }

            } else {

                showToast(frame.error || "Zone operation failed", false);

            }

            break;

    }

}
