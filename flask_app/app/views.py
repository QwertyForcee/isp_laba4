from . import db
from flask import jsonify
from flask_restful import Resource
from .models import Task, Solution

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

    



