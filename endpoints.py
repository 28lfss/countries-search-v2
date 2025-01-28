from app import app
from flask import render_template, redirect, url_for, request
from service import *

from models.db_models import db, User
from models.login_form import LoginForm
from models.register_form import RegisterForm


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/all')
def test():
    return get_all_countries()

@app.route('/register', methods=['GET'])
def register():
    return render_template('register.html')

@app.route('/validate-register', methods=['POST'])
def validate_submit():
    form = request.form
    if request.method == 'POST':
        user = RegisterForm(
            username=form['username'],
            email=form['email'],
            password=form['password'],
            confirm_password=form['confirm_password']
        )

        if user.validate_email():
            return "valid user"
        else:
            return "invalid user"

@app.route('/auth-user', methods=['POST'])
def auth_user():
    if request.method == 'POST':
        data = jsonify({'username_exists': 'false'})
        username = request.get_json()['username']
        if check_username(username):
            data = jsonify({'username_exists': 'true'})
        return data

@app.route('/auth-email', methods=['POST'])
def auth_email():
    if request.method == 'POST':
        data = jsonify({'email_exists': 'false'})
        email = request.get_json()['email']
        if check_email(email):
            data = jsonify({'email_exists': 'true'})
        return data

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data

        user = search_username(username)

        if user and user.check_password(password):
            return redirect(url_for('index'))
        else:
            return 'Invalid username or password.'
    return render_template('login.html', form=form)