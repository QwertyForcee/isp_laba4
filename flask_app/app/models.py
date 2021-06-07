from typing import Text
from . import db
from flask_security import UserMixin, RoleMixin, SQLAlchemyUserDatastore

class User(db.Model, UserMixin):
    id = db.Column(db.Integer,primary_key=True)
    nickname = db.Column(db.String(30))
    status = db.Column(db.String(500))

class Role(db.Model, RoleMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40))
    description = db.Column(db.String(255))

class Task(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(100))
    description = db.Column(db.String(1500))
    author_id = db.Column(db.Integer,db.ForeignKey('user.id'))
    author_solution = db.relationship('Solution',backref='task',lazy=True,uselist=False)
    solutions = db.relationship('Solution',backref= 'task',lazy=False)
    tests = db.Column(db.Text)

class Solution(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    task_id = db.Column(db.Integer,db.ForeignKey('task.id'))
    user_id = db.Column(db.Integer,db.ForeignKey('user.id'))
    source_code = db.Column(db.Text)
    successful = db.Column(db.Boolean)

    
user_datastore = SQLAlchemyUserDatastore(db, User, Role)