#!/usr/bin/env python3
""" Module for Task 0"""
from flask import Flask
from flask_babel import Babel


class Config():
    """ Config class"""
    LANGUAGES = ["en", "fr"]


app = Flask(__name__)
babel = Babel(app, Config, default_locale='en', default_timezone='UTC')
