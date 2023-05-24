from datetime import datetime

from webapp.db import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    access_token = db.Column(db.String)
    creation_datetime = db.Column(db.DateTime, default=datetime.now())

    def __repr__(self):
        return f'<User {self.name}, id {self.id}>'
