from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, IntegerField
from wtforms.validators import Email, regexp


class StudentEditForm(FlaskForm):
    record_book = StringField('record_book')
    full_name = StringField('full_name')
    email = StringField('email', validators=[Email()])
    phone = StringField('phone')
    delete = BooleanField('delete', default=False)


class ResourceEditForm(FlaskForm):
    resource_name = StringField('resource_name')
    label = IntegerField('label')
    content = StringField('content')
    rating = IntegerField('rating')
    delete = BooleanField('delete', default=False)


class LaboratoryEditForm(FlaskForm):
    number = IntegerField('number')
    variant = IntegerField('variant')
    task = StringField('task')
    delete = BooleanField('delete', default=False)
