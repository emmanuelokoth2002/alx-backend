#!/usr/bin/env python3
"""
This module sets up a Flask app to emulate a user login and display
messages based on login status.
"""
from typing import Any
from flask import Flask, render_template, g, request
from flask_babel import Babel, _, lazy_gettext

app = Flask(__name__)
babel = Babel(app)

# Mock User Table
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config:
    """
    Config class to set available languages, default locale,
    and default timezone for Babel.
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'

app.config.from_object(Config)


@app.before_request
def before_request() -> None:
    """
    Find a user if login_as exists and set it as a global on flask.g.user.
    """
    user_id = int(request.args.get('login_as', 0))
    g.user = users.get(user_id) if user_id in users else None


@app.route('/')
def index() -> Any:
    """
    Render the index.html template based on the user's login status.
    """
    return render_template('5-index.html')


@app.route('/logout')
def logout() -> Any:
    """
    Simulates a logout by setting g.user to None and redirecting
    to the home page.
    """
    g.user = None
    return render_template('5-index.html')
