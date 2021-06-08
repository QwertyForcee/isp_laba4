#from flask_app.app.models import Task
from flask import Flask, app,jsonify,request
import flask.scaffold
flask.helpers._endpoint_from_view_func = flask.scaffold._endpoint_from_view_func
from flask_restful import Api,Resource
from flask_sqlalchemy import SQLAlchemy
import pymysql
pymysql.install_as_MySQLdb()
from flask_security import Security,current_user, auth_required, login_required
import flask_wtf

application = Flask(__name__,instance_relative_config=True)
from .config import Config

application.config.from_object(Config)
api = Api(application,prefix='/api/v1')

db = SQLAlchemy(application)


from flask_security import UserMixin, RoleMixin, SQLAlchemyUserDatastore

def configure_flask_security(app):
    # send CSRF cookie with the following key name
    app.config["SECURITY_CSRF_COOKIE"] = {"key": "XSRF-TOKEN"}

    # Don't have csrf tokens expire (they are invalid after logout)
    app.config["WTF_CSRF_TIME_LIMIT"] = None

    # don't return the CSRF cookie until user is logged in
    app.config["SECURITY_CSRF_IGNORE_UNAUTH_ENDPOINTS"] = True

    # disable WTF CSRF check since flask-security implements its own measures
    app.config["WTF_CSRF_CHECK_DEFAULT"] = False

    # allow login using username or email
    app.config["SECURITY_USER_IDENTITY_ATTRIBUTES"] = ["email", "username"]

    # allow registration of users
    app.config["SECURITY_REGISTERABLE"] = True

    # don't send registration email as we didn't specify a provider
    app.config["SECURITY_SEND_REGISTER_EMAIL"] = False

    # for security reasons always send the same message when username or password is wrong
    app.config["SECURITY_MSG_INVALID_PASSWORD"] = (
        "Wrong username or password.",
        "error",
    )
    app.config["SECURITY_MSG_USER_DOES_NOT_EXIST"] = (
        "Wrong username or password.",
        "error",
    )

    # disable redirects because Angular has its own forms
    app.config["SECURITY_REDIRECT_BEHAVIOR"] = "spa"

    # don't use the default unauthorized view since we implement
    # our own in angular
    app.config["SECURITY_UNAUTHORIZED_VIEW"] = None
    app.config["SECURITY_URL_PREFIX"] = "/api/v1"    

    from .models import user_datastore
    from flask_security.forms import ConfirmRegisterForm
    # Enable CSRF protection
    flask_wtf.CSRFProtect(app)
    from .sec_extentions import ExtendedLoginForm,ExtendedRegisterForm
    Security(
        app,
        user_datastore,
        confirm_register_form= ExtendedRegisterForm,#ExtendedRegisterForm,
        login_form=ExtendedLoginForm,
    )

    @app.before_request
    def is_valid_request():
        '''
        Checks if request is valid.
        :return:
        '''
        if (
            request.endpoint == "security.login"
            or request.endpoint == "security.register"
            or request.endpoint == "security.logout"
        ):
            print(request)
            if not request.is_json:
                raise CustomClientError("Mime type must be application/json.")
            if request.method != 'POST':
                raise CustomClientError("HTTP method is not valid.")


configure_flask_security(application)
class Somedata(Resource):
    def get(self):
        return jsonify({'some':'data'})

api.add_resource(Somedata,'/somedata')

from .views import Solutions,Tasks,UserGetView
api.add_resource(Solutions,"/solutions","/solutions/<int:solution_id>")
api.add_resource(Tasks,"/tasks","/tasks/<int:task_id>")
api.add_resource(UserGetView,"/users/current")

