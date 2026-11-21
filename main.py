#!/usr/bin/env python

import sys
import os
import time
import datetime
import re
import json
import random
from urllib.parse import unquote_plus, urlencode, urlsplit, urlunsplit
import pytz
import doc

sys.path.insert(0, os.path.dirname(__file__))

from flask import Flask, render_template, abort, redirect, Response, request, abort, jsonify, make_response
from docutils.core import publish_parts
from markupsafe import escape, Markup
import data
from feedgen.feed import FeedGenerator

from recaptcha import ReCaptcha

import sponsors

app = Flask(__name__)

app.config["RECAPTCHA_SITE_KEY"] = "6LeYkrsSAAAAACS53DFTOCeeslDtcVVSdv0K2ZuS"
app.config["RECAPTCHA_SECRET_KEY"] = "6LeYkrsSAAAAAEUjiS_oEeuSSxEDbshkr1ao5exQ"

recaptcha = ReCaptcha(app=app)

BASE = os.path.dirname(__file__)


sponsors.init()


@app.before_request
def before_request():
    sponsors.ensure_loaded()


@app.template_filter('rst')
def rst_filter(s):
    parts = publish_parts(s, writer_name='html4css1')
    return parts["fragment"]


# Matches a GitHub issue reference like #7522. The lookbehind skips HTML entities (&#39;, or &amp;#3 after escaping),
# URL fragments, and words.
ISSUE_RE = re.compile(r'(?<![\w&/#;])#(\d+)\b')


def link_issues(s):
    """
    Turns issue references like #7522 in the HTML or escaped text `s` into links to the Ren'Py issue tracker.
    """

    return ISSUE_RE.sub(r'<a href="https://github.com/renpy/renpy/issues/\1">#\1</a>', s)


@app.template_filter('issues')
def issues_filter(s):
    return link_issues(s)


@app.route("/release/<name>")
def release(name):
    if name not in data.release_version:
        abort(404)

    release = data.release_version[name]

    return render_template('release.html', release=release, data=data)


def is_list_item(l):
    """
    Returns true if the stripped line `l` starts a `*` list item. A bullet needs a space after the *, so lines
    opening with *emphasis* or **bold** are not items.
    """

    return l.startswith("* ") or l == "*"


def join_lines(text):
    """
    Unwraps the hard-wrapped plain text produced by the release.txt template.

    Returns a list of logical lines: each paragraph and each `*` list item becomes a single line, with whitespace
    stripped. Paragraphs are followed by an empty string, so runs of empty strings may occur.
    """

    output = [ ]
    line = ""

    for l in text.split("\n"):
        l = l.strip()

        if not l:
            output.append(line)
            output.append('')
            line = ""

        elif is_list_item(l):
            output.append(line)
            line = ""

        if line:
            line = line + " " + l
        else:
            line = l

    output.append(line)

    return output


def render_release_bbcode(release):
    """
    Returns the announcement of `release` as BBCode, for forum posts.
    """

    rv = render_template('release.txt', release=release, data=data)

    output = join_lines(rv)

    rv = [ ]
    in_list = False
    last_empty = False

    for l in output:

        if not l:
            if last_empty:
                continue
            last_empty = True
        else:
            last_empty = False

        is_item = is_list_item(l)

        # Convert markdown bold to BBCode.
        l = re.sub(r'\*\*(.+?)\*\*', r'[b]\1[/b]', l)

        if is_item:
            if not in_list:
                prefix = "[list]"
                in_list = True
            else:
                prefix = ""

            rv.append(prefix + "[*]" + l[1:])
            continue

        if in_list:
            rv.append('[/list]')
            in_list = False

        rv.append(l)

    return "\n".join(rv)


def render_release_markdown(release):
    """
    Returns the announcement of `release` as GitHub-flavored markdown, suitable for a GitHub release body.
    """

    text = render_template('release.txt', release=release, data=data, markdown=True)

    rv = [ ]
    in_list = False

    for l in join_lines(text):

        # Convert RST inline literals to markdown code spans.
        l = re.sub(r'``(.+?)``', r'`\1`', l)

        is_item = is_list_item(l)

        # Separate lists from the surrounding paragraphs.
        if is_item != in_list and rv and rv[-1]:
            rv.append('')

        in_list = is_item

        # Use the more conventional - as the bullet marker.
        if is_item:
            l = "- " + l[1:].lstrip()

        if not l and rv and not rv[-1]:
            continue

        rv.append(l)

    return "\n".join(rv).strip() + "\n"


@app.route("/release/<name>.md")
def release_md(name):
    """
    Serves the release announcement as markdown. Used by release tooling to fill in the GitHub release body.
    """

    if name not in data.release_version:
        abort(404)

    return Response(render_release_markdown(data.release_version[name]), mimetype="text/markdown")


# Matches a markdown [text](url) link (groups 1 and 2) or a bare URL (group 3). A bare URL doesn't take trailing
# punctuation, so "see https://example.com." links without the period.
LINK_RE = re.compile(r'\[([^\]]+)\]\((https?://[^)\s]+)\)|(https?://\S*[^\s.,;:!?)])')


def convert_text_to_html(s):
    """
    Escapes the plain text `s`, then converts its **bold**, ``code``, and #NNNN issue references to HTML.
    """

    s = str(escape(s))
    s = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', s)
    s = re.sub(r'``(.+?)``', r'<code>\1</code>', s)

    return link_issues(s)


def convert_inline_to_html(l):
    """
    Converts one logical line of release.txt (markdown flavor) to HTML, including [text](url) links and bare URLs.
    """

    rv = [ ]
    pos = 0

    for m in LINK_RE.finditer(l):
        rv.append(convert_text_to_html(l[pos:m.start()]))

        if m.group(3):
            text = url = m.group(3)
        else:
            text, url = m.group(1), m.group(2)

        rv.append('<a href="{}">{}</a>'.format(escape(url), convert_text_to_html(text)))
        pos = m.end()

    rv.append(convert_text_to_html(l[pos:]))

    return "".join(rv)


def convert_lines_to_html(lines):
    """
    Converts the logical lines produced by `join_lines` to HTML: "* " items become a list, and other non-empty
    lines become paragraphs.
    """

    rv = [ ]
    in_list = False

    for l in lines:
        if not l:
            continue

        is_item = is_list_item(l)

        if is_item and not in_list:
            rv.append("<ul>")
        elif in_list and not is_item:
            rv.append("</ul>")

        in_list = is_item

        if is_item:
            rv.append("<li>" + convert_inline_to_html(l[1:].strip()) + "</li>")
        else:
            rv.append("<p>" + convert_inline_to_html(l) + "</p>")

    if in_list:
        rv.append("</ul>")

    return "\n".join(rv)


def render_release_html(release):
    """
    Returns the announcement of `release` as rich HTML, meant to be copied and pasted into sites that accept
    formatted text. It has the same content as the BBCode and markdown versions.
    """

    text = render_template('release.txt', release=release, data=data, markdown=True)

    return Markup(convert_lines_to_html(join_lines(text)))


def get_releasenotes_releases():
    """
    Returns the (prerelease, final) releases the /releasenotes page offers. `final` is the newest public 8.x final
    release. `prerelease` is the newest 8.x release if it's a prerelease, public or private (an announcement is
    prepared before the prerelease is made public), and None otherwise.
    """

    releases_8 = [ i for i in data.releases if i.major >= 8 and not i.wiki ]

    prerelease = releases_8[0] if releases_8 and releases_8[0].prerelease else None
    final = next((i for i in releases_8 if not i.prerelease and not i.invisible), None)

    return prerelease, final


@app.route("/releasenotes")
def releasenotes():
    """
    Renders the release checklist and copyable announcements (BBCode, markdown, rich HTML) for the current prerelease
    and final release. A private tool, so it asks search engines not to index it.
    """

    prerelease, final = get_releasenotes_releases()

    tabs = [ ]

    for kind, release in (("prerelease", prerelease), ("release", final)):
        if release is None:
            continue

        tabs.append(dict(
            kind=kind,
            release=release,
            bbcode=render_release_bbcode(release),
            markdown=render_release_markdown(release),
            html=render_release_html(release),
        ))

    response = make_response(render_template('releasenotes.html', tabs=tabs))
    response.headers.set('X-Robots-Tag', 'noindex, nofollow')

    return response


@app.route("/latest.html")
def latest():
    return render_template('release.html', name='latest', release=data.current_8 or data.current_7, data=data)

@app.route("/latest-7.html")
def latest_7():
    return render_template('release.html', name='latest', release=data.current_7, data=data)


@app.route("/support.html")
def support():
    return redirect("/")


@app.route("/l/<path:name>")
def link(name):
    name = name.rstrip('/')

    links = {
        "license" : "/doc/html/license.html",
        "voicing" : "/doc/html/self_voicing.html",
        }

    return redirect(links.get(name, '/'))


@app.route("/wiki/<path:path>")
def wiki(path):
    fn = os.path.join(BASE, "wiki", "page", path + ".html")

    if not os.path.exists(fn):
        raise abort(404)

    with open(fn, "rb") as f:
        content = f.read()

    try:
        content = content.decode("utf-8")
    except:
        content = content.decode("latin-1")

    obsolete = not path.startswith("renpy/releases")
    title = os.path.basename(path).replace("_", " ")

    if not obsolete:
        download = "https://www.renpy.org/dl/" + os.path.basename(path) + "/"
    else:
        download = None

    return render_template('wiki.html', content=content, obsolete=obsolete, title=title, download=download)


@app.route("/<name>.html")
def page(name):
    """
    Matches html-like pages and renders them using a template.
    """

    return render_template(name + ".html", name=name, data=data)


@app.route("/robots.txt")
def robots_txt():
    rv = """\
User-agent: *
Disallow: /wiki/renpy/doc/reference/
Disallow: /w/
"""

    return Response(rv, mimetype="text/plain")


@app.route("/")
def index():
    """
    Renders the index page.
    """

    FEATURED = os.path.join(BASE, "static/featured")
    featured = [ ]

    for i in os.listdir(FEATURED):
        if not (i.endswith(".jpg") or i.endswith(".png")):
            continue

        with open(os.path.join(FEATURED, i.rpartition(".")[0] + ".html"), "r") as f:
            html = f.read()

        featured.append((i, html))

    featured = random.sample(featured, 5)

    return render_template(
        "index.html",
        data=data,
        featured=featured,
        banner_sponsors=sponsors.banner(),
        non_banner_sponsors=sponsors.sample_non_banner(),
        more_sponsors=sponsors.index_more_count(),
        )


@app.route("/sponsors.html")
def sponsors_page():
    return render_template(
        "sponsors.html",
        data=data,
        banner_sponsors=sponsors.banner(),
        non_banner_sponsors=sponsors.non_banner(),
        anonymous_sponsors=sponsors.anonymous_count(),
        current_month=sponsors.current_month(),
        )


AGEGATE_PREFIX = "https://www.renpy.org/agegate?url="
"""
The start of a sponsor link that sends visitors through the age gate. The rest of the link is the destination.
"""


def agegate_destination(sponsor_url: str) -> str | None:
    """
    Returns the destination of a sponsor's age gate link, decoded, or None if the link doesn't go through the age
    gate. Sponsors write the destination with or without encoding its ? and other characters, so everything after
    the prefix is taken as the destination.
    """

    if not sponsor_url.startswith(AGEGATE_PREFIX):
        return None

    return unquote_plus(sponsor_url[len(AGEGATE_PREFIX):])


@app.route("/agegate")
def agegate():
    url = request.args.get("url", "/")

    if not any(agegate_destination(i.url) == url for i in sponsors.sponsors):
        abort(404)

    # Pass query parameters other than url (like utm_source=) along to the destination.
    extra = [ (k, v) for k, v in request.args.items(multi=True) if k != "url" ]

    if extra:
        parts = urlsplit(url)
        query = "&".join(i for i in (parts.query, urlencode(extra)) if i)
        url = urlunsplit(parts._replace(query=query))

    return render_template(
        "agegate.html",
        url=url)


@app.route("/email", methods=[ "GET", "POST" ])
def email():

    verified = False

    if (request.method == "POST") and recaptcha.verify():
        verified = True

    return render_template(
        "email.html",
        verified=verified,
        )


@app.route("/artcard.html")
def artcard():
    artcard_dir = os.path.join(BASE, "static", "artcard")
    cards = [ ]

    for filename in os.listdir(artcard_dir):
        if not re.match(r"^\d{4}-\d{2}\.(jpg|jpeg|png|webp)$", filename, re.IGNORECASE):
            continue

        cards.append(filename)

    cards.sort()

    return render_template("artcard.html", data=data, cards=cards)


@app.route("/feed/")
def feed():
    """
    Renders the atom feed.
    """

    fg = FeedGenerator()
    fg.id("http://www.renpy.org/feed/")
    fg.title("Ren'Py Visual Novel Engine")
    fg.description("Ren'Py Visual Novel Engine")
    fg.link(href="https://www.renpy.org", rel="alternate")
    fg.language("en")

    prerelease_8 = data.prerelease_8
    current_8 = data.current_8

    def parse_date(s):
        ts = time.strptime(s, "%B %d, %Y")
        return datetime.datetime.fromtimestamp(time.mktime(ts), pytz.utc)

    def add(release, version, date, mode):
        suffix = "?mode=" + mode + "&version=" + version
        fe = fg.add_entry()
        fe.id("http://www.renpy.org/release/" + version + suffix)
        fe.link(href="https://www.renpy.org/release/" + version + suffix, rel="alternate")

        if mode.startswith("prerelease"):
            fe.title(u"Ren'Py {} Pre-Released".format(version))
        else:
            fe.title(u"Ren'Py {} Released".format(version))

        fe.content(
            content=render_template("feed.html", release=release, mode=mode),
            type="text/html"
        )
        fe.updated(parse_date(date))

    # The prerelease date comes from the SDK zip, so it's None until the prerelease has been uploaded.
    if prerelease_8 and prerelease_8.prerelease_date:
        add(prerelease_8, prerelease_8.version, prerelease_8.prerelease_date, "prerelease-8")

    if current_8 and current_8.patch_date:
        add(current_8, current_8.full_version, current_8.patch_date, "update-8")

    if current_8:
        add(current_8, current_8.version, current_8.date, "release-8")


    response = make_response(fg.rss_str())
    response.headers.set('Content-Type', 'application/rss+xml')

    return response


@app.route("/channels.json")
def channels():

    rv = [ ]
    seen = set()

    request_version = request.values.get("version", "7.0.0")

    allow_7 = request_version.split(".")[0] == "7"

    def scan_version(channel, url, description, always, *paths):
        for path in paths:

            updates_json = os.path.join(path, "updates.json")

            if os.path.exists(updates_json):
                break

        else:
            return

        with open(updates_json, "r") as f:
            u = json.load(f)

        sdk = u["sdk"]

        version = sdk["pretty_version"].split()[1]

        if (not always) and (version in seen):
            return

        seen.add(version)

        record = {
            "channel" : channel,
            "url" : url,
            "pretty_version" : version,
            "split_version" : [ int(i) for i in version.partition("+")[0].split(".") ],
            "description" : description,
            "timestamp" : os.path.getmtime(updates_json),
            }

        if record["split_version"][0] == 7 and not allow_7:
            return

        rv.append(record)

    scan_version(
        "Release",
        "http://update.renpy.org/release-8/updates.json",
        "{b}Recommended.{/b} The version of Ren'Py that should be used in all newly-released games.",
        True,
        "/home/tom/WWW.update/release-8",
        "/home/tom/ab/renpy/dl/release-8",
        )

    scan_version(
        "Release (Ren'Py 7, Python 2)",
        "http://update.renpy.org/release-7/updates.json",
        "{b}Recommended.{/b} The version of Ren'Py that should be used in all newly-released games.",
        True,
        "/home/tom/WWW.update/release-7",
        "/home/tom/ab/renpy/dl/release-7",
        )

    scan_version(
        "Prerelease",
        "http://update.renpy.org/prerelease-8/updates.json",
        "A preview of the next version of Ren'Py that can be used for testing and taking advantage of new features, but not for final releases of games.",
        False,
        "/home/tom/WWW.update/prerelease-8",
        "/home/tom/ab/renpy/dl/prerelease-8",
        )

    scan_version(
        "Prerelease (Ren'Py 7, Python 2)",
        "http://update.renpy.org/prerelease-7/updates.json",
        "A preview of the next version of Ren'Py that can be used for testing and taking advantage of new features, but not for final releases of games.",
        False,
        "/home/tom/WWW.update/prerelease-7",
        "/home/tom/ab/renpy/dl/prerelease-7",
        )

    scan_version(
        "Nightly Fix",
        "http://nightly.renpy.org/current-8-fix/updates.json",
        "A nightly build of fixes to the release version of Ren'Py.",
        True,
        "/home/tom/WWW.nightly/current-8-fix",
        "/home/tom/ab/WWW.nightly/current-8-fix",
        )

    scan_version(
        "Nightly Fix (Ren'Py 7, Python 2)",
        "http://nightly.renpy.org/current-7-fix/updates.json",
        "A nightly build of fixes to the release version of Ren'Py.",
        True,
        "/home/tom/WWW.nightly/current-7-fix",
        "/home/tom/ab/WWW.nightly/current-7-fix",
        )

    scan_version(
        "Nightly",
        "http://nightly.renpy.org/current-8/updates.json",
        "The bleeding edge of Ren'Py development. This may have the latest features, or might not run at all.",
        True,
        "/home/tom/WWW.nightly/current-8",
        "/home/tom/ab/WWW.nightly/current-8",
        )

    scan_version(
        "Nightly (Ren'Py 7, Python 2)",
        "http://nightly.renpy.org/current-7/updates.json",
        "The bleeding edge of Ren'Py development. This may have the latest features, or might not run at all.",
        True,
        "/home/tom/WWW.nightly/current-7",
        "/home/tom/ab/WWW.nightly/current-7",
        )

    response = jsonify({ "releases" : rv })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route("/jdk/<int:version>")
def jdk(version):
    return redirect("https://adoptium.net/temurin/releases/?version=" + str(version))

@app.route("/d/<path:path>")
def d(path):
    doc_map = doc.get_doc_map()

    path = path.strip()

    if path in doc_map:
        return redirect("https://www.renpy.org/doc/html/" + doc_map[path])
    else:
        return f"Couldn't find {path}.", 404


# WSGI entry point, served by gunicorn as main:application (see renpyweb.service).
application = app

if __name__ == "__main__":
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument("--public", action='store_true', default=False)
    ap.add_argument("--port", action='store', type=int, default=5000)
    args = ap.parse_args()

    if args.public:
        app.run(host='0.0.0.0', port=args.port, debug=True)
    else:
        app.jinja_env.auto_reload = True
        app.run(debug=True, port=args.port)
