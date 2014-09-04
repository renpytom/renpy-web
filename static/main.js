var pageTracker;

$(function () {
    pageTracker = _gat._getTracker("UA-1855234-1");
    pageTracker._trackPageview();

    $(".download-button").on('click', function (ev) {
    	pageTracker._trackPageview(ev.target.href);
    });


    if ($.browser.linux) {
    	$(".download-button.linux").removeClass("btn-other").addClass("btn-primary");
    } else if ($.browser.mac) {
    	$(".download-button.mac").removeClass("btn-other").addClass("btn-primary");
    } else if ($.browser.win) {
    	$(".download-button.win").removeClass("btn-other").addClass("btn-primary");
    } else {
    	$(".download-button.linux").removeClass("btn-other").addClass("btn-primary");
    	$(".download-button.mac").removeClass("btn-other").addClass("btn-primary");
    	$(".download-button.win").removeClass("btn-other").addClass("btn-primary");
    }

});
