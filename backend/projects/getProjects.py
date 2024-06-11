from flask import request, jsonify
from projects import projects


@projects.route('/',method=['GET'])
def showProjects(): #show all projects list
    if True:
        return jsonify({'message': 'project list'}), 200
    else:
        return jsonify({'message': 'Invalid mail or password'}), 401

