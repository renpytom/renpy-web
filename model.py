# This file contains the definitions of the classes used in data. It should
# always be imported _after_ data, if it needs to be imported at all.

import data
import os
import time


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


class Release(Data):
    """
    A non-wiki release.
    """

    prerelease = False
    wiki = False

    # The "world order" of the release.
    # 0-3 (before 6.14)
    # 4 (6.14)
    world_order = 0
    dmg = None

    exe=None
    bz2=None
    zip=None
    sdkarm = None
    powerpc=False

    deprecations = None

    # HTML appended to the end of the Credits section of the release page.
    extra_credits = None

    # Release notes shared by the whole x.y series (e.g. COMMON_8_6). Shown after the announcement on the release
    # page, and in place of `changes` in the social formats when a release has no changes of its own.
    notes = None

    # The changes made in this release, using the announcement markup (paragraphs, "* " items, **bold**). Once any
    # release in an x.y series has non-empty changes, the series is "new-style" (see `series_has_changes`): its
    # release pages show `series_history` in place of `history`, and its x.y.0 release, which leaves this unset, is
    # listed there as "* Initial release of Ren'Py x.y.". The social formats (.txt, .md, .update.html) show these
    # changes, or the series notes when there are none.
    changes = None

    def __init__(self, **kwargs):

        self.patch = None
        self.patch_date = None

        self.prerelease = False
        self.prerelease_date = None

        super(Release, self).__init__(**kwargs)

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

        for l in getattr(self, "credits", "").split("\n"):
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

        return bool(getattr(self, "history", None))

    @property
    def major(self):
        return int(self.version.split(".")[0])

    @property
    def major_minor(self):
        return ".".join(self.version.split(".")[:2])


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
        pygame =  getattr(self, "pygame", None)

        if pygame:
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

    def __init__(self, **kwargs):
        super(WikiRelease, self).__init__(**kwargs)
        data.releases.append(self)

        self.full_version = self.version


class Alias(Data):

    def __init__(self, **kwargs):
        super(Alias, self).__init__(**kwargs)
        data.aliases.append(self)
