from flask import request, jsonify
from projects import projects


@projects.route('/delete',method=['DELETE'])
def deleteCourses():
    if True:
        return jsonify({'message': 'Project delete successful'}), 200
    else:
        return jsonify({'message': 'Invalid mail or password'}), 401

