from flask import request, jsonify
from flask_bcrypt import Bcrypt
from api import api

bcrypt = Bcrypt()

@api.route('login', methods=['POST'])
def login(db,mail):
    User=db['UserInfo']
    data = request.get_json()
    if not data:
        return jsonify({'message': 'Mail and password are required'}), 400
    if not data['mail']:
        return jsonify({'message': 'Mail address are required'}), 400
    if not data['password']:
        return jsonify({'message': 'Password are required'}), 400
    # Check if the user exists
    existing_user = User.find_one({'mail': data['mail']})   
    if not existing_user:
        return jsonify({'message': 'No such a User! Invalid mail or password'}), 401

    # Check if the password is correct
    if bcrypt.check_password_hash(existing_user['password'], data['password']):
        return jsonify({'message': 'Login successful'}), 200
    else:
        return jsonify({'message': 'Invalid mail or password'}), 401
