var scrolled = false;
function updateScroll() {
    $("#inner").animate({scrollTop: $('#content').prop("scrollHeight")}, 1000);
}

function onScrolledMessageList() {
    scrolled = true;
}