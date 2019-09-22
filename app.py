from server import create_app
from flask_jwt_extended import (JWTManager)
from dotenv import load_dotenv
from flask import Flask
from flask_bcrypt import Bcrypt
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from instance.config import app_config
from server.routes import routes

import os



db = SQLAlchemy()
#
APP_ROOT = os.path.join(os.path.dirname(__file__), '.')
dotenv_path = os.path.join(APP_ROOT, '.env')
load_dotenv(dotenv_path)

app_name = os.environ.get('APP_SETTINGS')
JWT_SECRET_KEY = os.environ.get("SECRET")


app = create_app(app_name, 'config.py', Api, Flask, app_config, routes, db, JWT_SECRET_KEY)
app.app_context().push()
secure_password = Bcrypt(app)
jwt = JWTManager(app)

