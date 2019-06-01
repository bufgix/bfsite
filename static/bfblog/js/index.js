function openNav() {
    $(".navbar-toggler").hide("fast")
    document.getElementById("mobilenav").style.width = "100%";
}

function closeNav() {
    $(".navbar-toggler").show("fast")
    document.getElementById("mobilenav").style.width = "0%";
}

$(document).ready(() => {
    $('img').wrap(function(){
        return "<div class='text-center'><a class='venobox_custom' href='" + $(this).attr('src') +"'></a></div>"
    });

    $('img').addClass('img-fluid deep');
    $('.venobox_custom').venobox({
        spinner: 'cube-grid',
        spinColor: '#FDCE93'
    }); 
})