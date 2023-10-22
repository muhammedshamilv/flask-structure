import datetime

import bcrypt
from app import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    created_at = db.Column(db.DateTime, default=datetime.datetime.now)
    updated_at = db.Column(db.DateTime)
    username = db.Column(db.String(128))
    password_hash = db.Column(db.String(128))

    def set_password(self, password):
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(password.encode("utf-8"), salt)
        self.password_hash = hashed_password

    def check_password(self, password):
        return bcrypt.checkpw(password.encode("utf-8"), self.password_hash)

    def __repr__(self):
        return "<User %r>" % self.id
