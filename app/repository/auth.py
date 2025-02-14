from ..models.user_model import User

def get_user_by_id(user_id):
    return User.query.get(user_id)

def get_user_by_username(username):
    return User.query.filter_by(username=username).first()

def get_user_by_email(email):
    return User.query.filter_by(email=email).first()

def check_username(username):
    return User.query.filter_by(username=username).first() is not None

def check_email(email):
    return User.query.filter_by(email=email).first() is not None