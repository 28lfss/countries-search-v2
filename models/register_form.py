import re
from repository import check_username, check_email

class RegisterForm:
    def __init__(self, username, email, password, confirm_password):
        self.username = username
        self.email = email
        self.password = password
        self.confirm_password = confirm_password

    def validate_username(self):
        pattern = r"^[a-zA-Z0-9_]{4,20}$"
        return not check_username(self.username) and re.match(pattern, self.username)

    def validate_email(self):
        pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
        return not check_email(self.email) and re.match(pattern, self.email)

    def validate_passwords(self):
        pattern = r"^[\x21-\x7E]+$"
        return self.password == self.confirm_password \
                and re.match(pattern, self.password) \
                and re.match(pattern, self.password)

    def validate_all(self):
        return self.validate_username() and self.validate_email() and self.validate_passwords()
