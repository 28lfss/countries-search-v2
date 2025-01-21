from models.db_models import User, Country, user_favorites

def search_id(user_id):
    return User.query.get(user_id)

def search_username(username):
    return User.query.filter_by(username=username).first()

def check_username(username):
    return User.query.filter_by(username=username).first() != None

def search_email(email):
    return User.query.filter_by(email=email).first()

def check_email(email):
    return User.query.filter_by(email=email).first() != None

def all_countries():
    return Country.query.all()
