/// <reference path="../node_modules/@types/chrome/chrome-app.d.ts" />

function checkHN(): boolean{
    var windowLocation: string;
    var semIsUrlQueried: boolean = false
    var spam = chrome.tabs.query({"active": true, "lastFocusedWindow": true}, function(tabs){
        windowLocation = tabs[0].url;
        console.log("inside", windowLocation);
        return true;
    });
    console.log("outside", windowLocation);
    console.log("spam", spam);
    return windowLocation == "news.ycombinator.com";
}

function main(){
    var det = document.getElementById("det");
    if(checkHN()){
        det.innerHTML = "At HN";
    } else{
        det.innerHTML = "Not at HN";
    }
}

window.onload = main;
