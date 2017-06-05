from config import config

import flask
import flask_bootstrap
import flask_sqlalchemy
import flask_login
import flask_wtf.csrf


login_manager = flask_login.LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'
bootstrap = flask_bootstrap.Bootstrap()
db = flask_sqlalchemy.SQLAlchemy()
csrf = flask_wtf.csrf.CSRFProtect()


def create_app(config_name):
    app = flask.Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    bootstrap.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)
    csrf.init_app(app)

    import app.main as main_blueprint
    app.register_blueprint(main_blueprint.main)

    import app.stories as stories_blueprint
    app.register_blueprint(stories_blueprint.stories)

    import app.auth as auth_blueprint
    app.register_blueprint(auth_blueprint.auth)

    return app
