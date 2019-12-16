from db import Base
from sqlalchemy import Column, Integer, String, Text, ForeignKey, Table
from sqlalchemy.orm import relationship

groups_have_subjects_table = Table('groups_have_subjects', Base.metadata,
                                   Column('subject_name', String(100), ForeignKey('subject.subject_name')),
                                   Column('group_name', String(10), ForeignKey('group.group_name')),
                                   Column('group_year', Integer, ForeignKey('group.group_year'))
                                   )
laboratory_have_tests_table = Table('laboratory_have_tests', Base.metadata,
                                    Column('test_name', String(500), ForeignKey('test.test_name')),
                                    Column('laboratory_theme', String(500), ForeignKey('laboratory.laboratory_theme'))
                                    )
subjects_have_materials_table = Table('subjects_have_materials', Base.metadata,
                                      Column('subject_name', String(100), ForeignKey('subject.subject_name')),
                                      Column('material_name', String(500), ForeignKey('material.material_name')),
                                      Column('material_author', String(500), ForeignKey('material.material_author'))
                                      )


class Student(Base):
    __tablename__ = 'student'
    record_book = Column(String(6), primary_key=True)
    group_year = Column(Integer, ForeignKey('group.group_year'), primary_key=True)
    group_name = Column(String(10), ForeignKey('group.group_name'), nullable=False)
    student_name = Column(String(500), nullable=False)
    student_email = Column(String(200), nullable=False)
    student_phone = Column(String(50), nullable=True)
    group = relationship('Group', back_populates='students')
    implementations = relationship('Implementation', back_populates='student')


class Group(Base):
    __tablename__ = 'group'
    group_name = Column(String(10), primary_key=True)
    group_year = Column(Integer, primary_key=True)
    students = relationship('Student', back_populates='group')
    subjects = relationship('Subject', secondary=groups_have_subjects_table)


class Subject(Base):
    __tablename__ = 'subject'
    subject_name = Column(String(100), primary_key=True)
    laboratory = relationship('Laboratory', back_populates='subject')
    materials = relationship('Material', secondary=subjects_have_materials_table)


class Laboratory(Base):
    __tablename__ = 'laboratory'
    laboratory_theme = Column(String(500), primary_key=True)
    subject_name = Column(String(100), ForeignKey('subject.subject_name'), nullable=False)
    laboratory_goal = Column(String(500), nullable=True)
    laboratory_number = Column(Integer, nullable=False)
    subject = relationship('Subject', back_populates='laboratory')
    tasks = relationship('Task', back_populates='laboratory')
    implementations = relationship('Implementation', back_populates='laboratory')
    tests = relationship('Test', secondary=laboratory_have_tests_table)


class Task(Base):
    __tablename__ = 'task'
    variant = Column(Integer, primary_key=True)
    laboratory_theme = Column(String(500), ForeignKey('laboratory.laboratory_theme'), primary_key=True)
    laboratory_task = Column(Text, nullable=False)
    laboratory = relationship('Laboratory', back_populates='tasks')


class Implementation(Base):
    __tablename__ = 'implementation'
    attempt = Column(Integer, primary_key=True)
    record_book = Column(String(6), ForeignKey('student.record_book'), primary_key=True)
    group_year = Column(Integer, ForeignKey('student.group_year'), primary_key=True)
    laboratory_theme = Column(String(500), ForeignKey('laboratory.laboratory_theme'), primary_key=True)
    mark = Column(Integer, nullable=True)
    implementation_content = Column(Text, nullable=False)
    test_output = Column(Text, nullable=True)
    operator_sequence = Column(Text, nullable=True)
    plagiary = Column(Integer, nullable=True)
    student = relationship('Student', back_populates='implementations')
    laboratory = relationship('Laboratory', back_populates='implementations')


class Test(Base):
    __tablename__ = 'test'
    test_name = Column(String(500), primary_key=True)
    input_data = Column(Text, nullable=False)
    expected_result = Column(Text, nullable=False)
    output_data = Column(Text, nullable=True)


class Material(Base):
    __tablename__ = 'material'
    material_name = Column(String(500), primary_key=True)
    material_author = Column(String(500), primary_key=True)
    label_number = Column(Integer, ForeignKey('label.label_number'), nullable=True)
    material_content = Column(Text, nullable=True)
    label = relationship('Label', back_populates='materials')


class Label(Base):
    __tablename__ = 'label'
    label_number = Column(Integer, primary_key=True)
    label_name = Column(String(100), nullable=True)
    materials = relationship('Material', back_populates='label')
    resources = relationship('Resource', back_populates='label')


class Resource(Base):
    __tablename__ = 'resource'
    resource_name = Column(String(500), primary_key=True)
    resource_source = Column(String(500), primary_key=True)
    label_number = Column(Integer, ForeignKey('label.label_number'), nullable=True)
    resource_content = Column(Text, nullable=True)
    rating = Column(Integer, nullable=False)
    label = relationship('Label', back_populates='resources')
