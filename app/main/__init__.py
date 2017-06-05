"""Initializer."""

import flask


main = flask.Blueprint('main', __name__)


import app.main.views
