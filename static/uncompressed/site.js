(function() {

var pageTracker;

var Site = this.Site = {
    start: function() {
        this.runAnalytics();
        if ($('search')) this.fixSearch();
        if ($('downloads')) this.filterDownloads();
    },

    runAnalytics: function() {
        pageTracker = _gat._getTracker("UA-1855234-1");
        pageTracker._trackPageview();
    },

    filterDownloads: function(showAll) {
        $$('.download-button').each(function(item) {
            if (!showAll && !item.hasClass(Browser.Platform.name)) item.addClass('inactive');
        }).addEvent('click', function() {
            if (pageTracker) pageTracker._trackPageview(this.get('href'));
        });
    },

    fixSearch: function() {
        new OverText('search');
    }
};

window.addEvent('domready', Site.start.bind(Site));

})();