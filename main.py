#!/usr/bin/env python

import sys
import os
import time
import datetime
import re
sys.path.insert(0, os.path.dirname(__file__))

from flask import Flask, render_template, abort, redirect, Response, request, abort
from docutils.core import publish_parts
import data
from werkzeug.contrib.atom import AtomFeed

import sponsors

app = Flask(__name__)


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
                prefix="[list]"
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
    return render_template('release.html', name='latest', release=data.current, data=data)


@app.route("/support.html")
def support():
    return redirect("/")


@app.route("/l/<name>")
def link(name):
    name = name.rstrip('/')

    links = {
        "license" : "/doc/html/license.html",
        "voicing" : "/doc/html/self_voicing.html",
        }

    return redirect(links.get(name, '/'))


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

    return render_template(
        "index.html",
        data=data,
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


@app.route("/artcard.html")
def artcard():
    return render_template("artcard.html", data=data)


@app.route("/feed/")
def feed():
    """
    Renders the atom feed.
    """

    feed = AtomFeed(
        "Ren'Py Visual Novel Engine",
        feed_url="http://www.renpy.org/feed/",
        url="http://www.renpy.org/"
        )

    prerelease = data.prerelease
    current = data.current

    def parse_date(s):
        ts = time.strptime(s, "%B %d, %Y")
        return datetime.datetime.fromtimestamp(time.mktime(ts))

    if prerelease:
        feed.add(
            u"Ren'Py {} Pre-Released".format(prerelease.version),
            unicode(render_template("feed.html", release=prerelease, mode="prerelease")),
            content_type="html",
            url="http://www.renpy.org/release/" + prerelease.version + "?mode=prerelease",
            updated=parse_date(prerelease.prerelease_date),
            author="Ren'Py Developers",
            )

    if current.patch_date:
        feed.add(
            u"Ren'Py Updated to {}".format(current.full_version),
            unicode(render_template("feed.html", release=current, mode="update")),
            content_type="html",
            url="http://www.renpy.org/release/" + current.version + "?mode=update&version=" + current.full_version,
            updated=parse_date(current.patch_date),
            author="Ren'Py Developers",
            )

    feed.add(
        u"Ren'Py {} Released".format(current.version),
        unicode(render_template("feed.html", release=current, mode="release")),
        content_type="html",
        url="http://www.renpy.org/release/" + current.version + "?mode=release",
        updated=parse_date(current.date),
        author="Ren'Py Developers",
        )

    return feed.get_response()



# For use under mod wsgi.
application = app

if __name__ == "__main__":
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument("--public", action='store_true', default=False)
    ap.add_argument("--port", action='store', type=int, default=5000)
    args = ap.parse_args()

    if args.public:
        app.run(host='0.0.0.0', port=args.port)
    else:
        app.run(debug=True, port=args.port)
