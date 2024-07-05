#!/usr/bin/env python3
""" Module for Task 0"""
from flask import Flask, request, render_template
from flask_babel import Babel

app = Flask(__name__)


class Config:
    """ Config class for app"""
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'
    DEBUG = True


app.config.from_object(Config)
app.url_map.strict_slashes = False
babel = Babel(app)


@babel.localeselector
def get_locale():
    """ get locale"""

    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    '''default route
    '''
    if request.args.get('locale') in app.config['LANGUAGES']:
        return render_template("2-index.html")
    else:
        return None


if __name__ == "__main__":
    app.run()
