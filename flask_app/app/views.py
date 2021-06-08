from . import db
from flask import jsonify
from flask_restful import Resource,reqparse
from .models import Task, Solution
from flask_security import current_user

class Tasks(Resource):
    def get(self,task_id=0):
        print('task id',task_id)
        if task_id == 0:
            data = Task.query.all()
            res = []
            for d in data:
                res.append(
                {
                    'id':d.id,
                    'title':d.title,
                    'description':d.description,
                    'author_id':d.author_id,
                    'tests':d.tests
                }
                )
            return jsonify(res)
        else:
            data = Task.query.filter_by(id=task_id).first()
            res = {
                    'id':data.id,
                    'title':data.title,
                    'description':data.description,
                    'author_id':data.author_id,
                    'tests':data.tests
                }
            return jsonify(res)

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('title', type=str)
        parser.add_argument('description', type=str)
        parser.add_argument('author_id',type=int)
        parser.add_argument('tests',type=str)        
        data = parser.parse_args()
        task = Task()
        task.author_id=data['author_id']
        task.title=data['title']
        task.description=data['description']
        task.tests = data['tests']
        db.session.add(task)
        db.session.commit()

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



