import app
class User(app.db.Model):
    """This class represents the user table"""

    __table__name = 'users'

    id = app.db.Column(app.db.Integer, primary_key=True)
    name = app.db.Column(app.db.String(255))
    email = app.db.Column(app.db.String(255), unique=True, index=True)
    password = app.db.Column(app.db.String(255), unique=True)

    date_created = app.db.Column(app.db.DateTime, default=app.db.func.current_timestamp())
    date_modified = app.db.Column(
        app.db.DateTime, default=app.db.func.current_timestamp(),
        onupdate=app.db.func.current_timestamp())

    def __init__(self, name, email, password):
        """Initializing with name"""
        self.name = name
        self.email = email
        self.password = app.secure_password.generate_password_hash(password)


    def save(self):
        app.db.session.add(self)
        app.db.session.commit()

    @staticmethod
    def get_all():
        return User.query.all()

    @staticmethod
    def get_one(value):
        return User.query().filter_by(id=value).first()

    def delete(self):
        app.db.session.delete(self)
        app.db.session.commit()

    def __refr__(self):
        return "<User: {}>".format(self.name)
