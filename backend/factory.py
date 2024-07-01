from flask.json import JSONEncoder
from bson import json_util, ObjectId
from datetime import datetime, timedelta
from flask import Flask
from database import *
from flask_restful import Api
from flask_cors import CORS
from flask_mail import Mail,Message
from auth import auth
from courses import courses
from dashboard import dashboard
from projects import projects
import os


class MongoJsonEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.strftime("%Y-%m-%d %H:%M:%S")
        if isinstance(obj, ObjectId):
            return str(obj)
        return json_util.default(obj, json_util.CANONICAL_JSON_OPTIONS)

def create_app():

    app = Flask(__name__)
    CORS(app)
    app.config['MAIL_SERVER']='smtp.163.com'   
    app.config['MAIL_PORT'] = 465      
    app.config['MAIL_USERNAME'] = os.getenv('EMAIL_USERNAME')
    app.config['MAIL_PASSWORD'] = os.getenv('EMAIL_PASSWORD')
    app.config['MAIL_USE_TLS'] = False    
    app.config['MAIL_USE_SSL'] = True   
    mail = Mail(app)    

    app.register_blueprint(auth,url_prefix='/auth')
    app.register_blueprint(dashboard,url_prefix='/dashboard')
    app.register_blueprint(courses,url_prefix='/courses')
    app.register_blueprint(projects,url_prefix='/projects')
    app.json_encoder = MongoJsonEncoder
    @app.route('/a')
    def login():
        return "You successfully connect to here!"

    return app