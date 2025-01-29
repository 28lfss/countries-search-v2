from flask import Blueprint

page = Blueprint("page", __name__)

from .pages import page