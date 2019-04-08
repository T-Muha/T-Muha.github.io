function loadInitialAnimations() {
    document.getElementById('titleBlocker').style.height = '0';
    document.getElementById('titleBlocker').style.top = '23.5%';
}

function loadSecondaryAnimations() {
    document.getElementById('linkBox').style.width = '100%';
    document.getElementsByClassName('link')[0].style.opacity = '1';
    document.getElementsByClassName('link')[1].style.opacity = '1';
    document.getElementsByClassName('link')[2].style.opacity = '1';

}

linkHover = function (lineNumber, mouseIn) {
    if (mouseIn) {
        switch (lineNumber) {
            case 'one':
                element = document.getElementById('hoverLineOne');
                element.style.width = '33.3%';
                element.style.left = '0';
                break;
            case 'two':
                element = document.getElementById('hoverLineTwo');
                element.style.width = '33.25%';
                element.style.left = '33.3%';
                break;
            case 'three':
                element = document.getElementById('hoverLineThree');
                element.style.width = '33.45%';
                element.style.left = '66.55%';
                break;
        }
    }
    else {
        switch (lineNumber) {
            case 'one':
                element = document.getElementById('hoverLineOne');
                element.style.width = '0';
                element.style.left = '16.6%';
                break;
            case 'two':
                element = document.getElementById('hoverLineTwo');
                element.style.width = '0';
                element.style.left = '49.85%';
                break;
            case 'three':
                element = document.getElementById('hoverLineThree');
                element.style.width = '0';
                element.style.left = '83.25%';
                break;
        }
    }
    
    
}


setTimeout(loadInitialAnimations, 50);
setTimeout(loadSecondaryAnimations, 550);