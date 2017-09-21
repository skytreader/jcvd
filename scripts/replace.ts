/// <reference path="../node_modules/@types/chrome/chrome-app.d.ts" />
/// <reference path="../node_modules/@types/jquery/index.d.ts" />

console.log("test");

$(document).ready(() => {
    $(this).attr("href", "http://skytreader.net");
    //$("a").attr("href", "test.html");
    console.log($(this));
    //$("a").click(() => {
    //    console.log("click detected");
    //    chrome.tabs.create({"url": chrome.extension.getURL("test.html")},
    //        (tab) => {}
    //    );
    //});
});
