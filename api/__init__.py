from flask import Blueprint

from .auth import auth
from .country import country

api = Blueprint("api", __name__, url_prefix="/api")

api.register_blueprint(auth, url_prefix="/auth")
api.register_blueprint(country, url_prefix="/country")