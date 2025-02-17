from flask import Blueprint

mail_bp = Blueprint("mail_bp", __name__)

from . import routes