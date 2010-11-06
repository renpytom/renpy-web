from flask import Flask, render_template
app = Flask(__name__)
app.debug = True

@app.route("/<name>.html")
def page(name):
    """
    Matches html-like pages and renders them using a template.
    """

    return render_template(name + ".html", name=name)

@app.route("/")
def index():
    """
    Renders the index page.
    """

    return page("index")

if __name__ == "__main__":
    app.run()
