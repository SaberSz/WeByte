from flask import Flask
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.secret_key = b'some_secret'
bcrypt = Bcrypt(app)

from CodeArena import routes
