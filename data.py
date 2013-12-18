# This file contains data about Ren'Py, and its various
# releases. Think of it as a kind of database, except that it's stored
# as code rather than as data.

from model import *

# A list of releases. This is automatically filled up when we execute the
# Release and WikiRelease statement-commands, below.
releases = [ ]

# Patch release checklist:
#
# 1. Bump patch.
# 2. Update patch_date.
# 3. Add to history.



Release(
    prerelease=False,
    invisible=False,
    version="6.16",
    prerelease_date="November 4, 2013",
    date="November 6, 2013",
    patch=5,
    patch_date="December 17, 2013",
    name="In the Arena",
    exe=24,
    bz2=31,
    zip=34,
    android=True,
    powerpc=False,
    deps="6.15.5",
    world_order=4,
    announcement="""\
On behalf of the Ren'Py team, I'm pleased to announce Ren'Py 6.16 "In the
Arena". This release brings with it:

* Improved Android support, including the ability to build APKs from the
  launcher, support for Expansion APKs, and support for televison-based
  consoles like the OUYA.
* The ability to associate JSON information with a save file, and access
  that information in the load and save screens.
* Save file synchronization when Ren'Py is run from a shared directory.
* Support for a creator dumping the text of the game script, and for
  automatically playing appropriately-named voice files.
* Improvements to the gallery (including a new navigation overlay) and the
  music room (such as shuffle, loop, and single-track toggles.)
* A Japanese translation of the launcher, template, and documentation.

As well as a number of minor improvements and bugfixes.

This release has been brought to you by:

* javimat
* kyouryuukunn
* Koichi "vbkaisetsu" Akabe
* Daniel Luque
* Tom "PyTom" Rothamel

With thanks to antoinentx for improving support for international
directories, and everyone who contributed ideas, bug reports, and feedback
to Ren'Py development.
""",

    history="""\
**6.16.5.525**: December 17, 2013
    This release adds back a missing file that is required to launch jEdit.

**6.16.4.524**: December 16, 2013
    This release fixed Android building support, the Replay function, and
    the scanning of save games. It also includes a number of improvements
    to the documentation.

**6.16.3.502**: November 29, 2013
    This release fixes a problem that could cause excessive texture memory
    usage. It also improves Android support in several ways, making it
    possible for Ren'Py games to appear in the tablet section of Google Play.

**6.16.2.490**: November 21, 2013
    This release adds new Spanish translations of the launcher and template
    game. It adds a new function that gets the mouse position, and fixes
    bugs, typos, and usability flaws in the launcher and Ren'Py proper.

**6.16.1.409**: November 9, 2013
    This release includes a number of bug fixes related to translation and
    running in non-ASCII directories, including a fix to the updater. It
    also includes documentation improvements.
""",

    full_html="""\
<img src="/static/6.16.jpg" width="1000" alt="Screenshot of Ren'Py 6.16">
""",

    top_html="""\
""",
    )



Release(
    prerelease=False,
    invisible=False,
    version="6.15",
    prerelease_date="February 17, 2013",
    date="March 3, 2013",
    patch=7,
    patch_date="June 26, 2013",
    name="Foreign Policy",
    exe=22,
    bz2=27,
    zip=29,
    android=True,
    powerpc=False,
    deps="6.15.5",
    world_order=4,
    announcement="""\
I'm pleased to announce Ren'Py 6.15 "Foreign Policy", the result of about
six months of Ren'Py development. The main focus of this release was on
internationalization, the creation of a comprehensive translation system,
and better support for displaying Japanese text. Other new features
include:

* An interactive console that allows you to type Ren'Py and python commands,
  that can be accessed by typing shift+O.
* Screens now take positional and named parameters.
* Support for creating a replay gallery.
* Voice improvements, including the ability to mute particular voices.
* Support for skinning the launcher.

Ren'Py now includes a Japanese translation of the tutorial game, which can
be accessed from the preferences menu. For a full list of features and bug fixes,
please see the changelog.

Ren'Py 6.15 has increased the minimum requirements to run on the Macintosh
platform. It now requires a 64-bit Intel Macintosh running OS X 10.6 or
later.

Once again, this release has seen many contributions from the community. We
thank:

* Koichi Akabe for much of the new Japanese support and the Japanese
  translation of the tutorial game.
* Shiz, C, and Delta for the interactive Console.
* Ren for advice on how the translation system should work.

And, of course, everyone who contributed ideas, bug reports, and feedback
to Ren'Py development.
""",

    history="""\
**6.15.7.374**: June 26, 2013

    Fix a regression in ImageDissolve.

**6.15.6.372**: June 25, 2013

    This release includes improvements for the Android platform:

    * Assets are now read exclusively from the APK and expansion file.
    * Logs and tracebacks are placed on external storage.
    * Saves are placed on external storage, except when saves from
      older versions of Ren'Py exist.

    The GL2 shaders Ren'Py uses have been simplified in the (usual) case
    where no clipping is occurring. This leads to a noticeable speed
    improvement on Android, and potentially other platforms as well.

    An issue with Drag-and-drop has been fixed. Thanks go to Kinsman
    for contributing this fix.

    The Skip action now triggers the skip indicator. It also
    supports a new fast parameter, which causes skipping to the
    next menu.

    This release includes various minor changes to improve compatibility
    with very old Ren'Py games. (It now runs the Ren'Py 5 demo.)

**6.15.5.354**: June 6, 2013

    New features:

    * Additive blending, but only in the GL and DirectX/ANGLE renderers.
    * The new Flatten displayable, which combines multiple textures into one.

    Bug/Build fixes:

    * Before this release, Ren'Py produced zip files with unix modes that
      were writable by all users. If unzipped by a program that ignored the
      umask (like info-zip), the files could be overwritten by other users,
      causing a security problem.

      This problem only existed on unix-like systems that are shared by
      multiple users.
    * Ren'Py once again uses freetype auto-hinting when displaying fonts.
    * Ren'Py builds with the current libav (and ffmpeg).


**6.15.4.320**: April 6, 2013

    Bug fixes and improvements, including:

    * The 64-bit Linux version of Ren'Py is linked against the correct
      libraries. Versions 6.14.x and 6.15.0-3 were linked against
      incorrect Python libraries.

    * In the common case, the python interpreter is no longer locked while
      images are preloading. This helps prevent image preloading from causing
      framerate problems.

    * The new build.exclude_empty_directories variable determines if empty
      directories are included in archive files. Previously, this was
      undefined, and varied from platform to platform.


**6.15.3.303**: March 30, 2013

    Many bug fixes and improvements:

    * Image prediction has been broken up, such that a small amount of image
      prediction will run each frame. This prevent looping ATL animations
      from blocking image prediction.

    * When playing a fullscreen video, the screen will not be updated before
      the first frame is ready. This makes it possible to smoothly transition
      into a movie without displaying a black screen.

    * Fix problems with text input display on fonts that do not contain a
      zero-width space glyph.

    * Rare segfaults relating to font unloading have been fixed.

    * Fixed a memory leaks related to the rollback log and text layout cache.

    * Script parsing will fail with an error if a logical line exceeds 64 KB.

    * Quicksave will not fail of if the current file page is the auto-save page.

    * When a viewport changes size before being shown to the user, the offsets
      are re-applied to the viewport

    * SpriteManager now respects sprite zorder.

**6.15.2.280**: March 5, 2013

    This release fixes an issue with selecting the project directory on the
    mac. It also adds the ability to loop a single track in the music room.

**6.15.1.275**: March 5, 2013

    This release fixes the packaging of the editra text editor.
""",

    full_html="""\
<img src="/static/6.15.jpg" width="1000" height="367" alt="Screenshot of Ren'Py 6.15">
""",

    top_html="""\
""",
    )



Release(
    prerelease=False,
    invisible=False,
    version="6.14",
    prerelease_date="July 22, 2012",
    date="August 18, 2012",
    patch=1,
    patch_date="August 26, 2012",
    name="Steampunk Hamster",
    exe=22,
    bz2=27,
    zip=29,
    android=True,
    powerpc=True,
    deps="6.14.0",
    world_order=4,
    announcement="""\
I'm pleased to announce Ren'Py 6.14 "Steampunk Hamster", a release that brings
with it many improvements to Ren'Py and Ren'Py development.

Perhaps the largest theme of this release is that the tools we use to make
Ren'Py are now the same tools that we use to make Ren'Py games. Along this
vein:

* The Ren'Py launcher has been rewritten. It's now far more attractive, and
  contains a new script navigation function that makes it easy to navigate
  Ren'Py code.
* For most creators, we now recommend using the Editra editor with Ren'Py
  support. While still in beta, Editra is a lightweight and powerful
  programmer's editor to which we've added features that ease Ren'Py development.
  (jEdit is still supported, when Editra is not suitable.)
* The Ren'Py build process has also been updated. Now, it's possible to, in
  a single click, archive files and build a distribution of your game. Games
  may also use the same web updater that's used to update Ren'Py.

The engine proper has also seen many improvements:

* Video playback has been rewritten to improve robustness, performance, and
  stability. WebM is now a supported format.
* The new A White Tulip theme, written from scratch, provides some diversity
  to the look of Ren'Py games.
* Improvements to rollback, including the ability to fix rollback so that
  the user can't change a choice once made, without reloading.
* Several convenience shortcuts have been added to screens. A viewport with
  scrollbars can now be created as a single statement, and the style properties
  of text inside textbuttons and labels can be changed directly.
* An experimental new image load log helps creators understand image prediction
  and cache misses.
* Linux x86_64 is now supported by Ren'Py. Linux distributions will support
  both x86 and x86_64 cpus.
* Ren'Py ships with Python 2.7, and many of the libraries that underly
  Ren'Py have been updated.

This release has seen a huge amount of support from the community. I
especially thank:

* Edwin, for contributing the improved rollback support and several bug
  fixes and new features.
* Doomfest, for the visual design of the new launcher.
* Ren and Jake Staines for contributing the new A White Tulip theme.
* SleepKirby for improvements to Ren'Py's documentation.
* Apricotorange, for adding the NVL-mode tutorial to Ren'Py's documentation.

As of this release, Ren'Py uses github for project hosting.

Due to the change to the new web updater, shift+U updating from previous
versions of Ren'Py is not supported.
""",

    history="""\
**6.14.1.366**: August 26, 2012

   This release fixes a number of bugs in Ren'Py 6.14, including:

   * A major bug that prevented rollback and save from working for variables
     that are only updated in python functions.
   * Crashes during video and audio playback, especially on Mac OS X.
   * The version of zsync used by the updater didn't work on Windows XP.
   * Several string encoding problems in the new launcher.

   All users of Ren'Py 6.14.0 should upgrade to this release. Windows XP
   users should download the release again, while users of other supported
   operating systems can use the launcher to update.
""",

    full_html="""\
<img src="/static/t1000.jpg" width="1000" height="367" alt="Screenshot of Ren'Py, Editra, and the Ren'Py Launcher">
""",

    top_html="""\
""",
    )


Release(
    prerelease=False,
    invisible=False,
    version="6.13",
    date="September 14, 2011",
    patch=12,
    patch_date="April 17, 2012",
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
**6.13.12.1728**: April 17, 2012
    This release:

    * Fixes a related minimize and restore bug.
    * Improves compatibility with games that replace config.keymap.
    * Allows StylePreference and Language to work together.
    * Logs to the system temp directory if it can't writhe to the current
      directory.
    * Allows the screenshot filename to be configured by the creator.
    * Fixes keyboard adjustment of bars.
    * Updates the preferences screen when the window resizes.
    * Clears keyboard modifiers (like alt) when the window gains focus. This
      fixes a problem where the alt from an alt-tab would be remembered by
      Ren'Py, even after the key has been released.

**6.13.11.1715**: March 27, 2012
    This fixes a bug triggered (in some circumstances) by minimizing and
    restoring the game on Windows.

**6.13.10.1710**: March 25, 2012
    This release fixes a bug that can cause image buttons and image maps to
    not work on the software renderer. Other changes include more aggressive
    pruning of the rollback log to reduce memory consumption, improved handling
    of display initialization errors, and fixes to the loading of pure-python
    packages included as part of a game.

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
