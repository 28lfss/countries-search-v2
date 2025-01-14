from flask import jsonify

from repository import all_countries, search_username
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
    for i in countries:
        formated_countries.append({
            'id': i.id,
            'cca2' : i.cca2,
            'country_name' : i.country_name,
            'flag_url' : i.flag_url,
            'region' : i.region,
            'subregion' : i.subregion,
            'population' : i.population
        })
    return jsonify(formated_countries)

def get_by_username(user_name):
    user = search_username(user_name)
    return user
