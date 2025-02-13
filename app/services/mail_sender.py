from flask import render_template
from flask_mail import Mail, Message

mail = Mail()

def send_custom_email(to, subject, body):
    msg = Message(subject=subject, recipients=[to])
    msg.body = body
    mail.send(msg)

def generate_new_password(to):
    link = "http://127.0.0.1:5000/"
    msg = Message(subject="Reset Password", recipients=[to])
    msg.body = "Change your account password"
    msg.html = render_template("mail_reset_password.html", link=link)
    mail.send(msg)