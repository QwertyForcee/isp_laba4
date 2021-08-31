  
import os

class Config:
    SECRET_KEY = 'zxc'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    ENV = "production"
    SECURITY_PASSWORD_SALT = "security-password-salt"
    basedir = os.path.abspath(os.path.dirname(__file__))
    SERVER_NAME = "localhost:5000"
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:maxim@db:3306/pyex'
    CORS_HEADERS = 'Content-Type'