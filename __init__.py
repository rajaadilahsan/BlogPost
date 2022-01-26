from distutils.log import debug
from email.policy import default
from turtle import title
from flask import Flask
from flask_sqlalchemy import SQLAlchemy 



app = Flask(__name__)
app.config['SECRET_KEY'] = 'ef52ebe6a374d40d7106a92e8d5d0651'
app.config['SQLALCHEMY_DATABASE_URI']="sqlite:///site.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db=SQLAlchemy(app)

from app import routes
