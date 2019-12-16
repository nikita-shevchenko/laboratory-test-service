from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, IntegerField
from wtforms.validators import Email, regexp


class StudentEditForm(FlaskForm):
    record_book = StringField('record_book')
    group_year = IntegerField('group_year')
    student_name = StringField('student_name')
    group_name = StringField('group_name')
    student_email = StringField('student_email', validators=[Email()])
    student_phone = StringField('student_phone')
    delete = BooleanField('delete', default=False)


class ResourceEditForm(FlaskForm):
    resource_name = StringField('resource_name')
    resource_source = StringField('resource_source')
    label_number = IntegerField('label_number')
    resource_content = StringField('resource_content')
    rating = IntegerField('rating')
    delete = BooleanField('delete', default=False)


class LaboratoryEditForm(FlaskForm):
    laboratory_theme = StringField('laboratory_theme')
    subject_name = StringField('subject_name')
    laboratory_goal = StringField('laboratory_goal')
    laboratory_number = IntegerField('laboratory_number')
    delete = BooleanField('delete', default=False)
