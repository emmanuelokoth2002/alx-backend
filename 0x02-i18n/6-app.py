#!/usr/bin/env python3
"""
This module sets up a Flask app with prioritized locale selection based on user's preferences and request headers.
"""
from typing import Any
from flask import Flask, render_template, g, request
from flask_babel import Babel, _

app = Flask(__name__)
babel = Babel(app)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}

class Config:
    """
    Config class to set available languages and default locale/timezone for Babel.
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'

app.config.from_object(Config)

@babel.localeselector
def get_locale() -> str:
    """
    Determine the best-matching language based on user preferences, request
    header, or default locale.
    """
    # Locale from URL parameters
    if 'locale' in request.args and request.args['locale'] in app.config['LANGUAGES']:
        return request.args['locale']
    
    # Locale from user settings
    if g.user and g.user['locale'] in app.config['LANGUAGES']:
        return g.user['locale']
    
    # Locale from request header
    if request.accept_languages:
        return request.accept_languages.best_match(app.config['LANGUAGES'])
    
    # Default locale
    return app.config['BABEL_DEFAULT_LOCALE']

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
    Render the index.html template with localized content.
    """
    return render_template('6-index.html')
