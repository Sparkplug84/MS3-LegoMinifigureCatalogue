const searchName = document.getElementById('searchName');
const searchBox = document.getElementById('search-box');
const searchOptions = document.getElementById('searchOptions');



if(searchName) {
    function addSearch() {
        if (searchOptions.value=="1") {
            searchBox.classList.remove("d-none");
        } else if (searchOptions.value=="2") {
            searchBox.classList.add("d-none");
        } else {
            searchBox.classList.remove("d-none");
        }
    }
}

// if(searchName) {
//     searchName.onchange = function () { addSearch() };
//     function addSearch() {
//         searchBox.classList.remove("d-none");
//         // print ("Hello!!!")
//     }
// }