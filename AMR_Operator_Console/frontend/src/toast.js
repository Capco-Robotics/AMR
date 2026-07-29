// One transient notification strip, shared by every panel.
//
// Each panel used to own a private showToast() plus its own lazily-created
// #toast div, so two panels reporting at once fought over the same element id
// and the stylesheet carried two conflicting #toast rules.

let element = null;

let hideTimer = null;

function ensureElement() {

    if (element) {
        return element;
    }

    element = document.getElementById("toast");

    if (!element) {

        element = document.createElement("div");
        element.id = "toast";

        document.body.appendChild(element);

    }

    return element;
}

export function showToast(message, success = true, durationMs = 3000) {

    const node = ensureElement();

    node.textContent = message;

    node.className = success ? "toast-success" : "toast-error";

    // Force the visible state before starting a fresh timer, so a second
    // toast arriving mid-fade does not inherit the first one's countdown.
    node.classList.add("toast-visible");

    if (hideTimer) {
        clearTimeout(hideTimer);
    }

    hideTimer = setTimeout(() => {

        node.classList.remove("toast-visible");

        hideTimer = null;

    }, durationMs);

}
