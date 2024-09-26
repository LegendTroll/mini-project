from . import db
from flask_login import UserMixin

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(200))
    date = db.Column(db.String(20))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))  # Plain text password
    username = db.Column(db.String(150))
    tasks = db.relationship('Task')
