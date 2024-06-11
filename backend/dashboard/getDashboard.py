from dashboard import dashboard
from flask import request, jsonify

@dashboard.route('/',methods=['GET'])
def getDashboard():
    return jsonify({"message":"111"}),200
