"""Story forms"""

from . import fields

import flask_wtf
import wtforms
import wtforms.validators as form_val


class StoryForm(flask_wtf.FlaskForm):
    """Story form from flask_wtf.FlaskForm."""

    title = wtforms.StringField(
        fields.title, validators=[form_val.Required()])
    post = wtforms.TextAreaField(
        fields.post, validators=[form_val.Required()])
    submit = wtforms.SubmitField(fields.submit)


class EditStoryForm(StoryForm):
    """Extend StoryForm to change submit button text"""

    submit = wtforms.SubmitField(fields.edit)
