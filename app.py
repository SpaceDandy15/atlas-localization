#!/usr/bin/env python3
"""
Flask app for a simple web application with internationalization (i18n) support using Babel.
"""

from flask import Flask, render_template
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)

# Configuration
app.config['BABEL_DEFAULT_LOCALE'] = 'en'
app.config['BABEL_DEFAULT_TIMEZONE'] = 'UTC'


@app.route('/')
def index():
    """Home route that returns a simple HTML page."""
    return render_template('index.html')


if __name__ == "__main__":
    app.run()
