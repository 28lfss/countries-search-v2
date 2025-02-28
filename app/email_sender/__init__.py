from flask import Blueprint
#from flask_mail import Mail

#email_sender = Mail()
mail_bp = Blueprint("mail_bp", __name__)

from . import routes