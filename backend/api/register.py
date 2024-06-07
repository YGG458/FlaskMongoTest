from flask import Blueprint, request, jsonify
from flask_pymongo import PyMongo
from flask_bcrypt import Bcrypt
from pymongo import MongoClient
import re
from flask_cors import CORS
register_api = Blueprint('register_api', __name__)

CORS(register_api)

bcrypt = Bcrypt()

@register_api.route('', methods=['POST'])
def register(UserCollection):
    data = request.get_json()
    
    if not data['username'] or not data['password']:
        return jsonify({'message': 'Username and password are required'}), 400
    
    if not validate_username(data['username']):
        return jsonify({'message': 'Username must be between 2 and 8 characters long'}), 400
    
    if not validate_password(data['password']):
        return jsonify({'message': 'Password must contain at least one uppercase letter, one lowercase letter, one digit, and be no longer than 12 characters'}), 400

    # Check if the user already exists
    existing_user = UserCollection.find_one({'username': data['username']})
    if existing_user:
        return jsonify({'message': 'Username already exists'}), 400

    # Hash the password
    hashed_password = bcrypt.generate_password_hash(data['password']).decode('utf-8')

    # Insert new user into the database
    user_id = UserCollection.insert_one({'username': data['username'], 'password': hashed_password})
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
    if len(username) < 2 or len(username) > 8:
        return False
    return True
