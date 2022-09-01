import uuid
import datetime

from app import db
from app.models.user import User


def add_new_user(data):
    user = User.query.filter_by(email=data['email']).first()
    if not user:
        password = data['password']
        passwordConfirm = data['passwordConfirm']
        if password != passwordConfirm:
            response_object = {
                'status': 'fail',
                'message': "Password and Confirm Password doesn't match."
                }
            return response_object, 400
        
        new_user = User(
            publicId=str(uuid.uuid4()),
            email=data['email'],
            fullName=data['fullName'],
            password=data['password'],
            updated=datetime.datetime.utcnow()
        )
        save_changes(new_user)
        response_object = {
            'status': 'success',
            'message': "Successfully registered."
        }
        return response_object, 201
    else:
        response_object = {
            'status': 'fail',
            'message': "User already exists. Please Log in.",
        }
        return response_object, 409


def get_all_users():
    return User.query.all()


def get_a_user(publicId):
    return User.query.filter_by(publicId=publicId).first()


def save_changes(data):
    db.session.add(data)
    db.session.commit()