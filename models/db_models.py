from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped
from sqlalchemy.testing.schema import mapped_column
from werkzeug.security import generate_password_hash, check_password_hash

class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)

user_favorites = db.Table('user_favorites',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id'), primary_key=True),
    db.Column('country_id', db.Integer, db.ForeignKey('country.id'), primary_key=True)
)


class User(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(db.String(20), unique=True, nullable=False)
    email: Mapped[str] = mapped_column(db.String(255), unique=True, nullable=False)
    password_hash: Mapped[str] = mapped_column(db.String(128), nullable=False)
    favorites = db.relationship('Country', secondary=user_favorites, backref='users')

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        check_password_hash(self.password_hash, password)


class Country(db.Model):
    id: Mapped[int] = mapped_column(primary_key = True)
    cca2: Mapped[str] = mapped_column(db.String(3), unique=True, nullable=False)
    country_name: Mapped[str] = mapped_column(db.String(128), unique=True, nullable=False)
    flag_url: Mapped[str] = mapped_column(db.String(128), nullable=False)
    region: Mapped[str] = mapped_column(db.String(32), nullable=False)
    subregion: Mapped[str] = mapped_column(db.String(128), nullable=True)
    population: Mapped[int] = mapped_column(db.SmallInteger, nullable=False)
