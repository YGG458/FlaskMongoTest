from flask import Flask
from database import *
#from api.register import register_api
#from api.login import login_api
from flask_cors import CORS
from flask_mail import Mail,Message
from api import api
import os
app = Flask(__name__)
CORS(app)

app.config['MAIL_SERVER']='smtp.163.com'   
app.config['MAIL_PORT'] = 465      
app.config['MAIL_USERNAME'] = os.getenv('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.getenv('MAIL_PASSWORD')
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
app.register_blueprint(api,url_prefix='/api', url_defaults={'db':db,'mail':mail})

if __name__ == '__main__':

    app.run(debug=True)
