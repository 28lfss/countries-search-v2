from app.database import db

user_favorites = db.Table('user_favorites',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id'), primary_key=True),
    db.Column('country_id', db.Integer, db.ForeignKey('country.id'), primary_key=True)
)
