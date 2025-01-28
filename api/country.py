from flask import Blueprint

from service import get_all_countries

country = Blueprint("country", __name__)

@country.route('/all')
def test():
    return get_all_countries()

