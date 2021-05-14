from flask import Flask,jsonify
import flask.scaffold
flask.helpers._endpoint_from_view_func = flask.scaffold._endpoint_from_view_func
from flask_restful import Api,Resource
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

application = Flask(__name__)
api = Api(application)

class Somedata(Resource):
    def get(self):
        return jsonify({'some':'data'})

api.add_resource(Somedata,'/somedata')

