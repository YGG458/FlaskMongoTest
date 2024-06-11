from flask import Flask
from database import *
from flask_restful import Api
from flask_cors import CORS
from flask_mail import Mail,Message
from auth import auth
from courses import courses
import os
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
app.register_blueprint(courses,url_prefix='/courses')
@app.route('/')
def login():
    return "You successfully connect to here!"

if __name__ == '__main__':
    app.run(host="0.0.0.0",debug=True)
