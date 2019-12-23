from flask import render_template, Flask, request
from forms import StudentEditForm, ResourceEditForm, LaboratoryEditForm, AttemptToMarkDep
from models import Test, Implementation, Label, Material, Group, Subject, Task, Resource, Student, Laboratory, Library
from db import db
from commands import create_tables, populate_tables
import plotly
import plotly.graph_objs as go
import numpy as np
import json
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
app.config['SECRET_KEY'] = 'Thisisasecret'

db.init_app(app)

app.cli.add_command(create_tables)
app.cli.add_command(populate_tables)


@app.route('/')
def main():
    return render_template('main.html')


@app.route('/filllibrary')
def filllibrary():
    lib1 = Library('Kyiv library 1', 'gde-to', 'KM6202', 2016, 'Kyiv', 'Ukraine')
    lib2 = Library('Kyiv library 2', 'gde-to', 'KM6202', 2016, 'Kyiv', 'Ukraine')
    lib3 = Library('Kyiv library 3', 'gde-to', 'KM6202', 2016, 'Kyiv', 'Ukraine')

    db.session.add(lib1)
    db.session.add(lib2)
    db.session.add(lib3)

    db.session.commit()

@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    form = AttemptToMarkDep()
    if request.method == 'POST':
        recordbook = form.record_book.data
        labtheme = form.laboratory_theme.data
    else:
        recordbook = 'KM6203'
        labtheme = 'Integral'
    print(recordbook)
    data = Implementation.query\
        .filter_by(record_book=recordbook, laboratory_theme=labtheme).order_by(Implementation.attempt).all()
    attempt_list = []
    mark_list = []
    for i in range(len(data)):
        attempt_list.append(data[i].attempt)
        mark_list.append(data[i].mark)
    trace = go.Scatter(
        x=np.array(attempt_list),
        y=np.array(mark_list)
    )
    data_to_plot = [trace]
    graphJSON = json.dumps(data_to_plot, cls=plotly.utils.PlotlyJSONEncoder)
    return render_template('dashboard.html', graphJSON=graphJSON, form=form)


@app.route('/students', methods=['GET', 'POST'])
def students():
    form = StudentEditForm()
    if form.validate_on_submit():
        student = Student.query.filter_by(record_book=form.record_book.data).first()
        if form.delete.data:
            db.session.delete(student)
            db.session.commit()
        elif student is None:
            new_student = Student(form.record_book.data, form.group_year.data, form.group_name.data,
                                  form.student_name.data, form.student_email.data, form.student_phone.data)
            db.session.add(new_student)
            db.session.commit()
        else:
            student.group_year = form.group_year.data
            student.student_name = form.student_name.data
            student.group_name = form.group_name.data
            student.student_email = form.student_email.data
            student.student_phone = form.student_phone.data
            db.session.commit()
    headlines = ['record_book', 'group_year', 'group_name', 'student_name', 'student_email', 'student_phone',
                 'delete?', 'action']
    results = Student.query.all()
    student_list = []
    for i in range(len(results)):
        student_list.append(results[i])
    return render_template('students.html', students=student_list, form=form, headlines=headlines)


@app.route('/resources', methods=['GET', 'POST'])
def resources():
    form = ResourceEditForm()
    if form.validate_on_submit():
        resource = Resource.query.filter_by(resource_name=form.resource_name.data).first()
        if form.delete.data:
            db.session.delete(resource)
            db.session.commit()
        elif resource is None:
            new_resource = Resource(form.resource_name.data, form.resource_source.data,
                                    form.label_number.data, form.resource_content.data, form.rating.data)
            db.session.add(new_resource)
            db.session.commit()
        else:
            resource.resource_source = form.resource_source.data
            resource.label_number = form.label_number.data
            resource.resource_content = form.resource_content.data
            resource.rating = form.rating.data
            db.session.commit()

    headlines = ['resource_name', 'resource_source', 'label_number', 'resource_content', 'rating', 'delete?', 'action']
    results = Resource.query.all()
    resource_list = []
    for i in range(len(results)):
        resource_list.append(results[i])
    return render_template('resources.html', resources=resource_list, form=form, headlines=headlines)


@app.route('/laboratory', methods=['GET', 'POST'])
def laboratory():
    form = LaboratoryEditForm()
    if form.validate_on_submit():
        lab = Laboratory.query.filter_by(laboratory_theme=form.laboratory_theme.data).first()
        if form.delete.data:
            db.session.delete(lab)
            db.session.commit()
        elif lab is None:
            new_lab = Laboratory(form.laboratory_theme.data, form.subject_name.data,
                                 form.laboratory_goal.data, form.laboratory_number.data)
            db.session.add(new_lab)
            db.session.commit()
        else:
            lab.subject_name = form.subject_name.data
            lab.laboratory_goal = form.laboratory_goal.data
            lab.laboratory_number = form.laboratory_number.data
            db.session.commit()
    headlines = ['laboratory_theme', 'subject_name', 'laboratory_goal', 'laboratory_number', 'delete?', 'action']
    results = Laboratory.query.all()
    laboratory_list = []
    for i in range(len(results)):
        laboratory_list.append(results[i])
    return render_template('laboratory.html', laboratory=laboratory_list, form=form, headlines=headlines)


@app.route('/tasks')
def tasks():
    headlines = ['variant', 'laboratory_theme', 'laboratory_task']
    results = Task.query.all()
    task_list = []
    for i in range(len(results)):
        task_list.append([results[i].variant, results[i].laboratory_theme, results[i].laboratory_task])
    return render_template('table.html', entity='Task', data=task_list, headlines=headlines)


@app.route('/groups')
def groups():
    headlines = ['group_name', 'group_year']
    results = Group.query.all()
    group_list = []
    for i in range(len(results)):
        group_list.append([results[i].group_name,
                           results[i].group_year])
    return render_template('table.html', entity='Group', data=group_list, headlines=headlines)


@app.route('/subjects')
def subjects():
    headlines = ['subject_name']
    results = Subject.query.all()
    subject_list = []
    for i in range(len(results)):
        subject_list.append([results[i].subject_name])
    return render_template('table.html', entity='Subject', data=subject_list, headlines=headlines)


@app.route('/materials')
def materials():
    headlines = ['material_name', 'material_author', 'label_number', 'material_content']
    results = Material.query.all()
    material_list = []
    for i in range(len(results)):
        material_list.append([results[i].material_name,
                              results[i].material_author,
                              results[i].label_number,
                              results[i].material_content])
    return render_template('table.html', entity='Material', data=material_list, headlines=headlines)


@app.route('/labels')
def labels():
    headlines = ['label_number', 'label_name']
    results = Label.query.all()
    label_list = []
    for i in range(len(results)):
        label_list.append([results[i].label_number,
                           results[i].label_name])
    return render_template('table.html', entity='Cluster', data=label_list, headlines=headlines)


@app.route('/implementations')
def implementations():
    headlines = ['attempt', 'record_book', 'group_year', 'laboratory_theme', 'mark',
                 'implementation_content', 'test_output', 'operator_sequence', 'plagiary']
    results = Implementation.query.all()
    implementation_list = []
    for i in range(len(results)):
        implementation_list.append([results[i].attempt,
                                    results[i].record_book,
                                    results[i].group_year,
                                    results[i].laboratory_theme,
                                    results[i].mark,
                                    results[i].implementation_content,
                                    results[i].test_output,
                                    results[i].operator_sequence,
                                    results[i].plagiary,
                                    ])
    return render_template('table.html', entity='Work', data=implementation_list, headlines=headlines)


@app.route('/tests')
def tests():
    headlines = ['test_name', 'input_data', 'expected_result', 'output_data']
    results = Test.query.all()
    test_list = []
    for i in range(len(results)):
        test_list.append([results[i].test_name,
                          results[i].input_data,
                          results[i].expected_result,
                          results[i].output_data])
    return render_template('table.html', entity='Test', data=test_list, headlines=headlines)


if __name__ == '__main__':
    app.run()
