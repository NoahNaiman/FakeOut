var s = document.createElement('script');
console.log("Heyo");
// TODO: add "script.js" to web_accessible_resources in manifest.json
s.src = chrome.extension.getURL('index.js');
s.onload = function() {
    this.remove();
};
(document.head || document.documentElement).appendChild(s);