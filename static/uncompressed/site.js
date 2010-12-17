(function() {

// analytics queue
var _gaq = this._gaq = _gaq || [
    ['_setAccount', 'UA-1855234-1'],
    ['_trackPageview']
];

var Site = this.Site = {
    start: function() {
        if ($('search')) this.fixSearch();
        if ($('downloads')) this.filterDownloads();
    },

    filterDownloads: function(showAll) {
        $$('.download-button').each(function(item) {
            if (!showAll && !item.hasClass(Browser.Platform.name)) item.addClass('inactive');
        }).addEvent('click', function() {
            pageTracker._trackPageview(this.get('href'));            
        });
    },

    fixSearch: function() {
        new OverText('search');
    },

};

window.addEvent('domready', Site.start.bind(Site));

})();