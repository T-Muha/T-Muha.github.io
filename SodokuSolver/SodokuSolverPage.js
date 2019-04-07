for (i = 0; i < 9; i++) {
    var div = document.createElement("div");
    div.id = "innerBox" + i;
    div.className = "innerBox";
    document.getElementById("sodokuGrid").appendChild(div);
    for (j = 1; j < 10; j++) {
        var innerDiv = document.createElement("div");
        innerDiv.className = "gridBox";
        innerDiv.innerHTML = j;
        document.getElementById("innerBox" + i).appendChild(innerDiv);
    }
}