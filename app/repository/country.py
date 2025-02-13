from app.models.db_models import Country

def all_countries():
    return Country.query.all()