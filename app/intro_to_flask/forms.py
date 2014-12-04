from flask.ext.wtf import Form
from wtforms import  StringField, TextAreaField, SubmitField, validators, ValidationError, PasswordField


class ContactForm(Form):
    name = StringField("Name", [validators.DataRequired("Please enter your name.")])
    email = StringField("Email", [validators.DataRequired("Please enter your email address."), validators.Email('Please enter a valid email.')])
    subject = StringField("Subject", [validators.DataRequired("Please enter a subject.")])
    message = TextAreaField("Message", [validators.DataRequired("Please enter a message.")])
    submit = SubmitField("Send")

class SignUpForm(Form):
    firstname = StringField("First name", [validators.DataRequired("Please enter your first name.")])
    lastname = StringField("Last name", [validators.DataRequired("Please enter your last name.")])
    email = StringField("Email", [validators.DataRequired("Please enter your email address."), validators.Email('Please enter a valid email.')])
    password = PasswordField('Password', [validators.DataRequired("Please select a password.")])
    submit = SubmitField("Create account")

    def __init__(self, *args, **kwargs):
        Form.__init__(self. *args, **kwargs)

    def validate(self):
        if not Form.validate(self):
            return False

        user = User.query.filter_by(email = self.email.data.lower()).first()
        if user:
            self.email.errors.append("That email is already taken")
            return False
        else:
            return True
