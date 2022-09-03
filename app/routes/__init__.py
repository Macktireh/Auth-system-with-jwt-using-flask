from flask_restplus import Api
from flask import Blueprint

from app.routes.auth_route import api as auth_api
from app.routes.user_route import api as user_api

blueprint = Blueprint('api', __name__)

api = Api(blueprint,
        title='API REST Credit Cards',
        version='1.0',
        description='a boilerplate for flask restplus web service'
    )

api.add_namespace(auth_api, path='/auth/user')
api.add_namespace(user_api, path='/user')