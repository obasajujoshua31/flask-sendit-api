# from server import create_app
# from dotenv import load_dotenv
# from flask_bcrypt import Bcrypt
# from flask_restful import Api
# from flask_sqlalchemy import SQLAlchemy
#
# import os
#
#
#
#
# APP_ROOT = os.path.join(os.path.dirname(__file__), '.')
# dotenv_path = os.path.join(APP_ROOT, '.env')
# load_dotenv(dotenv_path)
#
# app_name = os.environ.get('APP_SETTINGS')
#
#
# app = create_app(app_name, 'config.py', Api)
# secure_password = Bcrypt(app)
# db = SQLAlchemy(app)
