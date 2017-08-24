/// <reference path="../node_modules/@types/chrome/chrome-app.d.ts" />
/// <reference path="../node_modules/@types/chrome/index.d.ts" />

/**
Expects fullUrl to look like "https://domain.com/possibleArgs".
*/
function getDomain(fullUrl: string): string{
    var urlParse: string[] = fullUrl.split("/");
    return urlParse[2];
}

function _getUrl(callback){
    chrome.tabs.query({"active": true, "lastFocusedWindow": true}, (tabs: chrome.tabs.Tab[]) => {
        var windowLocation: string = getDomain(tabs[0].url);
        console.log("_getUrl url is", windowLocation);
        callback(windowLocation == "news.ycombinator.com");
    });
}

function pseudoMain(isHN: boolean){
    var det = document.getElementById("det");
    if(isHN){
        det.innerHTML = "At HN";
    } else{
        det.innerHTML = "Not at HN";
    }
}

function main(){
    _getUrl(pseudoMain);
}

window.onload = main;
