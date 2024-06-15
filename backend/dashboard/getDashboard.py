from dashboard import dashboard
from flask import request, jsonify,session

@dashboard.route('/', methods=['GET'])
def profile():
    if 'user' in session:
        return jsonify({'message': f"Hello, {session['user']}!"}),200
    return jsonify({'message': f"please login!"}),400