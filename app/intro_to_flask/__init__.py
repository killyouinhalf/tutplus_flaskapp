from flask import Flask
 
app = Flask(__name__)
 
app.secret_key = 'development key'
 
app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 465
app.config["MAIL_USE_SSL"] = True
app.config["MAIL_USERNAME"] = 'klabeau@gmail.com'
app.config["MAIL_PASSWORD"] = 'syD10gabY14'
 
from intro_to_flask.routes import mail
mail.init_app(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:GABY6SYD2@localhost/development'

from intro_to_flask.models import db
db.init_app(app)
import intro_to_flask.routes