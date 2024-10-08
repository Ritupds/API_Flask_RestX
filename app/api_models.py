from .extensions import api
from flask_restx import fields

student_model = api.model("Student", {
    "id": fields.Integer,
    "name": fields.String,
    # "course": fields.Nested(course_model)
})

course_model = api.model("Course", {
    "id": fields.Integer,
    "name": fields.String,
    "students": fields.List(fields.Nested(student_model))
})

# student_model = api.model("Student", {
#     "id": fields.Integer,
#     "name": fields.String,
#     # "course": fields.Nested(course_model)
# })

course_input_model = api.model("CourseInput", {
    "name": fields.String,
})

student_input_model = api.model("StudentInput", {
    "name": fields.String,
    "course_id": fields.Integer
})

event_model = api.model("Event", {
    "id": fields.Integer,
    "name": fields.String,
    "date": fields.DateTime,
    "description": fields.String
})

event_input_model = api.model("EventInput", {
    "name": fields.String,
    "date": fields.DateTime,
    "description": fields.String
})