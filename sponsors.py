import os
import datetime
import random

SPONSORSDIR = os.path.join(os.path.abspath(os.path.dirname(__file__)), "sponsors")

level_by_name = { }


class Level(object):
    def __init__(self, name, postcard=True, banner=None, span=None, public=True, count=True):
        self.name = name
        self.postcard = postcard
        self.banner = banner
        self.span = span
        self.public = public
        self.count = count

        if banner:
            self.width = banner[0]
            self.height = banner[1]
        else:
            self.width = 0
            self.height = 0

        level_by_name[self.name] = self


Level("500 + Reward", True, (740, 150), "col-md-12")
Level("250 + Reward", True, (740, 100), "col-md-12")
Level("100 + Reward", True, (350, 100), "col-md-6")

Level("10 + Reward", True)
Level("2 + Reward", False)
Level("1 + Reward", False, public=False)
Level("No Reward", False, public=False)

Level("Admin", postcard=True, public=False, count=False)


# All sponsors, map from email to data object.
by_email = { }

# A list of good sponsors.
sponsors = [ ]


class Sponsor(object):

    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)
        by_email[self.email] = self

    def sort_key(self):
        return (
            self.pledge,
            self.lifetime,
            random.random(),
            )


def latest_month():

    tsvs = [ i for i in os.listdir(SPONSORSDIR) if (len(i) == 11) if i.endswith(".tsv") ]
    tsvs.sort()
    return tsvs[-1][:-4]


def current_month():
    # Figure out the sponsor filename for today.

    today = datetime.date.today()

    if today.day < 15:
        today = today - datetime.timedelta(days=15)

    if today < datetime.date(2017, 6, 15):
        today = datetime.date(2017, 6, 15)

    return "{:04d}-{:02d}".format(
        today.year,
        today.month,
        )


def load_sponsorfn(fn):

    rv = [ ]

    with open(fn, "rb") as f:

        l = f.readline()

#         for i, s in enumerate(l.split("\t")):
#             print(i, s)

        level = ''

        for l in f:
            l = l.decode("utf-8")
            l = l.rstrip()
            l = l.split("\t")

            if len(l) == 7:
                level = level_by_name[l[5]]
                continue

            name = l[5] + " " + l[6]

            url = l[3]
            if url == 'n/a':
                url = ""

            status = (l[10] == "Ok")

            s = Sponsor(
                name=name,
                credit_name=l[2] or name,
                url=url,
                email=l[7],
                pledge=float(l[8]),
                lifetime=float(l[9]),
                status=status,
                street=l[12],
                city=l[13],
                state=l[14],
                zip=l[15],
                country=l[16],
                start=l[17],
                level=level,
                raw_postcard=(l[4] != "No")
                )

            rv.append(s)

    return rv


def init(month=None):
    today = datetime.date.today()

    if month is None:
        month = current_month()

    filenames = [
        "{}/{}.tsv".format(SPONSORSDIR, month),
        "{}/overrides - main.tsv".format(SPONSORSDIR),
        ]

    for i in filenames:
        if not os.path.exists(i):
            return

        load_sponsorfn(i)

    sl = [ i for i in by_email.values() if i.status ]
    sl.sort(key=lambda s : s.sort_key())
    sl.reverse()

    global sponsors
    sponsors = sl


def banner():
    rv =  [ i for i in sponsors if i.level.banner ]
    rv.sort(key=lambda s : s.sort_key())
    rv.reverse()
    return rv


def non_banner():
    rv = [ i for i in sponsors if not i.level.banner and i.level.public ]
    rv.sort(key=lambda s : s.sort_key())
    rv.reverse()
    return rv


def sample_non_banner():
    return random.sample(non_banner(), 4)


def anonymous_count():
    return(len([i for i in sponsors if i.level.count if not i.level.public]))


def index_more_count():
    return len([ i for i in sponsors if i.level.count if not i.level.banner]) - 4
