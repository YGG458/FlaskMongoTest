from flask import request, jsonify
from backend.courses.getCourses import courses

@courses.route('/',method=['GET'])
def showCourses(): #show all courses list
    if True:
        return jsonify({'message': 'Course(s) add successful'}), 200
    else:
        return jsonify({'message': 'Invalid mail or password'}), 401

