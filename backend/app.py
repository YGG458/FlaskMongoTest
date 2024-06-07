from flask import Flask
from database import *
from api.register import register_api
from api.login import login_api
from flask_cors import CORS
app = Flask(__name__)
CORS(app)

my_client=get_client()
dbname =  get_database(my_client)
Collection = get_collection(dbname,'UserInfo')   
try:
    my_client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)     

app.register_blueprint(register_api,url_prefix='/register',url_defaults={'UserCollection':Collection})
app.register_blueprint(login_api,url_prefix='/login', url_defaults={'UserCollection':Collection})


if __name__ == '__main__':

    app.run(debug=True)
