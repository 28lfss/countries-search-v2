from flask import Flask
from app.database import db
from app.api import api
from app.main import main_bp
from app.user import user_bp
from app.services.mail_sender import mail
from dotenv import load_dotenv
import os


def create_app():
    app = Flask(__name__)

    load_dotenv()

    app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")

    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.sqlite3"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    app.config["MAIL_SERVER"] = "smtp.gmail.com"
    app.config["MAIL_PORT"] = 465
    app.config["MAIL_USE_SSL"] = True
    app.config["MAIL_USERNAME"] = os.getenv("MAIL_USERNAME")
    app.config["MAIL_PASSWORD"] = os.getenv("MAIL_PASSWORD")
    app.config["MAIL_DEFAULT_SENDER"] = os.getenv("MAIL_USERNAME")

    mail.init_app(app)
    db.init_app(app)

    app.register_blueprint(api)
    app.register_blueprint(main_bp)
    app.register_blueprint(user_bp)

    return app