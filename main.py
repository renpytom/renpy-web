#!bin/python

import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from flask import Flask, render_template, abort
from docutils.core import publish_parts
import data

app = Flask(__name__)

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

@app.route("/latest.html")
def latest():
    return render_template('release.html', name='latest', release=data.current, data=data)

@app.route("/<name>.html")
def page(name):
    """
    Matches html-like pages and renders them using a template.
    """

    return render_template(name + ".html", name=name, data=data)

@app.route("/")
def index():
    """
    Renders the index page.
    """

    return render_template("index.html", data=data)

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

