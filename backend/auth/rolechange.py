from flask import request, jsonify
from flask_mail import Message
from auth import auth
from datetime import datetime, timedelta
from database import db
from mail import mail
from flask_jwt_extended import JWTManager, jwt_required,get_jwt_identity

@auth.route("/rolechange",methods=["POST"])
@jwt_required()
def rolechange():
    current_user = get_jwt_identity()  # 获取当前用户的身份信息
    username=current_user["username"]
    email=current_user["mail"]
    role=current_user["role"]
    if role!="student":
        return jsonify({'message': f'You are already an academic user!'}), 400
    application=db["RoleChangeApplication"]
    data=request.get_json()
    reason=data["reason"]
    applyTime=datetime.now().strftime("%Y-%m-%d %H:%M")
    if application.find_one({'Email':email}):
        application.update_one({"Email":email},{'$set': {'Reason':reason,'Apply time': applyTime}})
        return jsonify({'message': f'You already apply once! Your application was update! Pleas wait for approval!'}), 201
    #SendMail(mail,reason,username,email)
    application.insert_one({'Name':username,"Email":email,"Reason":reason,"Status":"under review",'Apply time':applyTime})
    return jsonify({'message': f'Application was sent to admin successfully! Pleas wait for approval!'}), 201

def SendMail(mail,reason,name,email):
    msg = Message('A new application', sender = 'G506404@163.com' , recipients = ['1229200091@qq.com'] )
    msg.body = f'''
        Hello,there is a new application by user:{name} email:{email}:
        Details: {reason} !
    '''
    success = mail.send(msg)

    if success:
        return True
    else:
        return False
    