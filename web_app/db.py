import os
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))

class Wallet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    priv_key = db.Column(db.String)
    pub_key = db.Column(db.String)
    address = db.Column(db.String)

