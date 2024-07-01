from flask import request, jsonify
from flask_bcrypt import Bcrypt
import re
from flask_mail import Message
from auth import auth
from datetime import datetime, timedelta
from database import db
bcrypt = Bcrypt()

@auth.route('test',methods=['post'])
def TESTregister():
    User=db["UserInfo"]
    data=request.get_json()
    hashed_password = bcrypt.generate_password_hash(data['password']).decode('utf-8')
    # Insert new user into the database
    User.insert_one({'username': data['username'], 'password': hashed_password,'mail':data['mail'].lower(),'role':'student'})
    return jsonify({'message': 'User registered successfully'}), 201
    


