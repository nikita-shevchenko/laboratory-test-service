from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:3044344@127.0.0.1:5432/test'
db = SQLAlchemy(app)

groups_have_subjects_table = db.Table('groups_have_subjects',
                                      db.Column('subject_name', db.String(100),
                                                db.ForeignKey('subject.subject_name'), primary_key=True),
                                      db.Column('group_name', db.String(10), primary_key=True),
                                      db.Column('group_year', db.Integer, primary_key=True),
                                      db.ForeignKeyConstraint(('group_name', 'group_year'),
                                                              ('group.group_name', 'group.group_year'))
                                      )
laboratory_have_tests_table = db.Table('laboratory_have_tests',
                                       db.Column('test_name', db.String(500),
                                                 db.ForeignKey('test.test_name'), primary_key=True),
                                       db.Column('laboratory_theme', db.String(500),
                                                 db.ForeignKey('laboratory.laboratory_theme'), primary_key=True)
                                       )
subjects_have_materials_table = db.Table('subjects_have_materials',
                                         db.Column('subject_name', db.String(100),
                                                   db.ForeignKey('subject.subject_name'), primary_key=True),
                                         db.Column('material_name', db.String(500), primary_key=True),
                                         db.Column('material_author', db.String(500), primary_key=True),
                                         db.ForeignKeyConstraint(('material_name', 'material_author'),
                                                                 ('material.material_name', 'material.material_author'))
                                         )


class Student(db.Model):
    record_book = db.Column(db.String(6), primary_key=True)
    group_year = db.Column(db.Integer, primary_key=True)
    group_name = db.Column(db.String(10), nullable=False)
    student_name = db.Column(db.String(500), nullable=False)
    student_email = db.Column(db.String(200), nullable=False)
    student_phone = db.Column(db.String(50), nullable=True)
    implementations = db.relationship('Implementation', backref='student')
    __table_args__ = (db.ForeignKeyConstraint(('group_name', 'group_year'),
                                              ('group.group_name', 'group.group_year')), {})


class Group(db.Model):
    group_name = db.Column(db.String(10), primary_key=True)
    group_year = db.Column(db.Integer, primary_key=True)
    students = db.relationship('Student', backref='group')
    subjects = db.relationship('Subject', secondary=groups_have_subjects_table)


class Subject(db.Model):
    subject_name = db.Column(db.String(100), primary_key=True)
    laboratory = db.relationship('Laboratory', backref='subject')
    materials = db.relationship('Material', secondary=subjects_have_materials_table)


class Laboratory(db.Model):
    laboratory_theme = db.Column(db.String(500), primary_key=True)
    subject_name = db.Column(db.String(100), db.ForeignKey('subject.subject_name'), nullable=False)
    laboratory_goal = db.Column(db.String(500), nullable=True)
    laboratory_number = db.Column(db.Integer, nullable=False)
    tasks = db.relationship('Task', backref='laboratory')
    implementations = db.relationship('Implementation', backref='laboratory')
    tests = db.relationship('Test', secondary=laboratory_have_tests_table)


class Task(db.Model):
    variant = db.Column(db.Integer, primary_key=True)
    laboratory_theme = db.Column(db.String(500), db.ForeignKey('laboratory.laboratory_theme'), primary_key=True)
    laboratory_task = db.Column(db.Text, nullable=False)


class Implementation(db.Model):
    attempt = db.Column(db.Integer, primary_key=True)
    record_book = db.Column(db.String(6), primary_key=True)
    group_year = db.Column(db.Integer, primary_key=True)
    laboratory_theme = db.Column(db.String(500), db.ForeignKey('laboratory.laboratory_theme'), primary_key=True)
    mark = db.Column(db.Integer, nullable=True)
    implementation_content = db.Column(db.Text, nullable=False)
    test_output = db.Column(db.Text, nullable=True)
    operator_sequence = db.Column(db.Text, nullable=True)
    plagiary = db.Column(db.Integer, nullable=True)
    __table_args__ = (db.ForeignKeyConstraint(('record_book', 'group_year'),
                                              ('student.record_book', 'student.group_year')), {})


class Test(db.Model):
    test_name = db.Column(db.String(500), primary_key=True)
    input_data = db.Column(db.Text, nullable=False)
    expected_result = db.Column(db.Text, nullable=False)
    output_data = db.Column(db.Text, nullable=True)


class Material(db.Model):
    material_name = db.Column(db.String(500), primary_key=True)
    material_author = db.Column(db.String(500), primary_key=True)
    label_number = db.Column(db.Integer, db.ForeignKey('label.label_number'), nullable=True)
    material_content = db.Column(db.Text, nullable=True)


class Label(db.Model):
    label_number = db.Column(db.Integer, primary_key=True)
    label_name = db.Column(db.String(100), nullable=True)
    materials = db.relationship('Material', backref='label')
    resources = db.relationship('Resource', backref='label')


class Resource(db.Model):
    resource_name = db.Column(db.String(500), primary_key=True)
    resource_source = db.Column(db.String(500), primary_key=True)
    label_number = db.Column(db.Integer, db.ForeignKey('label.label_number'), nullable=True)
    resource_content = db.Column(db.Text, nullable=True)
    rating = db.Column(db.Integer, nullable=False)


db.create_all()
