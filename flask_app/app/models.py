from . import db

class User(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    nickname = db.Column(db.String(30))
    status = db.Column(db.String(500))

class Task(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(100))
    description = db.Column(db.String)
    author_id = db.Column(db.Integer,db.ForeignKey('user.id'))
    author_solution = db.relationship('Solution',backref='task',lazy=True,uselist=False)
    solutions = db.relationship('Solution',backref= 'task',lazy=False)
    tests = db.Column(db.String)

class Solution(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    task_id = db.Column(db.Integer,db.ForeignKey('task.id'))
    user_id = db.Column(db.Integer,db.ForeignKey('user.id'))
    source_code = db.Column(db.String)
