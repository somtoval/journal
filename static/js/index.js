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
//getting the values of the journal
let journalExpand = document.querySelector('.mobile-nav-links-journals');
let journalExpanded = document.querySelector('.mobile-inner-nav-journals');

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
expandMenu(journalExpand, journalExpanded);
expandMenu(informationExpand, informationExpanded);
expandMenu(initiativeExpand, initiativeExpanded);
expandMenu(aboutExpand, aboutExpanded);

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

//function to open the search button
function openSearch() {
    document.querySelector('.search-section').classList.toggle('hidden');
}
document.querySelector('.search-button').addEventListener('click', openSearch);
