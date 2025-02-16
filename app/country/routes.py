from . import country_bp
from .services import CountryService
from flask import request, jsonify

@country_bp.route('/get-all-countries', methods=["GET"])
def get_all_countries():
    formatted_countries = [country.to_dict() for country in CountryService.get_all_countries()]
    return jsonify(formatted_countries)

@country_bp.route("/create-countries-cards", methods=["GET"])
def create_countries_cards():
    #CountryService.create_countries_cards()
    return "ok"