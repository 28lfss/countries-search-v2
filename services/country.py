from flask import jsonify
from repository import all_countries
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