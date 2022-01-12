from werkzeug.security import generate_password_hash, check_password_hash
import os
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()

migrate = Migrate()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))
    # HD Wallets 
    master_node = db.Column(db.String)
    #accounts = db.Column(db.String)
    #wallet_chains = db.Column(db.String)
    #addresses = db.Column(db.String)



#class User(db.Model):
#    #...
#    password_hash = db.Column(db.String(128))
#
#    @property
#    def password(self):
#        raise AttributeError('password is not a readable attribute')
#
#    @password.setter
#    def password(self, password):
#        self.password_hash = generate_password_hash(password)
#    
#    def verify_password(self, password):
#        return check_password_hash(self.password_hash, password)

class Wallet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    #priv_key = db.Column(db.String)
    pub_key = db.Column(db.String)
    address = db.Column(db.String)
    child_key = db.Column(db.String)