"""Tests"""

import app.models
import app
import unittest
import flask


class StoriesTest(unittest.TestCase):

    def setUp(self):
        self.app = app.create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        app.db.create_all()
        user = app.models.User(username = "user_one", password = "cat")
        story = app.models.Story(title = "Lorem ipsum", post = "Lorem ipsum dolor sit amet, consectetur adipiscing elit.")
        app.db.session.add(user)
        app.db.session.add(story)
        app.db.session.commit()
        self.client = self.app.test_client(use_cookies=True)

    def tearDown(self):
        app.db.session.remove()
        app.db.drop_all()
        self.app_context.pop()

    def test_app_exists(self):
        self.assertFalse(flask.current_app is None)

    def test_app_is_testing(self):
        self.assertTrue(flask.current_app.config['TESTING'])

    def test_app_get_home(self):
        response = self.client.get(flask.url_for('main.home'))
        self.assertTrue(b'Lorem ipsum' in response.data)

    def test_login_no_user(self):
        response = self.client.post(flask.url_for('auth.login'), data={
            'username': 'nouser',
            'password': 'dog',
        })
        self.assertFalse(response.status_code == 302)

    def test_login(self):
        response = self.client.post(flask.url_for('auth.login'), data={
            'username': 'user_one',
            'password': 'cat',
        })
        self.assertTrue(response.status_code == 302)

    def test_logout(self):
        response = self.client.get(flask.url_for('auth.logout'))
        self.assertTrue(response.status_code == 302)
        response = self.client.get(flask.url_for('stories.stories'))
        self.assertTrue(response.status_code == 302)
