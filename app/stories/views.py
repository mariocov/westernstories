"""Stories module"""

from . import stories
from .. import db
import app.stories.forms
import app.models


import flask
import flask_login


@stories.route('/story', methods=['GET', 'POST'])
@flask_login.login_required
def make_story():
    """Generate a view with a form to publish a story."""

    form = app.stories.forms.StoryForm()
    if flask.request.method == 'POST' and form.validate_on_submit():
        story = app.models.Story()
        story.title = form.title.data
        story.post = form.post.data
        app.db.session.add(story)
        app.db.session.commit()
        return flask.redirect(flask.url_for('stories.stories'))
    return flask.render_template("form_template.html", form=form, title="edit Story")


@stories.route('/story/edit/<int:story_id>', methods=['GET', 'POST'])
@flask_login.login_required
def edit_story(story_id):
    """Get the story id as argument and return a view
    with a form to publish or update a story."""

    story = app.models.Story.query.filter_by(
        _id=story_id).first_or_404()
    form = app.stories.forms.EditStoryForm(obj=story)
    form.populate_obj(story)
    if flask.request.method == 'POST' and form.validate_on_submit():
        db.session.add(story)
        db.session.commit()
        return flask.redirect(flask.url_for('stories.stories'))
    return flask.render_template("form_template.html", form=form, title="edit Story")


@stories.route('/story/delete/<int:story_id>', methods=['POST'])
@flask_login.login_required
def delete_story(story_id):
    """Delete story"""

    if flask.request.method == 'POST':
        story = app.models.Story.query.filter_by(
            _id=story_id).first_or_404()
        db.session.delete(story)
        db.session.commit()
    return flask.redirect(flask.url_for('stories.stories'))


@stories.route('/stories')
@flask_login.login_required
def stories():
    """Get all published stories"""

    stories = app.models.Story.query.all()
    return flask.render_template("stories.html", title="Stories", stories=stories)
