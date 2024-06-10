from flask import Flask
from database import *
from flask_cors import CORS
from flask_mail import Mail,Message
from auth import auth
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

my_client=get_client()
db =  get_database(my_client)
Collection = get_collection(db,'UserInfo')   
try:
    my_client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)     

#app.register_blueprint(register_api,url_prefix='/register',url_defaults={'UserCollection':Collection,'mail':mail})
#app.register_blueprint(register_api,url_prefix='/register', url_defaults={'UserCollection':Collection})
app.register_blueprint(auth,url_prefix='/auth', url_defaults={'db':db,'mail':mail})

@app.route('/')
def login():
    return "You successfully connect to here!"

if __name__ == '__main__':
    app.run(host="0.0.0.0",debug=True)
