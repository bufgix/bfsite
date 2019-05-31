function openNav() {
    $(".navbar-toggler").hide("fast")
    document.getElementById("mobilenav").style.width = "100%";
}

function closeNav() {
    $(".navbar-toggler").show("fast")
    document.getElementById("mobilenav").style.width = "0%";
}