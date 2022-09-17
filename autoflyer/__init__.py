from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('autoflyer.config') 

db = SQLAlchemy(app)
from .models import items
import autoflyer.views