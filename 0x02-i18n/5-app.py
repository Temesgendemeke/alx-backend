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



users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}

def define_user():
    """ define user"""
    user = request.args.get('login_as')
    if user in users:
        return users[user]
    return None

@app.before_request
def before_request():
    """ before request"""
    Flask.g.user = define_user()


@app.route('/')
def index():
    '''default route
    '''
    locale = request.args.get('locale', '').strip()
    if locale and locale in Config.LANGUAGES:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


if __name__ == "__main__":
    app.run()
