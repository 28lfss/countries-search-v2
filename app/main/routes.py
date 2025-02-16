from flask import render_template
from . import page

@page.route('/', methods=["GET"])
def index():
    return render_template('index.html')

@page.route('/register', methods=["GET"])
def register():
    return render_template('register.html')

@page.route('/login', methods=['GET'])
def login():
    return render_template('login.html')