from . import mail_bp
from .services import MailService
from flask import request, jsonify

@mail_bp.route("/mail-reset-password", methods=["POST"])
def mail_reset_password():
     email = MailService(request.get_json()["email"])
     email.generate_new_password()
     return jsonify({"status": "ok"})

