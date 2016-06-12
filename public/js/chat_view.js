var scrolled = false;
function updateScroll() {
    $("#inner").animate({scrollTop: $('#content').prop("scrollHeight")}, 1000);
}

function onScrolledMessageList() {
    scrolled = true;
}

$("#text-message-input").keypress(function (e) {
    if (e.keyCode == 13) {
        if (e.shiftKey === true) {
            // new line
        }
        else {
            submit_message()
        }
        return false;
    }
});