// Folds the sidebar panels away on a narrow screen.
//
// All five panels expanded put the drive pad about 2000 px down a phone, so
// reaching it meant scrolling past four managers the operator was not using.
// They stay open on a laptop, where there is a column to put them in.
//
// Only the *initial* state is set. Once the operator opens or closes a panel
// themselves, that is their choice and a later resize must not undo it.

const NARROW = "(max-width: 700px)";

export function initPanels() {

    const panels = document.querySelectorAll("details.card");

    if (!panels.length) {
        return;
    }

    if (!window.matchMedia(NARROW).matches) {
        return;
    }

    panels.forEach((panel) => {

        // Path Execution is what someone watching a run is looking at, so it
        // is the one panel worth the vertical space by default.
        if (panel.hasAttribute("data-keep-open")) {
            return;
        }

        panel.open = false;

    });

}
