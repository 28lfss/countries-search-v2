from ..models.country_model import Country
from ..database import db
from flask import jsonify
import requests

url = 'https://restcountries.com/v3.1/all' # This URL get all the country data

class CountryService:

    @staticmethod
    def get_all_countries():
        return Country.query.all()

    @staticmethod
    def create_countries_cards():
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            for i in data:
                cca2 = i["cca2"]
                name = i["name"]["common"]
                flag_url = i["flags"]["svg"]
                region = i["region"]
                population = i["population"]
                try:
                    subregion = i["subregion"]
                except:
                    subregion = "--"
                country_card = Country(
                    cca2 = cca2,
                    country_name = name,
                    flag_url = flag_url,
                    region = region,
                    subregion = subregion,
                    population = population
                )
                db.session.add(country_card)
            db.session.commit()
            print("All country cards added")
        else:
            print("Error")

#    @staticmethod
#    def get_all_data():
#        response = requests.get(url)
#        if response.status_code == 200:
#            data = response.json()
#            return data
#        else:
#            return "Error"
#
#    @staticmethod
#    def get_all_countries():
#        countries = all_countries()
#        formated_countries = []
#        for country in countries:
#            formated_countries.append({
#                'id': country.id,
#                'cca2' : country.cca2,
#                'country_name' : country.country_name,
#                'flag_url' : country.flag_url,
#                'region' : country.region,
#                'subregion' : country.subregion,
#                'population' : country.population
#            })
#        return jsonify(formated_countries)