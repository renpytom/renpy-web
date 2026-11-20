import os
import csv
import datetime
import functools
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
    """
    A sponsor loaded from a Patreon export, with fields passed as keywords by the load_sponsorfn_* functions.
    Registers itself in `by_email`, so a later row with the same email replaces an earlier one.
    """

    name: str
    credit_name: str
    url: str
    email: str

    # The current pledge and lifetime support, in dollars.
    pledge: float
    lifetime: float

    # True if the pledge is currently paid.
    status: bool

    street: str
    city: str
    state: str
    zip: str
    country: str
    start: str

    level: Level

    # True unless the sponsor declined a postcard.
    raw_postcard: bool

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
    def banner_filename(self):
        """
        The banner image this sponsor's level calls for, relative to static/sponsors, such as
        "740x100/Moonbox Games.png". It may not exist.
        """

        return "{}x{}/{}.png".format(self.level.width, self.level.height, self.credit_name)

    @property
    def banner(self):

        fn = self.banner_filename

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

    if os.environ.get("MONTH", None):
        return os.environ["MONTH"]

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

    with open(fn, "r", encoding="utf-8") as f:

        l = f.readline()

        # if not rv:
        #     for i, s in enumerate(l.split("\t")):
        #         print(i, s)

        level = ''

        for l in f:

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


def read_rows_new(fn):
    """
    Yields the data rows of a new-format (2020-07 on) Patreon export, normalized to a fixed column layout whatever
    optional columns the export has: 1 and 6 are emails, 13 the tier, 24 the last charge status, and so on.
    """

    with open(fn, "r", encoding="utf-8", newline="") as f:

        rows = csv.reader(f, delimiter="\t")
        l = next(rows)

        # if not rv:
        #     for i, s in enumerate(l):
        #         print(i, s)

        has_twitter = l[7] == "Twitter"
        if not has_twitter:
            l.insert(7, 'Twitter')

        # for i, s in enumerate(l):
        #     print(i, s)

        has_discord = l[8] == "Discord"
        has_free = l[11] == "Free Member"
        has_free_trial = l[12] == "Free Trial"

        for l in rows:

            if len(l) < 12 or not any(l):
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

            yield l


def single_level(tier):
    """
    Returns the Level named by a Patreon tier, or None when the tier is unknown or lists several tiers (as Patreon
    does for a sponsor changing tiers, e.g. "Platinum Sponsor, Gold Sponsor").
    """

    return level_by_name.get(tier)


def first_level(tiers):
    """
    Returns the Level of the first known tier in a comma-separated list of Patreon tiers, or None if none is known.
    """

    for tier in tiers.split(","):
        tier = tier.strip()

        # Skip empty entries, since "" names the No Reward level.
        if not tier:
            continue

        level = level_by_name.get(tier)

        if level is not None:
            return level

    return None


@functools.cache
def levels_by_email(fn):
    """
    Maps each sponsor's email to their Level in the new-format export `fn`, leaving out rows without a single known
    tier. Cached, since past exports don't change and lookups would otherwise reread them on every request.
    """

    rv = { }

    for l in read_rows_new(fn):
        level = single_level(l[13])

        if level is not None:
            rv[l[1] or l[6]] = level

    return rv


def previous_level(fn, email):
    """
    Returns the sponsor's Level in the newest monthly export before `fn` that gives them a single known tier, or
    None if no new-format export does.
    """

    basefn = os.path.basename(fn)

    older = [ i for i in os.listdir(SPONSORSDIR) if len(i) == 11 and i.endswith(".tsv") ]
    older = [ i for i in older if "2020-07.tsv" <= i < basefn ]
    older.sort(reverse=True)

    for i in older:
        level = levels_by_email(os.path.join(SPONSORSDIR, i)).get(email)

        if level is not None:
            return level

    return None


def load_sponsorfn_new(fn):

    rv = [ ]

    for l in read_rows_new(fn):

        email = l[1] or l[6]

        level = single_level(l[13])

        # A sponsor changing tiers is listed under several, new tier first, e.g. "Platinum Sponsor, Gold Sponsor".
        # Take the first known one, or else the tier from the newest earlier export that has them.
        if level is None and "," in l[13]:
            level = first_level(l[13]) or previous_level(fn, email)

        if level is None:
            continue

        name = l[5]

        url = l[3]
        if url == 'n/a':
            url = ""

        # for i, s in enumerate(l):
        #     print(i, s)

        status = (l[24] == "Paid" or l[24] == "Active patron")

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
            email=email,
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
        raise
        return False

    global sponsors
    sponsors = sl

    print([(i.credit_name, i.status) for i in sl if i.credit_name == "Fallen Eros"])

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
    non_banner_sponsors = non_banner()
    return random.sample(non_banner_sponsors, min(8, len(non_banner_sponsors)))


def anonymous_count():
    return(len([i for i in sponsors if i.level.count if not i.level.public]))


def index_more_count():
    return len([ i for i in sponsors if i.level.count if not i.level.banner]) - 4
