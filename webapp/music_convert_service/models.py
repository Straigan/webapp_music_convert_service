from datetime import datetime
from sqlalchemy.orm import relationship

from webapp.db import db
from webapp.users.models import User


class Record(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    user_id = db.Column(db.Integer, db.ForeignKey(User.id))
    user = relationship('User', backref='records')
    creation_datetime = db.Column(db.DateTime, default=datetime.now())

    def __repr__(self):
        return f'<Record {self.name}, id {self.id}, id_user {self.user_id}>'