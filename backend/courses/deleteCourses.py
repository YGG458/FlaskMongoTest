from flask import request, jsonify
from courses import courses

@courses.route('/delete',methods=['DELETE'])
def deleteCourses():
    if True:
        return jsonify({'message': 'Course(s) delete successful'}), 200
    else:
        return jsonify({'message': 'Invalid mail or password'}), 401

