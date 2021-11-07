from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Creating a new data table for a user
# Has index, name of the user, email of the user, password of the user
class InfoModel(db.Model):

    __tablename__ = "info_table"

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String())
    email = db.Column(db.String())
    password = db.Column(db.String())



    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

    def __repr__(self):
        return f"{self.name}:{self.email, self.password}"

