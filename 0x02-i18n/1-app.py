#!/usr/bin/env python3
""" Module for Task 0"""
from flask import Flask
from flask_babel import Babel

app = Flask(__name__)


class Config:
    """ Config class for app"""
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)
babel = Babel(app)
