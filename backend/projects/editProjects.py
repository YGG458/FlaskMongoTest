from flask import request, jsonify
from projects import projects

@projects.route('/edit',method=['PUT'])
def putProjects():
    if True:
        return jsonify({'message': 'Project(s) add successful'}), 200
    else:
        return jsonify({'message': 'Invalid mail or password'}), 401

