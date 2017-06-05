"""Authentication Views."""

from . import auth
import app.models
import app.auth.forms

import flask
import flask_login


@auth.route('/login', methods=['GET', 'POST'])
def login():
    """Login method."""

    form = app.auth.forms.LoginForm()
    if flask.request.method == 'POST' and form.validate_on_submit():
        user = app.models.User.query.filter_by(
            username=form.username.data).first()
        if user is not None and user.verify_password(form.password.data):
            flask_login.login_user(user, True)
            return flask.redirect(
                flask.request.args.get('next') or flask.url_for('main.home'))
    return flask.render_template(
        "form_template.html", form=form, title="Login")



@auth.route('/logout')
@flask_login.login_required
def logout():
    """Logout method."""

    flask_login.logout_user()
    return flask.redirect(flask.url_for('main.home'))
