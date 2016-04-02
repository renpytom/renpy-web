# This file contains the definitions of the classes used in data. It should
# always be imported _after_ data, if it needs to be imported at all.

import data

class Data(object):
    """
    This is a class that represents unstructured data. It simply
    adds the keyword arguments to its constructor to its __dict__,
    so they can be accessed as properties.
    """

    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)


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

    def __init__(self, **kwargs):

        self.patch = None
        self.patch_date = None

        super(Release, self).__init__(**kwargs)

        data.releases.append(self)

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

class WikiRelease(Data):
    """
    An older wiki-based release.
    """

    prerelease = False
    wiki = True

    def __init__(self, **kwargs):
        super(WikiRelease, self).__init__(**kwargs)
        data.releases.append(self)

        self.full_version = self.version

