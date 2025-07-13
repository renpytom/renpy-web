# coding=utf-8
# This file contains data about Ren'Py, and its various
# releases. Think of it as a kind of database, except that it's stored
# as code rather than as data.

from model import *

# A list of releases. This is automatically filled up when we execute the
# Release and WikiRelease statement-commands, below.
releases = [ ]

# All aliases.
aliases = [ ]

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
# git shortlog 7.0..HEAD


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




# 8.3.0 / 7.8.0 ##############################################################

COMMON_8_3 = """
Ren'Py 8.3 and Ren'Py 7.8 are joint releases that add many new features,
fixes, and improvements to Ren'Py. The two biggest features are:

* Audio Filters, a system for processing audio in real-time, allowing for
  effects like high-pass and low-pass filters, reverb, and more.
* Text shaders, which allow GLSL shaders to be applied to text. These allow
  for many text effects that were not possible, and make it possible to replace
  the default typewriter slow-text effect with other options, like a moving
  dissolve.

Some of the other changes are:

* Improvements to shaders, including shader-part local variables that make it easier to combine
  shaders.
* Changes and improvements to the ``window`` statements to give better control over window
  management.
* New functions that make it possible to screenshot displayable (for example, a layered image that
  contains a paper doll) and save that screenshot to a file.
* Updated Steam support, including new support for the Steam Timeline.
* Ren'Py's Android support now targets Android 15 (API Level 35).
* Ren'Py's Android support now supports sizes of up to 4GB on Google Play.
* Retained speech bubbles are now automatically cleared when appropriate.

As well as many other fixes, changes, and improvements. Please see the changelog for a complete list of changes.
"""

CREDITS_8_3 = """
Abdul (4):
Aleksandar Belic Aleksanchez (1):
Alexandre Detiste (1):
Andrej Klychin (1):
Andy_kl (6):
avonder (1):
Ayowel (2):
Bas Couwenberg (1):
Brainos (1):
brimbel (2):
CensoredUsername (1):
Chengtian He (1):
Craig de Stigter (1):
Denys (14):
Dipesh Aggarwal (5):
do10HM (1):
Edward Nicholes Jr. (1):
Elckarow (2):
Gio (1):
Gouvernathor (58):
HB38 (1):
iivusly (1):
ImJustAQ (1):
Jan Masek (1):
Kassy (3):
Kuro (1):
kyouryuukunn (10):
Lent1 (2):
levicratic (3):
luejerry (1):
Mal Graty (4):
Mark (2):
m-from-space (7):
minger0 (1):
naughty road (3):
npckc (1):
nullvoid8 (1):
octospacc (1):
OleSTEEP (1):
Petr Abdulin (1):
Ruben Garcia (1):
shawna-p (4):
the66F95 (6):
TDCMC (1):
Tichq (8):
veydzh3r (1):
Viktoras Agejevas (1):
woolion (1):
"""

# 8.3.7 / 7.8.7

Release(
    prerelease=False,
    invisible=False,
    version="8.3.7",
    pygame="-2.1.0",
    date="March 17, 2025",
    patch=None,
    name="Second Star to the Right",
    world_order=14,
    announcement="""\
I'm happy to announce the release of Ren'Py 8.3.7, a fix release that improves earlier versions of Ren'Py 8.3.
This release fixes multiple reported issues, with a focus on Live2D and Arabic text shaping.

Ren'Py 8.3 should be used for all new games.
""" + COMMON_8_3,
    history="""\
""",

    full_html="""\
""",
top_html="""\
""",

deprecations="""\
The original OpenGL renderer will be removed in the next major release.

Support for Windows 7, 8, and 8.1 will be dropped in the next major release.
""",

credits=CREDITS_8_3)


Release(
    prerelease=False,
    invisible=False,
    version="7.8.7",
    pygame="-2.1.0",
    date="March 17, 2025",
    patch=None,
    name="Straight on Till Morning",
    world_order=14,
    announcement="""\
I'm happy to announce the release of Ren'Py 7.8.7, a fix release that improves earlier versions of Ren'Py 7.8.
This release fixes multiple reported issues, with a focus on Live2D and Arabic text shaping.

The Ren'Py 7 series attempts to match Ren'Py 8 in features, while retaining support for Python 2.
As some of the new features require Python 3 support, not every new feature in Ren'Py 8 is available in Ren'Py 7.
As Ren'Py 7.8 will be the last major release in the 7.x series, all games should be updated to Ren'Py 8 before
the release of Ren'Py 8.4, when support for Ren'Py 7 will end.
""" + COMMON_8_3,
    history="""\
""",
    full_html="""\
""",
top_html="""\
""",

deprecations="""\
Support for Python 2 and Ren'Py 7 will be dropped in the next major release.
""",

credits=CREDITS_8_3)



# 8.3.6 / 7.8.6

Release(
    prerelease=False,
    invisible=False,
    version="8.3.6",
    pygame="-2.1.0",
    date="February 28, 2025",
    patch=None,
    name="Second Star to the Right",
    world_order=14,
    announcement="""\
I'm happy to announce the release of Ren'Py 8.3.6, a fix release that improves earlier versions of Ren'Py 8.3.

Ren'Py 8.3 should be used for all new games.
""" + COMMON_8_3,
    history="""\
""",

    full_html="""\
""",
top_html="""\
""",

deprecations="""\
The original OpenGL renderer will be removed in the next major release.

Support for Windows 7, 8, and 8.1 will be dropped in the next major release.
""",

credits=CREDITS_8_3)


Release(
    prerelease=False,
    invisible=False,
    version="7.8.6",
    pygame="-2.1.0",
    date="February 28, 2025",
    patch=None,
    name="Straight on Till Morning",
    world_order=14,
    announcement="""\
I'm happy to announce the release of Ren'Py 7.8.6, a fix release that improves earlier versions of Ren'Py 7.8.
The Ren'Py 7 series attempts to match Ren'Py 8 in features, while retaining support for Python 2.
As some of the new features require Python 3 support, not every new feature in Ren'Py 8 is available in Ren'Py 7.

As Ren'Py 7.8 will be the last major release in the 7.x series, all games should be updated to Ren'Py 8 before
the release of Ren'Py 8.4, when support for Ren'Py 7 will end.
""" + COMMON_8_3,
    history="""\
""",
    full_html="""\
""",
top_html="""\
""",

deprecations="""\
Support for Python 2 and Ren'Py 7 will be dropped in the next major release.
""",

credits=CREDITS_8_3)



# 8.3.5 / 7.8.5

Release(
    prerelease=False,
    invisible=False,
    version="8.3.5",
    pygame="-2.1.0",
    date="February 28, 2025",
    patch=None,
    name="Second Star to the Right",
    world_order=14,
    announcement="""\
I'm happy to announce the release of Ren'Py 8.3.5, a fix release that improves earlier versions of Ren'Py 8.3.

Ren'Py 8.3 should be used for all new games.
""" + COMMON_8_3,
    history="""\
""",

    full_html="""\
""",
top_html="""\
""",

deprecations="""\
The original OpenGL renderer will be removed in the next major release.

Support for Windows 7, 8, and 8.1 will be dropped in the next major release.
""",

credits=CREDITS_8_3)


Release(
    prerelease=False,
    invisible=False,
    version="7.8.5",
    pygame="-2.1.0",
    date="February 28, 2025",
    patch=None,
    name="Straight on Till Morning",
    world_order=14,
    announcement="""\
I'm happy to announce the release of Ren'Py 7.8.5, a fix release that improves earlier versions of Ren'Py 7.8.
The Ren'Py 7 series attempts to match Ren'Py 8 in features, while retaining support for Python 2.
As some of the new features require Python 3 support, not every new feature in Ren'Py 8 is available in Ren'Py 7.

As Ren'Py 7.8 will be the last major release in the 7.x series, all games should be updated to Ren'Py 8 before
the release of Ren'Py 8.4, when support for Ren'Py 7 will end.
""" + COMMON_8_3,
    history="""\
""",
    full_html="""\
""",
top_html="""\
""",

deprecations="""\
Support for Python 2 and Ren'Py 7 will be dropped in the next major release.
""",

credits=CREDITS_8_3)


# 8.3.4 / 7.8.4

Release(
    prerelease=False,
    invisible=False,
    version="8.3.4",
    pygame="-2.1.0",
    date="December 8, 2024",
    patch=None,
    name="Second Star to the Right",
    world_order=14,
    announcement="""\
I'm happy to announce the release of Ren'Py 8.3.4, a fix release that improves earlier versions of Ren'Py 8.3.

Ren'Py 8.3 should be used for all new games.
""" + COMMON_8_3,
    history="""\
""",

    full_html="""\
""",
top_html="""\
""",

deprecations="""\
The original OpenGL renderer will be removed in the next major release.

Support for Windows 7, 8, and 8.1 will be dropped in the next major release.
""",

credits=CREDITS_8_3)


Release(
    prerelease=False,
    invisible=False,
    version="7.8.4",
    pygame="-2.1.0",
    date="December 8, 2024",
    patch=None,
    name="Straight on Till Morning",
    world_order=14,
    announcement="""\
I'm happy to announce the release of Ren'Py 7.8.4, a fix release that improves earlier versions of Ren'Py 7.8.
The Ren'Py 7 series attempts to match Ren'Py 8 in features, while retaining support for Python 2.
As some of the new features require Python 3 support, not every new feature in Ren'Py 8 is available in Ren'Py 7.

As Ren'Py 7.8 will be the last major release in the 7.x series, all games should be updated to Ren'Py 8 before
the release of Ren'Py 8.4, when support for Ren'Py 7 will end.
""" + COMMON_8_3,
    history="""\
""",
    full_html="""\
""",
top_html="""\
""",

deprecations="""\
Support for Python 2 and Ren'Py 7 will be dropped in the next major release.
""",

credits=CREDITS_8_3)



# 8.3.3 / 7.8.3

Release(
    prerelease=False,
    invisible=False,
    version="8.3.3",
    pygame="-2.1.0",
    date="November 15, 2024",
    patch=None,
    name="Second Star to the Right",
    world_order=14,
    announcement="""\
I'm happy to announce the release of Ren'Py 8.3.3, a fix release that improves earlier versions of Ren'Py 8.3.

Ren'Py 8.3 should be used for all new games.
""" + COMMON_8_3,
    history="""\
""",

    full_html="""\
""",
top_html="""\
""",

deprecations="""\
The original OpenGL renderer will be removed in the next major release.

Support for Windows 7, 8, and 8.1 will be dropped in the next major release.
""",

credits=CREDITS_8_3)


Release(
    prerelease=False,
    invisible=False,
    version="7.8.3",
    pygame="-2.1.0",
    date="November 15, 2024",
    patch=None,
    name="Straight on Till Morning",
    world_order=14,
    announcement="""\
I'm happy to announce the release of Ren'Py 7.8.3, a fix release that improves earlier versions of Ren'Py 7.8.
The Ren'Py 7 series attempts to match Ren'Py 8 in features, while retaining support for Python 2.
As some of the new features require Python 3 support, not every new feature in Ren'Py 8 is available in Ren'Py 7.

As Ren'Py 7.8 will be the last major release in the 7.x series, all games should be updated to Ren'Py 8 before
the release of Ren'Py 8.4, when support for Ren'Py 7 will end.
""" + COMMON_8_3,
    history="""\
""",
    full_html="""\
""",
top_html="""\
""",

deprecations="""\
Support for Python 2 and Ren'Py 7 will be dropped in the next major release.
""",

credits=CREDITS_8_3)




# 8.3.2 / 7.8.2

Release(
    prerelease=False,
    invisible=False,
    version="8.3.2",
    pygame="-2.1.0",
    date="September 9, 2024",
    patch=None,
    name="Second Star to the Right",
    world_order=14,
    announcement="""\
I'm happy to announce the release of Ren'Py 8.3.2, a fix release that improves earlier versions of Ren'Py 8.3.
This release fixes a build issue with 8.3.1 that prevented games from starting properly on Android.

Ren'Py 8.3 should be used for all new games.
""" + COMMON_8_3,
    history="""\
""",

    full_html="""\
""",
top_html="""\
""",

deprecations="""\
The original OpenGL renderer will be removed in the next major release.

Support for Windows 7, 8, and 8.1 will be dropped in the next major release.
""",

credits=CREDITS_8_3)


Release(
    prerelease=False,
    invisible=False,
    version="7.8.2",
    pygame="-2.1.0",
    date="September 9, 2024",
    patch=None,
    name="Straight on Till Morning",
    world_order=14,
    announcement="""\
I'm happy to announce the release of Ren'Py 7.8.2, a fix release that improves earlier versions of Ren'Py 7.8.
The Ren'Py 7 series attempts to match Ren'Py 8 in features, while retaining support for Python 2.
As some of the new features require Python 3 support, not every new feature in Ren'Py 8 is available in Ren'Py 7.

As Ren'Py 7.8 will be the last major release in the 7.x series, all games should be updated to Ren'Py 8 before
the release of Ren'Py 8.4, when support for Ren'Py 7 will end.
""" + COMMON_8_3,
    history="""\
""",
    full_html="""\
""",
top_html="""\
""",

deprecations="""\
Support for Python 2 and Ren'Py 7 will be dropped in the next major release.
""",

credits=CREDITS_8_3)





# 8.3.1 / 7.8.1

Release(
    prerelease=False,
    invisible=False,
    version="8.3.1",
    pygame="-2.1.0",
    date="September 7, 2024",
    patch=None,
    name="Second Star to the Right",
    world_order=14,
    announcement="""\
I'm happy to announce the release of Ren'Py 8.3.1, a fix release that improves earlier versions of Ren'Py 8.3,
and should be used for all new games.
""" + COMMON_8_3,
    history="""\
""",

    full_html="""\
""",
top_html="""\
""",

deprecations="""\
The original OpenGL renderer will be removed in the next major release.

Support for Windows 7, 8, and 8.1 will be dropped in the next major release.
""",

credits=CREDITS_8_3)


Release(
    prerelease=False,
    invisible=False,
    version="7.8.1",
    pygame="-2.1.0",
    date="September 7, 2024",
    patch=None,
    name="Straight on Till Morning",
    world_order=14,
    announcement="""\
I'm happy to announce the release of Ren'Py 7.8.1, a fix release that improves earlier versions of Ren'Py 7.8.
The Ren'Py 7 series attempts to match Ren'Py 8 in features, while retaining support for Python 2.
As some of the new features require Python 3 support, not every new feature in Ren'Py 8 is available in Ren'Py 7.

As Ren'Py 7.8 will be the last major release in the 7.x series, all games should be updated to Ren'Py 8 before
the release of Ren'Py 8.4, when support for Ren'Py 7 will end.
""" + COMMON_8_3,
    history="""\
""",
    full_html="""\
""",
top_html="""\
""",

deprecations="""\
Support for Python 2 and Ren'Py 7 will be dropped in the next major release.
""",

credits=CREDITS_8_3)



# 8.3.0 / 7.8.0

Release(
    prerelease=False,
    invisible=False,
    version="8.3.0",
    pygame="-2.1.0",
    date="August 22, 2024",
    patch=None,
    name="Second Star to the Right",
    world_order=14,
    announcement="""\
I'm happy to announce the release of Ren'Py 8.3, the result of months of development. Ren'Py 8.3.0 is a feature
release that adds many new features, fixes, and improvements to Ren'Py, and should be used for all new games.
""" + COMMON_8_3,
    history="""\
""",

    full_html="""\
""",
top_html="""\
""",

deprecations="""\
The original OpenGL renderer will be removed in the next major release.

Support for Windows 7, 8, and 8.1 will be dropped in the next major release.
""",

credits=CREDITS_8_3)


Release(
    prerelease=False,
    invisible=False,
    version="7.8.0",
    pygame="-2.1.0",
    date="August 22, 2024",
    patch=None,
    name="Straight on Till Morning",
    world_order=14,
    announcement="""\
I'm happy to announce the release of Ren'Py 7.8. The Ren'Py 7 series attempts to match Ren'Py 8 in features, while retaining
support for Python 2. As some of the new features require Python 3 support, not every new feature in
Ren'Py 8 is available in Ren'Py 7.

As Ren'Py 7.8 will be the last major release in the 7.x series, all games should be updated to Ren'Py 8 before
the release of Ren'Py 8.4, when support for Ren'Py 7 will end.
""" + COMMON_8_3,
    history="""\
""",
    full_html="""\
""",
top_html="""\
""",

deprecations="""\
Support for Python 2 and Ren'Py 7 will be dropped in the next major release.
""",

credits=CREDITS_8_3)



# 8.2.0 / 7.7.0 ##############################################################

COMMON_8_2 = """
Ren'Py 8.2 and Ren'Py 7.7 are joint releases that add many new features,
fixes, and improvements to Ren'Py. Some of the most important are:

* For 8.2 only, integration with the Harfbuzz text shaping library, which
  supports more languages and more complex text shaping than Ren'Py supported
  before. This adds support for Brahmic/Indic scripts, with an appropriate font.
* Support for displaying Emoji in color, simply by typing it into your game. 🎉
* Support for OpenType variable fonts.
* Improvements to the text interpolation system to allow expressions to be used,
  similar to Python's f-strings.
* The ability to show multiple speech bubbles at once, and to have speech bubbles
  animate in and out.
* Changes to Transform and ATL Transforms to be able to (in most cases)
  interpolate between absolute and relative positions.
* A new HTTPS/HTTP fetch function that properly pauses Ren'Py as the fetch occurs,
  and works with the web platform.
* Several new accessibility properties.
* Improvements to loading translations. Loading translations is roughly 2/3rds
  faster, and it's possible to defer loading translations for languages not in
  use.
* The ability to specify a transition that runs after each sequence of
  scene, show, and hide statements.
* A modernization of the Android build process, which now can use (and requires)
  the supported Java 21.
* The ability to create an Android game that can download its data from a
  web server, allowing the creation of games that are more than 2GB in size.
* Improvements and fixes to Web support, especially fullscreen modes.
* A complete rewrite of the Ren'Py updater to use a new format that works
  better with modern web servers.

But with so many changes, it's hard to list them all. For a full list, see
the changelog.

There is two behavior changes I want to call out:

* The first is that Ren'Py 7.7 and 8.2 will attempt to remember and restore the
  window position, so you can expect that it may pop up in the last place you left it.
* The second is that config.gl2 is now ignored, and the only way to use
  the soon-to-be removed first-generation GL renderer is for the player to
  select it.
"""

CREDITS_8_2 = """
Abdul (3):
Andy_kl (2):
Asriel Senna (9):
Ayowel (1):
Bas Couwenberg (1):
Brainos (3):
Daniel Brookman (1):
Denys (3):
Dipesh Aggarwal (1):
Do10HM (1):
Elckarow (2):
Gouvernathor (133):
Helmut K. C. Tessarek (1):
iivusly (1):
ImJustAQ (1):
JamiesonC (1):
Joseph Boyd (1):
Joshua Fehler (2):
KagariSoft-Dev (4):
Kassy (4):
Lezalith (3):
Mal Graty (18):
Michael (1):
Minger0 (1):
Morgan Willcock (2):
Moshibit (9):
OleSTEEP (1):
Tichq (11):
Tom Rothamel (505):
Vladya (2):
brainos233 (2):
jsfehler (1):
kyouryuukunn (4):
midgethetree (1):
shawna-p (4):
symegac (12):
the66F95 (5):
zedraxlo (1):
Zout141 (1):
ねゆんせ (1):
"""

Release(
    prerelease=False,
    invisible=False,
    version="8.2.3",
    pygame="-2.1.0",
    date="June 17, 2024",
    patch=None,
    name="64bit Sensation",
    world_order=14,
    announcement="""\
I'm happy to announce Ren'Py 8.2.2, the third fix release for Ren'Py 8.2.

Ren'Py 8.2 is a major release of Ren'Py, containing new features,
fixes, and improvements. It is recommended for all new games, and it's
strongly recommended that existing games update to Ren'Py 8.

""" + COMMON_8_2,
    history="""\
""",

    full_html="""\
""",
top_html="""\
""",

deprecations="""\
The original OpenGL renderer will be removed after the next major release.

Support for Windows 7, 8, and 8.1 will be dropped after the next major release.
""",

credits=CREDITS_8_2)


Release(
    prerelease=False,
    invisible=False,
    version="7.7.3",
    pygame="-2.1.0",
    date="June 17, 2024",
    patch=None,
    name="32bit Sensation",
    world_order=14,
    announcement="""\
I'm happy to announce Ren'Py 7.7.3, the third fix release for Ren'Py 7.7.

Ren'Py 7.7 attempts to match Ren'Py 8.2 in features, while retaining
support for Python 2. A some of the new features require Python 3
support, not every new feature in Ren'Py 8.2 is available in Ren'Py 7.7.

It's strongly recommended that all new games start with Ren'Py 8, and
that existing games update to Ren'Py 8.
""" + COMMON_8_2,
    history="""\
""",
    full_html="""\
""",
top_html="""\
""",

deprecations="""\
Support for Python 2 and Ren'Py 7 will be dropped after the next major release.
""",

credits=CREDITS_8_2)




Release(
    prerelease=False,
    invisible=False,
    version="8.2.2",
    pygame="-2.1.0",
    date="June 12, 2024",
    patch=None,
    name="64bit Sensation",
    world_order=14,
    announcement="""\
I'm happy to announce Ren'Py 8.2.2, the second fix release for Ren'Py 8.2. This release
contains many fixes and several accessibility improvements.

Ren'Py 8.2 is a major release of Ren'Py, containing new features,
fixes, and improvements. It is recommended for all new games, and it's
strongly recommended that existing games update to Ren'Py 8.

""" + COMMON_8_2,
    history="""\
""",

    full_html="""\
""",
top_html="""\
""",

deprecations="""\
The original OpenGL renderer will be removed after the next major release.

Support for Windows 7, 8, and 8.1 will be dropped after the next major release.
""",

credits=CREDITS_8_2)


Release(
    prerelease=False,
    invisible=False,
    version="7.7.2",
    pygame="-2.1.0",
    date="June 12, 2024",
    patch=None,
    name="32bit Sensation",
    world_order=14,
    announcement="""\
I'm happy to announce Ren'Py 7.7.2, the second fix release for Ren'Py 7.7.

Ren'Py 7.7 attempts to match Ren'Py 8.2 in features, while retaining
support for Python 2. A some of the new features require Python 3
support, not every new feature in Ren'Py 8.2 is available in Ren'Py 7.7.

It's strongly recommended that all new games start with Ren'Py 8, and
that existing games update to Ren'Py 8.
""" + COMMON_8_2,
    history="""\
""",
    full_html="""\
""",
top_html="""\
""",

deprecations="""\
Support for Python 2 and Ren'Py 7 will be dropped after the next major release.
""",

credits=CREDITS_8_2)


Release(
    prerelease=False,
    invisible=False,
    version="8.2.1",
    pygame="-2.1.0",
    date="March 4, 2024",
    patch=None,
    name="64bit Sensation",
    world_order=14,
    announcement="""\
I'm happy to announce Ren'Py 8.2.1, the first fix release for Ren'Py 8.2.

Ren'Py 8.2 is a major release of Ren'Py, containing new features,
fixes, and improvements. It is recommended for all new games, and it's
strongly recommended that existing games update to Ren'Py 8.

""" + COMMON_8_2,
    history="""\
""",

    full_html="""\
""",
top_html="""\
""",

deprecations="""\
The original OpenGL renderer will be removed after May 2024.

Support for Windows 7, 8, and 8.1 will be dropped after May 2024.
""",

credits=CREDITS_8_2)


Release(
    prerelease=False,
    invisible=False,
    version="7.7.1",
    pygame="-2.1.0",
    date="March 4, 2024",
    patch=None,
    name="32bit Sensation",
    world_order=14,
    announcement="""\
I'm happy to announce Ren'Py 7.7.1, the first fix release for Ren'Py 7.7.

Ren'Py 7.7 attempts to match Ren'Py 8.2 in features, while retaining
support for Python 2. A some of the new features require Python 3
support, not every new feature in Ren'Py 8.2 is available in Ren'Py 7.7.

It's strongly recommended that all new games start with Ren'Py 8, and
that existing games update to Ren'Py 8.
""" + COMMON_8_2,
    history="""\
""",
    full_html="""\
""",
top_html="""\
""",

deprecations="""\
Support for Python 2 and Ren'Py 7 will be dropped in May 2024.
""",

credits=CREDITS_8_2)



Release(
    prerelease=False,
    invisible=False,
    version="8.2.0",
    pygame="-2.1.0",
    date="January 27, 2024",
    patch=None,
    name="64bit Sensation",
    world_order=14,
    announcement="""\
I'm happy to announce Ren'Py 8.2.0, the latest release of Ren'Py, the
results of months of work by many contributors.

Ren'Py 8.2 is a major release of Ren'Py, containing new features,
fixes, and improvements. It is recommended for all new games, and it's
strongly recommended that existing games update to Ren'Py 8.

""" + COMMON_8_2,
    history="""\
""",

    full_html="""\
""",
top_html="""\
""",

deprecations="""\
The original OpenGL renderer will be removed after May 2024.

Support for Windows 7, 8, and 8.1 will be dropped after May 2024.
""",

credits=CREDITS_8_2)


Release(
    prerelease=False,
    invisible=False,
    version="7.7.0",
    pygame="-2.1.0",
    date="January 27, 2024",
    patch=None,
    name="32bit Sensation",
    world_order=14,
    announcement="""\
I'm happy to announce Ren'Py 7.7.0, the latest release of Ren'Py
7.

Ren'Py 7.7 attempts to match Ren'Py 8.2 in features, while retaining
support for Python 2. A some of the new features require Python 3
support, not every new feature in Ren'Py 8.2 is available in Ren'Py 7.7.

It's strongly recommended that all new games start with Ren'Py 8, and
that existing games update to Ren'Py 8.
""" + COMMON_8_2,
    history="""\
""",
    full_html="""\
""",
top_html="""\
""",

deprecations="""\
Support for Python 2 and Ren'Py 7 will be dropped in May 2024.
""",

credits=CREDITS_8_2)


# 8.1.x / 7.6.x ##############################################################

COMMON_8_1 = """
Ren'Py 8.1 and Ren'Py 7.6 are a joint release that add improved
documentation, fixes, and many new features to Ren'Py. Some of the
new features are:

* Ren'Py Sync, an easy way to synchronize save games between computers,
  phones, and the web.
* A built-in way for displaying character dialogue in speech bubbles,
  including an interactive editor for positioning the bubbles.
* Ren'Py 8-only support for progressive web apps, including features like
  installing on a device and caching data locally.
* Apple Silicon support.
* Sticky layers, such that an image tag remains associated with a layer
  until it's hidden.
* Detached layers, that are displayables themselves.
* Support for displaying AVIF images.
* Support for displaying SVG images.
* Support for oversampled images, which can be used to upgrade a game
  to a higher resolution.
* Support for AV1 video on PC and Mobile platforms, with web support
  depending on browser support.
* A rewritten audio mixing system that works on a per-sample basis,
  allowing for smoother fadeouts and removing clicks.
* Volume sliders that work in decibels, and hence are more responsive.
* Viewports that can be dragged on touch screen devices, even if the
  player is touching a button or bar.
* Support for \_ren.py files, that allow Ren'Py script to be edited using
  Python text editors (allowing for better completion of Python-heavy
  files).
* The use of lenticular brackets as a simpler syntax for ruby text (furigana).
* The ability to substitute text before self-voicing is performed, allowing
  pronunciation to be changed.
* A new warning that reminds people that it's insecure to load saves from
  people you do not fully trust.
* New transform properties that control rotation on the 3D Stage.

As well as many more new features, improvements, fixes, and a dark theme
for the documentation.

**Note:** This release moves the android keys to a per-project location.
While Ren'Py will automatically move the keys, you should make a backup
of rapt/android.keystore and rapt/bundle.keystore before upgrading.
"""

CREDITS_8_1 = """
Abdul (1):
Adam Trzypolski (5):
Altskop (6):
Andy_kl (8):
Awakening (1):
Ayowel (2):
Brainos (1):
Chrisclone (1):
Clinton Nguyen (1):
Daniel Brookman (1):
DinakiS (1):
Elckarow (4):
Erufailon4 (1):
Galo223344 (1):
Gio (2):
Gouvernathor (252):
Haelwenn (lanodan) Monnier (1):
Jeremy Rand (1):
Jesusaves (1):
Joseph Boyd (1):
Kassy (5):
Kyouryuukunn (21):
LaUwUrence (5):
Llyama (2):
Mal Graty (30):
Michael (1):
Midgethetree (4):
Morgan Willcock (1):
Moshibit (11):
NattyanTV (1):
Noriverwater (5):
Oscar Six (1):
Sandra "Maxi" Molina (1):
Shawna-p (4):
Tey (16):
Teyut (5):
The66F95 (2):
Tichq (9):
Tom Rothamel (716):
Totally a booplicate (9):
Julian Uy (1):
Vadim Karpenko (15):
Valery Iwanofu (4):
Xareyli (1):
zedraxlo (1):
ねゆんせ (3):
琴梨梨 (2):
"""

# 8.1.3 / 7.6.3


Release(
    prerelease=False,
    invisible=False,
    version="8.1.3",
    pygame="-2.1.0",
    date="September 18, 2023",
    patch=None,
    name="Where No One Has Gone Before",
    world_order=14,
    announcement="""\
I'd like to announce Ren'Py 8.1.3, the third fix release for
Ren'Py 8.1. This release fixes issues reported in Ren'Py 8.1.

Ren'Py 8.1 is the second feature release of Ren'Py
to support Python 3. It is is the first version
of Ren'Py 8 to run on the web platform, and is recommended for all
new games and games that plan to release after May 2024.

""" + COMMON_8_1,
    history="""\
""",

    full_html="""\
<img src="/static/8.1.jpg" alt="" style="width: 100%">
""",
top_html="""\
""",

deprecations="""\
The original OpenGL renderer will be removed 1 year after Ren'Py 8.1 is released,
in May 2024.
If your game sets ``config.gl2`` to ``False``, you should set it to ``True``,
and make sure your game runs well. If it doesn't, please report any issues.
When reporting issues, please determine the hardware (device and GPU),
os and driver versions, and year of manufacture.
""",

credits=CREDITS_8_1)


Release(
    prerelease=False,
    invisible=False,
    version="7.6.3",
    pygame="-2.1.0",
    date="September 18, 2023",
    patch=None,
    name="To Boldly Go",
    world_order=14,
    announcement="""\
I'd like to announce Ren'Py 7.6.3, the third fix release for
Ren'Py 7.6. This release fixes issues reported in Ren'Py 7.6.

Ren'Py 7.6 is a feature release that retains support for
Python 2.7. It is intended to support games that do not support
Python 3 yet, and plan to release before May 2024.
    """ + COMMON_8_1,
    history="""\
""",
    full_html="""\
<img src="/static/8.1.jpg" alt="" style="width: 100%">
""",
top_html="""\
""",

deprecations="""\
Support for Python 2 and Ren'Py 7 will be dropped 1 year after Ren'Py 8.1 is
released, in May 2024.
""",

credits=CREDITS_8_1)



# 8.1.2 / 7.6.2


Release(
    prerelease=False,
    invisible=False,
    version="8.1.2",
    pygame="-2.1.0",
    date="September 5, 2023",
    patch=None,
    name="Where No One Has Gone Before",
    world_order=14,
    announcement="""\
I'm happy to announce Ren'Py 8.1.2, the second fix release for
Ren'Py 8.1. This release fixes issues reported in Ren'Py 8.1.

Ren'Py 8.1 is the second feature release of Ren'Py
to support Python 3. It is is the first version
of Ren'Py 8 to run on the web platform, and is recommended for all
new games and games that plan to release after May 2024.

""" + COMMON_8_1,
    history="""\
""",

    full_html="""\
<img src="/static/8.1.jpg" alt="" style="width: 100%">
""",
top_html="""\
""",

deprecations="""\
The original OpenGL renderer will be removed 1 year after Ren'Py 8.1 is released,
in May 2024.
If your game sets ``config.gl2`` to ``False``, you should set it to ``True``,
and make sure your game runs well. If it doesn't, please report any issues.
When reporting issues, please determine the hardware (device and GPU),
os and driver versions, and year of manufacture.
""",

credits=CREDITS_8_1)


Release(
    prerelease=False,
    invisible=False,
    version="7.6.2",
    pygame="-2.1.0",
    date="September 5, 2023",
    patch=None,
    name="To Boldly Go",
    world_order=14,
    announcement="""\
I'm happy to announce Ren'Py 7.6.1, the second fix release for
Ren'Py 7.6. This release fixes issues reported in Ren'Py 7.6.

Ren'Py 7.6 is a feature release that retains support for
Python 2.7. It is intended to support games that do not support
Python 3 yet, and plan to release before May 2024.
    """ + COMMON_8_1,
    history="""\
""",
    full_html="""\
<img src="/static/8.1.jpg" alt="" style="width: 100%">
""",
top_html="""\
""",

deprecations="""\
Support for Python 2 and Ren'Py 7 will be dropped 1 year after Ren'Py 8.1 is
released, in May 2024.
""",

credits=CREDITS_8_1)



# 8.1.1 / 7.6.1

Release(
    prerelease=False,
    invisible=False,
    version="8.1.1",
    pygame="-2.1.0",
    date="June 7, 2023",
    patch=None,
    name="Where No One Has Gone Before",
    world_order=13,
    announcement="""\
I'm happy to announce Ren'Py 8.1.1, the first fix release for
Ren'Py 8.1. This release fixes issues reported in Ren'Py 8.1.

Ren'Py 8.1 is the second feature release of Ren'Py
to support Python 3. It is is the first version
of Ren'Py 8 to run on the web platform, and is recommended for all
new games and games that plan to release after May 2024.

""" + COMMON_8_1,
    history="""\
""",

    full_html="""\
<img src="/static/8.1.jpg" alt="" style="width: 100%">
""",
top_html="""\
""",

deprecations="""\
The original OpenGL renderer will be removed 1 year after Ren'Py 8.1 is released,
in May 2024.
If your game sets ``config.gl2`` to ``False``, you should set it to ``True``,
and make sure your game runs well. If it doesn't, please report any issues.
When reporting issues, please determine the hardware (device and GPU),
os and driver versions, and year of manufacture.
""",

credits=CREDITS_8_1)


Release(
    prerelease=False,
    invisible=False,
    version="7.6.1",
    pygame="-2.1.0",
    date="June 7, 2023",
    patch=None,
    name="To Boldly Go",
    world_order=13,
    announcement="""\
I'm happy to announce Ren'Py 7.6.1, the first fix release for
Ren'Py 7.6. This release fixes issues reported in Ren'Py 7.6.

Ren'Py 7.6 is a feature release that retains support for
Python 2.7. It is intended to support games that do not support
Python 3 yet, and plan to release before May 2024.
    """ + COMMON_8_1,
    history="""\
""",
    full_html="""\
<img src="/static/8.1.jpg" alt="" style="width: 100%">
""",
top_html="""\
""",

deprecations="""\
Support for Python 2 and Ren'Py 7 will be dropped 1 year after Ren'Py 8.1 is
released, in May 2024.
""",

credits=CREDITS_8_1)


# 8.1.0 / 7.6.0

Release(
    prerelease=False,
    invisible=False,
    version="8.1.0",
    pygame="-2.1.0",
    date="May 14, 2023",
    patch=None,
    name="Where No One Has Gone Before",
    world_order=13,
    announcement="""\
I'm happy to announce Ren'Py 8.1, the second feature release of Ren'Py
to support Python 3. This release is the first version
of Ren'Py 8 to run on the web platform, and is recommended for all
new games and games that plan to release after May 2024.

""" + COMMON_8_1,
    history="""\
""",

    full_html="""\
<img src="/static/8.1.jpg" alt="" style="width: 100%">
""",
top_html="""\
""",

deprecations="""\
The original OpenGL renderer will be removed 1 year after Ren'Py 8.1 is released,
in May 2024.
If your game sets ``config.gl2`` to ``False``, you should set it to ``True``,
and make sure your game runs well. If it doesn't, please report any issues.
When reporting issues, please determine the hardware (device and GPU),
os and driver versions, and year of manufacture.
""",

credits=CREDITS_8_1)


Release(
    prerelease=False,
    invisible=False,
    version="7.6.0",
    pygame="-2.1.0",
    date="May 14, 2023",
    patch=None,
    name="To Boldly Go",
    world_order=13,
    announcement="""\
I'm happy to announce Ren'Py 7.6, a feature release that retains support for
Python 2.7. This release is intended to support games that do not support
Python 3 yet, and plan to release before May 2024.
    """ + COMMON_8_1,
    history="""\
""",
    full_html="""\
<img src="/static/8.1.jpg" alt="" style="width: 100%">
""",
top_html="""\
""",

deprecations="""\
Support for Python 2 and Ren'Py 7 will be dropped 1 year after Ren'Py 8.1 is
released, in May 2024.
""",

credits=CREDITS_8_1)

# 8.0 / 7.5 ##############################################################


COMMON_8_0 = """
Ren'Py 8.0 and Ren'Py 7.5 are the first in what is planned to be a joint
series of releases. Ren'Py 8.0:

* Adds support for Python 3, which is recommended for all new games.

* Removes support for 32-bit Windows and Linux.

* Temporarily removes support for the web platform, to be added back in a
  near-future release.

Ren'Py 7.5:

* Continues support for Python 2.7, to allow current games to release.

* Improves support for the web platform, including:

  * Workarounds for changes introduced by web browsers that caused the browser
    to consume more memory when running Ren'Py, resulting in RangeErrors.

  * Detecting if the audio types supported by your game are available,
    and falling back if they are.

Ren'Py 8.0 and 7.5 are released in parallel, and share the same source code,
which means the bulk of changes apply to both versions, including:

* Support for the Visual Studio Code text editor, including the Ren'Py
  Language extension. This extension include support for many advanced
  including live diagnostics and an outline. It also allows access
  to many other Visual Studio Code extensions.

* The new ``dismiss`` and ``nearrect`` displayables provide support for
  pop-up tooltips and drop-down menus.

* A rewritten wrapper for Steamworks that supports the full API. This allows
  for Steam Deck integration, including automatically setting a "steam_deck"
  variant and displaying the on-screen keyboard.

* Improvements to how graphics work on Android and iOS, improving compatibility
  with those devices.

* Over 140 issues - a mix of fixes and feature requests - have been addressed
  in this release.

For a full list of what's changed in Ren'Py 8.0 and 7.5, see the changelog.
These releases are brought to you by:

.. raw:: html

    <table style="width: 100%;">
    <tr>
    <td style="width: 25%; vertical-align: top">
    <ul>
        <li> Alex
        <li> Andy_kl
        <li> Daniel Luque
        <li> Elckarow
        <li> GNCanva
        <li> Gouvernathor
        <li> Jacob Kauffmann
        <li> Joshua Fehler
        <li> Julian Uy
        <li> Julvenzor
        <li> Kigyo
        <li> Kyouryuukunn
        <li> Lari Liuhamo
        <li> LaUwUrence
        <li> Lezalith
        <li> Liu Wenyuan
        <li> LoafyLemon
        <li> Loliconazter
    </ul></td><td style="width: 25%; vertical-align: top"><ul>
        <li> Mal Graty
        <li> Matias B.
        <li> Matt George
        <li> Moshibit
        <li> Numerlor
        <li> Raj Singh Chauhan
        <li> Raspberry-soft
        <li> Rob Colton
        <li> Siege-Wizard
        <li> Tey
        <li> Tichq
        <li> Totally a Booplicate
        <li> Zedraxlo
        <li> ねゆんせ
        <li> 琴梨梨
    </ul></td><td style="width: 25%; vertical-align: top"><ul>
    </ul></td><td style="width: 25%; vertical-align: top"><ul>
    </ul><td></tr></table>

everyone who's tested these releases, and myself, Tom "PyTom" Rothamel.
"""

# 8.0.3 / 7.5.3 ##############################################################

Release(
    prerelease=False,
    invisible=False,
    version="8.0.3",
    pygame="-2.1.0",
    date="September 10, 2022",
    patch=None,
    name="Heck Freezes Over",
    world_order=12,
    announcement="""\
I'd like to announce Ren'Py 8.0.0, the first release of Ren'Py based on
Python 3. This release modernizes Ren'Py by embracing a decade of Python
development, and brings the many improvements of Python 3.9 to Ren'Py.

""" + COMMON_8_0,
    history="""\
**8.0.3**
    This release updates the Android port to target Android 13, ensuing that
    games can be added to the google play store. It also includes a way to
    have pauses that will expire when a modal screen is display, , and
    adds Ukrainian translations of the Tutorial game and The Question.
    Please see the changelog for a full list of changes.

**8.0.2**
    This release fixes multiple issues with Ren'Py 8.0.1. Please see the
    changelog for a full list of changes.

**8.0.1**
    This release fixes multiple issues with Ren'Py 8.0.0, including one that
    prevented upgrading from Ren'Py 7.4 when Steam support was installed.

    This release also includes a new Ukrainian translation of the
    launcher.
""",

    full_html="""\
<img src="/static/8.0.jpg" alt="" style="width: 100%">
""",

top_html="""\
"""

)


Release(
    prerelease=False,
    invisible=False,
    version="7.5.3",
    pygame="-2.1.0",
    date="September 10, 2022",
    patch=None,
    name="Heck's Getting Frosty",
    world_order=12,
    announcement="""\
I'd like to announce Ren'Py 7.5.0. This release is a continuation of the
Ren'Py 7 series, supporting Python 2.7 and all platforms Ren'Py 7.4 supported,
while bringing you many of the new features of Ren'Py 8.0.
""" + COMMON_8_0,
    history="""\
**7.5.3**
    This release updates the Android port to target Android 13, ensuing that
    games can be added to the google play store. It also includes a way to
    have pauses that will expire when a modal screen is display, and
    adds Ukrainian translations of the Tutorial game and The Question.
    Please see the changelog for a full list of changes.

**7.5.2**
    This release fixes multiple issues with Ren'Py 7.5.1. Please see the
    changelog for a full list of changes.

**7.5.1**
    This release fixes multiple issues with Ren'Py 7.5.0, including one that
    prevented upgrading from Ren'Py 7.4 when Steam support was installed.

    This release also includes a new Ukrainian translation of the
    launcher.
""",
    full_html="""\
""",

top_html="""\
  """)

# 8.0.2 / 7.5.2 ##############################################################

Release(
    prerelease=False,
    invisible=False,
    version="8.0.2",
    pygame="-2.1.0",
    date="August 14, 2022",
    patch=None,
    name="Heck Freezes Over",
    world_order=12,
    announcement="""\
I'd like to announce Ren'Py 8.0.0, the first release of Ren'Py based on
Python 3. This release modernizes Ren'Py by embracing a decade of Python
development, and brings the many improvements of Python 3.9 to Ren'Py.

""" + COMMON_8_0,
    history="""\
**8.0.2**
    This release fixes multiple issues with Ren'Py 8.0.1. Please see the
    changelog for a full list of changes.

**8.0.1**
    This release fixes multiple issues with Ren'Py 8.0.0, including one that
    prevented upgrading from Ren'Py 7.4 when Steam support was installed.

    This release also includes a new Ukrainian translation of the
    launcher.
""",

    full_html="""\
<img src="/static/8.0.jpg" alt="" style="width: 100%">
""",

top_html="""\
  """)


Release(
    prerelease=False,
    invisible=False,
    version="7.5.2",
    pygame="-2.1.0",
    date="August 14, 2022",
    patch=None,
    name="Heck's Getting Frosty",
    world_order=12,
    announcement="""\
I'd like to announce Ren'Py 7.5.0. This release is a continuation of the
Ren'Py 7 series, supporting Python 2.7 and all platforms Ren'Py 7.4 supported,
while bringing you many of the new features of Ren'Py 8.0.
""" + COMMON_8_0,
    history="""\
**7.5.2**
    This release fixes multiple issues with Ren'Py 7.5.1. Please see the
    changelog for a full list of changes.

**7.5.1**
    This release fixes multiple issues with Ren'Py 7.5.0, including one that
    prevented upgrading from Ren'Py 7.4 when Steam support was installed.

    This release also includes a new Ukrainian translation of the
    launcher.
""",
    full_html="""\
""",

top_html="""\
  """)


# 8.0.1 / 7.5.1 ##############################################################

Release(
    prerelease=False,
    invisible=False,
    version="8.0.1",
    pygame="-2.1.0",
    date="July 8, 2022",
    patch=None,
    name="Heck Freezes Over",
    world_order=12,
    announcement="""\
I'd like to announce Ren'Py 8.0.0, the first release of Ren'Py based on
Python 3. This release modernizes Ren'Py by embracing a decade of Python
development, and brings the many improvements of Python 3.9 to Ren'Py.

""" + COMMON_8_0,
    history="""\
**8.0.1**

This release fixes multiple issues with Ren'Py 8.0.0, including one that
prevented upgrading from Ren'Py 7.4 when Steam support was installed.

This release also includes a new Ukrainian translation of the
launcher.
""",

    full_html="""\
<img src="/static/8.0.jpg" alt="" style="width: 100%">
""",

top_html="""\
  """)

Release(
    prerelease=False,
    invisible=False,
    version="7.5.1",
    pygame="-2.1.0",
    date="July 8, 2022",
    patch=None,
    name="Heck's Getting Frosty",
    world_order=12,
    announcement="""\
I'd like to announce Ren'Py 7.5.0. This release is a continuation of the
Ren'Py 7 series, supporting Python 2.7 and all platforms Ren'Py 7.4 supported,
while bringing you many of the new features of Ren'Py 8.0.
""" + COMMON_8_0,
    history="""\
**7.5.1**

This release fixes multiple issues with Ren'Py 7.5.0, including one that
prevented upgrading from Ren'Py 7.4 when Steam support was installed.

This release also includes a new Ukrainian translation of the
launcher.
""",
    full_html="""\
""",

top_html="""\
  """)



Release(
    prerelease=False,
    invisible=False,
    version="8.0.0",
    pygame="-2.1.0",
    date="June 26, 2022",
    patch=None,
    name="Heck Freezes Over",
    world_order=12,
    announcement="""\
I'd like to announce Ren'Py 8.0.0, the first release of Ren'Py based on
Python 3. This release modernizes Ren'Py by embracing a decade of Python
development, and brings the many improvements of Python 3.9 to Ren'Py.

""" + COMMON_8_0,
    history="""\
""",

    full_html="""\
<img src="/static/8.0.jpg" alt="" style="width: 100%">
""",

top_html="""\
  """)

Release(
    prerelease=False,
    invisible=False,
    version="7.5.0",
    pygame="-2.1.0",
    date="June 26, 2022",
    patch=None,
    name="Heck's Getting Frosty",
    world_order=12,
    announcement="""\
I'd like to announce Ren'Py 7.5.0. This release is a continuation of the
Ren'Py 7 series, supporting Python 2.7 and all platforms Ren'Py 7.4 supported,
while bringing you many of the new features of Ren'Py 8.0.
""" + COMMON_8_0,
    history="""\
""",

    full_html="""\
""",

top_html="""\
  """)


__import__("data_old")


# The currrent pre-release and release.
prerelease_8 = None
current_8 = None
prerelease_7 = None
current_7 = None


# A map from version to the release object. Used to get information about
# a particular release.
release_version = { }

# All final releases.
final_releases = [ ]

for i in releases:
    if i.prerelease and not i.invisible:
        if i.major < 8:
            prerelease_7 = prerelease_7 or i
        else:
            prerelease_8 = prerelease_8 or i
    else:
        if i.major < 8:
            current_7 = current_7 or i
        else:
            current_8 = current_8 or i

        final_releases.append(i)

    if not i.wiki:
        release_version[i.version] = i

for i in aliases:
    release_version[i.old] = release_version[i.new]

for n, i in enumerate(final_releases):
    i.ordinal = len(final_releases) - n
