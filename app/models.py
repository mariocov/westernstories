"""Stories Database schema."""

import datetime
import flask_sqlalchemy
import werkzeug.security
import flask_login
import app


class User(flask_login.UserMixin, app.db.Model):
    """User table."""

    _id = app.db.Column('id', app.db.Integer, primary_key=True)
    username = app.db.Column(app.db.String(20), unique=True)
    password_hash = app.db.Column(app.db.String(128))

    def __repr__(self):
        return "<User: {0}>".format(self.username)

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        """Hashing password"""
        self.password_hash = werkzeug.security.generate_password_hash(password)

    def verify_password(self, password):
        return werkzeug.security.check_password_hash(
            self.password_hash, password)

    def get_id(self):
        return str(self._id)


class Story(app.db.Model):
    """Story table."""

    _id = app.db.Column('id', app.db.Integer, primary_key=True)
    title = app.db.Column(app.db.String(200))
    post = app.db.Column(app.db.Text())
    timestamp = app.db.Column(app.db.DateTime, default=datetime.datetime.utcnow)


@app.login_manager.user_loader
def load_user(user_id):
    try:
        return User.query.get(int(user_id))
    except:
        return None
