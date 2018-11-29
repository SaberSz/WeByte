from flask import Flask
from flask_bcrypt import Bcrypt
from flask_mail import Mail
import threading
from CodeArena.schedulcheck import job

app = Flask(__name__)
app.secret_key = b'some_secret'
bcrypt = Bcrypt(app)
app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'ravinshahtopper@gmail.com'#enter here
app.config['MAIL_PASSWORD'] = 'iamthetopper'#enter here
mail = Mail(app)



def update_db():
    t = threading.Timer(60.0, update_db)
    print("scheduled check")
    # t.deamon=True
    t.start()
    job()


update_db()

from CodeArena import routes
