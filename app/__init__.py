from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from flask_admin import Admin
from flask_login import LoginManager
from app.admin.views import HomeAdminModelView

from app.config import config_by_name


db = SQLAlchemy()
flask_bcrypt = Bcrypt()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config_by_name[config_name])
    db.init_app(app)
    JWTManager(app)
    LoginManager(app)
    admin = Admin(app, index_view=HomeAdminModelView())
    flask_bcrypt.init_app(app)

    return app, admin