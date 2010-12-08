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

    def __init__(self, **kwargs):
        super(Release, self).__init__(**kwargs)
        data.releases.append(self)

class WikiRelease(Data):
    """
    An older wiki-based release.
    """
    
    prerelease = False
    wiki = True
    
    def __init__(self, **kwargs):
        super(WikiRelease, self).__init__(**kwargs)
        data.releases.append(self)
    
