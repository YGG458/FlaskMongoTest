from flask import request, jsonify
from projects import projects

@projects.route('/add',methods=['POST'])
def addProjects():
    if True:
        return jsonify({'message': 'Project(s) add successful'}), 200
    else:
        return jsonify({'message': 'Invalid mail or password'}), 401

