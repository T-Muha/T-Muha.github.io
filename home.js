var init = function () {
    GenerateDropDown();
    AddDropCloseListener();
    Resize();
    CreateShadowColors();
    window.onscroll = AdjustShadows;
    AdjustShadows();
}

ToggleDropDown = function () {
    dropBoxes = document.getElementsByClassName('drop-box');
    for (i = 0; i < dropBoxes.length; i++) {
        dropBoxes[i].classList.toggle('hidden');
    }
    AddDropCloseListener();
}

SelectFilter = function (filter) {
    if (filter == 'C#') {
        filter = 'cSharp';
    }
    else if (filter == '.NET Core') {
        filter = 'netCore';
    }
    projectCards = document.getElementsByClassName('card');
    console.log(filter);
    for (i = 0; i < projectCards.length; i++) {
        var card = projectCards[i];
        console.log(card.classList);
        if (card.classList.contains(filter.toLowerCase()) == 0) {
            card.classList.toggle('hidden');
        }
    }
    Resize();
}

var GenerateDropDown = function () {
    var dropDown = document.getElementById('drop-down');
    var languages = ['Python', 'C#', '.NET Core', 'Javascript', 'PHP', 'mySQL'];
    for (i = 0; i < languages.length; i++) {
        var filter = document.createElement('div');
        filter.classList.add('drop-box');
        filter.classList.add('hidden');
        filter.onclick = 'SelectFilter(this)'
        filter.textContent += languages[i];
        dropDown.appendChild(filter);
    }
}

var AddDropCloseListener = function () {
    document.onclick = function (e) {
        if (e.target.classList.contains('drop-box')) {
            SelectFilter(e.target.textContent);
        }
        else if (e.target.id != 'main-box' && document.getElementsByClassName('drop-box')[0].classList.contains('hidden') == 0) {
            ToggleDropDown();
        }
    };
}

window.addEventListener('load', function () {
    init();
});

var Resize = function () {
    container = document.getElementById('project-flex');
    numCards = container.children.length;
    size = [window.innerWidth, window.innerHeight];
    projectRowLen = Math.floor(size[0] / 346);
    cardsToAdd = projectRowLen - numCards % projectRowLen;
    for (i = 0; i < cardsToAdd; i++) {
        invisiDiv = document.createElement('div');
        invisiDiv.classList.add('card');
        invisiDiv.style.visibility = 'hidden';
        container.appendChild(invisiDiv);
    }
}

//Creates the darkened version of container background colors
//Better to compute it once now then on scroll
//Allows you to only have to update background colors, makes better shadows
//Pretty proud of this one ngl
CreateShadowColors = function() {
    factor = .6; //Darkening factor
    containers = document.getElementsByClassName('container');
    Array.from(containers).forEach(container => {
        shadowCol = getComputedStyle(container).backgroundColor;
        console.log(shadowCol);
        var retrieveRGB = /rgb\((\d{1,3}), (\d{1,3}), (\d{1,3})\)/;
        var RGB = retrieveRGB.exec(shadowCol);
        console.log(RGB);
        RGB.forEach(function(col, i) { RGB[i] = parseInt(col) * factor});
        console.log(RGB);
        shadowCol = "rgb(" + RGB[1] + ", " + RGB[2] + ", " + RGB[3] + ")";
        console.log(shadowCol);
        container.style.borderLeftColor = shadowCol;
    });

}

AdjustShadows = function () {
    var factor = 1.3 //adjust shadow weight increase with this
    var calc = factor * (5 + document.documentElement.scrollTop / 100);
    // rgb(47, 69, 91)
    var weight = 'inset 0 ' + calc + 'px ' + calc + 'px -1px '
    containers = document.getElementsByClassName('container');
    Array.from(containers).forEach(container => {
        // newShadow += document.getElementById(container.id).style.backgroundColor;
        shadow = weight + getComputedStyle(container).borderLeftColor;
        // console.log(shadow);
        container.style.boxShadow = shadow;
    });
}