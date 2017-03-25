from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import sys
from os.path import dirname
sys.path.append(dirname(__file__))

app = Flask(__name__, static_url_path="")
app.config.from_object('config')
db = SQLAlchemy(app)

from app import views, models

