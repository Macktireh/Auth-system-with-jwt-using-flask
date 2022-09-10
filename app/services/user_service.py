import uuid
import datetime

from app import db
from app.models.user import User


class UserServices:
    def __init__(self):
        return

    def create(self, data):
        user = User(
                publicId=str(uuid.uuid4()),
                email=data.get('email'),
                firstName=data.get('firstName'),
                lastName=data.get('lastName'),
                password=data.get('password'),
                updated=datetime.datetime.utcnow()
            )
        return self.save(user)

    def get_by_publicId(self, publicId):
        return User.query.filter_by(publicId=publicId).first()

    def get_by_email(self, email):
        return User.query.filter_by(email=email).first()

    def get_all_users(self):
        return User.query.all()

    def save(self, user):
        db.session.add(user)
        db.session.commit()
        return user