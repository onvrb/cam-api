var intervalId;

function showEditRefreshRate() {
    if (document.getElementById("editRefreshRateForm").style.visibility == "visible") {
        document.getElementById("editRefreshRateForm").style.visibility = "hidden";
    } else {
        document.getElementById("editRefreshRateForm").style.visibility = "visible";
    }
}

function submitRefreshRate() {
    let newRefreshRate = parseInt(document.getElementById("refreshRateInput").value);

    if (newRefreshRate == 0) {
        document.getElementById("refreshRate").innerText = "0";
        clearInterval(intervalId);
    } else {
        document.getElementById("refreshRate").innerText = newRefreshRate;
        if (intervalId) {
            clearInterval(intervalId);
        }
        intervalId = setInterval(getImages, newRefreshRate * 1000);
    }
}

function getImages() {
    const channels = document.getElementsByClassName("channel");
    for (let i = 0; i < channels.length; i++) {
        channels[i].src = channels[i].src.split("?")[0] + "?timestamp=" + new Date().getTime();
    }
}
