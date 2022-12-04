from app import db
from flask_login import UserMixin
from datetime import datetime



class Users(db.Model, UserMixin):
    id = db.Column(db.Integer, nullable=False, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False, unique=True)
    login = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(500), nullable=False)

    def __repr__(self):
        return f"<Users {self.id}>"

class Posts(db.Model):
    post_id = db.Column(db.Integer, nullable=False, primary_key=True, autoincrement=True)
    categor = db.Column(db.String(50), nullable=False)
    topic = db.Column(db.String(250), nullable=False)
    text = db.Column(db.Text, nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<Posts {self.id}>"
