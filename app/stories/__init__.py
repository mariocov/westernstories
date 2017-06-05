"""Initializer."""

import flask


stories = flask.Blueprint('stories', __name__)


import app.stories.views
