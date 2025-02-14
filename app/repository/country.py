from app.models.country_model import Country

def all_countries():
    return Country.query.all()