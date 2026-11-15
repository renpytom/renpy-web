# coding=utf-8
# This file contains data about Ren'Py, and its various
# releases. Think of it as a kind of database, except that it's stored
# as code rather than as data. The releases themselves are in the releases/ package, one module per major version.

# A list of releases, newest first. This is filled up when the modules in releases/ are imported, below, as each
# Release and WikiRelease appends itself.
releases = [ ]

# All aliases.
aliases = [ ]

# Import the release modules newest first, since import order is release order. New releases go in releases/v8.py
# (or a new releases/v9.py, imported first). This must stay a "from releases import" statement: "import releases.v8"
# would bind the name releases to the package, replacing the list above.
from releases import v8, v7_8, v7, v6, v5, v4



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
