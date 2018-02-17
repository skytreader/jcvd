/// <reference path="../node_modules/@types/chrome/chrome-app.d.ts" />
/// <reference path="../node_modules/@types/jquery/index.d.ts" />

console.log("test");

$(document).ready(() => {
    //console.log($(this).find($(".storylink")));
    //$(this).attr("href", "http://skytreader.net");
    //$("a").attr("href", "test.html");
    //console.log($(this));
    //console.log("href click jQuery storylink");
    //console.log($(this).attr("href"));
    $("a").click(() => {
        console.log("click detected");
        //chrome.tabs.create({"url": chrome.extension.getURL("test.html")},
        //    (tab) => {}
        //);
        window.open(chrome.runtime.getURL("test.html"));
    });
});
