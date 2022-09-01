from flask_restplus import Namespace, fields


class UserDto:
    api = Namespace('user', description='user related operations')
    user = api.model('user', {
        'email': fields.String(required=True, description='user email address'),
        'fullName': fields.String(required=True, description='user username'),
        'publicId': fields.String(description='user Identifier'),
        'password': fields.String(required=True, description='user password'),
        'passwordConfirm': fields.String(required=True, description='user password confirm'),
    })
    users = api.model('users', {
        'email': fields.String(required=True, description='user email address'),
        'fullName': fields.String(required=True, description='user username'),
        'publicId': fields.String(description='user Identifier'),
    })