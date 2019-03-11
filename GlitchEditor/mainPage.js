function imageHandler(e2) {
    document.getElementById("mainBody").style.visibility = "hidden";
    document.getElementById("textEditor").style.visibility = "visible";
    document.getElementById("imgStore").style.visibility = "visible";
    document.getElementById("showImg").style.visibility = "visible";
    document.getElementById("textEditor").style.zIndex = "999";
    document.getElementById("mainBody").style.zIndex = "-1";

    var store = document.getElementById('imgStore');
    store.innerHTML = '<img id="tempId" src = "' + e2.target.result + '">';
    getDataUri(e2.target.result, function (dataUri) {
        document.getElementById("displayTxt").innerHTML = dataUri;
    });
}

function loadImage(e1) {
    var fileName = e1.target.files[0];
    var fr = new FileReader();
    fr.onload = imageHandler;
    fr.readAsDataURL(fileName);
}

window.onload = function () {
    var y = document.getElementById("getImage");
    y.addEventListener('change', loadImage, false);
}

function getDataUri(url, callback) {
    var image = new Image();

    image.onload = function () {
        var canvas = document.createElement('canvas');
        canvas.width = this.naturalWidth;
        canvas.height = this.naturalHeight;

        canvas.getContext('2d').drawImage(this, 0, 0);
        callback(canvas.toDataURL('image/png').replace(/^data:image\/(png|jpg);base64,/, ''));
        callback(canvas.toDataURL('image/png'));
    };
    image.src = url;
}

var tCtx = document.getElementById('hiddenCanvas').getContext('2d'), //Hidden canvas

displayImage = function () {
    imageElem = document.getElementById('tempId'); //Image element
    tCtx.canvas.width = tCtx.measureText(this.value).width;
    tCtx.fillText(this.value, 0, 10);
    imageElem.src = tCtx.canvas.toDataURL();
    console.log(imageElem.src);
}