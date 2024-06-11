from flask import request, jsonify
from flask_bcrypt import Bcrypt
import re
from flask_mail import Message
from auth import auth
from datetime import datetime, timedelta
from database import db
bcrypt = Bcrypt()

@auth.route('register',methods=['post'])
def register():
    User=db["UserInfo"]
    Temp=db["TempUser"]
    data = request.get_json()
    if not data:
        return jsonify({'message': 'Username and password are required'}), 400
    if not data['username']:
        return jsonify({'message': 'Username are required'}), 400
    if not data['password']:
        return jsonify({'message': 'Password are required'}), 400
    if not data['passwordConfirm'] :
        return jsonify({'message': 'Please enter your password twice'}), 400
    if not data['mail']:
        return jsonify({'message': 'Please enter your email!'}), 400
    if not validate_username(data['username']):
        return jsonify({'message': 'Username must be between 2 and 16 characters long'}), 400
    if not validate_password(data['password']):
        return jsonify({'message': 'Password must contain at least one uppercase letter, one lowercase letter, one digit, and be no longer than 12 characters'}), 400
    if not is_valid_email(data['mail'].lower()):
        return jsonify({'message': 'Please enter a valid email address'}), 400
    if data['passwordConfirm']!=data['password']:
        return jsonify({'message': 'Please confirm the two passwords you enter is same'}), 400
    if User.find_one({'username': data['username']}):
        return jsonify({'message': 'This username is already registered'}), 400
    if User.find_one({'mail': data['mail'].lower()}):
        return jsonify({'message': 'This email is already registered'}), 400
    TempUser=Temp.find_one({'mail': data['mail'].lower()})
    if not TempUser:
        return jsonify({'message': 'This email is not the one you just enter!'}), 400
    
    if datetime.now()>TempUser['lastTime']+timedelta(minutes=5):
        return jsonify({'message': 'This CAPTCHA is already Expired! Please retry!'}), 400
    if TempUser['code']!=data['code']:
        return jsonify({'message': 'You should enter the correct CAPTCHA! Please retry!'}), 400
    # Hash the password
    hashed_password = bcrypt.generate_password_hash(data['password']).decode('utf-8')
    # Insert new user into the database
    User.insert_one({'username': data['username'], 'password': hashed_password,'mail':data['mail'].lower(),'role':'student'})
    Temp.delete_one({'mail':data['mail'].lower()})
    return jsonify({'message': 'User registered successfully'}), 201
    


def validate_password(password):

    if not re.search(r'[A-Z]', password):
        return False
    if not re.search(r'[a-z]', password):
        return False
    if not re.search(r'[0-9]', password):
        return False
    if len(password) > 12:
        return False
    return True

def validate_username(username):
    if len(username) < 2 or len(username) > 16:
        return False
    return True

def outOfTime(InTemp):
    last_time=InTemp['lastTime']
    time=datetime.now()-last_time
    if  time < timedelta(seconds=30):
        return False
    return True


def is_valid_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if re.match(pattern, email):
        return True
    else:
        return False