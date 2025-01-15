from models.db_models import User, Country, user_favorites

def search_username(username):
    data = User.query.filter_by(username=username).first()
    return data

def search_email(email):
    data = User.query.filter_by(email=email).first()
    return data

def all_countries():
    data = Country.query.all()
    return data