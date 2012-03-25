# This file contains data about Ren'Py, and its various
# releases. Think of it as a kind of database, except that it's stored
# as code rather than as data.

from model import *

# A list of releases. This is automatically filled up when we execute the
# Release and WikiRelease statement-commands, below.
releases = [ ]

Release(    
    prerelease=False,
    invisible=False,
    version="6.13",
    date="September 14, 2011",
    patch=10,
    patch_date="March 25, 2012",
    name="Eye of the Storm",
    exe=21,
    zip=26,
    bz2=28,
    android=True,
    powerpc=True,
    deps="6.13.0",
    announcement="""\
Ren'Py 6.13 "Eye of the Storm" includes two fundamental improvements to Ren'Py. The
first is a complete rewrite of the text display code. In addition to supporting
new features such as interpolation of fields, kerning, ruby text, the new
display code is far faster than the previous code.

Ren'Py 6.13 also adds a DirectX rendering path. This new renderer should lead to
faster and more functional graphics display on Windows systems lacking OpenGL
support.

In addition to these major features, 6.13 adds a style preferences system, new 
actions - including actions for image galleries and music rooms - and new 
themes.

Some notes for upgraders:

* The change in interpolation may cause your old scripts to stop working. Please
  see the incompatible changes documentation for information on how to upgrade 
  your script or enable a compatibility mode.
  
* The shift+U updater is not capable of upgrading 6.12.2 to this release. Please
  download 6.13 from the website.
""",
    
    history="""\
**6.13.10.1710**: March 25, 2012
    This release fixes a bug that can cause image buttons and image maps to
    not work on the software renderer. Other changes include more aggressive
    pruning of the rollback log to reduce memory consumption, improved handling
    of display initialization errors, and fixes to the loading of pure-python
    packages includes as part of a game.
    
**6.13.9.1702**: March 14, 2012
    This release introduces the RAPT tool, a new way of packaging your Ren'Py 
    game for use with Android. It fixes several bugs, including problems with
    hardware compatibility, non-ASCII filenames, and save file size. 
    
    It introduces a new text editor documentation, backported from 
    Ren'Py 6.14. If you use an editor other than jEdit, you'll need to
    check out the new text editor section of the Ren'Py documentation.


**6.13.8.1675**: January 17, 2012
    This release fixes a number of bugs and hardware compatibility problems in
    Ren'Py. It also includes improvements to new-style side image support, and
    adds the ability to run a callback after each Python block.
    
    It has one incompatible change - it reverts the removal of old-style
    substitution support. Please see the list of incompatible changes for
    more information.
    
**6.13.7.1646**: October 18, 2011
    Fixes a problem with substitutions in the launcher. Fixes a crash on font
    searching. On Android, merges multiple taps so as not to overwhelm the 
    event queue.
    
**6.13.6.1642**: October 13, 2011
    Fixes a crash when loading automatically-created styles. Fixes a problem
    with quick saving not taking a screenshot. Fixes a problem with small solid
    textures not showing up, on the software renderer. Fixes a crash when 
    playing back movies on Linux.
    
    This release introduces two new actions, QuickSave and QuickLoad, which
    are used for quick save and qick load functionality. If your game uses
    the new quick menu, please update it with the new code found in 
    template/game/screens.rpy.
    
**6.13.5.1638**: October 10, 2011
    Fixes slow text.

**6.13.4.1637**: October 8, 2011
    Bugfix release 6.13.4 includes the following fixes:
    
    * Jumps from called screens now work. This fixes the developer menu.
    * Hitting shift+G in-game brings the user to the renderer selection menu.
    * Include all source required to rebuild Ren'Py.
    * Fix the renpy-ppc packaging.
    
**6.13.2.1632**: October 5, 2011
    Released bugfix release 6.13.2, which allows Text displayables to be 
    instantiated in init blocks, and fixes error handling.

**6.13.1.1629**: October 3, 2011
    Released bugfix release 6.13.1, which makes Ren'Py run stably.
    
**6.13.0.1601**: September 14, 2011
    Official release.
    
**6.13.0.1601**: September 11, 2011
    Support reading files out of an Android package. User-defined statements can
    take blocks. A fix to lint with non-ASCII characters. A fix to error
    handling.
    
**6.13.0.1598**: September 5, 2011
    Adds error reporting when a non-string is used as text, fixes sound problems
    by moving to libav, and various other fixes.
    
**6.13.0.1594**: September 4, 2011
    First public pre-release.
""",
    
    aside_html="""\
""",    
################################################################################
#    top_html="""\
# <div style="color: #800; background: #fcc; border: 2px solid #800; padding: 1em; margin: .5em; text-align: center;">
# Ren'Py 6.13 has been reported to be incompatible with many users's systems.<br>
# Please download and use <a href="/release/6.12.2">6.12.2</a> until we can fix these problems.
# </div>
# """
################################################################################
    )

Release(    
    prerelease=False,
    invisible=False,
    version="6.12.2",
    name="Human Factor II",
    date="July 30, 2011",
    exe=21,
    zip=27,
    bz2=25,
    android=True,
    deps="6.11.0",
    announcement="""\
Ren'Py 6.12.2 "Human Factor II" is an update that fixes several bugs
found in Ren'Py 6.12.1.
""",
    
    history="""\
**6.12.2.1531**: July 30, 2011
    Initial release.
""",
    
    aside_html="""\
        <object width="380" height="238">
            <param name="movie" value="http://www.youtube.com/v/_MRDp2RHGEc?fs=1&amp;hl=en_US&amp;rel=0"></param>
            <param name="allowFullScreen" value="true"></param>
            <param name="allowscriptaccess" value="always"></param>
            <embed src="http://www.youtube.com/v/_MRDp2RHGEc?fs=1&amp;hl=en_US&amp;rel=0" type="application/x-shockwave-flash" allowscriptaccess="always" allowfullscreen="true" width="380" height="238"></embed>
        </object>

    <i><a href="http://sonia-leong.livejournal.com/200681.html">Let Me Save You! Your Faithful Companion</a></i> time-lapse creation screencast. Courtesy Sonia Leong.
"""    
    )


Release(    
    prerelease=False,
    invisible=False,
    version="6.12.1",
    name="Human Factor",
    date="May 02, 2011",
    bugfix_revision=1520,
    bugfix_date="June 23, 2011",
    exe=21,
    zip=27,
    bz2=25,
    android=True,
    deps="6.11.0",
    announcement="""\
Ren'Py 6.12.1 "Human Factor" is the first of a series of minor releases
focusing on improving the experience of visual novel makers. This release
features several improvements to the process of showing images:

* Image attributes make it no longer necessary to specify every part
  of a changed image.
* The say statement can change image attributes when a character speaks.
* Side images can be specified with the image statement, and can be used
  with NVL-mode dialogue.
* Sticky transforms allow a transform to continue through an image change.

As these new features can change the behavior of existing games, it may be
convenient to disable them for in-development projects. Please see the list of
incompatible changes for instructions on how to do this.

The other major improvement is in error handling. Where previous versions of
Ren'Py would terminate on errors, 6.12.1 will display a screen that allows the
maker to edit problematic files and reload the game, and the user to rollback or
ignore the problem.

Ren'Py 6.12.1 also includes many other minor features and bug fixes, please 
see the full changelog for more details.
""",
    
    history="""\
**6.12.1.1520**: June 23, 2011
    A major bugfix release, including:
    
    * Fixed a problem with texture upload that made games noticeably slower.
    * A better default size for windows on small monitors, like netbooks.
    * xfill and yfill now work for vbox and hbox, respectively.
    * Click-to-continue fixes.
    * Side image fixes.
    
**6.12.1.1502**: May 16, 2011
    Compatibility fixes for Android. This release only consisted of
    new versions of Ren'Py for Android and renpy-apk. If you're only
    developing for desktop platforms, there's no need to update 
    Ren'Py.
    
**6.12.1.1501**: May 04, 2011
    Updated release. Mistakes were made in the update release process, leading
    to a version of Ren'Py that could not switch between windowed and fullscreen
    modes. (Among other problems.) Those problems have been fixed.

**6.12.1.1500**: May 03, 2011
    Updated release. This fixes a bug that prevented Ren'Py from running on
    systems with very old ATI drivers.

**6.12.1.1499**: May 02, 2011
    Final release. Fixes a bug with screenshots.
    
**6.12.1.1497**: April 30, 2011
    Fixes display of exceptions during init code. Allows the contents of 
    viewports to be displayed by the shift+I style inspector. Populates
    config.archives in ascii order.

**6.12.1.1493**: April 24, 2011
    Bug fixes involving say with image attributes.
    Added config.say_attribute_transition as a way to invoke a transition 
    when the image is changed by a say with image attributes, in response
    to feedback from the first users of the feature.

**6.12.1.1487**: April 24, 2011
    First public pre-release.
""",
    
    aside_html="""\
        <object width="380" height="238">
            <param name="movie" value="http://www.youtube.com/v/_MRDp2RHGEc?fs=1&amp;hl=en_US&amp;rel=0"></param>
            <param name="allowFullScreen" value="true"></param>
            <param name="allowscriptaccess" value="always"></param>
            <embed src="http://www.youtube.com/v/_MRDp2RHGEc?fs=1&amp;hl=en_US&amp;rel=0" type="application/x-shockwave-flash" allowscriptaccess="always" allowfullscreen="true" width="380" height="238"></embed>
        </object>

    <i><a href="http://sonia-leong.livejournal.com/200681.html">Let Me Save You! Your Faithful Companion</a></i> time-lapse creation screencast. Courtesy Sonia Leong.
"""    
    )


Release(
    prerelease=False,
    version="6.12.0",
    name="Positronic Brain",
    revision="e",
    date="February 7, 2011",
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
**2011-02-07**
    Final release (6.12.0e). Improves the default screen and fixes
    bugs.

**2011-02-05**
    Fourth pre-release (6.12.0d). Adds main menu prediction, fixes
    screen bugs, improves the default screens, and fixes documentation.

**2011-02-03**
    Third pre-release (6.12.0c). Updates are documented `here <http://lemmasoft.renai.us/forums/viewtopic.php?f=32&t=9207&p=121140#p121140>`_.

**2011-01-30**
    Second pre-release (6.12.0b). Fixes the following bugs:

    * Ren'Py did not work for non-ASCII languages.
    * libGLEW was not distributed on Linux.
    * Could not load savegames that had Renders leak to them.
    * Frames had visual artifacts on the software renderer.

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
            <param name="movie" value="http://www.youtube.com/v/2qrPIdRhv_Y?fs=1&amp;hl=en_US&amp;rel=0"></param>
            <param name="allowFullScreen" value="true"></param>
            <param name="allowscriptaccess" value="always"></param>
            <embed src="http://www.youtube.com/v/2qrPIdRhv_Y?fs=1&amp;hl=en_US&amp;rel=0" type="application/x-shockwave-flash" allowscriptaccess="always" allowfullscreen="true" width="380" height="238"></embed>
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
        if not i.invisible:
            prerelease = prerelease or i
    else:
        current = current or i
        final_releases.append(i)
        
    if not i.wiki:
        release_version[i.version] = i
        
for n, i in enumerate(final_releases):
    i.ordinal = len(final_releases) - n
