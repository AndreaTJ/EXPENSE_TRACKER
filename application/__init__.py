from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, instance_relative_config=True)
app.config.from_object('config')

app.config["SQLALCHEMY_DATABASE_URI"]
db = SQLAlchemy(app)

from application import routes