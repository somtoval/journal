let body = document.querySelector('body');

//function to open the mobile menu
function openMenu() {
    document.querySelector('.mobile-navigation-body').style.display = 'block';
    body.style.position = 'fixed';
}
document.querySelector('.mobile-menu-button-open').addEventListener('click', openMenu)


//function to close the mobile menu
function closeMobileMenu() {
    document.querySelector('.mobile-navigation-body').style.display = 'none';
    body.style.position = 'initial';
}
document.querySelector('#close-button').addEventListener('click', closeMobileMenu);

// function to open inner dropdown 
//getting the information elements
let informationExpand = document.querySelector('.mobile-nav-links-information');
let informationExpanded = document.querySelector('.mobile-inner-nav-information');

//getting the initiative elements
let initiativeExpand = document.querySelector('.mobile-nav-links-initiative');
let initiativeExpanded = document.querySelector('.mobile-inner-nav-initiative');

//getting the about elements 
let aboutExpand = document.querySelector('.mobile-nav-links-about');
let aboutExpanded = document.querySelector('.mobile-inner-nav-about');

function expandMenu(expander, expandedMenu) {
    expander.addEventListener('click', () => {
        if (expandedMenu.style.display == 'none') {
            expandedMenu.style.display = 'block';
        } else {
            expandedMenu.style.display = 'none';
        };
    });
}
expandMenu(informationExpand, informationExpanded);

console.log(window.innerWidth)

// getting the list-with-picture element 
let resizer = document.querySelectorAll('.details');
function ModalHandler() {
    if (window.innerWidth > 767) {
        resizer.forEach((detail) => {
            detail.setAttribute('open', 'open');
        });
    } else {
        resizer.forEach((detail) => {
            detail.removeAttribute('open');
        });
    }
}
ModalHandler();
window.addEventListener('resize', ModalHandler);

//remove the searchbar at 1200px 
function removeSearchBar() {
    if (window.innerWidth < 1200) {
        document.querySelector('.search-section').classList.add('hidden');
    }
}
removeSearchBar();
window.addEventListener('resize', removeSearchBar);

//function to open the search button
function openSearch() {
    document.querySelector('.search-section').classList.toggle('hidden');
}
document.querySelector('.search-button').addEventListener('click', openSearch);


// //scripts for the uplading file 
// function _(el) {
//     return document.getElementById(el);
// }

// function uploadFile() {
//     var file = _("file1").files[0];
//     // alert(file.name+" | "+file.size+" | "+file.type);
//     var formdata = new FormData();
//     formdata.append("file1", file);
//     var ajax = new XMLHttpRequest();
//     ajax.upload.addEventListener("progress", progressHandler, false);
//     ajax.addEventListener("load", completeHandler, false);
//     ajax.addEventListener("error", errorHandler, false);
//     ajax.addEventListener("abort", abortHandler, false);
//     ajax.open("GET", "upload.php"); // http://www.developphp.com/video/JavaScript/File-Upload-Progress-Bar-Meter-Tutorial-Ajax-PHP
//     //use file_upload_parser.php from above url
//     ajax.send(formdata);
// }

// function progressHandler(event) {
//     _("loaded_n_total").innerHTML = "Uploaded " + event.loaded + " bytes of " + event.total;
//     var percent = (event.loaded / event.total) * 100;
//     _("progressBar").value = Math.round(percent);
//     _("status").innerHTML = Math.round(percent) + "% uploaded... please wait";
// }

// function completeHandler(event) {
//     _("status").innerHTML = event.target.responseText;
//     _("progressBar").value = 0; //wil clear progress bar after successful upload
// }

// function errorHandler(event) {
//     _("status").innerHTML = "Upload Failed";
// }

// function abortHandler(event) {
//     _("status").innerHTML = "Upload Aborted";
// }



$(function () {
    $('#btnUpload').on("click", function () {
        $('.progress').remove();
        var sizeInKb = parseFloat($('#fuUpload').prop("files")['0'].size / 1024).toFixed(2);
        // var fileName = $('#fuUpload').prop("files")['0'].name;
        uploadProgress = $('#dvProgress').progressbarManager({
            totalValue: sizeInKb,
            initValue: '0kb',
            animate: true,
            stripe: true,
            style: 'primary'
        });
        var chunk = 0;
        var uploading = setInterval(function () {
            uploadProgress.setValue(chunk);
            if (uploadProgress.isComplete()) {
                clearInterval(uploading);
                uploadProgress.style('success');
            }
            chunk += 500;
        }, 500);
    });
});

$(function () {
    $('#btnUpload2').on("click", function () {
        $('.progress').remove();
        console.log((document.querySelector('#fuUpload2').files[0].size / 1024).toFixed(2))
        var sizeInKb2 = parseFloat((document.querySelector('#fuUpload2').files[0].size / 1024).toFixed(2));
        // var fileName = $('#fuUpload2').prop("files")['1'].name;
        uploadProgress = $('#dvProgress2').progressbarManager({
            totalValue: sizeInKb2,
            initValue: '0kb',
            animate: true,
            stripe: true,
            style: 'primary'
        });
        var chunk = 0;
        var uploading = setInterval(function () {
            uploadProgress.setValue(chunk);
            if (uploadProgress.isComplete()) {
                clearInterval(uploading);
                uploadProgress.style('success');
            }
            chunk += 500;
        }, 500);
    });
});