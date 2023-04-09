window.onload = function() {
// Getting the current photo index from Flask and scrolling to the corresponding menu link
var currentPhoto = {{ current_index }};
var photoMenu = document.querySelector('.photo-menu');
var photoLinks = photoMenu.querySelectorAll('a');
photoLinks[currentPhoto].scrollIntoView();

// Getting the height of the images and the menu with links
var imgHeight = document.getElementById("image-container").offsetHeight;
var menuHeight = document.getElementById("image-menu").offsetHeight;

// Function to check if the currently displayed photo has a corresponding link in the menu
function checkImageLink() {
var currentImage = document.querySelector(".active");
var currentImageNumber = currentImage.getAttribute("id");
var imageLink = document.querySelector('a[href="#' + currentImageNumber + '"]');
var imageLinkTop = imageLink.getBoundingClientRect().top;

// If the currently displayed photo is not visible in the menu, scroll the menu so that the link to the current photo is visible
if (imageLinkTop < menuHeight || imageLinkTop > imgHeight) {
imageLink.scrollIntoView();
}
}

// Checking the menu links on page load or window resize
window.addEventListener("load", checkImageLink);
window.addEventListener("resize", checkImageLink);
}