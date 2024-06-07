from flask import Blueprint, request, jsonify
from flask_pymongo import PyMongo
from flask_bcrypt import Bcrypt
from flask_cors import CORS

login_api = Blueprint('login_api', __name__)
CORS(login_api)
bcrypt = Bcrypt()

@login_api.route('', methods=['POST'])
def login(UserCollection):
    data = request.get_json()

    # Check if the user exists
    existing_user = UserCollection.find_one({'username': data['username']})
    if not existing_user:
        return jsonify({'message': 'Invalid username or password'}), 401

    # Check if the password is correct
    if bcrypt.check_password_hash(existing_user['password'], data['password']):
        return jsonify({'message': 'Login successful'}), 200
    else:
        return jsonify({'message': 'Invalid username or password'}), 401
