import re

class EmailValidator:
    def __init__(self, email):
        self.email = email
        self.validate()

    def validate(self):
        regex = r"^[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?$"
        if re.fullmatch(regex, self.email):
            print("Valid email")
        else:
            print("Invalid email")


is_valid_email = EmailValidator("example1name@gmail.com")
is_valid_email_2 = EmailValidator("ex..ample1name@gmail.com")
