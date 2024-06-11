from dashboard import dashboard
from flask import request, jsonify,session

@dashboard.route('/profile', methods=['GET'])
def profile():
    if 'user' in session and '1229200091@qq.com' in session['user']:
        return jsonify({'message': f"Hello, {session['user']}!"}),200
    return jsonify({'message': f"please login!"}),400