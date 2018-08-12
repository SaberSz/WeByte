from flask import Flask
from flask_bcrypt import Bcrypt
from flask_mail import Mail

app = Flask(__name__)
app.secret_key = b'some_secret'
bcrypt = Bcrypt(app)
app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'ravinshahtopper@gmail.com'
app.config['MAIL_PASSWORD'] = 'iamthetopper'
mail = Mail(app)

from CodeArena import routes
