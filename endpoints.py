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

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    print("------------------")
    print(form.validate())
    print(form.validate_on_submit())
    print(
        form.username.data,
        form.email.data,
        form.password.data
    )
    print("------------------")
    if form.validate_on_submit():
        user = User(
            username=form.username.data,
            email=form.email.data
        )
        user.set_password(form.password.data)

        #db.session.add(user)
        #db.session.commit()
        print("-----ACCOUNT CREATED-----")

        form.username.data = ''
        form.email.data = ''
        form.password.data = ''
        form.confirm_password.data = ''

        return redirect(url_for('login'))
    return render_template('register.html', form=form)

@app.route('/auth-user', methods=['POST'])
def auth_user():
    if request.method == 'POST':
        data = 'None'
        username = request.get_json()['username']
        if check_username(username):
            data = jsonify({'username_exists': 'true'})
        return data

@app.route('/auth-email', methods=['POST'])
def auth_email():
    if request.method == 'POST':
        data = 'None'
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