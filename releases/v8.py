# Release data for Ren'Py 8.4 and later, newest first.

from model import *

# A new x.y series starts with a Series("x.y", ...) above its first Release, holding the fields shared by every
# release in the series (name, world_order, notes, credits, ...). See 8.6 below.

# Private Prerelease checklist:
#
# 1. prerelease=True
# 2. invisible=True
# 3. version
# 4. patch=0
# 5. patch_date=None
# 6. name (on the Series, for a series that has one)
# 7. sizes
# 8. -
# 9. announcement.

# Patch release checklist:
#
# 1. Bump patch.
# 2. Update patch_date.
# 3. Write changes. (From 8.6 on: a release-note-level list of the changes in this release.)

# Final release checklist:
#
# 1. Bump date.
# 2. prerelease=False

# The release steps (scripts, website, socials) are a checklist on /releasenotes, which also has the announcement
# text to copy.

# To get the list of contributors to a release, we can use the command:
# git shortlog 8.5.0.25111603..HEAD | grep -v ^\\s | sort -i | uniq


# 8.6.0 ################################################################################################################ Copyright 2004-2026 Tom Rothamel <pytom@bishoujo.us>


COMMON_8_6 = """

The major features and improvements in Ren'Py 8.6 include:

**SDL3.** Perhaps the biggest change in Ren'Py 8.6 is the move to SDL3, the newest version of the Simple DirectMedia Layer library, which provides low-level access to audio, keyboard, mouse, controller and graphics hardware. SDL3 is where new platform support is being developed, so this lets Ren'Py take advantage of new hardware and operating systems. It also brings high-DPI support on Windows and support for the Nintendo Switch Pro Controller.

**Performance.** Ren'Py's prediction system has been rewritten to use Python coroutines, which are small functions that can be interrupted in the middle, so prediction can be split into chunks that fit inside a single frame. Ren'Py 8.6 eliminates the need to design pauses into your animation to allow prediction, as prediction can now occur seamlessly as animations play. Images are decoded on multiple threads, texture uploads are spread across frames, redundant drawing work is skipped, and shaders are compiled ahead of time and cached across launches.

**Accessibility.** A new screen reader mode, toggled with Shift+V, uses the Prism library to talk directly to screen readers like NVDA, JAWS, VoiceOver, and Orca, presenting the game's text through speech and braille displays. It turns on automatically when a screen reader is running. Self-voicing can now use any voice installed on the user's system, at an adjustable speed.

**Shaders.** Shader parts can now be written in GLSL ES 3.00, the default for new games. Existing shaders don't need to change, as Ren'Py translates between versions automatically, and parts written in either version can be combined.

**Live2D.** Ren'Py's Live2D support has been updated to support the blend modes and offscreen drawing of Cubism 5.3. Ren'Py also now supports Live2D physics and pose files, allowing for more dynamic and expressive character animations.

Other new features include:

* On Windows, Ren'Py draws input method candidate lists itself, so they're visible in fullscreen games.
* Warping to a line now replays the dialogue along the way, rebuilding the history, NVL-mode text, and speech bubbles.
* Automated tests can be selected with wildcards and parameters, and more test statements accept expressions.
* New clipboard functions allow games to work with text, data, and images on the system clipboard. Screenshots are automatically copied to the clipboard.
* The new renpy.get_user_age function reports the user's age range on Android and iOS devices that support it.
* Ren'Py supports wavedash.com, a platform and marketplace for web-based games, and the launcher can upload to it directly.
* Different languages can be set for strings and files, so you could have one language for text, another for audio, and yet another for images.
* It's now possible to seek in music, and loop in movies.
* It's now possible to specify more than one directory to search for images, audio, and/or fonts.
* Font sizes can be adjusted per-font, without editing the font files.
* Files created when a new project is made are now dedicated to the public domain.

There are also dozens of other features and fixes, please refer to the full changelog for a complete list.

Ren'Py 8.6 raises some system requirements. iOS games now require iOS 15 or later, up from iOS 13, and macOS games now require macOS 10.13 or later, up from macOS 10.10. On Android, iOS, and the web, Ren'Py now requires a GPU that supports OpenGL ES 3.0, which most devices with a GPU from 2013 or later have. Desktop requirements are unchanged: Ren'Py uses OpenGL 3.3 when it's available, and falls back to OpenGL 2.0. The new Live2D features require Cubism SDK for Native 5-r.5 or later, but older versions continue to work without them.

Ren'Py 8.6 is the next step in our goal of providing tools that enable human creativity in the form of visual novels and similar styles
of games. I'm proud to announce that more people than ever have contributed to this release of Ren'Py. Thanks to everyone that has contributed to this release, and to those of you who will create with it.
"""

CREDITS_8_6 = """
A-Voski (4):
Aarushbbh (23):
Andy_kl (278):
Arsym (40):
Atlas Cove (3):
AxelBeary (2):
Ayowel (4):
Bkats (21):
Chris Bier (1):
Cosumicu (1):
Devon Lewis (1):
Dipesh Aggarwal (2):
DublikuntMux (3):
Elckarow (11):
Erik Chou (8):
Estelle Booher (1):
Felipe Carvajal Brown (1):
Galo223344 (1):
Gio (1):
Gouvernathor (1):
HB38 (9):
Hsandt (1):
Izarii-dev (11):
Jacob Grady (1):
Jed (3):
Joey luu (1):
Juhani Krekelä (1):
juperMonkey (2):
Kassy (1):
Kayenuonuo (1):
Kyouryuukunn (3):
Kyuiazusa (2):
LaUwUrence (1):
loviuz (4):
Mal Graty (14):
Matt Murdock (1):
Merilynn Paisley (2):
Moshibit (14):
Mubashir78 (1):
Naughty Road (1):
Neyunse (10):
Nora Lua (1):
Npckc (1):
OneCrisisAtATime (2):
Peder Bergan (4):
River (1):
Rodrigo Oliveira (2):
Ronchonbon (108):
Rose20 (3):
Saamkhaih Kyakya (5):
Sab Pyrope (1):
Saki (1):
TDCMC (2):
The66F95 (5):
Tichq (7):
Totally a booplicate (1):
Ulysses Zhan (4):
Veydzh3r (3):
VivianTu789 (1):
Yorkyang2333 (16):
Zaveshaa (8):
"""

Series(
    "8.6",
    name="Real Artists Ship",
    world_order=16,
    notes=COMMON_8_6,
    credits=CREDITS_8_6,
    extra_credits="'Real Artists Ship' is inspired by a story from <a href=\"https://folklore.org/Real_Artists_Ship.html\">folklore.org</a>.",
    top_html='<img src="/static/8.6.jpg" alt="" style="width: 100%">',
    full_html="",
    deprecations="",
)

Release(
    prerelease=True,
    invisible=False,
    version="8.6.1",
    date="November xx, 2026",
    patch=None,
    announcement="""
I'd like to announce Ren'Py 8.6.1, a fix release of Ren'Py 8.6. This fixes a single issue with downloading Visual Studio Code from the launcher.
""",
    changes="""
* Fixed downloading Visual Studio Code from the launcher by ensuring that the public key the downloader signatures rely on is properly supported. (#7522)
""",
)

Release(
    prerelease=False,
    invisible=False,
    version="8.6.0",
    date="November 14, 2026",
    patch=None,
    announcement="""
I'm happy to announce the release of Ren'Py 8.6, a feature release of Ren'Py that is the result of a year of work to add new features, fixes, optimizations, and other improvements.
""",
)


# 8.5.0 ################################################################################################################ Copyright 2004-2024 Tom Rothamel <pytom@bishoujo.us>


COMMON_8_5 = """

Some of the major changes in Ren'Py 8.5 are:

* Live2D models are now supported on the Web platform.
* A new Automated Testing framework makes it possible to perform automated tests of games and of Ren'Py itself.
* Local labels have been relaxed so that they can be declared with any global label.
* Ren'Py supports Unicode 17 and more Emoji characters.

As well as many other improvements, changes, and fixes. For a complete list of changes, please see the changelog.
"""

CREDITS_8_5 = """
aliengeo (1):
Andy_kl (48):
Arsym (110):
Atlas Cove (1):
bkats (1):
Devon Lewis (1):
Dipesh Aggarwal (3):
dynamiclinking (1):
Elckarow (5):
Galo223344 (1):
Gouvernathor (1):
HB38 (11):
juperMonkey (2):
Kassy (1):
levicratic (1):
LoafyLemon (1):
loviuz (2):
Mal Graty (11):
NaughyRoad (1):
Rastagong (1):
River (1):
Rodrigo Oliveira (1):
Rose20 (1):
Ruben Garcia (1):
TDCMC (15):
the66F95 (5):
Totally a booplicate (1):
Ulysses Zhan (2):
veydzh3r (3):
VivianTu789 (1):
Vladya (1):
"""

Release(
    prerelease=False,
    invisible=False,
    version="8.5.3",
    date="May 15, 2026",
    patch=None,
    name="We Can Go to the Moon",
    world_order=15,
    announcement="""
I'd like to announce Ren'Py 8.5.3, a fix release of Ren'Py 8.5. This release fixes multiple issues, adds a few small features,
and improves documentation. It also adds and updates translations of the tutorial games. Ren'Py now supports and requires
Live2D 5.3 when Live2D is in use.
""" + COMMON_8_5,
    history="",
    full_html="",
    # top_html='<img src="/static/8.4.jpg" alt="" style="width: 100%">',
    top_html="",
    deprecations="",
    credits=CREDITS_8_5,
    extra_credits=""
)



Release(
    prerelease=False,
    invisible=False,
    version="8.5.2",
    date="January 3, 2026",
    patch=None,
    name="In Good Health",
    world_order=15,
    announcement="""
I'd like to announce Ren'Py 8.5.2, a fix release of 8.5.1. This release fixes a single issue in Ren'Py 8.5.1.
""" + COMMON_8_5,
    history="",
    full_html="",
    # top_html='<img src="/static/8.4.jpg" alt="" style="width: 100%">',
    top_html="",
    deprecations="",
    credits=CREDITS_8_5,
    extra_credits=""
)


Release(
    prerelease=False,
    invisible=False,
    version="8.5.1",
    date="December 31, 2025",
    patch=None,
    name="In Good Health",
    world_order=15,
    announcement="""
I'm happy to ring in the new year with the release of Ren'Py 8.5.1, a fix release of Ren'Py 8.5. This release addresses
multiple reported issues.
""" + COMMON_8_5,
    history="",
    full_html="",
    # top_html='<img src="/static/8.4.jpg" alt="" style="width: 100%">',
    top_html="",
    deprecations="",
    credits=CREDITS_8_5,
    extra_credits=""
)


Release(
    prerelease=False,
    invisible=False,
    version="8.5.0",
    date="November 16, 2025",
    patch=None,
    name="In Good Health",
    world_order=15,
    announcement="""
I'm pleased to announce the release of Ren'Py 8.5, a major release of Ren'Py. Major releases include new features,
major improvements, and fixes.
""" + COMMON_8_5,
    history="",
    full_html="",
    # top_html='<img src="/static/8.4.jpg" alt="" style="width: 100%">',
    top_html="",
    deprecations="",
    credits=CREDITS_8_5,
    extra_credits=""
)



# 8.4.0 ################################################################################################################ Copyright 2004-2024 Tom Rothamel <pytom@bishoujo.us>


COMMON_8_4 = """
Some of the new features and improvements Ren'Py 8.4 are:

* Ren'Py now utilizes Python 3.12 across all platforms.
* Performance has been improved in script loading, persistent data management, OpenGL drawing, and Live2D integration.
* OpenGL shader support is enhanced, now including more data types, arrays, separate projection, view, and model
  matrices. It also allows for displayables to be supplied to shaders as textures.
* Ren'Py now supports the loading of GLTF models. Currently, only static models are supported, and a custom shader is
  required for rendering.
* The new ``libs`` and ``mods`` directories allow for the organized placement of libraries and mods with an adjusted loading
  order.
* The layered images sub-language has been updated to be more concise and powerful.
* Oversampled images—higher-resolution assets for upscaling and high-DPI displays—are now selected automatically.
  Movies also support oversampling.
* The Shift+A accessibility menu has been redesigned to include options for adjusting text kerning and forcing mono
  audio output.
* The launcher now supports the organization of projects into folders and allows for the customization of which files
  and directories are displayed.
* Ren'Py now supports OpenType features, enabling the use of ligatures, stylistic sets, and other typographic
  enhancements.
* When a traceback error occurs, the game's state is automatically saved. This save file can be sent to teammates to
  help diagnose the issue.

As well as many other improvements, changes, and fixes. For a complete list of changes, please see the changelog.

Ren'Py 8.4 increases the minimum system requirements for Ren'Py and games. The Windows version now requires Windows 10 or
later. Linux now requires Ubuntu 20.04 or later, the Steam "soldier" runtime, or a similar Linux distribution. 32-bit ARM
Linux is no longer supported.

Finally, Ren'Py 8.4 is now the sole supported version of Ren'Py - there is not an equivalent Ren'Py 7 release that uses
Python 2.
"""

CREDITS_8_4 = """
Abdul (4):
Andy_kl (83):
Arman (1):
avonder (2):
Ayowel (7):
brimbel (2):
Craig de Stigter (2):
Dipesh Aggarwal (6):
Doohyeon Won (1):
dm1sh (1):
Edward Nicholes Jr. (2):
Elckarow (11):
Emmanuel Ferdman (1):
Farzher (2):
Gio (6):
Gouvernathor (55):
Gregor Riepl (5):
HB38 (1):
Jade Macho (2):
jamaine (1):
Jaybe Games (1):
Joshua Fehler (5):
Kassy (6):
lauwurence (1):
levicratic (2):
Lezalith (12):
Mal Graty (49):
Mark (4):
Matěj Račinský (1):
Moshibit (4):
naughty road (6):
nullvoid8 (1):
Opolis13 (2):
Peter Dave Hello (1):
Puxap-3opre (1):
Quetz (5):
Ruben Garcia (3):
shawna-p (2):
Stanislau Tsitsianok (1):
Sunrise Sarsaparilla (2):
TDCMC (3):
the66F95 (20):
Tichq (3):
tinyboxvk (1):
veydzh3r (4):
Vladya (3):
woolion (2):
"""


Release(
    prerelease=False,
    invisible=False,
    version="8.4.1",
    pygame="-2.1.0",
    date="July 24, 2025",
    patch=None,
    name="Tomorrowland",
    world_order=14,
    announcement="""
I'm happy to announce the release of Ren'Py 8.4.1. This release is a fix release that addresses multiple issues,
including a problem that prevented creators on Windows from creating new games in non-English languages.
""" + COMMON_8_4,
    history="",
    full_html="",
    top_html='<img src="/static/8.4.jpg" alt="" style="width: 100%">',
    deprecations="",
    credits=CREDITS_8_4,
    extra_credits="""
<p>I'd like to give a special thank you to Mal Graty, who contributed most of the fixes in this release.</p>
""")




# 8.4.0

Release(
    prerelease=False,
    invisible=False,
    version="8.4.0",
    pygame="-2.1.0",
    date="July 12, 2025",
    patch=None,
    name="Tomorrowland",
    world_order=14,
    announcement="""
I'm happy to announce the release of Ren'Py 8.4, a feature release that includes many new features,
fixes, and improvements to Ren'Py.

""" + COMMON_8_4,
    history="",
    full_html="",
    top_html='<img src="/static/8.4.jpg" alt="" style="width: 100%">',
    deprecations="",
    credits=CREDITS_8_4)
