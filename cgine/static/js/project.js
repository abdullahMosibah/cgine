let playButtons = document.querySelectorAll(".play_button");
const AudioContext = window.AudioContext || window.webkitAudioContext;
const audioContext = new AudioContext();
let test_audios = document.querySelectorAll(".test_audio");


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
            playButtons[i].textContent =  "play";
        }
    }, false);
    test_audios[i].addEventListener('ended', function () {
        this.dataset.playing = 'false';
        playButtons[i].textContent = "play";
    }, false);
}




