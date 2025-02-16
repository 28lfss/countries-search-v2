from flask import Blueprint

country_bp = Blueprint("country_bp", __name__)

from . import routes
