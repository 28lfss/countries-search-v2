from flask import Blueprint, request, jsonify
from models.register_form import RegisterForm
from repository import check_username, check_email

#from models.login_form import LoginForm

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

        if user.validate_all():
            return "valid user"
        else:
            return "invalid user"

@auth.route('/user', methods=['POST'])
def auth_user():
    if request.method == 'POST':
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