from flask import Blueprint
courses=Blueprint('courses',__name__)

from . import addCourses,deleteCourses,editCourses,getCourses

