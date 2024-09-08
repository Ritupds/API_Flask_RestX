from .extensions import db

class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    students = db.relationship('Student', back_populates='course')




class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique= True, nullable=False)
    course_id = db.Column(db.ForeignKey('course.id'))

    course = db.relationship('Course', back_populates='students')


# # Adding multiple courses to the database session




# # Commit the session to save changes to the database
# db.session.commit()
