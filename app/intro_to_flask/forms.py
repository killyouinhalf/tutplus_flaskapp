from flask.ext.wtf import Form
from wtforms import  StringField, TextAreaField, SubmitField, validators, ValidationError


class ContactForm(Form):
    name = StringField("Name", [validators.DataRequired("Please enter your name.")])
    email = StringField("Email", [validators.DataRequired("Please enter your email address."), validators.Email('Please enter a valid email.')])
    subject = StringField("Subject", [validators.DataRequired("Please enter a subject.")])
    message = TextAreaField("Message", [validators.DataRequired("Please enter a message.")])
    submit = SubmitField("Send")
