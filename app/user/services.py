from app.models.user_model import User
from app.database_config import db
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import exists
from flask import jsonify
import re

class UserService:
    def __init__(self, username, email, password, confirm_password):
        self.username = username
        self.email = email
        self.password = password
        self.confirm_password = confirm_password

    def validate_username(self):
        pattern = r"^[a-zA-Z0-9_]{4,20}$"

        if not re.match(pattern, self.username):
            status = 520 #STATUS 520: username wrong pattern
        elif self.check_username(self.username):
            status = 521 #STATUS 521: username in use
        else:
            status = 200 #STATUS 200: OK
        return status

    def validate_email(self):
        pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"

        if not re.match(pattern, self.email):
            status = 522 #STATUS 522: email wrong pattern
        elif self.check_email(self.email):
            status = 523 #STATUS 523: e mail in use
        else:
            status = 200 #STATUS 200: OK
        return status

    def validate_passwords(self):
        pattern = r"^[\x21-\x7E]+$"

        if not re.match(pattern, self.password):
            status = 524 #STATUS 524: password wrong pattern
        elif self.password == self.confirm_password:
            status = 200 #STATUS 200: OK
        else:
            status = 525 #STATUS 525: passwords don't match
        return status

    def validate_register(self):
        return [self.validate_username(), self.validate_email(), self.validate_passwords()]

    @staticmethod
    def register_validation(request):
        match request:
            case 200:
                return jsonify({"message": "success"}), 200
            case 520:
                return jsonify({"message": "username wrong pattern"}), 520
            case 521:
                return jsonify({"message": "username in use"}), 521
            case 522:
                return jsonify({"message": "email wrong pattern"}), 522
            case 523:
                return jsonify({"message": "email in use"}), 523
            case 524:
                return jsonify({"message": "password wrong pattern"}), 524
            case 525:
                return jsonify({"message": "passwords must match"}), 525
            case _:
                return jsonify({"message": "Invalid"}), 400

    def create_user(self):
        try:
            user = User(
                username=self.username,
                email=self.email
            )
            user.set_password(self.password)
            db.session.add(user)
            db.session.commit()
            return True
        except SQLAlchemyError as e:
            db.session.rollback()
            print(f"Error: {str(e)}")
            return False

    @staticmethod
    def get_user_by_id(user_id):
        return User.query.get(user_id)

    @staticmethod
    def get_user_by_username(username):
        try:
            user = User.query.filter_by(username=username).first()
            return user if user else None
        except SQLAlchemyError as e:
            print(f"Error: {str(e)}")
            return None

    @staticmethod
    def get_user_by_email(email):
        try:
            user = User.query.filter_by(email=email).first()
            return user if user else None
        except SQLAlchemyError as e:
            print(f"Error: {str(e)}")
            return None

    @staticmethod
    def check_username(username):
        return db.session.query(exists().where(User.username == username)).scalar()

    @staticmethod
    def check_email(email):
        return db.session.query(exists().where(User.email == email)).scalar()