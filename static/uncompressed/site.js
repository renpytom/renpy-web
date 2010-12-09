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
        this.startAnalytics();
    },

    filterDownloads: function(showAll) {
        $$('.download-button').each(function(item) {
            if (!showAll && !item.hasClass(Browser.Platform.name)) item.addClass('inactive');
        }).addEvent('click', function() {
            //if (window.console && console.log) console.log('_trackPageview: ' + this.get('href'));
            _gaq.push(['_trackPageview', this.get('href')]);
        });
    },

    fixSearch: function() {
        new OverText('search');
    },

    startAnalytics: function() {
        var ga = document.createElement('script'); ga.type = 'text/javascript'; ga.async = true;
        ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';
        var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(ga, s);
    }
};

window.addEvent('domready', Site.start.bind(Site));

})();