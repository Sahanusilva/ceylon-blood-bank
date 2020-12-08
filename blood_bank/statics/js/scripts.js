
window.onload = function () {
document.getElementsByTagName('h1')[2,3].className -= "animate__animated animate__fadeInUp animate__faster";
document.getElementsByTagName('p')[2,3].className -= "animate__animated animate__fadeInUp animate__delay-2s animate__faster";
document.getElementsByClassName('slidder-link')[2,3].className -= "animate__animated animate__fadeInUp animate__delay-2s animate__faster";
}

// owl-carousel2
$(document).ready(function () {
    var owl = $('.owl-carousel');

    owl.owlCarousel({
        autoplay: true,
        autoplayTimeout: 6000,
        animateOut: 'animate__slideOutLeft',
        animateIn: 'animate__slideInRight',
        margin: 0,
        nav: false,
        loop: true,
        touchDrag: true,
        mouseDrag: true,
        dots: false,
        smartSpeed: 750,
        responsive: {
            0: {
                items: 1
            },
            600: {
                items: 1
            },
            1000: {
                items: 1
            }
        }
    });

    owl.on('changed.owl.carousel', function (event) {
        var item = event.item.index - 2; // Position of the current item
        $('h1').removeClass('animate__animated animate__fadeInUp animate__faster');
        $('p').removeClass('animate__animated animate__fadeInUp animate__delay-2s animate__faster');
        $('.slidder > button').removeClass(
            'animate__animated animate__fadeInUp animate__delay-2s animate__faster');
        $('.owl-item').not('.cloned').eq(item).find('h1').addClass(
            'animate__animated animate__fadeInUp animate__delay-1s animate__faster');
        $('.owl-item').not('.cloned').eq(item).find('p').addClass(
            'animate__animated animate__fadeInUp animate__delay-2s animate__faster');
        $('.owl-item').not('.cloned').eq(item).find('.slidder > button').addClass(
            'btn btn-danger animate__animated animate__fadeInUp animate__delay-3s animate__faster');
    
    });

});

// bootstrap-validate


    // const signup = document.getElementById('signup')
    // bootstrapValidate(['#fname','#lname'], 'min:5:Please enter at least 5 characters')






