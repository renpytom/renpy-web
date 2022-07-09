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
        <li> Gouvernathor
        <li> Jacob Kauffmann
        <li> Joshua Fehler
        <li> Julian Uy
        <li> Julvenzor
        <li> Kigyo
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
