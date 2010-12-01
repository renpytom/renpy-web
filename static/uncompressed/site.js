(function() {

var Site = this.Site = {
    start: function() {
        if ($('search')) this.fixSearch();
        if ($('downloads')) this.filterDownloads();
    },

    filterDownloads: function(showAll) {
        $$('.download-button').each(function(item) {
            if (!showAll && !item.hasClass(Browser.Platform.name)) item.addClass('inactive');
        });
    },

    fixSearch: function() {
        new OverText('search');
    }
};

window.addEvent('domready', Site.start.bind(Site));

})();