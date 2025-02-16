from flask import Blueprint

from .country import country

api = Blueprint("api", __name__, url_prefix="/api")

api.register_blueprint(country, url_prefix="/country")