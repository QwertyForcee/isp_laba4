from . import db
from flask import jsonify
from flask_restful import Resource
from .models import Task, Solution
from flask_security import current_user

class Tasks(Resource):
    def get(self):
        data = Task.query.all()
        res = []
        for d in data:
            res.append(
            {
                'id':d.id,
                'title':d.title,
                'description':d.description,
                'author_id':d.author_id,
            }
            )
        return jsonify(res) 

class Solutions(Resource):
    def get(self):
        data = Solution.query.all()
        res = []
        for d in data:
            res.append(
            {
                'id':d.id,
                'task_id':d.task_id,
                'author_id':d.author_id,
                'source_code':d.source_code,
                'successful':d.successful
            }
            )
        return jsonify(res)         

    
def build_data_response(data, code=200):
    res = {"meta": {"code": code}, "response": {"data": data}}
    response = jsonify(res)
    response.status_code = code
    return response

class UserGetView(Resource):
    def get(self):
        if not current_user.is_authenticated:
            #print('anonimoys')
            response = build_data_response({"user_id": None, "username": None, "email": None}, 200)
        else:
            response = build_data_response({
                "user_id": current_user.id,
                "username": current_user.username,
                "email": current_user.email,
            },
            200,)
        return response


