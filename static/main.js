var pageTracker;

$(function () {
    $(".download-button").on('click', function (ev) {
        let url = new URL(ev.target.href, document.baseURI).href;

        gtag('event', 'page_view', {
            page_location: url,
        });

    	$("#patreon").show();
    });

    $(".colorbox").colorbox({ rel : 'colorbox', maxWidth: "95%", maxHeight : "95%" });

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
