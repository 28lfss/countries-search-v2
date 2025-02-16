from flask import Blueprint

from app.services.country import get_all_countries

country = Blueprint("country", __name__)

@country.route('/all')
def test():
    return get_all_countries()

