import os
import zlib

ROLES = {
    'py:attribute' : 5,
    'py:class' : 5,
    'py:exception' : 5,
    'py:function' : 5,
    'py:method' : 5,
    'std:doc' : 3,
    'std:label' : 2,
    'std:style-property' : 4,
    'std:text-tag' : 4,
    'std:token' : 0,
    'std:transform-property' : 3,
    'std:var' : 5,
}

PATHS = [
    "/home/tom/WWW.renpyorg/doc/html/objects.inv",
    "/home/tom/ab/renpy/doc/objects.inv",
]

def get_doc_map():

    # Find the path.
    for path in PATHS:
        if os.path.exists(path):
            break
    else:
        print("Not found")
        return { }

    # Load the index.
    with open(path, "rb") as f:
        for _ in range(4):
            f.readline()

        index = f.read()

    index = zlib.decompress(index)
    index = index.decode("utf-8")

    # Finds a map from a name to a URI.

    rv = { }
    priority_map = { }

    for l in index.splitlines():
        if not l:
            continue

        a = l.split(' ', 4)

        name, role, priority, uri, displayname = a
        uri = uri.replace("$", name)

        if displayname == "-":
            displayname = name

        role_priority = ROLES.get(role, -1)

        if name in rv  and priority_map[name] >= role_priority:
            continue

        rv[name] = uri
        priority_map[name] = role_priority

    return rv
