from intro_to_flask import app
from flask import Flask, render_template, request, flash, session, redirect, url_for
from intro_to_flask.forms import ContactForm, SignUpForm
from flask.ext.mail import Message, Mail
from intro_to_flask.forms import ContactForm
from intro_to_flask.models import db

mail = Mail()


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm()

    if request.method == 'POST':
        if form.validate() == False:
            flash('All fields are required.')
            return render_template('contact.html', form=form)
        else:
            msg = Message(form.subject.data, sender='klabeau@gmail.com', recipients=['klabeau@gmail.com'])
            msg.body = """
            From: %s <%s>
            %s
            """ % (form.name.data, form.email.data, form.message.data)
            mail.send(msg)

            return render_template('contact.html', success = True)


    elif request.method == 'GET':
        return render_template('contact.html', form=form)


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignUpForm()

    if request.method == 'POST':
        if form.validate == 'False':
            return render_template('signup.html', form = form)
        else:
            return "[1] Create a new user [2] sign in the user [3] redirect to the user's profile"

    elif request.method == 'GET':
        return render_template('signup.html', form = form)

