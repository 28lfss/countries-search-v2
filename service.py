from flask import jsonify

from repository import *
import requests

url = 'https://restcountries.com/v3.1/all' # This URL get all the api data

def get_all_data():
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return "Error"

def get_all_countries():
    countries = all_countries()
    formated_countries = []
    for country in countries:
        formated_countries.append({
            'id': country.id,
            'cca2' : country.cca2,
            'country_name' : country.country_name,
            'flag_url' : country.flag_url,
            'region' : country.region,
            'subregion' : country.subregion,
            'population' : country.population
        })
    return jsonify(formated_countries)

def http_status(request):
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
