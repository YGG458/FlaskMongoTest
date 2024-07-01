from flask import request, jsonify
from flask_bcrypt import Bcrypt
import re
from flask_mail import Message
from admin import admin
from datetime import datetime, timedelta
from database import db
bcrypt = Bcrypt()
@admin.route('register',methods=['post'])
def register():
    User=db["UserInfo"]
    Temp=db["TempUser"]
    data=request.get_json()
    hashed_password = bcrypt.generate_password_hash(data['password']).decode('utf-8')
    # Insert new user into the database
    User.insert_one({'username': data['username'], 'password': hashed_password,'mail':data['mail'].lower(),'role':'admin'})
    Temp.delete_one({'mail':data['mail'].lower()})
    User.create_index('mail', unique=True)
    return jsonify({'message': 'ADMIN registered successfully'}), 201
    