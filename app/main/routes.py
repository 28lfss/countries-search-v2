from flask import render_template
from . import main_bp

@main_bp.route('/', methods=["GET"])
def index():
    return render_template('index.html')

@main_bp.route('/register', methods=["GET"])
def register():
    return render_template('register.html')

@main_bp.route('/login', methods=['GET'])
def login():
    return render_template('login.html')