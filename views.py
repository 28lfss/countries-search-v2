from flask import render_template
from app import app
from service import *

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/test")
def test():
    return get_all_data()