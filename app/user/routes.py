from . import user_bp
from .services import UserService
from flask import request, jsonify
import requests

@user_bp.route("/get-user", methods=["POST"])
def get_user():
    username = request.get_json()["username"]
    user = UserService.get_user_by_username(username)
    if user:
        return jsonify(user.to_dict()), 200
    else:
        return jsonify({"error": "User not found"}), 404

@user_bp.route("/register-user", methods=["POST"])
def register_user():
    form = request.form
    user = UserService(
        username=form["username"],
        email=form["email"],
        password=form["password"],
        confirm_password=form["confirm_password"]
    )
    for result in user.validate_register():
        if result != 200:
            return UserService.register_validation(result)

    if user.create_user():
        return jsonify({"message": "ok"}), 200
    else:
        return jsonify({"error": "Error creating user"})

@user_bp.route("/auth-username-&-email", methods=["POST"])
def auth_username_and_email():
    username = True if UserService.check_username(request.get_json()["username"]) else False
    email = True if UserService.check_email(request.get_json()["email"]) else False

    if username:
        return jsonify({"error": "User already in use"}), 404
    elif email:
        return jsonify({"error": "Email already in use"}), 404
    else:
        return jsonify({"status": "Ok"}), 200

@user_bp.route("/login", methods=["POST"])
def login():
    form = request.form
    user = UserService.get_user_by_username(form["username"])

    if user and user.check_password(form["password"]):
        token, nonce = UserService.generate_session_token(user.username)
        return jsonify({
            "token": token,
            "nonce": nonce
        }), 200
    else:
        return jsonify({"error": "User and Email don't match"})

@user_bp.route("/validate-token", methods=["POST"])
def validate_token():
    token = request.get_json()["token"]
    nonce = request.get_json()["nonce"]
    if UserService.validate_session_token(token, nonce):
        return jsonify({"status": "ok"})
    else:
        return jsonify({
            "error": "Token expired",
            "message": "Log in again for a new token"
        }), 401

@user_bp.route("/forgot-password", methods=["POST"])
def forgot_password():
    user_email = request.get_json()["email"]
    if UserService.check_email(user_email):
        response = requests.post(
            "http://127.0.0.1:5000/mail-reset-password",
            json={"email": user_email}
        )
        return response.json(), response.status_code
    else:
        return jsonify({"error": "Email not found"}), 404