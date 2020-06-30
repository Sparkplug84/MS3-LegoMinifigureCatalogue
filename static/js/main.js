const searchName = document.getElementById('searchName');
const searchBox = document.getElementById('search-box');
const searchOptions = document.getElementById('searchOptions');
const themeBox = document.getElementById('theme-box');
const ageBox = document.getElementById('age-box');



if(searchName) {
    function addSearch() {
        if (searchOptions.value=="1") {
            searchBox.classList.remove("d-none");
            themeBox.classList.add("d-none");
            ageBox.classList.add("d-none");
        } else if (searchOptions.value=="2") {
            searchBox.classList.add("d-none");
            themeBox.classList.remove("d-none");
            ageBox.classList.add("d-none");
        } else {
            searchBox.classList.add("d-none");
            themeBox.classList.add("d-none");
            ageBox.classList.remove("d-none");
        }
    }
}

function likeMinifig(x) {
    x.classList.toggle("love-icon2");
}