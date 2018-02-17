/// <reference path="../node_modules/@types/chrome/chrome-app.d.ts" />
/// <reference path="../node_modules/@types/jquery/index.d.ts" />

console.log("test");

$(document).ready(() => {
    $("a").click(() => {
        console.log("click detected");
        window.open(chrome.runtime.getURL("pages/test.html"));
    });
});
