// Transient messages, shown at the top of the page.
//
// Replaces the old bottom-right toast, and more importantly replaces failures
// being reported by turning a panel's own text red: "Path Status: Rejected"
// in red, three panels down, is not something an operator watching the map
// notices. A refusal is an event, so it is announced as one.
//
// Errors linger longer than confirmations, and stay dismissible, because a
// rejection usually needs the operator to do something about it.

const DEFAULT_MS = 3200;
const ERROR_MS = 6000;

// Cap the stack so a flapping backend cannot bury the page in notices.
const MAX_VISIBLE = 3;

function area() {

    let node = document.getElementById("notice-area");

    if (!node) {
        node = document.createElement("div");
        node.id = "notice-area";
        document.body.prepend(node);
    }

    return node;
}

function dismiss(notice) {

    if (notice.dataset.leaving) {
        return;
    }

    notice.dataset.leaving = "1";
    notice.classList.remove("notice-in");

    // Let the transition finish before removing, so it fades rather than
    // vanishing mid-animation.
    setTimeout(() => notice.remove(), 220);
}

function show(message, kind, durationMs) {

    if (!message) {
        return;
    }

    const container = area();

    while (container.children.length >= MAX_VISIBLE) {
        container.firstElementChild.remove();
    }

    const notice = document.createElement("div");

    notice.className = `notice notice-${kind}`;
    notice.setAttribute("role", kind === "error" ? "alert" : "status");

    const text = document.createElement("span");
    text.className = "notice-text";
    text.textContent = message;

    const close = document.createElement("button");
    close.className = "notice-close";
    close.type = "button";
    close.setAttribute("aria-label", "Dismiss");
    close.textContent = "×";
    close.addEventListener("click", () => dismiss(notice));

    notice.appendChild(text);
    notice.appendChild(close);

    container.appendChild(notice);

    // Next frame, so the entry transition actually runs.
    requestAnimationFrame(() => notice.classList.add("notice-in"));

    setTimeout(() => dismiss(notice), durationMs);
}

export function notifyError(message) {
    show(message, "error", ERROR_MS);
}

export function notifySuccess(message) {
    show(message, "success", DEFAULT_MS);
}

export function notifyInfo(message) {
    show(message, "info", DEFAULT_MS);
}

/** Back-compat with the old toast call sites. */
export function showToast(message, success = true) {

    if (success) {
        notifySuccess(message);
    } else {
        notifyError(message);
    }
}
