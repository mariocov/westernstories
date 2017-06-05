"""Initializer."""

import flask


auth = flask.Blueprint('auth', __name__)


import app.auth.views
