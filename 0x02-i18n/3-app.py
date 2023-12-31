#!/usr/bin/env python3
"""
This module sets up a Flask app with Flask-Babel extension, using translations.
"""
from typing import Any
from flask import Flask, render_template
from flask_babel import Babel, _

app = Flask(__name__)
babel = Babel(app)


class Config:
    """
    Config class to set available languages and default locale/timezone
    for Babel.
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'

app.config.from_object(Config)


@babel.localeselector
def get_locale() -> str:
    """
    Determine the best-matching language based on request.accept_languages.
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index() -> Any:
    """
    Render the index.html template with internationalized text.
    """
    return render_template('3-index.html', home_title=_('home_title'),
                           home_header=_('home_header'))
