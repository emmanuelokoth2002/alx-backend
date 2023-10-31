#!/usr/bin/env python3
"""
This module sets up a Flask app with Flask-Babel extension and
language selection logic.
"""
from typing import Any
from flask import Flask, render_template, request
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)


class Config:
    """
    Config class to set available languages and default
    locale/timezone for Babel.
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
    Render the index.html template.
    """
    return render_template('2-index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
