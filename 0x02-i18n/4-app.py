#!/usr/bin/env python3
"""
This module sets up a Flask app with Flask-Babel extension and
supports forcing a particular locale.
"""
from flask import Flask, render_template, request
from flask_babel import Babel
app = Flask(__name__)
babel = Babel(app)


class Config(object):
    """
    Config class to set available languages and default
    locale/timezone for Babel.
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


@app.route('/')
def index_page():
    """
    Render the index.html template with internationalized text.
    """
    return render_template('4-index.html')


@babel.localeselector
def get_locale():
    """
    Determine the best-matching language based on request.accept_languages
    or forced locale.
    """
    requested_locale = request.args.get('locale')

    if requested_locale and requested_locale in Config.LANGUAGES:
        return requested_locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])
