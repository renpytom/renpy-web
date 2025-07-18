import os
import datetime
import dateutil.relativedelta
import random

STATICSPONSORS = os.path.join(os.path.abspath(os.path.dirname(__file__)), "static", "sponsors")
SPONSORSDIR = os.path.join(os.path.abspath(os.path.dirname(__file__)), "sponsors")

level_by_name = { }


class Level(object):

    def __init__(self, name, newname, postcard=True, banner=None, span=None, public=True, count=True):
        self.name = name
        self.newname = newname
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
        level_by_name[self.newname] = self


Level("500 + Reward", "Diamond Sponsor", True, (740, 150), "col-md-12")
Level("250 + Reward", "Platinum Sponsor", True, (740, 100), "col-md-12")
Level("100 + Reward", "Gold Sponsor", True, (350, 100), "col-md-6")

Level("10 + Reward", "Silver Postcard Sponsor", True)
Level("2 + Reward", "Bronze Sponsor", False)
Level("1 + Reward", "Secret Sponsor", False, public=False)
Level("No Reward", "", False, public=False)

Level("Admin", "Admin", postcard=True, public=False, count=False)

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

    @property
    def banner(self):

        fn = "{}x{}/{}.png".format(self.level.width, self.level.height, self.credit_name)

        if os.path.exists(os.path.join(STATICSPONSORS, fn)):
            return "/static/sponsors/" + fn
        else:
            return None


def latest_month():

    tsvs = [ i for i in os.listdir(SPONSORSDIR) if (len(i) == 11) if i.endswith(".tsv") ]
    tsvs.sort()
    return tsvs[-1][:-4]


def current_month(offset=0):
    # Figure out the sponsor filename for today.

    today = datetime.date.today()
    today = today + dateutil.relativedelta.relativedelta(months=offset)

    if today.day < 15:
        today = today - datetime.timedelta(days=15)

    if today < datetime.date(2017, 6, 15):
        today = datetime.date(2017, 6, 15)

    return "{:04d}-{:02d}".format(
        today.year,
        today.month,
        )


def load_sponsorfn_old(fn):

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

            if l[5] in level_by_name:
                level = level_by_name[l[5]]
                continue

            name = l[5] + " " + l[6]

            url = l[3]
            if url == 'n/a':
                url = ""

            status = (l[10] == "Ok") or (l[10] == "Processed")

            while len(l) < 18:
                l.append('')

            s = Sponsor(
                name=name,
                credit_name=l[2] or name,
                url=url,
                email=l[7],
                pledge=float(l[8].replace(",", "")),
                lifetime=float(l[9].replace(",", "")),
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


def load_sponsorfn_new(fn):

    rv = [ ]

    with open(fn, "rb") as f:

        l = f.readline()

        l = l.decode("utf-8")
        l = l.rstrip()
        l = l.split("\t")

        has_twitter = l[7] == "Twitter"
        if not has_twitter:
            l.insert(7, 'Twitter')

        # for i, s in enumerate(l):
        #     print(i, s)

        has_discord = l[8] == "Discord"
        has_free = l[11] == "Free Member"
        has_free_trial = l[12] == "Free Trial"

        level = ''

        for l in f:
            l = l.decode("utf-8")
            l = l.rstrip()
            l = l.split("\t")

            if len(l) < 12:
                continue

            if not has_twitter:
                l.insert(7, 'Twitter')

            if has_free_trial:
                l.pop(12)

            if has_free:
                l.pop(11)

            if has_discord:
                l.pop(8)
                l.insert(22, '')

            if l[13] in level_by_name:
                level = level_by_name[l[13]]
            else:
                continue

            name = l[5]

            url = l[3]
            if url == 'n/a':
                url = ""

            # for i, s in enumerate(l):
            #     print(i, s)

            status = (l[24] == "Paid")

            if "Declined patron" in l:
                status = False

            if "Former patron" in l:
                status = False

            while len(l) < 18:
                l.append('')

            def money(s):
                s = s.replace("$", "")
                s = s.replace(",", "")
                return float(s)

            s = Sponsor(
                name=name,
                credit_name=l[2] or name,
                url=url,
                email=l[6],
                pledge=money(l[11]),
                lifetime=money(l[10]),
                status=status,
                street=l[15],
                city=l[16],
                state=l[17],
                zip=l[18],
                country=l[19],
                start=l[21],
                level=level,
                raw_postcard=(l[4] != "No")
                )

            rv.append(s)

    return rv


def load_sponsorfn(fn):

    basefn = os.path.basename(fn)

    if basefn[0] == "2" and basefn >= "2020-07.tsv":
        return load_sponsorfn_new(fn)
    else:
        return load_sponsorfn_old(fn)


def init(month=None):
    today = datetime.date.today()

    offset = 0

    while True:

        month = current_month(offset)

        month_fn = "{}/{}.tsv".format(SPONSORSDIR, month)
        override_fn = "{}/overrides - main.tsv".format(SPONSORSDIR)

        if not os.path.exists(month_fn):
            offset -= 1
            continue

        break

    try:

        load_sponsorfn(month_fn)
        load_sponsorfn(override_fn)

        sl = [ i for i in by_email.values() if i.status ]
        sl.sort(key=lambda s : s.sort_key())
        sl.reverse()

    except Exception as e:
        print("Failed to load sponsors:", e)
        return False

    global sponsors
    sponsors = sl

    return True

def banner():
    rv = [ i for i in sponsors if i.level.banner  ]
    rv.sort(key=lambda s : s.sort_key())
    rv.reverse()
    return rv


def non_banner():
    rv = [ i for i in sponsors if not i.level.banner and i.level.public ]
    rv.sort(key=lambda s : s.sort_key())
    rv.reverse()
    return rv


def sample_non_banner():
    return random.sample(non_banner(), min(8, len(sponsors)))


def anonymous_count():
    return(len([i for i in sponsors if i.level.count if not i.level.public]))


def index_more_count():
    return len([ i for i in sponsors if i.level.count if not i.level.banner]) - 4
