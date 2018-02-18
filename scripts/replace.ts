/// <reference path="../node_modules/@types/chrome/chrome-app.d.ts" />
/// <reference path="../node_modules/@types/jquery/index.d.ts" />

console.log("test");

$(document).ready(() => {
    // TODO Type this because fuck, there aren't even _basic_ examples in the internet today!
    $("a").click((e) => {
        console.log(JSON.stringify(e));
        console.log(JSON.stringify(e.target));
        window.open(chrome.runtime.getURL("pages/test.html"));
    });
});
