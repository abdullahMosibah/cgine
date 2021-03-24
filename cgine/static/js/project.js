let text_in_knowledge_blocks = document.querySelectorAll("#text-block");

//--------------------- info box pop-up-------------------------------
// info keyword that is located inside the info box
let infoKeyword = document.getElementById("info_keyword");
// the actual info box
let infoBox = document.getElementById("info_box");
// progress bar effect reference
let progressBar = document.getElementById('progress-bar');
// the buttons in the info box.
let googleBtn = document.getElementById("google_btn");
let googleScholarBtn = document.getElementById("google_scholar_btn");

//----------------------------------------------------------------------
function google_search(evt) {
    window.open(`https://www.google.com/search?q=${evt.target.myParam}`, '_blank');
}
function  google_scholar_search(evt){
    window.open(`https://scholar.google.com/scholar?hl=en&as_sdt=0,5&q=${evt.target.myParam}`, "_blank");

}

function populate_info_box(keyword) {
    infoKeyword.textContent = keyword;
    //listener for the google normal search
    googleBtn.addEventListener("click", google_search);
    googleBtn.myParam = keyword;
    //listener for the google scholar search.
    googleScholarBtn.addEventListener('click',google_scholar_search);
    googleScholarBtn.myParam = keyword;
    // to make the info box disappear when clicked at any location at the document.
    window.addEventListener('click', function () {
        infoBox.classList.remove("show");
    })

    //googleBtn.removeEventListener("click", google_search(keyword));
}

// for each span that contains text
text_in_knowledge_blocks.forEach(function (e) {
    // double click event listener
    e.addEventListener("dblclick", function (f) {
        // to populate the info box + to make it appear when double clicked at any text.
        populate_info_box(e.textContent);
        infoBox.classList.add("show");

    })
})

// to add  the percentage progressBar effect
window.addEventListener('scroll', function () {
    let max = document.body.scrollHeight - innerHeight;
    progressBar.style.width = `${(pageYOffset / max) * 100}%`;
})

let playButtons = document.querySelectorAll(".play_button");

const AudioContext = window.AudioContext || window.webkitAudioContext;
const audioContext = new AudioContext();

let test_audios = document.querySelectorAll(".test_audio");


//event listener on the play button.

for (let i = 0; i <= playButtons.length; i++) {
    let track = audioContext.createMediaElementSource(test_audios[i]);
    track.connect(audioContext.destination);
    playButtons[i].addEventListener("click", function (e) {
        // check if context is in suspended state (autoplay policy)
        if (audioContext.state === "suspended") {
            audioContext.resume();
        }
        if (this.dataset.playing === "false") {
            test_audios[i].play()
            this.dataset.playing = "true";
            playButtons[i].textContent = "pause";
        } else if (this.dataset.playing === "true") {
            test_audios[i].pause();
            this.dataset.playing = "false";
            playButtons[i].textContent = "play";
        }
    }, false);

    test_audios[i].addEventListener('ended', function () {
        this.dataset.playing = 'false';
        playButtons[i].textContent = "play";
    }, false);

}
