from app import app
from flask import render_template, redirect, url_for
from service import *

from models.db_models import db, User
from models.login_form import LoginForm
from models.registration_form import RegistrationForm

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/all')
def test():
    return get_all_countries()

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        username = form.username.data
        email = form.email.data
        password = form.password.data

        user = User(username=username, email=email)
        user.set_password(password)

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('login'))
    return render_template('register.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data

        user = get_by_username(username)

        if user and user.check_password(password):
            return redirect(url_for('index'))
        else:
            return 'Invalid username or password.'
    return render_template('login.html', form=form)