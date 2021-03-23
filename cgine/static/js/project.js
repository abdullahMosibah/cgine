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


function populate_info_box(keyword) {
    infoKeyword.textContent = keyword;
}

// for each span that contains text
text_in_knowledge_blocks.forEach(function (e) {
    // double click event listener
    e.addEventListener("dblclick", function (f) {
        // to populate the info box + to make it appear when double clicked at any text.
        populate_info_box(e.textContent);
        infoBox.classList.add("show");
        //listener for the google normal search
        googleBtn.addEventListener("click", () => {
            window.open(`https://www.google.com/search?q=${e.textContent}`, '_blank');
        })
        //listener for the google scholar search.
        googleScholarBtn.addEventListener('click', () => {
            window.open(`https://scholar.google.com/scholar?hl=en&as_sdt=0,5&q=${e.textContent}`, "_blank");
        })
        // to make the info box disappear when clicked at any location at the document.
        window.addEventListener('click', function () {
            infoBox.classList.remove("show");
        })
    })
})

// to add  the percentage progressBar effect
window.addEventListener('scroll', function () {
    let max = document.body.scrollHeight - innerHeight;
    progressBar.style.width = `${(pageYOffset / max) * 100}%`;
})
