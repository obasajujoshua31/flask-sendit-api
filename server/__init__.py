from flask import Flask
from server.config import app_config
from server.routes import application_routes

def create_app(app_name, config_file, db, api):
    app = Flask(__name__)
    app.config.from_object(app_config[app_name])
    app.config.from_pyfile(config_file)
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
    import models
    db.init_app(app)
    initialize_routes(app, api)
    return app

def initialize_routes(app, Api):
    endpoints = Api(app)
    application_routes(endpoints)
