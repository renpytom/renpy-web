#!/usr/bin/env python

import sys
import os
import time
import datetime
import re
import json
import random
import pytz
import doc

sys.path.insert(0, os.path.dirname(__file__))

from flask import Flask, render_template, abort, redirect, Response, request, abort, jsonify, make_response
from docutils.core import publish_parts
import data
from feedgen.feed import FeedGenerator

from flask_recaptcha import ReCaptcha

import sponsors

app = Flask(__name__)

app.config["RECAPTCHA_SITE_KEY"] = "6LeYkrsSAAAAACS53DFTOCeeslDtcVVSdv0K2ZuS"
app.config["RECAPTCHA_SECRET_KEY"] = "6LeYkrsSAAAAAEUjiS_oEeuSSxEDbshkr1ao5exQ"

recaptcha = ReCaptcha(app=app)

BASE = os.path.dirname(__file__)


@app.before_request
def before_request():
    sponsors.init(os.environ.get("MONTH", None))


@app.template_filter('rst')
def rst_filter(s):
    parts = publish_parts(s, writer_name='html4css1')
    return parts["fragment"]


@app.route("/release/<name>")
def release(name):
    if name not in data.release_version:
        abort(404)

    release = data.release_version[name]

    return render_template('release.html', release=release, data=data)


@app.route("/release/<name>.txt")
def release_txt(name):
    if name not in data.release_version:
        abort(404)

    release = data.release_version[name]

    rv = render_template('release.txt', release=release, data=data)

    output = [ ]
    line = ""

    for l in rv.split("\n"):
        l = l.strip()

        if not l:
            output.append(line)
            output.append('')
            line = ""

        elif l[0] == '*':
            output.append(line)
            line = ""

        if line:
            line = line + " " + l
        else:
            line = l

    output.append(line)

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

        if l.startswith("*"):
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

    rv = "\n".join(rv)

    return Response(rv, mimetype="text/plain")


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


@app.route("/agegate")
def agegate():
    url = request.args.get("url", "/")

    for i in sponsors.sponsors:
        if i.url == "https://www.renpy.org/agegate?url=" + url:
            break
    else:
        abort(404)

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
    return render_template("artcard.html", data=data)


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

    prerelease_7 = data.prerelease_7
    current_7 = data.current_7

    def parse_date(s):
        ts = time.strptime(s, "%B %d, %Y")
        return datetime.datetime.fromtimestamp(time.mktime(ts), pytz.utc)

    def add(release, version, date, mode):
        suffix = "?mode=" + mode + "&version=" + version
        fe = fg.add_entry()
        fe.id("http://www.renpy.org/release/" + version + suffix)
        fe.link(href="https://www.renpy.org/release/" + version + suffix, rel="alternate")

        if mode == "prerelease":
            fe.title(u"Ren'Py {} Pre-Released".format(version))
        else:
            fe.title(u"Ren'Py {} Released".format(version))

        fe.content(
            content=render_template("feed.html", release=release, mode=mode),
            type="text/html"
        )
        fe.updated(parse_date(date))

    if prerelease_7:
        add(prerelease_7, prerelease_7.version, prerelease_7.prerelease_date, "prerelease-7")

    if prerelease_8:
        add(prerelease_8, prerelease_8.version, prerelease_8.prerelease_date, "prerelease-8")

    if current_7.patch_date:
        add(current_7, current_7.full_version, current_7.patch_date, "update-7")

    if current_8 and current_8.patch_date:
        add(current_8, current_8.full_version, current_8.patch_date, "update-8")

    add(current_7, current_7.version, current_7.date, "release-7")

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
        "Release (Ren'Py 8, Python 3)",
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
        "Prerelease (Ren'Py 8, Python 3)",
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
        "Nightly Fix (Ren'Py 8, Python 3)",
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
        "Nightly (Ren'Py 8, Python 3)",
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


# For use under mod wsgi.
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
