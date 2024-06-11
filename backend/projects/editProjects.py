from flask import request, jsonify
from projects import projects

@projects.route('/edit',methods=['PUT'])
def putProjects():
    if True:
        return jsonify({'message': 'Project(s) edit successful'}), 200
    else:
        return jsonify({'message': 'Invalid mail or password'}), 401

