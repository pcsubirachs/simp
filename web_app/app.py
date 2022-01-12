import os
from dotenv import load_dotenv
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from web_app.routes import simp
from web_app.models import db, migrate, User, Wallet 
from flask_qrcode import QRcode
from flask_sqlalchemy import SQLAlchemy


load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL", default="OOPS")

def create_app():
    # initializing new flask app
    app = Flask(__name__)
    # just an example
    #app.config["CUSTOM_VAR"] = 5
    app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URL
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    # initialize db & migrate, tie to  app
    db.init_app(app)
    migrate.init_app(app)
    
    # extending app to QR code
    QRcode(app)
    
    # linking to routes.py page via the "routes" variable
    app.register_blueprint(simp)
    
    return app