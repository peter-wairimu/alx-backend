#!/usr/bin/env python3
"""
Get locale from request
"""
from flask_babel import Babel
from flask import Flask, request, render_template, g
import pytz.exceptions


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
    Config class
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object('6-app.Config')


@app.route('/', methods=['GET'], strict_slashes=False)
def index():
    """
    an index.html template
    """
    return render_template('6-index.html')


@babel.localeselector
def get_locale():
    """
    get_locale function
    """
    if request.args.get('locale'):
        locale = request.args.get('locale')
        if locale in app.config['LANGUAGES']:
            return locale
    elif g.user and g.user.get('locale')\
            and g.user.get('locale') in app.config['LANGUAGES']:
        return g.user.get('locale')
    else:
        return request.accept_languages.best_match(app.config['LANGUAGES'])


def get_user():
    """
    get user function
    """
    if request.args.get('login_as'):
        user = int(request.args.get('login_as'))
        if user in users:
            print(user)
            return users.get(user)
    else:
        return None


@app.before_request
def before_request():
    """
    before request function
    """
    g.user = get_user()


@babel.timezoneselector
def get_timezone():
    """
    get timezone function
    """
    if request.args.get('timezone'):
        timezone = request.args.get('timezone')
        try:
            return timezone(timezone).zone
        except pytz.exceptions.UnknownTimeZoneError:
            return None
    elif g.user and g.user.get('timezone'):
        try:
            return timezone(g.user.get('timezone')).zone
        except pytz.exceptions.UnknownTimeZoneError:
            return None
    else:
        return request.accept_languages.best_match(app.config['LANGUAGES'])


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
