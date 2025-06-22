function showImg(){
    // PARA GALERIA
    // (A) GET LIGHTBOX & ALL .ZOOMD IMAGES
    let all = document.querySelectorAll(".galeriaTrueImg, .galeriaTrueVideo"),
        lightbox = document.getElementById("lightbox");

    // (B) CLICK TO SHOW IMAGE IN LIGHTBOX
    // * SIMPLY CLONE INTO LIGHTBOX & SHOW
    if (all.length>0) {
        for (let i of all) {
            i.onclick = () => {
                let clone;
                if (i.tagName.toLowerCase() === 'video') {
                    clone = i.cloneNode(true);
                    clone.className = "";
                    clone.setAttribute("controls", "controls");
                    clone.setAttribute("autoplay", "autoplay");
                } else {
                    clone = i.cloneNode();
                    clone.className = "";
                    if (i.classList.contains("pixelArt")) {
                        clone.classList.add("pixelated");
                    }
                }

                lightbox.innerHTML = "";
                lightbox.appendChild(clone);
                lightbox.className = "show";
            };
        }}

    // (C) CLICK TO CLOSE LIGHTBOX
    lightbox.onclick = () => {
        lightbox.className = "";
        lightbox.innerHTML = "";
    };
}

function ul(index) {
    var underlines = document.querySelectorAll(".underline");

    for (var i = 0; i < underlines.length; i++) {
        underlines[i].style.transform = 'translate3d(' + index * 100 + '%,0,0)';
    }
}