from app import db
from sqlalchemy import (Column, Integer, String, DateTime, func, ForeignKey)
from sqlalchemy.orm import joinedload, relationship


class Parcel(db.Model):
    """This class represents the parcel table"""
    # from server.resources.users.users_model import User
    __table__name = 'parcels'

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    status = Column(String(255), nullable=False, default='pending')
    destination = Column(String(255), nullable=False)
    pick_up_location = Column(String(255), nullable=False)

    date_created = Column(DateTime, default=func.current_timestamp())
    date_modified = Column(
        DateTime, default=func.current_timestamp(),
        onupdate=func.current_timestamp())
    placed_by = Column(Integer, ForeignKey("user.id"))
    owner = relationship("User", back_populates="parcels")

    def __init__(self, name, destination, pick_up_location, placed_by):
        """Initializing with name"""
        self.name = name
        self.destination = destination
        self.pick_up_location = pick_up_location
        self.placed_by = placed_by
        #

    def save(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_all(cls):
        return Parcel.query.all()

    @staticmethod
    def get_one_by_id(parcel_id):
        return db.session.query(Parcel).get(parcel_id)

    def update_parcel_destination(self, destination):
        self.destination = destination
        db.session.commit()

    def cancel_parcel(self):
        self.status = "cancelled"
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def __repr__(self):
        return "<Parcel: {}>".format(self.name)
