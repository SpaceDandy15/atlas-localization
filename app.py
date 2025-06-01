#!/usr/bin/env python3
"""Flask app with Babel internationalization"""

from flask import Flask, render_template
from flask_babel import Babel, _
from datetime import datetime

app = Flask(__name__)
babel = Babel(app)

# Configuration
app.config['BABEL_DEFAULT_LOCALE'] = 'en'
app.config['BABEL_DEFAULT_TIMEZONE'] = 'UTC'


@app.route('/')
def index():
    """Home route with a translated greeting"""
    greeting = _("Hello, world!")
    time_msg = _("Current server time: %(time)s", time=datetime.utcnow().strftime("%H:%M:%S"))
    return render_template('index.html', greeting=greeting, time_msg=time_msg)


if __name__ == '__main__':
    app.run()
