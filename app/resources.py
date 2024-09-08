from flask_restx import Namespace, Resource
from .models import Course
from .models import Student
from .api_models import student_model
from .api_models import course_model
from .api_models import course_input_model
from .api_models import student_input_model
from .extensions import db

ns = Namespace("api")

@ns.route("/hello")
class Hello(Resource):
    def get(self):
        return {'hello': 'world'}
    

@ns.route("/courses")
class CoursesListAPI(Resource):
    @ns.marshal_list_with(course_model)
    def get(self):
        return Course.query.all()
    
    @ns.expect(course_input_model)
    @ns.marshal_with(course_model, code=201)
    def post(self):
        print(ns.payload)
        course = Course(name=ns.payload["name"])
        db.session.add(course)
        db.session.commit()
        return course, 201
    
@ns.route("/course/<int:id>")
class CourseAPI(Resource):
    @ns.marshal_with(course_model)
    def get(self, id):
        return Course.query.get(id)
    
    def delete(self, id):
        course = Course.query.get(id)
        db.session.delete(course)
        db.session.commit()
        return None, 204
    
    @ns.expect(course_input_model)
    @ns.marshal_with(course_model)
    def put(self, id):
        course = Course.query.get(id)
        course.name = ns.payload["name"]
        db.session.commit()
        return course
    
@ns.route("/student")
class StudentAPI(Resource):
    @ns.marshal_list_with(student_model)
    def get(self):
        return Student.query.all()
    
    @ns.expect(student_input_model)
    @ns.marshal_with(student_model, code=201)
    def post(self):
        print(ns.payload)
        student = Student(name=ns.payload["name"], course_id = ns.payload["course_id"])
        db.session.add(student)
        db.session.commit()
        return student, 201
    
@ns.route("/student/<int:id>")
class StudentAPI(Resource):
    @ns.marshal_with(student_model)
    def get(self, id):
        return Student.query.get(id)
    
    def delete(self, id):
        student = Student.query.get(id)
        db.session.delete(student)
        db.session.commit()
        return None, 204
    
    @ns.expect(student_input_model)
    @ns.marshal_with(student_model)
    def put(self, id):
        student = Student.query.get(id)
        student.name = ns.payload["name"]
        student.course_id = ns.payload["course_id"]
        db.session.commit()
        return student
    