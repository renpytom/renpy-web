import os
import datetime
import random

level_by_name = { }


class Level(object):
    def __init__(self, name, postcard=True, banner=None, span=None, public=True):
        self.name = name
        self.postcard = postcard
        self.banner = banner
        self.span = span
        self.public = public

        if banner:
            self.width = banner[0]
            self.height = banner[1]
        else:
            self.width = 0
            self.height = 0

        level_by_name[self.name] = self


Level("500 + Reward", True, (740, 150), "col-md-12")
Level("250 + Reward", True, (740, 100), "col-md-12")
Level("100 + Reward", True, (300, 100), "col-md-6")

Level("10 + Reward", True)
Level("2 + Reward", False)
Level("1 + Reward", False, public=False)
Level("No Reward", False, public=False)


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


def init():

    # Figure out the sponsor filename for today.

    today = datetime.date.today()

    if today.day < 15:
        today = today - datetime.timedelta(days=15)

    if today < datetime.date(2017, 6, 15):
        today = datetime.date(2017, 6, 15)

    sponsorfn = "{}/sponsors/{:04d}-{:02d}.tsv".format(
        os.path.abspath(os.path.dirname(__file__)),
        today.year,
        today.month,
        )

    if not os.path.exists(sponsorfn):
        return

    # Pull in the sponsors.

    with open(sponsorfn) as f:

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

    month = "{:04d}-{:02d}".format(today.year, today.month)

    with open(os.path.abspath(os.path.dirname(__file__)) + "/sponsors/overrides.txt") as f:
        for l in f:
            l = l.decode("utf-8")
            l = l.strip().split(None, 2)

            level = level_by_name[l[2]]

            s = by_email[l[0]]
            s.pledge = float(l[1])
            s.level = level

    # Manual overrides.
    if 'sunrider.visualnovel@gmail.com' in by_email:
        s = by_email['sunrider.visualnovel@gmail.com']
        s.credit_name = "Love in Space"
        s.url = "http://starnova.moe"

    global sponsors
    sponsors = [ i for i in by_email.values() if i.status ]
    sponsors.sort(key=lambda s : s.sort_key())
    sponsors.reverse()


def banner():
    return [ i for i in sponsors if i.level.banner ]


def non_banner():
    return [ i for i in sponsors if not i.level.banner and i.level.public ]


def sample_non_banner():
    return random.sample(non_banner(), 4)


def anonymous_count():
    return(len(i for i in sponsors if not i.level.public))


def index_more_count():
    return len([ i for i in sponsors if not i.level.banner]) - 4


init()
