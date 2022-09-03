from datetime import timedelta
from flask_jwt_extended import create_access_token, decode_token

from app.models.user import User


def generate_access_token(user):
    return create_access_token(
        identity={'publicId': user.publicId, 'isActive': user.isActive}, 
        expires_delta=timedelta(hours=24)
    )

def check_access_token(token):
    try:
        identity = decode_token(token)["sub"]
        user = User.query.filter_by(publicId=identity['publicId']).first()
        if identity['isActive'] == user.isActive:
            return user
        return None
    except:
        return None