from flask import Blueprint, request, jsonify
from models.register_form import RegisterForm
from repository import check_username, check_email
from service import http_status

auth = Blueprint("auth", __name__)

@auth.route('/register', methods=['POST'])
def validate_submit():
    form = request.form
    if request.method == 'POST':
        user = RegisterForm(
            username=form['username'],
            email=form['email'],
            password=form['password'],
            confirm_password=form['confirm_password']
        )
        return http_status(user.validate_all())

@auth.route('/username', methods=['POST'])
def auth_user():
    if request.method ==     'POST':
        data = jsonify({'username_exists': 'false'})
        username = request.get_json()['username']
        if check_username(username):
            data = jsonify({'username_exists': 'true'})
        return data

@auth.route('/email', methods=['POST'])
def auth_email():
    if request.method == 'POST':
        data = jsonify({'email_exists': 'false'})
        email = request.get_json()['email']
        if check_email(email):
            data = jsonify({'email_exists': 'true'})
        return data

@auth.route('/test', methods=['POST'])
def test():
    return "test"
