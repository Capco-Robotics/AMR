let rawStroke = [];
let cleanStroke = [];

export function beginStroke(point) {
    rawStroke = [point];
}

export function appendPoint(point) {
    rawStroke.push(point);
}

export function endStroke() {

}

export function clear() {
    rawStroke = [];
    cleanStroke = [];
}

export function loadPath(points) {
    cleanStroke = points;
}

export function getCleanPath() {
    return cleanStroke;
}
