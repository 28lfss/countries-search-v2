from models.db_models import User, Country, user_favorites

def all_countries():
    return Country.query.all()
