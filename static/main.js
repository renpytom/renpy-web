var pageTracker;

$(function () {
    pageTracker = _gat._getTracker("UA-1855234-1");
    pageTracker._trackPageview();

    $(".download-button").on('click', function (ev) {
    	pageTracker._trackPageview(ev.target.href);
    });


    var btn_class = "btn-success";

    if ($("#prerelease-warning").size() > 0) {
    	btn_class = "btn-warning";
    }

    if ($.browser.linux) {
    	$(".download-button.linux").removeClass("btn-other").addClass(btn_class);
    } else if ($.browser.mac) {
    	$(".download-button.mac").removeClass("btn-other").addClass(btn_class);
    } else if ($.browser.win) {
    	$(".download-button.win").removeClass("btn-other").addClass(btn_class);
    } else {
    	$(".download-button.linux").removeClass("btn-other").addClass(btn_class);
    	$(".download-button.mac").removeClass("btn-other").addClass(btn_class);
    	$(".download-button.win").removeClass("btn-other").addClass(btn_class);
    }

});
