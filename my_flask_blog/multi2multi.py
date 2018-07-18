from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from blue_print import users



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:mysql@localhost:3306/my_form_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.register_blueprint(users)
db = SQLAlchemy(app)

tb_student_course = db.Table('tb_student_course',
                             db.Column('student_id', db.Integer, db.ForeignKey('student.id')),
                             db.Column('course_id', db.Integer, db.ForeignKey('course.id')))

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32))
    courses = db.relationship('Course', backref='students', secondary='tb_student_course')
    def __repr__(self):
        return 'Student: %s %s' % (self.name, self.id)


class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))

    def __repr__(self):
        return 'Courses: %s %s ' % (self.name, self.id)


@app.route('/')
def index():

    student_list = Student.query.all()

    return render_template('multi2multi.html', student_list=student_list)


if __name__ == '__main__':
    db.drop_all()
    db.create_all()

    stu1 = Student(name='张三')
    stu2 = Student(name='李四')
    stu3 = Student(name='王五')

    cou1 = Course(name='物理')
    cou2 = Course(name='化学')
    cou3 = Course(name='生物')

    stu1.courses = [cou2, cou3]
    stu2.courses = [cou2]
    stu3.courses = [cou1, cou2, cou3]

    db.session.add_all([stu1, stu2, stu2])
    db.session.add_all([cou1, cou2, cou3])

    db.session.commit()

    app.run(debug=True)
