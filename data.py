# This file contains data about Ren'Py, and its various
# releases. Think of it as a kind of database, except that it's stored
# as code rather than as data.

from model import *

# A list of releases. This is automatically filled up when we execute the
# Release and WikiRelease statement-commands, below.
releases = [ ]

Release(
    prerelease=True,
    version="6.12.0",
    name="Positronic Brain",
    revision="a",
    date="February xx, 2010",
    exe=21,
    zip=27,
    bz2=25,
    android=True,
    deps="6.11.0",
    announcement="""\
Ren'Py 6.12.0 "Positronic Brain" is a major release of Ren'Py. This
release adds suport for the Android platform, allowing Ren'Py games to
run on millions of smartphones and tablets. It's possible to package
Ren'Py games and distribute them through the Android market.

On all platforms, this release benefits from improved performance in
the areas of image prediction and OpenGL rendering. New functionality
includes sprites, mouse hover areas, and drag-and-drop. The screen
support added in 6.11 has been improved, and new games now use screens
by default.
""",
    history="""\
**2011-01-29**
    Initial pre-release (6.12.0a).
""",
    aside_html="""\
<img src="/static/6.12.0small.jpg" width="380" height="295">
"""
    
    )


Release(
    version="6.11.2",
    name="It Takes Two",
    revision="b",
    date="October 31, 2010",
    exe=20,
    zip=25,
    bz2=24,
    deps="6.11.0",
    announcement="""\
Ren'Py 6.11.2 "It Takes Two" is the second
minor release of the Ren'Py 6.11 series. The primary focus of this
release is to fix bugs found in previous releases. It also includes
four new themes, and updates the included jEdit text editor.
""",
    history="""\
**2010-10-31**
    Promoted 6.11.2b to final release.
**2010-10-26**
    Second pre-release (6.11.2b). Fixes a longstanding but unlikely bug with Frame.
**2010-10-24**
    Initial pre-release (6.11.2a).
""",
    aside_html="""\
        <object width="380" height="238">
            <param name="movie" value="http://www.youtube.com/v/gMDwc2owtmk?fs=1&amp;hl=en_US&amp;rel=0"></param>
            <param name="allowFullScreen" value="true"></param>
            <param name="allowscriptaccess" value="always"></param>
            <embed src="http://www.youtube.com/v/gMDwc2owtmk?fs=1&amp;hl=en_US&amp;rel=0" type="application/x-shockwave-flash" allowscriptaccess="always" allowfullscreen="true" width="380" height="238"></embed>
        </object>
"""
    
    )

# Pre-web releases.
WikiRelease(version="6.11.1", name="Done in One", date="September 17, 2010")
WikiRelease(version="6.11.0", name="It Goes to Eleven", date="August 19, 2010")
WikiRelease(version="6.10.2", name="Fixing a Hole", date="January 24, 2010")
WikiRelease(version="6.10.1", name="I Can See Clearly Now", date="December 16, 2009")
WikiRelease(version="6.10.0", name="You Ain't Seen Nothing Yet", date="November 18, 2009")
WikiRelease(version="6.9.3", name="Road to Recovery", date="August 3, 2009")
WikiRelease(version="6.9.2", name="Roadside Attraction", date="May 3, 2009")
WikiRelease(version="6.9.1", name="Rest Stop", date="April 18, 2009")
WikiRelease(version="6.9.0", name="The Long and Winding Road", date="March 9, 2009")
WikiRelease(version="6.8.1", name="Heroic Hexameter", date="December 1, 2008")
WikiRelease(version="6.8.0", name="Good News", date="October 25, 2008")
WikiRelease(version="6.7.1", name="Apple Juice", date="September 28, 2008")
WikiRelease(version="6.7.0", name="Splines or Skins", date="September 10, 2008")
WikiRelease(version="6.6.3", name="Bender", date="July 25, 2008")
WikiRelease(version="6.6.2", name="But I Get Up Again", date="May 14, 2008")
WikiRelease(version="6.6.1", name="T-Minus", date="March 15, 2008")
WikiRelease(version="6.6.0", name="Layouts and themes and bears, oh my.", date="February 10, 2008")
WikiRelease(version="6.5.0", name="Breakeven", date="December 29, 2007")
WikiRelease(version="6.4.0", name="Character Actor", date="November 14, 2007")
WikiRelease(version="6.3.3", name="Spiral Energy", date="October 9, 2007")
WikiRelease(version="6.3.2", name="Wheel of Fire", date="August 15, 2007")
WikiRelease(version="6.3.1", name="Clairvoyant Koala", date="July 15, 2007")
WikiRelease(version="6.3.0", name="Giving Blood", date="June 21, 2007")
WikiRelease(version="6.2.0", name="Shpadoinkle Day", date="April 26, 2007")
WikiRelease(version="6.1.1", name="Snow Bunny", date="March 25, 2007")
WikiRelease(version="6.1.0", name="Once More Unto the Breach", date="March 6, 2007")
WikiRelease(version="6.0.0", name="The World Creates", date="February 17, 2007")
WikiRelease(version="5.6.7", name="Make a Statement", date="February 8, 2007")
WikiRelease(version="5.6.6", name="Mighty-X", date="January 12, 2007")
WikiRelease(version="5.6.5", name="Hachiko", date="December 18, 2006")
WikiRelease(version="5.6.4", name="Penguin Parity", date="November 17, 2006")
WikiRelease(version="5.6.3", name="Demo Party", date="November 11, 2006")
WikiRelease(version="5.6.2", name="New World Order", date="October 5, 2006")
WikiRelease(version="5.6.1", name="Community Service", date="September 13, 2006")
WikiRelease(version="5.6.0", name="Community Property", date="September 5, 2006")
WikiRelease(version="5.5.4", name="Engine X", date="August 7, 2006")
WikiRelease(version="5.5.3", name="The Intrigues of Upcoming Releases", date="July 16, 2006")
WikiRelease(version="5.5.2b", name="The Boredom of Bugfixing III", date="June 10, 2006")
WikiRelease(version="5.5.2a", name="The Boredom of More Bugfixing", date="June 1, 2006")
WikiRelease(version="5.5.2", name="The Boredom of Bugfixing", date="June 1, 2006")
WikiRelease(version="5.5.1", name="The Sighs of Hyperlinks", date="May 30, 2006")
WikiRelease(version="5.5.0", name="The Melancholy of Themeable Interfaces", date="April 30, 2006")
WikiRelease(version="5.4.5", name="Graf Eisen", date="April 7, 2006")
WikiRelease(version="5.4.4", name="Congrats Kathryn and mikey", date="March 12, 2006")
WikiRelease(version="5.4.3", name="Reinforce", date="March 8, 2006")
WikiRelease(version="5.4.2", name="Raging Heart", date="February 18, 2006")
WikiRelease(version="5.4.1", name="Bardiche", date="February 12, 2006")
WikiRelease(version="5.4.0", name="Death Clock", date="February 4, 2006")
WikiRelease(version="5.3.3", name="Particle Man", date="January 12, 2006")
WikiRelease(version="5.3.2", name="New Lang Syne", date="December 27, 2005")
WikiRelease(version="5.3.1", name="Joy To The World", date="December 25, 2005")
WikiRelease(version="5.3.0", name="Another Inked Finger", date="December 13, 2005")
WikiRelease(version="5.2.1", name="From Here On...", date="November 29, 2005")
WikiRelease(version="5.2.0", name="Skuld's Hammer", date="November 21, 2005")
WikiRelease(version="5.1.6", name="Artist's Alley", date="November 13, 2005")
WikiRelease(version="5.1.5", name="Palindrome", date="October 25, 2005")
WikiRelease(version="5.1.4", name="Love Simulation Syndrome", date="October 14, 2005")
WikiRelease(version="5.1.3", name="Sed Nobis", date="September 24, 2005")
WikiRelease(version="5.1.2", name="Click Already!", date="September 14, 2005")
WikiRelease(version="5.1.1", name="Katamari Bugfix", date="September 8, 2005")
WikiRelease(version="5.1.0", name="Paper Anniversary", date="August 24, 2005")
WikiRelease(version="5.0.1", name="Return to...", date="July 26, 2005")
WikiRelease(version="5.0", name="Spider", date="June 10, 2005")
WikiRelease(version="4.8.10", name="Zenith", date="June 23, 2005")
WikiRelease(version="4.8.9", name="Seagull", date="June 17, 2005")
WikiRelease(version="4.8.8", name="Cedar", date="June 12, 2005")
WikiRelease(version="4.8.7", name="American Eagle", date="June 9, 2005")
WikiRelease(version="4.8.6", name="Molly Brown", date="May 29, 2005")
WikiRelease(version="4.8.5", name="Faith 8", date="May 26, 2005")
WikiRelease(version="4.8.4", name="Sigma 8", date="May 13, 2005")
WikiRelease(version="4.8.3", name="Aurora 8", date="May 7, 2005")
WikiRelease(version="4.8.2a", name="", date="May 3, 2005")
WikiRelease(version="4.8.2", name="Friendship 8", date="May 2, 2005")
WikiRelease(version="4.8.1", name="Liberty Bell 8", date="April 26, 2005")
WikiRelease(version="4.8", name="Freedom 8", date="April 22, 2005")
WikiRelease(version="4.7.2", name="", date="April 2, 2005")
WikiRelease(version="4.7.1", name="The Clock is Running!", date="February 27, 2005")
WikiRelease(version="4.7", name="", date="February 14, 2005")
WikiRelease(version="4.6.1", name="", date="February 10, 2005")
WikiRelease(version="4.6", name="Start your Engines!", date="February 8, 2005")
WikiRelease(version="4.5", name="Inked Finger", date="February 5, 2005")
WikiRelease(version="4.4.2", name="", date="January 16, 2005")
WikiRelease(version="4.4", name="Christmas Bonus", date="December 25, 2004")
WikiRelease(version="4.3.1", name="", date="December 14, 2004")
WikiRelease(version="4.3", name="", date="December 11, 2004")
WikiRelease(version="4.2", name="", date="September 25, 2004")
WikiRelease(version="4.1", name="", date="September 12, 2004")
WikiRelease(version="4.0", name="", date="September 6, 2004")
WikiRelease(version="4pr1", name="Preview Release 1", date="August 24, 2004")

# The currrent pre-release and release.
prerelease = None
current = None

# A map from version to the release object. Used to get information about
# a particular release.
release_version = { }

# All final releases.
final_releases = [ ]

for i in releases:
    if i.prerelease:
        prerelease = prerelease or i
    else:
        current = current or i
        final_releases.append(i)
        
    if not i.wiki:
        release_version[i.version] = i
        
for n, i in enumerate(final_releases):
    i.ordinal = len(final_releases) - n
