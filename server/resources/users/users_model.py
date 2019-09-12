from manage import secure_password, db
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import (Column, Integer, String, DateTime, func)



class User(db.Model):
    """This class represents the user table"""

    __table__name = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    email = Column(String(255), unique=True, index=True, nullable=False)
    password = Column(String(255), unique=True,nullable=False)

    date_created = Column(DateTime, default=func.current_timestamp())
    date_modified = Column(
        DateTime, default=func.current_timestamp(),
        onupdate=func.current_timestamp())

    def __init__(self, name, email, password):
        """Initializing with name"""
        self.name = name
        self.email = email
        self.password = secure_password.generate_password_hash(password).decode('utf-8')
        # self.password = password

    def save(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_all():
        return User.query.all()

    @staticmethod
    def get_one(value):
        return User.query().filter_by(id=value).first()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def __repr__(self):
        return "<User: {}>".format(self.name)
