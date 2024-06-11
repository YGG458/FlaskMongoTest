from flask import request, jsonify, session
from flask_bcrypt import Bcrypt
from auth import auth
from flask_jwt_extended import create_access_token
from database import db
bcrypt = Bcrypt()

@auth.route('login', methods=['POST'])
def login():
    User=db['UserInfo']
    data = request.get_json()
    if not data:
        return jsonify({'message': 'Mail and password are required'}), 400
    if not data['mail']:
        return jsonify({'message': 'Mail address are required'}), 400
    if not data['password']:
        return jsonify({'message': 'Password are required'}), 400
    # Check if the user exists
    existing_user = User.find_one({'mail': data['mail'].lower()})   
    if not existing_user:
        return jsonify({'message': 'No such a User! Invalid mail or password'}), 401

    # Check if the password is correct
    if bcrypt.check_password_hash(existing_user['password'], data['password']):
        access_token = create_access_token(identity=existing_user['mail'])
        session['user'] = existing_user['mail']
        return jsonify({'message': 'Login successful', 'access_token': access_token}), 200
    else:
        return jsonify({'message': 'Invalid mail or password'}), 401
