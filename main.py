#!/usr/bin/python

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

if __name__ == "__main__":
    # app.run(debug=True)
    app.run(host='0.0.0.0', port=8008)
    
