from flask import request
from flask_restplus import Resource

from app.schemas.dto import UserDto
from app.services.user_service import add_new_user, get_all_users, get_a_user

api = UserDto.api
_user = UserDto.user


@api.route('/')
class UserList(Resource):
    @api.doc('list_of_registered_users')
    @api.marshal_list_with(UserDto.users, envelope='data')
    def get(self):
        """List all registered users"""
        return get_all_users()

    @api.response(201, 'User successfully created.')
    @api.doc('create a new user')
    @api.expect(_user, validate=True)
    def post(self):
        """Creates a new User """
        data = request.json
        return add_new_user(data=data)


@api.route('/<publicId>')
@api.param('publicId', 'The User identifier')
@api.response(404, 'User not found.')
class User(Resource):
    @api.doc('get a user')
    @api.marshal_with(UserDto.users)
    def get(self, publicId):
        """get a user given its identifier"""
        user = get_a_user(publicId)
        if not user:
            api.abort(404)
        else:
            return user