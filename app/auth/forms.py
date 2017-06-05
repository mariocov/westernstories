"""Form module."""

from . import fields

import flask_wtf

import wtforms
import wtforms.validators as form_val


class LoginForm(flask_wtf.FlaskForm):
    """Login form from flask_wtf.FlaskForm."""

    username = wtforms.StringField(
        fields.username, validators=[form_val.Required()])
    password = wtforms.PasswordField(validators=[form_val.Required()])
    submit = wtforms.SubmitField(fields.submit)
