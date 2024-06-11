from flask import request, jsonify
from courses import courses

@courses.route('/edit',methods=['PUT'])
def editCourses():
    if True:
        return jsonify({'message': 'Course(s) edit successful'}), 200
    else:
        return jsonify({'message': 'Invalid mail or password'}), 401

