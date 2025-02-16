from flask import Blueprint

page = Blueprint("endpoints", __name__)

from .pages import page