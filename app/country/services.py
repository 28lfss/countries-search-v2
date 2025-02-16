from ..models.country_model import Country
from flask import jsonify
import requests

url = 'https://restcountries.com/v3.1/all' # This URL get all the country data

class CountryService:

    @staticmethod
    def get_all_countries():
        return Country.query.all

    @staticmethod
    def get_all_data():
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return data
        else:
            return "Error"

    @staticmethod
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