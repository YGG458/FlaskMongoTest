from flask import request, jsonify
from admin import admin
from flask_jwt_extended import jwt_required, get_jwt_identity
from database import db
@admin.route('/rolechange',methods=['GET'])
@jwt_required()  
def listRoleChange():
    collection=db["RoleChangeApplication"]
    current_user = get_jwt_identity()  # 获取当前用户的身份信息
    
    if current_user['role'] != 'admin':
        return jsonify({'message': 'Unauthorized. Only admin users can create courses.'}), 403
    
    cursor = collection.find({})  # 查询所有数据，也可以添加条件进行过滤

    # 格式化返回数据
    messages = []
    for document in cursor:
        message = {
            'Name': document['Name'],
            'Email': document['Email'],
            'Reason': document['Reason'],
            'Status': document['Status'],
            'Apply Time':document['Apply time']
        }
        messages.append(message)

    return jsonify({'list': messages}), 201
