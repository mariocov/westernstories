"""Main Views."""

from . import main
import app.models

import sqlalchemy.sql.expression as expression
import flask
import json
import random


@main.route('/')
def home():
    """Get a story"""

    if flask.request.args.get('story'):
        story = app.models.Story.query.get_or_404(
            flask.request.args.get('story'))
    else:
        story = app.models.Story.query.order_by(
            expression.func.random()).first()
    return flask.render_template("home.html", story=story)


@main.route('/quote', methods=['POST'])
def quote():
    """Get a new story """

    story = app.models.Story.query.order_by(
        expression.func.random()).first()
    return json.dumps(story.post)
