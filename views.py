from flask import render_template
from app import app
from models.registration_form import RegistrationForm
from service import *

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        username = form.username.data
        email = form.email.data
        password = form.password.data
    return 'test'

@app.route("/test")
def test():
    return 'test'
