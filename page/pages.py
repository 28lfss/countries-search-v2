from flask import render_template
from . import page

@page.route('/')
def index():
    return render_template('index.html')

@page.route('/register')
def register():
    return render_template('register.html')

@page.route('/login', methods=['GET', 'POST'])
def login():
    #TODO: add feature
    return render_template('login.html')