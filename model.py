# This file contains the definitions of the classes used in data. It should
# always be imported _after_ data, if it needs to be imported at all.

import data
import os
import re
import time


# Marks a parameter of Series or Release that was not passed, since None is a meaningful value for several fields.
UNSET = sentinel("UNSET")


def pick[T](value: T | UNSET, series_value: T | UNSET, default: T) -> T:
    """
    Returns the first of `value` (passed to a Release), `series_value` (set on its Series), and `default` that is
    not UNSET.
    """

    if value is not UNSET:
        return value

    if series_value is not UNSET:
        return series_value

    return default


def get_major_minor(version: str) -> str:
    """
    Returns the "x.y" series of a version like "8.6.1".
    """

    return ".".join(version.split(".")[:2])


class Data(object):
    """
    This is a class that represents unstructured data. It simply
    adds the keyword arguments to its constructor to its __dict__,
    so they can be accessed as properties.
    """

    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)


FILE_PATHS = [
    "/home/tom/WWW.renpyorg/dl",
    "/home/tom/ab/renpy/dl",
    ]


# A map from an "x.y" version to the Series that supplies defaults for its releases.
SERIES: dict[str, Series] = { }


class Series:
    """
    Default values for the fields shared by every release in an x.y series (for example 8.6). A Release looks up the
    Series for its version when it is created, and uses each field set here unless it passes the field itself. A
    Series must therefore be created before any of its releases.
    """

    # The "x.y" version of the series.
    version: str

    # Defaults for the Release fields of the same name, or UNSET when the series doesn't set them.
    name: str | UNSET
    world_order: int | UNSET
    notes: str | None | UNSET
    credits: str | UNSET
    extra_credits: str | None | UNSET
    top_html: str | UNSET
    full_html: str | UNSET
    deprecations: str | None | UNSET
    pygame: str | UNSET

    def __init__(
        self,
        version: str,
        *,
        name: str | UNSET = UNSET,
        world_order: int | UNSET = UNSET,
        notes: str | None | UNSET = UNSET,
        credits: str | UNSET = UNSET,
        extra_credits: str | None | UNSET = UNSET,
        top_html: str | UNSET = UNSET,
        full_html: str | UNSET = UNSET,
        deprecations: str | None | UNSET = UNSET,
        pygame: str | UNSET = UNSET,
        ) -> None:
        """
        Registers the series in SERIES. Raises ValueError if `version` isn't of the form "x.y", if the series is
        already registered, or if a release in the series was created before it.
        """

        if not re.fullmatch(r"\d+\.\d+", version):
            raise ValueError("Series version {!r} is not of the form x.y.".format(version))

        if version in SERIES:
            raise ValueError("Series {} is defined twice.".format(version))

        if any((not r.wiki) and r.major_minor == version for r in data.releases):
            raise ValueError("Series {} must be defined before its releases.".format(version))

        self.version = version
        self.name = name
        self.world_order = world_order
        self.notes = notes
        self.credits = credits
        self.extra_credits = extra_credits
        self.top_html = top_html
        self.full_html = full_html
        self.deprecations = deprecations
        self.pygame = pygame

        SERIES[version] = self


class Release:
    """
    A non-wiki release. Creating one appends it to data.releases, so the order of the Release calls in data.py is
    the order of the releases (newest first). Fields marked "series" below may be supplied by the Series for the
    release's x.y version.
    """

    wiki = False

    # The version, like "8.6.1".
    version: str

    # The release name, like "Real Artists Ship". Series.
    name: str

    # The "world order" of the release, which selects era-specific parts of the release page. 0-3 is before 6.14,
    # 4 is 6.14, and it increases from there. Series.
    world_order: int

    # The release date, like "November 14, 2026". Filled in from the date of the SDK zip when None.
    date: str | None

    # The release-specific announcement, using the announcement markup (paragraphs, "* " items, **bold**).
    announcement: str

    # Free-form release history, used by releases in series that aren't new-style (see `series_has_changes`).
    history: str

    # Release notes shared by the whole x.y series (e.g. COMMON_8_6). Shown after the announcement on the release
    # page, and in place of `changes` in the social formats when a release has no changes of its own. Series.
    notes: str | None

    # The changes made in this release, using the announcement markup (paragraphs, "* " items, **bold**). Once any
    # release in an x.y series has non-empty changes, the series is "new-style" (see `series_has_changes`): its
    # release pages show `series_history` in place of `history`, and its x.y.0 release, which leaves this unset, is
    # listed there as "* Initial release of Ren'Py x.y.". The social formats (.txt, .md, .update.html) show these
    # changes, or the series notes when there are none.
    changes: str | None

    # The contributor list, one "Name (commits):" line per contributor. Series.
    credits: str

    # HTML appended to the end of the Credits section of the release page. Series.
    extra_credits: str | None

    # Deprecation notes, in reStructuredText. Series.
    deprecations: str | None

    # HTML shown full-width above the release page, and at the top of its main column. Series.
    full_html: str
    top_html: str

    # The suffix of the pygame_sdl2 source download name, like "-2.1.0". Series.
    pygame: str

    # True for a prerelease. A prerelease that is also invisible is a private prerelease.
    prerelease: bool
    invisible: bool

    # The patch number appended to the version in `full_version`, if any.
    patch: int | str | None

    # The dates of the patch and the prerelease. Filled in from the date of the SDK zip when None.
    patch_date: str | None
    prerelease_date: str | None

    # Download sizes in megabytes. Filled in from the files on disk when None.
    exe: int | None
    bz2: int | None
    zip: int | None
    dmg: int | None
    sdkarm: int | None

    # True if the release has a PowerPC Mac build, or an Android build (shown on old release pages).
    powerpc: bool
    android: bool

    # The version of the renpy-deps download, for old releases that have one.
    deps: str | None

    # Accepted for old releases in data_old.py, but no longer used.
    aside_html: str | None
    bugfix_date: str | None
    bugfix_revision: int | None
    revision: str | None

    # The release's position among the final releases, counting up from the oldest. Set at the bottom of data.py.
    ordinal: int

    def __init__(
        self,
        *,
        version: str,
        name: str | UNSET = UNSET,
        world_order: int | UNSET = UNSET,
        date: str | None = None,
        announcement: str = "",
        history: str = "",
        notes: str | None | UNSET = UNSET,
        changes: str | None = None,
        credits: str | UNSET = UNSET,
        extra_credits: str | None | UNSET = UNSET,
        deprecations: str | None | UNSET = UNSET,
        full_html: str | UNSET = UNSET,
        top_html: str | UNSET = UNSET,
        pygame: str | UNSET = UNSET,
        prerelease: bool = False,
        invisible: bool = False,
        patch: int | str | None = None,
        patch_date: str | None = None,
        prerelease_date: str | None = None,
        exe: int | None = None,
        bz2: int | None = None,
        zip: int | None = None,
        dmg: int | None = None,
        sdkarm: int | None = None,
        powerpc: bool = False,
        android: bool = False,
        deps: str | None = None,
        aside_html: str | None = None,
        bugfix_date: str | None = None,
        bugfix_revision: int | None = None,
        revision: str | None = None,
        ) -> None:
        """
        Creates the release, filling fields it doesn't pass from its Series, and appends it to data.releases. Fills
        in missing download sizes and dates from the files on disk. Raises TypeError if no name is given by either
        the release or its series.
        """

        series = SERIES.get(get_major_minor(version))

        resolved_name = pick(name, series.name if series else UNSET, UNSET)

        if resolved_name is UNSET:
            raise TypeError("Release {} needs a name, from its arguments or its Series.".format(version))

        self.version = version
        self.name = resolved_name
        self.world_order = pick(world_order, series.world_order if series else UNSET, 0)
        self.date = date
        self.announcement = announcement
        self.history = history
        self.notes = pick(notes, series.notes if series else UNSET, None)
        self.changes = changes
        self.credits = pick(credits, series.credits if series else UNSET, "")
        self.extra_credits = pick(extra_credits, series.extra_credits if series else UNSET, None)
        self.deprecations = pick(deprecations, series.deprecations if series else UNSET, None)
        self.full_html = pick(full_html, series.full_html if series else UNSET, "")
        self.top_html = pick(top_html, series.top_html if series else UNSET, "")
        self.pygame = pick(pygame, series.pygame if series else UNSET, "")
        self.prerelease = prerelease
        self.invisible = invisible
        self.patch = patch
        self.patch_date = patch_date
        self.prerelease_date = prerelease_date
        self.exe = exe
        self.bz2 = bz2
        self.zip = zip
        self.dmg = dmg
        self.sdkarm = sdkarm
        self.powerpc = powerpc
        self.android = android
        self.deps = deps
        self.aside_html = aside_html
        self.bugfix_date = bugfix_date
        self.bugfix_revision = bugfix_revision
        self.revision = revision

        data.releases.append(self)

        if self.exe is None:
            self.exe = self.file_size("sdk.7z.exe")
        if self.bz2 is None:
            self.bz2 = self.file_size("sdk.tar.bz2")
        if self.zip is None:
            self.zip = self.file_size("sdk.zip")
        if self.dmg is None:
            self.dmg = self.file_size("sdk.dmg")
        if self.sdkarm is None:
            self.sdkarm = self.file_size("sdkarm.tar.bz2")

        zipfn = self.find_file("sdk.zip")

        if zipfn is not None:
            ziptime = os.path.getmtime(zipfn)
            zipdate = time.strftime("%B %d, %Y", time.localtime(ziptime))

            if self.prerelease and (self.prerelease_date is None):
                self.prerelease_date = zipdate

            if self.patch and (self.patch_date is None):
                self.patch_date = zipdate

        zipfn = self.find_file("sdk.zip", False)

        if zipfn is not None:
            ziptime = os.path.getmtime(zipfn)
            zipdate = time.strftime("%B %d, %Y", time.localtime(ziptime))

            if self.date is None:
                self.date = zipdate

    @property
    def split_credits(self):
        import re

        credits = [ ]

        for l in self.credits.split("\n"):
            m = re.match(r"^(.*) \(\d+\):\s*$", l)
            if m:
                credits.append(m.group(1))

        credits = [ i for i in credits if ("Rothamel" not in i) ]

        credits.sort()

        split = len(credits) - len(credits) // 2

        return credits[:split], credits[split:]


    @property
    def history_changes(self):
        """
        The changes shown for this release in a series history: `changes`, or, for an x.y.0 release without changes
        in a new-style series, "* Initial release of Ren'Py x.y.". Empty when there is nothing to show.
        """

        if self.changes:
            return self.changes

        if self.version.split(".")[2:] in ([ ], [ "0" ]) and self.series_has_changes:
            return "* Initial release of Ren'Py {}.".format(self.major_minor)

        return ""

    def series_releases(self):
        """
        Yields the non-wiki releases in the same x.y series as this one, newest first.
        """

        for r in data.releases:
            if not r.wiki and r.major_minor == self.major_minor:
                yield r

    @property
    def series_has_changes(self):
        """
        True if any release in this x.y series has non-empty `changes`, which makes the series "new-style".
        """

        return any(r.changes for r in self.series_releases())

    @property
    def series_history(self):
        """
        The releases whose changes appear in this release's history section: every release in the same x.y series
        that has `history_changes` and is either a public final release or this release itself. Newest first.
        """

        rv = [ ]

        for r in self.series_releases():
            if not r.history_changes:
                continue

            if r is self or not (r.prerelease or r.invisible):
                rv.append(r)

        return rv

    @property
    def has_history(self):
        """
        True if the release page and feed have a history section to show for this release. In a new-style series,
        that takes at least two releases, since a history of one release says nothing.
        """

        if self.series_has_changes:
            return len(self.series_history) > 1

        return bool(self.history)

    @property
    def major(self):
        return int(self.version.split(".")[0])

    @property
    def major_minor(self):
        return get_major_minor(self.version)


    @property
    def changelog_version(self):
        return self.version.replace(".", "-")

    def get_full_version(self):
        if self.patch is not None:
            return "{0}.{1}".format(self.version, self.patch)
        else:
            return self.version

    full_version = property(get_full_version)

    @property
    def pygame_ext(self):
        if self.pygame:
            return "gz"
        else:
            return "bz2"

    def find_file(self, variant, full_version=True):

        if full_version:
            version = self.full_version
        else:
            version = self.version

        fn = "renpy-" + version + "-" + variant

        for i in FILE_PATHS:
            ffn = os.path.join(i, version, fn)

            if os.path.exists(ffn):
                return ffn

        return None

    def file_size(self, variant):
        """
        Given `variant`, returns the file size in megabytes.
        """

        fn = self.find_file(variant)

        if fn is None:
            return None

        size = os.path.getsize(fn)

        return int(round(size / 1024.0 / 1024.0))


class WikiRelease(Data):
    """
    An older wiki-based release.
    """

    prerelease = False
    wiki = True
    major = 7

    # The version, release name, and release date, passed as keywords.
    version: str
    name: str
    date: str

    # The same as `version`, matching Release.full_version.
    full_version: str

    def __init__(self, **kwargs):
        super(WikiRelease, self).__init__(**kwargs)
        data.releases.append(self)

        self.full_version = self.version


class Alias(Data):
    """
    Makes the release page for version `old` show the release for version `new`.
    """

    old: str
    new: str

    def __init__(self, **kwargs):
        super(Alias, self).__init__(**kwargs)
        data.aliases.append(self)
