var layout = {
    title: 'transactions v.s. date',
    uirevision: 'true',
    xaxis: { autorange: true },
    yaxis: { autorange: true }
};

function plot(data) {
    layout.xaxis.autorange = true;
    layout.yaxis.autorange = true;
    Plotly.react(graphDiv, data, layout);
}

const eth = JSON.parse(ethereum);
const btc = JSON.parse(bitcoin);
const pol = JSON.parse(polygon);
const tzs = JSON.parse(tezos);
var data = [{ mode: 'lines', line: { color: "#4285F4" }, x: eth['x'], y: eth['y'], name: 'eth' }];
const show = { 'eth': true, 'btc': false, 'pol': false, 'tzs': false }
plot(data);

function updateEth() {
    if (show['eth']) {
        data = data.filter(entry => entry.name !== 'eth')
        show['eth'] = false
    } else {
        data.push({ mode: 'lines', line: { color: "#4285F4" }, x: eth['x'], y: eth['y'], name: 'eth' });
        show['eth'] = true
    }
    plot(data);
}
function updateBtc() {
    if (show['btc']) {
        data = data.filter(entry => entry.name !== 'btc')
        show['btc'] = false
    } else {
        data.push({ mode: 'lines', line: { color: "#F4B400" }, x: btc['x'], y: btc['y'], name: 'btc' });
        show['btc'] = true
    }
    plot(data);

}
function updatePol() {
    if (show['pol']) {
        data = data.filter(entry => entry.name !== 'pol')
        show['pol'] = false
    } else {
        data.push({ mode: 'lines', line: { color: "#0F9D58" }, x: pol['x'], y: pol['y'], name: 'pol' });
        show['pol'] = true
    }
    plot(data);
}
function updateTzs() {
    if (show['tzs']) {
        data = data.filter(entry => entry.name !== 'tzs')
        show['tzs'] = false
    } else {
        data.push({ mode: 'lines', line: { color: "#DB4437" }, x: tzs['x'], y: tzs['y'], name: 'tzs' });
        show['tzs'] = true
    }
    plot(data);
}