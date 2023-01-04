const { ipcRenderer, contextBridge, remote } = require('electron');

contextBridge.exposeInMainWorld(
    "api", {
    send: (channel, ...args) => {
        ipcRenderer.send(channel, ...args);
    },
    receive: (channel, func) => {
        ipcRenderer.on(channel, (event, ...args) => func(...args));
    }
}
);