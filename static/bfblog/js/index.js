// Particles.js
/*var partJson = {
    "particles": {
        "number": {
            "value": 75
        },
        "color":{
            "value": "#CCCCCC"
        },
        "shape":{
            "type": "circle"
        },
        "opacity":{
            "value": 0.9,
            "random": true
        },
        "size": {
            "value": 5
        },
        "line_linked":{
            "enable": true,
            "distance": 120
        },
        "move":{
            "enable": true,
            "speed": 1,
            "direction": "top-left"
        },
        "interactivity": {
            "enable": false,
            "detect_on": "canvas",
            "events": {
                "onclick": {
                    "enable": false,
                    "mode": "push"
                }
            },
        }
    } 
};
var jsonUri = "data:text/plain;base64,"+window.btoa(JSON.stringify(partJson));*/

function openNav() {
    $(".navbar-toggler").hide("fast")
    document.getElementById("mobilenav").style.width = "100%";
}

function closeNav() {
    $(".navbar-toggler").show("fast")
    document.getElementById("mobilenav").style.width = "0%";
}

$(document).ready(() => {
    /* Particles json load
    particlesJS.load('particles-js', jsonUri, () => {
        console.log('Particles json loaded');
    })*/

    $(document).find('.post-image').wrap(function(){
        return "<div class='text-center'><a class='venobox_custom' href='" + $(this).attr('src') +"'></a></div>"
    });
    $(".blog-content").find('img').wrap(function() {
        return "<div class='text-center'><a class='venobox_custom' href='" + $(this).attr('src') +"'></a></div>"
    })
    $(".blog-content").find('iframe').wrap(function(){
        return "<div class='text-center'></div>"
    })

    $(".blog-content").find('img').addClass('img-fluid deep');
    $('.venobox_custom').venobox({
        spinner: 'cube-grid',
        spinColor: '#FDCE93'
    }); 
})