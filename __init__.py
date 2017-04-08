execfile('env/bin/activate_this.py', dict(__file__='env/bin/activate_this.py'))

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)

import views, models