"""
Google reCAPTCHA v2 ("I'm not a robot" checkbox) for Flask.

This replaces the unmaintained Flask-ReCaptcha package, which imports `jinja2.Markup` and so fails with Jinja2 3.1
and later. It keeps the same interface: `ReCaptcha(app)` reads `RECAPTCHA_SITE_KEY` and `RECAPTCHA_SECRET_KEY` from
the app config and makes `{{ recaptcha }}` available to templates, and `verify()` checks the current request.
"""

import http.client
import json
import urllib.parse
import urllib.request

from flask import request
from markupsafe import Markup


VERIFY_URL = "https://www.google.com/recaptcha/api/siteverify"


class ReCaptcha:
    """
    Renders the reCAPTCHA widget and verifies the responses submitted with it.
    """

    def __init__(self, app=None):
        self.site_key = None
        self.secret_key = None

        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        """
        Reads the keys from `app.config` and registers a context processor that defines `recaptcha` in every
        template as the widget's HTML.
        """

        self.site_key = app.config.get("RECAPTCHA_SITE_KEY")
        self.secret_key = app.config.get("RECAPTCHA_SECRET_KEY")

        @app.context_processor
        def recaptcha_context():
            return dict(recaptcha=self.get_code())

    def get_code(self):
        """
        Returns the HTML for the widget, which must be placed inside the form whose submission is verified.
        """

        return Markup(
            "<script src='https://www.google.com/recaptcha/api.js' async defer></script>\n"
            '<div class="g-recaptcha" data-sitekey="{}"></div>'
        ).format(self.site_key)

    def verify(self):
        """
        Returns True if the current request carries a reCAPTCHA response that Google accepts. Returns False if the
        response is missing or rejected, or if Google cannot be reached.
        """

        response = request.form.get("g-recaptcha-response")

        if not response:
            return False

        body = urllib.parse.urlencode({
            "secret": self.secret_key,
            "response": response,
            "remoteip": request.remote_addr or "",
        }).encode("utf-8")

        try:
            with urllib.request.urlopen(VERIFY_URL, body, timeout=10) as f:
                result = json.load(f)
        except (OSError, ValueError, http.client.HTTPException):
            return False

        return bool(result.get("success"))
