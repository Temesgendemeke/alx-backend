#!/usr/bin/env python3
""" Module for Task 0"""
from flask import Flask, render_template


app = Flask(__name__, template_folder='templates')


@app.route("/", methods=['GET'], strict_slashes=False)
def home():
    """home page"""
    return render_template('0-index.html')
