#coding=utf-8
# This file contains data about Ren'Py, and its various
# releases. Think of it as a kind of database, except that it's stored
# as code rather than as data.

from model import *

# A list of releases. This is automatically filled up when we execute the
# Release and WikiRelease statement-commands, below.
releases = [ ]

# Private Prerelease checklist:
#
# 1. prerelease=True
# 2. invisible=True
# 3. version
# 4. patch=0
# 5. patch_date=None
# 6. name
# 7. sizes
# 8. -
# 9. announcement.

# Patch release checklist:
#
# 1. Bump patch.
# 2. Update patch_date.
# 3. Add to history.

# Final release checklist:
#
# 1. Bump date.
# 2. prerelease=False
#
# Remember to add.py --release !


# To get the list of contributors to a release, we can use the command:
# git shortlog 6.99..HEAD

Release(
    prerelease=True,
    invisible=False,
    version="6.99.12",
    pygame="-2.1.0",
    date="December xx, 2016",
    patch=None,
    name="We get the job done.",
    world_order=7,
    announcement="""\
I'd like to announce Ren'Py 6.99.12, the latest in a series of releases
that will culminate in Ren'Py 7, and one of the biggest Ren'Py releases
to date.

This release focuses on improving support for new versions of macOS, by
changing the macOS-specific package to support code signing and work
correctly when path randomization is enabled. When run on macOS, Ren'Py
can automatically sing the application, and create a signed disk image.
The launcher can launch older Ren'Py applications on macOS Sierra, to
improve compatibility with older games.

Because of this change, the -all distribution has been retired, replaced
with -mac and a new -pc distribution that supports Windows and Linux.

The other main focus of this release is improving support for translation
of the new GUI. Translating Ren'Py now translates both the launcher and the
interface of new games created in the launcher language. It is also possible
to change the font used by the launcher and new projects. There is a page
about translating Ren'Py in the documentation, to guide the process.

In addition to these major focuses, this release includes a number of new
features and bug fixes.

Ren'Py 6.99.12 is brought to you by:

* Bryan Tsang
* Daniel Luque
* Joshua Fehler
* Morgan Willcock
* Merumelu
* Nyaatrap
* Xela
* Xavi-Mat

and myself, Tom "PyTom" Rothamel.
""".decode("utf-8"),

    history="""\
The history of older Ren'Py 6.99 releases can be found at the following
URLs:

* https://www.renpy.org/release/6.99.11
* https://www.renpy.org/release/6.99.10
* https://www.renpy.org/release/6.99.9
* https://www.renpy.org/release/6.99.8
* https://www.renpy.org/release/6.99.7
* https://www.renpy.org/release/6.99.6
* https://www.renpy.org/release/6.99.5
* https://www.renpy.org/release/6.99
""",

    full_html="""\
<img src="/static/6.99.11.jpg" alt="" style="width: 100%">
""",

    top_html="""\
""",
)


Release(
    prerelease=False,
    invisible=False,
    version="6.99.11",
    pygame="-2.1.0",
    prerelease_date=None,
    date="September 5, 2016",
    patch=None,
    patch_date=None,
    name="Who tells your story?",
    exe=None,
    bz2=None,
    zip=None,
    powerpc=False,
    world_order=6,
    announcement="""\
I'd like to announce Ren'Py 6.99.11, the latest in a series of releases
that will culminate in Ren'Py 7, and one of the biggest Ren'Py releases
to date.

The biggest change is a new default GUI framework. Out of the box, the new
GUI looks more modern, works across a range of screen sizes, and supports
mobile devices out of the box. The GUI is also easier for creators of all
skill levels to customize, with re-theming accomplished by replacing image
files and optionally adjusting variables. The Ren'Py documentation now
includes a GUI customization guide explaining how to completely retheme
the new GUI.

Thanks go to Auro-Cyanide for the original design of the new GUI. (But
don't blame her - we've had to stray quite a bit from that design in pursuit
of resolution independence.)

There have been a number of features added to Ren'Py to support the new GUI.

* Ren'Py now natively supports a dialogue history/readback system.
* File pages can be renamed by clicking on the page title/number.
* Style properties that use image filenames can take a [prefix\_] substitution,
  which causes a style prefix search.

And the usual set of non-GUI-related changes:

* Android support has been partially rewritten. It now supports x86 in addition
  to ARM, supports immersive mode, and fixes problems downloading Android
  dependencies.
* Ren'Py supports Chrome OS by converting an Android package using the Android
  Runtime for Chrome tool.
* The Ren'Py script language supports locally-scoped labels.
* Transforms support tiling the child multiple times, and panning over the child
  image by an angle.

A Vietnamese translation of the launcher and tutorial has been added by Thuong
Nguyen Huu. An Indonesian translation of the launcher and default project has
been contributed by Pratomo Asta Nugraha.

Ren'Py 6.99.11 is brought to you by:

* Caryoscelus
* Diapolo10
* Edward Betts
* Ferdinand Thiessen
* Kevin Turner
* Morgan Willcock
* Nolanlemahn
* Pratomo Asta N
* Sapphi
* Shiz
* Vollschauer
* Xavi-mat
* Xela

and myself, Tom "PyTom" Rothamel.
""".decode("utf-8"),

    history="""\
The history of older Ren'Py 6.99 releases can be found at the following
URLs:

* https://www.renpy.org/release/6.99.10
* https://www.renpy.org/release/6.99.9
* https://www.renpy.org/release/6.99.8
* https://www.renpy.org/release/6.99.7
* https://www.renpy.org/release/6.99.6
* https://www.renpy.org/release/6.99.5
* https://www.renpy.org/release/6.99
""",

    full_html="""\
<img src="/static/6.99.11.jpg" alt="" style="width: 100%">
""",

    top_html="""\
""",
    )


Release(
    prerelease=False,
    invisible=False,
    version="6.99.10",
    pygame="-2.1.0",
    prerelease_date="March 21, 2016",
    date="March 24, 2016",
    patch=None,
    patch_date=None,
    name="NaNoRenO - The Other March Madness",
    exe=36,
    bz2=54,
    zip=59,
    powerpc=False,
    world_order=6,
    announcement="""\
I'd like to announce Ren'Py 6.99.10, the latest in a series of releases that
will culminate in Ren'Py 7. This release fixes two regressions that were
introduced in Ren'Py 6.99.9:

* Ren'Py would fail to start if a DirectInput gamepad could not be opened in
  exclusive mode.
* Ren'Py would fail to start with an SDL error on certain Android devices.

This release also includes:

* A new vpgrid widget, which combines a viewport and a grid into a single
  widget, with optimized rendering.
* InputValues that can be with the text input widget to allow multiple text
  inputs to be displayed at once.
* A Greek translation of the launcher, contributed by George Economidis.

Ren'Py 6.99.10 is brought to you by:

* George Economidis
* Jackmcbarn

and myself, Tom "PyTom" Rothamel.
""".decode("utf-8"),

    history="""\
The history of older Ren'Py 6.99 releases can be found at the following
URLs:

* https://www.renpy.org/release/6.99.9
* https://www.renpy.org/release/6.99.8
* https://www.renpy.org/release/6.99.7
* https://www.renpy.org/release/6.99.6
* https://www.renpy.org/release/6.99.5
* https://www.renpy.org/release/6.99
""",

    full_html="""\
""",

    top_html="""\
""",
    )


Release(
    prerelease=False,
    invisible=False,
    version="6.99.9",
    pygame="-2.1.0",
    prerelease_date="February 28, 2016",
    date="March 07, 2016",
    patch=None,
    patch_date=None,
    name="To the nines.",
    exe=36,
    bz2=54,
    zip=59,
    powerpc=False,
    world_order=6,
    announcement="""\
I'm happy to announce Ren'Py 6.99.9, the latest in a series of releases that
will culminate in Ren'Py 7. This release features a full rewrite of the audio
and video playback code, which allows for a number of often-requested features:

* Partial playback of audio files, including the specification of start,
  end, and loop points.
* A new audio channel that allows the playback of multiple sound files at
  once, for use by interface and game sound
* The ability to play multiple movies at once, and to seamlessly loop
  movies.
* Movie-backed sprites that use a pair of movies, one for the color channel
  and one containing alpha (opacity) information.

This release includes a major bugfix involving fullscreen games on Windows
when DPI scaling is used, and a number of other fixes and new features.

Ren'Py 6.99.9 is brought to you by:

* Carl
* Markus Koschany
* Shiz
* Vollschauer

and myself, Tom "PyTom" Rothamel.
""".decode("utf-8"),

    history="""\
The history of older Ren'Py 6.99 releases can be found at the following
URLs:

* https://www.renpy.org/release/6.99.8
* https://www.renpy.org/release/6.99.7
* https://www.renpy.org/release/6.99.6
* https://www.renpy.org/release/6.99.5
* https://www.renpy.org/release/6.99
""",

    full_html="""\
""",

    top_html="""\
""",
    )


Release(
    prerelease=False,
    invisible=False,
    version="6.99.8",
    prerelease_date="December 12, 2015",
    date="December 25, 2015",
    patch=None,
    patch_date=None,
    name="Here's to the crazy ones.",
    exe=34,
    bz2=48,
    zip=52,
    powerpc=False,
    world_order=6,
    announcement="""\
I'm pleased to announce Ren'Py 6.99.8. This is the latest in a series of
releases that introduce the new features that will make up Ren'Py 7. Ren'Py
6.99.8 fixes a bug with text spacing introduced in 6.99.7, and also adds
new features, including:

* The ability to associate an image tag with a layer, transform, and zorder,
  and a new function that makes adding custom layers easier.
* A full set of easing functions that can be used with ATL.
* An overhaul of new-style side images, allowing transforms (and hence,
  transitions) to be applied when the side image changes.
* A new PushMove transition class, which uses the new scene to push the
  old one out.
* HighDPI display support has been added for the Windows platform.

As usual, other features have been added, bugs have been fixed, and Ren'Py
has been generally improved.

Ren'Py 6.99.8 is brought to you by:

* BlackDragonHunt/Mangagamer
* Kalawore
* Kuroonehalf
* Nyaatrap
* Rikxz
* Vollschauer

and myself, Tom "PyTom" Rothamel.
""".decode("utf-8"),

    history="""\
The history of older Ren'Py 6.99 releases can be found at the following
URLs:

* http://www.renpy.org/release/6.99.7
* http://www.renpy.org/release/6.99.6
* http://www.renpy.org/release/6.99.5
* http://www.renpy.org/release/6.99
""",

    full_html="""\
<img src="/static/6.99.7.jpg" title="Syrup and the Ultimate Sweet, running under Ren'Py 6.99.7." style="width: 100%">
""",

    top_html="""\
""",
    )


Release(
    prerelease=False,
    invisible=False,
    version="6.99.7",
    prerelease_date="October 25, 2015",
    date="November 1, 2015",
    patch=None,
    patch_date=None,
    name="Here's to the crazy ones.",
    exe=34,
    bz2=48,
    zip=52,
    powerpc=False,
    world_order=6,
    announcement="""\
I'm pleased to announce Ren'Py 6.99.7. This is the latest in a series of
releases that introduce the new features that will make up Ren'Py 7. Ren'Py
6.99.7 is primarily to fixing bugs and rendering issues introduced in 6.99.7,
but also introduces a number of new features, including:

* A new dynamic images feature that lets Ren'Py interpolate text into displayables
  at the start of each interaction. This should make certain common patterns much
  easier to implement, such as dressup code that previously required a large
  number of ConditionSwitches.
* An extension to the define statement that makes it possible to define config
  and persistent variables. Persistent variables use special semantics to ensure
  a persistent variable is only defined once.

A number of other smaller features have been added, as described in the changelog.
Over a dozen fixes to bugs and regressions are listed in the changelog, and
there are probably a few more fixes that didn't make it.

Ren'Py 6.99.7 is brought to you by:

* Diapolo10
* Emmeken
* Kalawore
* Javimat
* Pavel Langwell
* Ricardo Pérez
* Spiky Caterpillar

and myself, Tom "PyTom" Rothamel.
""".decode("utf-8"),

    history="""\
The history of older Ren'Py 6.99 releases can be found at the following
URLs:

* http://www.renpy.org/release/6.99.6
* http://www.renpy.org/release/6.99.5
* http://www.renpy.org/release/6.99
""",

    full_html="""\
<img src="/static/6.99.7.jpg" title="Syrup and the Ultimate Sweet, running under Ren'Py 6.99.7." style="width: 100%">
""",

    top_html="""\
""",
    )


Release(
    prerelease=False,
    invisible=False,
    version="6.99.6",
    prerelease_date="September 14, 2015",
    date="September 14, 2015",
    patch=None,
    patch_date=None,
    name="Here's to the crazy ones.",
    exe=34,
    bz2=48,
    zip=52,
    powerpc=False,
    world_order=6,
    announcement="""\
I'm pleased to announce Ren'Py 6.99.6. This is the latest in a series of
releases that introduce the new features that will make up Ren'Py 7.

The 6.99.6 release:

* Has much better support for high-resolution displays. Retina displays are now supported
  on Mac OS X and iOS - the latter support was broken by 6.99.5. On all platforms,
  Ren'Py will try to render text at the display resolution, rather than the game's
  resolution. This means that text should remain sharp even as the window is scaled up.

* Joystick support has been removed from Ren'Py, and replaced with gamepad
  support based on SDL2's new controller API. This API maps all sorts of gamepads
  to an Xbox-style controller, making standard bindings possible in the same way
  such bindings are possible for a keyboard and mouse.

* Ren'Py now automatically backs up .rpy files when a game changes. These script
  files are backed up to the system-wide save directory.

This release also includes a number of other fixes and improvements.

We'd like to thank Patrick Dawson for writing much of the code of Pygame_SDL2,
a new, SDL2-based implementation of the Pygame API, and Chris Mear, who created
the initial iOS port of Ren'Py that our current support is based on. Other
contributors include:

* Asfdfdfd
* Baekansi
* Bbs3223474
* Beuc
* Caryoscelus
* Daniel Luque
* Denzil
* Diapolo10
* Evilantishad0w
* Giuseppe Bertone
* Huang Junjie
* Javimat
* Konstantin Nikolayev
* Kyouryuukunn
* Lapalissiano
* Nolanlemahn
* Renoa
* RangHo Lee
* rivvil
* Tlm-2501
* Zigmut

and myself, Tom "PyTom" Rothamel.
""",

    history="""\
The history of older Ren'Py 6.99 releases can be found at

  http://www.renpy.org/release/6.99.5

and

  http://www.renpy.org/release/6.99
""",

    full_html="""\
<img src="/static/6.99.jpg" alt="Screenshot of Ren'Py 6.17" style="width: 100%">
""",

    top_html="""\
""",
    )

Release(
    prerelease=False,
    invisible=False,
    version="6.99.5",
    prerelease_date="July 16, 2015",
    date="July 19, 2015",
    patch=None,
    patch_date=None,
    name="Here's to the crazy ones.",
    exe=34,
    bz2=48,
    zip=52,
    powerpc=False,
    world_order=6,
    announcement="""\
I'm pleased to announce Ren'Py 6.99.5. This is the latest in a series of
releases that introduce the new features that will make up Ren'Py 7.

The 6.99.5 release focuses on mobile platforms. It massively improved
startup time, which helps all platforms, but is especially important
on the slower mobile devices. It also improves support for iOS 8, and
has other fixes an improvements.

We'd like to thank Patrick Dawson for writing much of the code of Pygame_SDL2,
a new, SDL2-based implementation of the Pygame API, and Chris Mear, who created
the initial iOS port of Ren'Py that our current support is based on. Other
contributors include:

* Asfdfdfd
* Baekansi
* Bbs3223474
* Beuc
* Caryoscelus
* Daniel Luque
* Denzil
* Diapolo10
* Evilantishad0w
* Giuseppe Bertone
* Huang Junjie
* Javimat
* Konstantin Nikolayev
* Kyouryuukunn
* Lapalissiano
* Nolanlemahn
* Renoa
* RangHo Lee
* rivvil
* Tlm-2501
* Zigmut

and myself, Tom "PyTom" Rothamel.
""",

    history="""\
The history of older Ren'Py 6.99 releases can be found at

  http://www.renpy.org/release/6.99
""",

    full_html="""\
<img src="/static/6.99.jpg" alt="Screenshot of Ren'Py 6.17" style="width: 100%">
""",

    top_html="""\
""",
    )


Release(
    prerelease=False,
    invisible=False,
    version="6.99",
    prerelease_date="March 19, 2015",
    date="March 25, 2015",
    patch=4,
    patch_date="May 27, 2015",
    name="Here's to the crazy ones.",
    exe=34,
    bz2=48,
    zip=52,
    powerpc=False,
    world_order=6,
    announcement="""\
I'm pleased to announce Ren'Py 6.99 "Here's to the crazy ones." This release
focuses on modernizing Ren'Py by moving to the SDL2 family of libraries. This
modernization will lead to a series of benefits, both now and in the future.

This release is being managed as a rolling release leading to Ren'Py 7.0.
New features may be added in point releases.

Perhaps the most obvious benefit is the addition of iOS support. Ren'Py can
now produce iOS apps, targeting iPhone and iOS devices. To develop for iOS,
you will need a Macintosh computer and paid iOS developer license, and will
need to customize the interface to conform to iOS policies.

In addition, this release includes:

* Rewritten Android support, based on SDL2. Among other things, Android now
  supports the onscreen keyboard, rotating the screen, and bidirectional text.
* Audio playback, using the same code on desktop and mobile platforms, so the
  same audio files can be used on all platforms Ren'Py supports.
* Support for Input Methods (IMEs), allowing text entry in non-English languages.
* A high-level achievement API, including support for Steam achievements. (Steam
  support will be made available on request to Steam developers.)
* Improved support for custom text tags.
* A Russian translation of the tutorial game, and a Finnish translation of
  the launcher.

To this, the 6.99.2 release adds:

* Support for the images directory. Image files placed into this directory
  are automatically defined as images in Ren'Py,
* The new AlphaMask displayable, which allows the alpha channel of one
  displayable to be masked by that of another.

The 6.99.4 release adds:

* The new default statement, which is used to set the initial value of a
  variable in a game.
* Support for the transclusion of screen language code inside use statements,
  and support for creator-defined screen language statements.

The 6.99.5 release adds:

* Much faster startup, especially on mobile platforms.
* Better support for iOS 8.
* Many other small features.

These releases also include a number of other fixes and improvements.

We'd like to thank Patrick Dawson for writing much of the code of Pygame_SDL2,
a new, SDL2-based implementation of the Pygame API, and Chris Mear, who created
the initial iOS port of Ren'Py that our current support is based on. Other
contributors include:

* Asfdfdfd
* Baekansi
* Bbs3223474
* Beuc
* Caryoscelus
* Daniel Luque
* Denzil
* Diapolo10
* Evilantishad0w
* Giuseppe Bertone
* Huang Junjie
* Javimat
* Konstantin Nikolayev
* Kyouryuukunn
* Lapalissiano
* Nolanlemahn
* Renoa
* RangHo Lee
* rivvil
* Tlm-2501
* Zigmut

and myself, Tom "PyTom" Rothamel.
""",

    history="""\
**6.99.5.602**: July 19, 2015
    This release improves startup time, improves iOS 8 support, and
    includes other improvements and fixes.

**6.99.4.467**: May 27, 2015
    This release adds new features. It also fixes a number of bugs and
    performance problems.

**6.99.3.404**: April 26, 2015
    This removes extraneous code that was causing problems.

**6.99.2.403**: April 25, 2015
    This release adds new features, including the images directory and the
    AlphaMask displayable. It also fixes bugs.

**6.99.1.329**: March 29, 2015
    This release fixes crashes that occurred in a number of important cases,
    including non-ASCII directory names on Windows systems, 16-bit display
    depths, and display rotation when targeting recent versions of Android.

    It also fixes several non-crash bugs, adds three new functions, and
    updates the Spanish and Japanese translations.
""",

    full_html="""\
<img src="/static/6.99.jpg" alt="Screenshot of Ren'Py 6.17" style="width: 100%">
""",

    top_html="""\
""",
    )


Release(
    prerelease=False,
    invisible=False,
    version="6.18",
    prerelease_date="August 24, 2014",
    date="September 12, 2014",
    patch=3,
    patch_date="October 21, 2014",
    name="... through shared popular culture.",
    exe=31,
    bz2=44,
    zip=48,
    android=True,
    powerpc=False,
    deps="6.17.0",
    world_order=5,
    announcement="""\
I'm pleased to announce Ren'Py 6.18 "... through shared popular culture.". Major
improvements in this release include:

* A full rewrite of screen language that has the potential for significantly
  improved performance.
* Self-voicing support that provides a level of accessibility to blind
  users.
* A high-level Android in-app purchasing framework.
* New Italian, Portuguese, Simplified Chinese, and Traditional Chinese
  translations, and a new German template.

This release also includes many other features and fixes. It has been brought
to you by:

* Koichi Akabe
* Civalin
* Duanemoody
* Helloise
* Huanxuantian
* Daniel Luque
* Javimat
* Kyouryuukunn
* Emmannuel Marty
* Mrstalker
* Mugenjohncel
* Nojoker
* Oshi-Shinobu
* Renoa
* Tom "PyTom" Rothamel
* Shiz
* Winter Wolves
""",

    history="""\
**6.18.3.761**:
    This release improves prediction, adds the new screen language "showif"
    statement, adds minor features, and fixes bugs.

**6.18.2.729**:
    This release adds many small new features, and fixes several minor bugs.
    It also adds the Traditional Chinese translation.

**6.18.1.670**: September 22, 2014
    This release fixes a number of bugs in Ren'Py 6.18. It changes ATL behavior
    so that an ATL transform that is part of a screen will begin executing when
    the transform (rather than the screen) is first shown. It also adds a new
    placeholder image system, and a way to speak descriptive text as part of
    the self-voicing process.
""",

    full_html="""\
""",

    top_html="""\
""",
    )


Release(
    prerelease=False,
    invisible=False,
    version="6.17",
    prerelease_date="February 15, 2014",
    date="February 20, 2014",
    patch=7,
    patch_date="July 6, 2014",
    name="In This Decade...",
    exe=28,
    bz2=36,
    zip=39,
    android=True,
    powerpc=False,
    deps="6.17.0",
    world_order=5,
    announcement="""\
As we reach the tenth anniversary of the start of Ren'Py development,
I'm pleased to announce Ren'Py 6.17 "In This Decade...". Major improvements
in this release include:

* A rewrite of the Style system that should improve Ren'Py's performance.
* A new style statement that makes it easier to define styles.
* A rewritten shift+I style inspector lets you view those styles.
* A new "show layer" statement that makes it convenient to apply transforms
  and ATL transforms to entire layers at once.
* A new "window auto" statement that enables automatic management of the
  dialogue window.
* Several other syntax improvements.
* French and Russian translations.
* The integration of RAPT (the Ren'Py Android Packaging Tool) with the
  Ren'Py SDK. Ren'Py now downloads RAPT using the Ren'Py updater - it's
  no longer necessary to download RAPT separately.

This release also includes several other new functions and actions, and
major bugfixes that affect the Android platform.

This release has been brought to you by:

* Koichi "vbkaisetsu" Akabe
* CensoredUsername (C)
* kyouryuukunn
* Daniel Luque
* Renoa
* Tom "PyTom" Rothamel
* tlm-2501
""",

    history="""\
**6.17.7.521**: July 6, 2014
    This release updates the Android SDK to a working version, adds a low-level
    in-app purchasing framework, and fixes an issue with movie playback on
    desktop platforms.

**6.17.6.512**: May 7, 2014
    This release adds new German and Korean translations, and works around
    a bug that prevented the Ren'Py launcher from starting on certain macs.

**6.17.5.492**: May 1, 2014
    This release adds a new Arabic translation, and updates the Japanese and
    Spanish translations. It also fixes several bugs affecting the shift+R
    reload functionality, and provides several new features.

**6.17.4.409**: April 16, 2014
    This release fixes problems with Android (especially ones caused by a missing
    play licensing library), adds support for the Amazon Fire TV console, allows imagemaps
    in viewports, and prevents large memory leaks from occurring when shift+R is pressed.

**6.17.3.327**: March 4, 2014
    This release fixes a bug where Ren'Py would misparse properties and
    attributes that began with a Python operator. (For example, ``insensitive``,
    which begins with ``in``.) It also rewrites the missing image code to use
    styles and screens.

**6.17.2.319**: February 28, 2014
    This release adds a new "translate <i>language</i> style <i>style_name</i>"
    statement, which is used to customize styles in a particular language. It
    also improves scanning the projects directory and fixes various other
    issues.

**6.17.1.309**: February 24, 2014
    This release fixes a problem where an update could overwrite a file in
    the RAPT directory, preventing builds. It also updates and improves
    translations, and deals gracefully with improperly encoded files in
    the projects directory.
""",

    full_html="""\
<img src="/static/6.17.jpg" alt="Screenshot of Ren'Py 6.17">
""",

    top_html="""\
""",
    )


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
