from flask_wtf import FlaskForm
from wtforms import PasswordField, SubmitField, StringField
from wtforms.validators import DataRequired, Length


class LoginForm(FlaskForm):
    username = StringField(
        'Username',
        validators=[DataRequired(), Length(min=4, max=20)]
    )
    password = PasswordField(
        'Password',
        validators=[DataRequired(), Length(min=5, max=30)]
    )
    submit = SubmitField('Login')