function showImg(){
    // PARA GALERIA
    // (A) GET LIGHTBOX & ALL .ZOOMD IMAGES
    let all = document.getElementsByClassName("galeriaTrueImg"),
        lightbox = document.getElementById("lightbox");

    // (B) CLICK TO SHOW IMAGE IN LIGHTBOX
    // * SIMPLY CLONE INTO LIGHTBOX & SHOW
    if (all.length>0) {
        for (let i of all) {
            i.onclick = () => {
                let clone = i.cloneNode();
                clone.className = "";
                lightbox.innerHTML = "";
                lightbox.appendChild(clone);
                lightbox.className = "show";
            };
        }}

    // (C) CLICK TO CLOSE LIGHTBOX
    lightbox.onclick = () => {
        lightbox.className = "";
    };

    //PARA QHE HACEMOS
    // (A) GET LIGHTBOX & ALL .ZOOMD IMAGES
    let all2 = document.getElementsByClassName("circleTrueImg"),
        lightbox2 = document.getElementById("lightbox2");

    // (B) CLICK TO SHOW IMAGE IN LIGHTBOX
    // * SIMPLY CLONE INTO LIGHTBOX & SHOW
    if (all2.length>0) {
        for (let i of all2) {
            i.onclick = () => {
                let clone = i.cloneNode();
                clone.className = "";
                lightbox2.innerHTML = "";
                lightbox2.appendChild(clone);
                lightbox2.className = "show";
            };
        }}

    // (C) CLICK TO CLOSE LIGHTBOX
    lightbox2.onclick = () => {
        lightbox2.className = "";
    };
}

function ul(index) {
    var underlines = document.querySelectorAll(".underline");

    for (var i = 0; i < underlines.length; i++) {
        underlines[i].style.transform = 'translate3d(' + index * 100 + '%,0,0)';
    }
}