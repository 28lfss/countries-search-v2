from flask import Flask
from .database_config import db
from app.mail_config import mail
from dotenv import load_dotenv
import os

# Blueprints imports
from app.main import main_bp
from app.user import user_bp
from app.country import country_bp
from app.email_sender import mail_bp

def create_app():
    app = Flask(__name__)

    load_dotenv()

    app.config["SECRET_KEY"] = os.getenv("RENDER_SECRET_KEY") #Remove "RENDER_" to use .env locally

    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.sqlite3"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    app.config["MAIL_SERVER"] = "smtp.gmail.com"
    app.config["MAIL_PORT"] = 465
    app.config["MAIL_USE_SSL"] = True
    app.config["MAIL_USERNAME"] = os.getenv("RENDER_MAIL_USERNAME") #Remove "RENDER_" to use .env locally
    app.config["MAIL_PASSWORD"] = os.getenv("RENDER_MAIL_PASSWORD") #Remove "RENDER_" to use .env locally
    app.config["MAIL_DEFAULT_SENDER"] = os.getenv("RENDER_MAIL_USERNAME") #Remove "RENDER_" to use .env locally

    mail.init_app(app)
    db.init_app(app)

    app.register_blueprint(main_bp)
    app.register_blueprint(user_bp)
    app.register_blueprint(country_bp)
    app.register_blueprint(mail_bp)

# Create a database if it doesn't exist one already
    with app.app_context():
        db.create_all()

    return app