from flask import request, jsonify
from courses import courses

@courses.route('/',methods=['GET'])
def showCourses(): #show all courses list
    if True:
        return jsonify({'message': 'Course(s) get successful'}), 200
    else:
        return jsonify({'message': 'Invalid mail or password'}), 401

