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

Release(
    prerelease=True,
    invisible=False,
    version="8.0.0",
    pygame="-2.1.0",
    date="June xx, 2022",
    patch=None,
    name="Heck Freezes Over",
    world_order=11,
    announcement="""\
I'd like to announce Ren'Py 7.5.0.

Ren'Py 7.5 is brought to you by:

.. raw:: html

    <table style="width: 100%;">
    <tr>
    <td style="width: 25%; vertical-align: top">
    <ul>
        <li> Alex
        <li> Andy_kl
        <li> Daniel Luque
        <li> Gouvernathor
        <li> Jacob Kauffmann
        <li> Joshua Fehler
        <li> Julvenzor
        <li> LaUwUrence
        <li> Liu Wenyuan
        <li> LoafyLemon
        <li> Loliconazter
        <li> Mal Graty
        <li> Matt George
        <li> Moshibit
        <li> Raj Singh Chauhan
        <li> Siege-Wizard
        <li> Tey
        <li> Tichq
        <li> Raspberry-soft
        <li> Uyjulian
        <li> Zedraxlo
        <li> 琴梨梨
    </ul></td><td style="width: 25%; vertical-align: top"><ul>
    </ul></td><td style="width: 25%; vertical-align: top"><ul>
    </ul></td><td style="width: 25%; vertical-align: top"><ul>
    </ul><td></tr></table>

everyone who's tested this release, and myself, Tom "PyTom" Rothamel.
""",
    history="""\
""",

    full_html="""\
""",

top_html="""\
  """)




Release(
    prerelease=True,
    invisible=False,
    version="7.5.0",
    pygame="-2.1.0",
    date="June xx, 2022",
    patch=None,
    name="Heck's Getting Frosty",
    world_order=11,
    announcement="""\
I'd like to announce Ren'Py 7.5.0.

Ren'Py 7.5 is brought to you by:

.. raw:: html

    <table style="width: 100%;">
    <tr>
    <td style="width: 25%; vertical-align: top">
    <ul>
        <li> Alex
        <li> Andy_kl
        <li> Daniel Luque
        <li> Gouvernathor
        <li> Jacob Kauffmann
        <li> Joshua Fehler
        <li> Julvenzor
        <li> LaUwUrence
        <li> Liu Wenyuan
        <li> LoafyLemon
        <li> Loliconazter
        <li> Mal Graty
        <li> Matt George
        <li> Moshibit
        <li> Raj Singh Chauhan
        <li> Siege-Wizard
        <li> Tey
        <li> Tichq
        <li> Raspberry-soft
        <li> Uyjulian
        <li> Zedraxlo
        <li> 琴梨梨
    </ul></td><td style="width: 25%; vertical-align: top"><ul>
    </ul></td><td style="width: 25%; vertical-align: top"><ul>
    </ul></td><td style="width: 25%; vertical-align: top"><ul>
    </ul><td></tr></table>

everyone who's tested this release, and myself, Tom "PyTom" Rothamel.
""",
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
