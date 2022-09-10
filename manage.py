import os
import unittest

from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from flask import jsonify, render_template
from flask_admin.contrib.sqla import ModelView

from app import create_app, db
from app.admin.views import AdminModelView
from app.models.user import User
from app.routes import blueprint as blueprint_api
from app.views.auth import blueprint as blueprint_auth

app, admin = create_app(os.environ.get('BOILERPLATE_ENV', 'dev'))

app.register_blueprint(blueprint_api)
app.register_blueprint(blueprint_auth)


# Admin pannel register model
admin.add_view(AdminModelView(User, db.session))


import flask_login

login_manager = flask_login.LoginManager()

login_manager.init_app(app)

@app.errorhandler(403)
def forbidden(e):
    return jsonify({
        "message": "Forbidden",
        "error": str(e),
    }), 403

@app.errorhandler(404)
def forbidden(e):
    return jsonify({
        "message": "Endpoint Not Found",
        "error": str(e),
    }), 404

@login_manager.user_loader
def user_loader(email):
        return


@login_manager.request_loader
def request_loader(request):

        return


manager = Manager(app)

migrate = Migrate(app, db)

manager.add_command('db', MigrateCommand)

@manager.command
def run():
    app.run()

@manager.command
def test():
    """Runs the unit tests."""
    tests = unittest.TestLoader().discover('app/test', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1


if __name__ == '__main__':
    manager.run()