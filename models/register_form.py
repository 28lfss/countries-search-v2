from repository import check_username, check_email
import re

class RegisterForm:
    def __init__(self, username, email, password, confirm_password):
        self.username = username
        self.email = email
        self.password = password
        self.confirm_password = confirm_password

    def validate_username(self):
        pattern = r"^[a-zA-Z0-9_]{4,20}$"

        if not re.match(pattern, self.username):
            status = 520 #STATUS 520: username wrong pattern
        elif check_username(self.username):
            status = 521 #STATUS 521: username in use
        else:
            status = 200 #STATUS 200: OK
        return status

    def validate_email(self):
        pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"

        if not re.match(pattern, self.email):
            status = 522 #STATUS 522: email wrong pattern
        elif check_email(self.email):
            status = 523 #STATUS 523: email in use
        else:
            status = 200 #STATUS 200: OK
        return status

    def validate_passwords(self):
        pattern = r"^[\x21-\x7E]+$"

        if not re.match(pattern, self.password):
            status = 524 #STATUS 524: password wrong pattern
        elif self.password == self.confirm_password:
            status = 200 #STATUS 200: OK
        else:
            status = 525 #STATUS 525: passwords don't match
        return status

    def validate_all(self):
        return [self.validate_username(), self.validate_email(), self.validate_passwords()]
