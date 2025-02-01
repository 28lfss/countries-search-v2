from flask import Flask
from models.db_models import db
from api import api
from page import page
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

app = Flask(__name__)

app.secret_key = "MySecretKey"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.sqlite3"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

aes_key = get_random_bytes(32)
cipher = AES.new(aes_key, AES.MODE_CTR)

app.register_blueprint(api)
app.register_blueprint(page)

if __name__ == "__main__":
    app.run()