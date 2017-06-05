import app
from app import models
from app import db

import os
import flask_script
import flask_migrate


app = app.create_app(os.getenv('FLASK_CONFIG') or 'default')
manager = flask_script.Manager(app)
migrate = flask_migrate.Migrate(app, db)


def make_shell_context():
    return dict(app=app, db=db, User=models.User, Story=models.Story)


manager.add_command("shell", flask_script.Shell(make_context=make_shell_context))
manager.add_command("db", flask_migrate.MigrateCommand)


@manager.command
def test():
    """Run the unit tests."""
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)


@manager.command
def deploy():
    import flask_migrate

    flask_migrate.upgrade()


if __name__ == '__main__':
    manager.run()
