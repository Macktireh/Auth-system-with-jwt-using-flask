from flask_restplus import Api
from flask import Blueprint

from app.routes.user_route import api as user_ns

blueprint = Blueprint('api', __name__)

api = Api(blueprint,
        title='API REST Credit Cards',
        version='1.0',
        description='a boilerplate for flask restplus web service'
    )

api.add_namespace(user_ns, path='/auth/user')