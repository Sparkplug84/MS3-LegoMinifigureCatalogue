const searchName = document.getElementById('searchName');
const searchBox = document.getElementById('search-box');

searchName.onclick = function () { addSearch() };
function addSearch() {
    searchBox.classList.remove("d-none");
}