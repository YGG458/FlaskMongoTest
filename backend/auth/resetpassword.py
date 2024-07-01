from flask import request, jsonify
from flask_bcrypt import Bcrypt
import re
from flask_mail import Message
from auth import auth
from datetime import datetime, timedelta
import secrets
from database import db
from mail import mail
bcrypt = Bcrypt()

@auth.route('resetpassword', methods=['POST'])
def resetpassword():
    Temp=db["TempUser"]
    User=db["UserInfo"]
    data = request.get_json()
    if not data['password']:
        return jsonify({'message': 'Password are required'}), 400
    if not data['passwordConfirm'] :
        return jsonify({'message': 'Please enter your password twice'}), 400
    if not data['mail']:
        return jsonify({'message': 'Please enter your email!'}), 400
    if not validate_password(data['password']):
        return jsonify({'message': 'Password must contain at least one uppercase letter, one lowercase letter, one digit, and be no longer than 12 characters'}), 400
    if not is_valid_email(data['mail'].lower()):
        return jsonify({'message': 'Please enter a valid email address'}), 400
    if data['passwordConfirm']!=data['password']:
        return jsonify({'message': 'Please confirm the two passwords you enter is same'}), 400
    Email=data['mail'].lower()
    CurrentUser=User.find_one({'mail':Email})
    if CurrentUser:
        InTemp=Temp.find_one({'mail': Email})
        if InTemp:
            if outOfTime(InTemp):
                return jsonify({'message': 'Please don’t send too frequently！You can just send once in 30s'}), 429
            else:
                newCode=secrets.token_hex(3)
                newTime=datetime.now()
                SendMail(mail,newTime,newCode,data['mail'].lower())
                Temp.update_one({'mail': Email}, {'$set': {'lastTime': newTime,'code':newCode}})
                
                return jsonify({'message': f"CAPTCHA was sent to {Email} successfully! Please check your mail box!"}), 201
        newCode=secrets.token_hex(3)
        newTime=datetime.now()
        SendMail(mail,newTime,newCode,data['mail'])
        Temp.insert_one({'mail': Email,'lastTime': newTime,'code':newCode})
        return jsonify({'message': f'CAPTCHA was sent to {Email} successfully! Please check your mail box!'}), 201
    else:
        return jsonify({'message': 'This email is not yet registered'}), 400
def SendMail(mail,time,code,recipent):
    msg = Message('Your CAPTCHA', sender = 'G506404@163.com' , recipients = [recipent])
    msg.body = f'''
        Hello,THIS IS YOUR CAPTHA:
                {code}
        It is valid before {time+timedelta(minutes=5)} !
    '''
    success = mail.send(msg)

    if success:
        return True
    else:
        return False
    

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
        return True
    return False

def is_valid_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if re.match(pattern, email):
        return True
    else:
        return False