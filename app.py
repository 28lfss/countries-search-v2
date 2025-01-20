from flask import Flask
from models.db_models import db

app = Flask(__name__)

from endpoints import *

app.secret_key = 'MySecretKey'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

if __name__ == "__main__":
    app.run()