from flask import Blueprint, request, jsonify
from app.models.register_form import RegisterForm
from app.models.db_models import db, User
from app.repository.auth import check_username, check_email, get_user_by_username
from app.services.auth import get_registration_status
from app.services.crypto_utils import generate_user_token, validate_user_token
import time

from app.services.mail_sender import generate_new_password

auth = Blueprint("auth", __name__)

@auth.route("/register", methods=["POST"])
def validate_register_form():
    form = request.form
    register_form = RegisterForm(
        username=form["username"],
        email=form["email"],
        password=form["password"],
        confirm_password=form["confirm_password"]
    )

    for result in register_form.validate_all():
        if result != 200:
            return get_registration_status(result)

    user = User(
        username=form["username"],
        email=form["email"],
    )
    user.set_password(form["password"])
    db.session.add(user)
    db.session.commit()

    return jsonify({"status": "OK"}), 200

@auth.route("/username", methods=["POST"])
def auth_user():
    data = jsonify({"username_exists": "false"})
    username = request.get_json()["username"]
    if check_username(username):
        data = jsonify({"username_exists": "true"})
    return data

@auth.route("/email", methods=["POST"])
def auth_email():
    data = jsonify({"email_exists": "false"})
    email = request.get_json()["email"]
    if check_email(email):
        data = jsonify({"email_exists": "true"})
    return data

@auth.route("/login", methods=["POST"])
def validate_login_form():
    form = request.form.to_dict()
    user = get_user_by_username(form["username"]) if check_username(form["username"]) else None
    if user and user.check_password(form["password"]):
        username = form.get("username")
        timestamp = f"{int(time.time())}" #get timestamp in seconds
        data = {"timestamp": timestamp, "username": username}
        token, nonce = generate_user_token(data)
        return jsonify({
            "token": token,
            "nonce": nonce
        }), 200
    else:
        return jsonify({"error": "Login unauthorized"}), 401

@auth.route("/token-validation", methods=["POST"])
def token_validation():
    token = request.get_json()["token"]
    nonce = request.get_json()["nonce"]
    return validate_user_token(token, nonce)

@auth.route("/reset-password", methods=["POST"])
def reset_password():
    user_email = request.get_json()["email"]
    generate_new_password(user_email)
    return "ok"