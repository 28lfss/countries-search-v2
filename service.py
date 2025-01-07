import requests
from models.db_models import db, CountryCard

url = "https://restcountries.com/v3.1/all" # This URL get all the api data

def get_all_data():
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return "Error"


def countries_cards():
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

            country_card = CountryCard(
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