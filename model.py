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
    def major(self):
        return int(self.version.split(".")[0])

    @property
    def major_minor(self):
        return ".".join(self.version.split(".")[:2])

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
