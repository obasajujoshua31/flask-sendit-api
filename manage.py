from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from flask import Flask
from server import create_app
from dotenv import load_dotenv
from flask_bcrypt import Bcrypt
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from instance.config import app_config
from server.routes import routes
import os


APP_ROOT = os.path.join(os.path.dirname(__file__), '.')
dotenv_path = os.path.join(APP_ROOT, '.env')
load_dotenv(dotenv_path)

app_name = os.environ.get('APP_SETTINGS')

db = SQLAlchemy()
app = create_app(app_name, 'config.py', Api, Flask, app_config, routes, db)
app.app_context().push()
secure_password = Bcrypt(app)

migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command("db", MigrateCommand)

if __name__ == "__main__":
    app.run()