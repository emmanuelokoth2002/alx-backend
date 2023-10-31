#!/usr/bin/env python3
"""
This module sets up a Flask app with user mock login and display
messages based on login status.
"""
from typing import Any
from flask import Flask, render_template, g
from flask_babel import Babel, _, lazy_gettext

app = Flask(__name__)
babel = Babel(app)


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},

}


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
    Render the index.html template with login status messages.
    """
    return render_template('5-index.html', logged_in_as=lazy_gettext('You
                                                                      are logged in as %(username)s.'),
                           not_logged_in=lazy_gettext('You are not logged in.'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
