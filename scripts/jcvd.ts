function checkHN(){
    console.log(window.location.href);
    return window.location.href == "news.ycombinator.com";
}

function main(){
    console.log("main called");
    var det = document.getElementById("det");
    if(checkHN()){
        det.innerHTML = "At HN";
    } else{
        det.innerHTML = "Not at HN";
    }
}
