from .code_tester import Tester
from . import db
from flask import jsonify
from flask_restful import Resource,reqparse
from .models import Role, Task, Solution, User
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

    def delete(self,task_id):
        if task_id>0:
            Task.query.filter(Task.id==task_id).delete()
            db.session.commit()
            


class Solutions(Resource):
    def get(self):
        data = Solution.query.join(User,Solution.user_id==User.id)\
        .add_columns(User.username)\
        .join(Task,Solution.task_id==Task.id)\
        .add_columns(Task.title)\
        .all()
        res = []
        for d in data:
            solution,username,task_title = d
            res.append(
            {
                'id':solution.id,
                'task_id':solution.task_id,
                'user_id':solution.user_id,
                'source_code':solution.source_code,
                'successful':solution.successful,
                'username':username,
                'task_title':task_title
            }
            )
        return jsonify(res)         

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('title', type=str)
        parser.add_argument('task_id', type=str)
        #parser.add_argument('author_id',type=int)
        parser.add_argument('source_code',type=str)  
        parser.add_argument('user_id',type=int)      
        data = parser.parse_args()
        solution = Solution()
        solution.source_code=data['source_code']
        solution.task_id = data['task_id']
        solution.user_id = data['user_id']
        task_data = Task.query.filter_by(id=data['task_id']).first()
        task = Task()
        task.id=task_data.id
        task.tests=task_data.tests
        task.title=task_data.title
        task.author_id=task_data.author_id
        

        tester = Tester("",solution.source_code,task.title,task.tests)
        status,mes = tester.run_tests()
        if status:
            solution.successful=True
            db.session.add(solution)
            db.session.commit()
        return jsonify({'status':status,'mes':mes})

    def delete(self,solution_id):
        if solution_id>0:
            Solution.query.filter(Solution.id == solution_id).delete()
            db.session.commit()

    
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
            if len(current_user.roles)<1:
                role = ''
            else:
                role = current_user.roles[0].name
            response = build_data_response({
                "user_id": current_user.id,
                "username": current_user.username,
                "email": current_user.email,
                "role": role
            },
            200,)

        return response

class LogOut(Resource):
    def post(self):
        from flask_login import logout_user
        logout_user()

class Users(Resource):
    def get(self):
        users = User.query.with_entities(User.id,User.username,User.status)
        res = []
        for user in users:
            res.append(
                {
                    'id':user.id,
                    'username':user.username,
                    'status':user.status
                }
            )
        return res
    def delete(self,user_id):
        if user_id>0:
            User.query.filter(User.id == user_id).delete()
            db.session.commit()


