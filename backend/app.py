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
from flask_jwt_extended import JWTManager  # 添加 JWT 相关导入
from datetime import datetime, timedelta
from flask_session import Session
from jwt_utils import init_jwt
from admin import admin
app = Flask(__name__)
CORS(app)

app.config['MAIL_SERVER']='smtp.163.com'   
app.config['MAIL_PORT'] = 465      
app.config['MAIL_USERNAME'] = os.getenv('EMAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.getenv('EMAIL_PASSWORD')
app.config['MAIL_USE_TLS'] = False    
app.config['MAIL_USE_SSL'] = True   
mail = Mail(app)    

app.config['JWT_SECRET_KEY'] = 'Aa123456' #os.getenv('JWT_SECRET_KEY')   设置 JWT 密钥
app.secret_key = 'Aa123456' #os.getenv('SECRET_KEY') 
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(hours=1)  # 设置令牌有效期为1小时
jwt = JWTManager(app)  # 初始化 JWT 扩展
init_jwt(app)

app.config['SECRET_KEY'] = 'supersecretkey'
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)

app.register_blueprint(auth,url_prefix='/auth')
app.register_blueprint(dashboard,url_prefix='/dashboard')
app.register_blueprint(courses,url_prefix='/courses')
app.register_blueprint(projects,url_prefix='/projects')
app.register_blueprint(admin,url_prefix='/admin')

@app.route('/')
def login():
    return "You successfully connect to here!"

if __name__ == '__main__':
    app.run(host="0.0.0.0",debug=True)
