from app import mail
from flask_mail import Message
from flask import render_template

class MailService:

    def __init__(self, email):
        self.email = email

    def send_custom_email(self, subject, body):
        msg = Message(subject=subject, recipients=[self.email])
        msg.body = body
        mail.send(msg)

    def generate_new_password(self):
        link = "http://127.0.0.1:5000/"
        msg = Message(subject="Reset Password", recipients=[self.email])
        msg.body = "Change your account password"
        msg.html = render_template("mail_reset_password.html", link=link)
        mail.send(msg)