/// <reference path="../node_modules/@types/chrome/chrome-app.d.ts" />
/// <reference path="../node_modules/@types/jquery/index.d.ts" />

$(document).ready(() => {
    //$(this).attr("href", "http://skytreader.net");
    //$("a").attr("href", "test.html");
    $("a").click(() => {
        chrome.tabs.create({"url": chrome.extension.getURL("test.html")},
            (tab) => {}
        );
    });
});
