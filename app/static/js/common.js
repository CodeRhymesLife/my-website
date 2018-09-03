$(document).ready(() => {
    cycleThroughHeaderIcons();
});

const cycleThroughHeaderIcons = () => {
    // Cycle through nav bar images
    const images = [
        'glyphicon glyphicon-console',
        'glyphicon glyphicon-object-align-left',
        'glyphicon glyphicon-plus',
        'glyphicon glyphicon-cloud',
        'glyphicon glyphicon-search',
        'glyphicon glyphicon-globe',
        'glyphicon glyphicon-equalizer',
    ];

    let currentImageIndex = Math.floor((Math.random() * images.length));

    /** Sets the current image to the image at the given index */
    const displayImage = (imageIndex) => {
        // Make sure we stay in range
        imageIndex = imageIndex % images.length;
        $('.navbar-brand span').attr('class', images[imageIndex]);
        currentImageIndex = imageIndex;
    }

    /** Displays the next image in the array */
    const displayNextImage = () => {
        displayImage(currentImageIndex + 1);
    }

    // Display the first image
    displayImage(currentImageIndex)

    // Display a new image every 2 seconds
    setInterval(displayNextImage, 2000);
};
