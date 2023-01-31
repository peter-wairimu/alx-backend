#!/usr/bin/env python3
"""
Get locale from request
"""
from flask_babel import Babel
from flask import Flask, request, render_template


app = Flask(__name__)
babel = Babel(app)


class Config:
    """
    Config class
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object('2-app.Config')


@app.route('/', methods=['GET'], strict_slashes=False)
def index():
    """
    an index.html template
    """
    return render_template('2-index.html')


@babel.localeselector
def get_locale():
    """
    get_locale function
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
