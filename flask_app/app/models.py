from typing import Text
from . import db
from flask_security import UserMixin, RoleMixin, SQLAlchemyUserDatastore
from .config import Config

roles_users = db.Table(
    "roles_users",
    db.Column("user_id", db.Integer, db.ForeignKey("user.id")),
    db.Column("role_id", db.Integer, db.ForeignKey("role.id")),
)
class User(db.Model, UserMixin):
    id = db.Column(db.Integer,primary_key=True)
    status = db.Column(db.String(500))
    username = db.Column(db.String(255), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(255))
    active = db.Column(db.Boolean)
    confirmed_at = db.Column(db.DateTime)
    roles = db.relationship(
        "Role", secondary=roles_users, backref=db.backref("users", lazy="dynamic")
    )

    def verify_and_update_password(self,password):
        #hashed =  bcrypt.hashpw(str.encode(password), bcrypt.gensalt())
        #print('password: ',self.password)
        #print('user try hashed: ',hashed)
        #return self.password == hashed
        #return bcrypt.hashpw(str.encode(password),str.encode(self.password)) == self.password
        from flask_security.utils import verify_password
        return verify_password(password,self.password)


class Role(db.Model, RoleMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40))
    description = db.Column(db.String(255))

class Task(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(100))
    description = db.Column(db.String(1500))
    author_id = db.Column(db.Integer,db.ForeignKey('user.id'))
    #author_solution = db.relationship('Solution',backref='task',lazy=True,uselist=False)
    solutions = db.relationship('Solution',backref= 'task',lazy=False)
    tests = db.Column(db.Text)

class Solution(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    task_id = db.Column(db.Integer,db.ForeignKey('task.id'))
    user_id = db.Column(db.Integer,db.ForeignKey('user.id'))
    source_code = db.Column(db.Text)
    successful = db.Column(db.Boolean)

    
user_datastore = SQLAlchemyUserDatastore(db, User, Role)