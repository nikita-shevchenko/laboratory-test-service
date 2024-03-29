from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, IntegerField, SelectField
from wtforms.validators import Email, regexp, Length


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


class AttemptToMarkDep(FlaskForm):
    laboratory_theme = StringField('laboratory_theme')
    record_book = StringField('record_book')

class LibraryEditForm(FlaskForm):
    library_name = StringField('library_name')
    library_address = StringField('library_address', validators=[Length(0, 10)])
    record_book = StringField('record_book')
    group_year = IntegerFields('group_year')
    library_city = SelectField('library_city', [('Kyiv', 'Kyiv'), ('Lviv', 'Lviv')])
    library_country = StringField('library_country')
    delete = BooleanField('delete', default=False)

