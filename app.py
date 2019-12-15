from flask import render_template, Flask
from forms import StudentEditForm, ResourceEditForm, LaboratoryEditForm
from db import engine

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Thisisasecret'


@app.route('/')
def hello_world():
    return render_template('main.html')


@app.route('/student/delete', methods=['POST'])
def delete_student():
    pass


@app.route('/students', methods=['GET', 'POST'])
def students():
    form = StudentEditForm()
    if form.validate_on_submit():
        student_data = engine.execute("SELECT * FROM Student WHERE record_book='{record_book}'"
                                      .format(record_book=form.record_book.data))
        if form.delete.data:
            engine.execute("""
            DELETE FROM Student WHERE record_book='{record_book}'"""
                           .format(record_book=form.record_book.data))
        elif len(list(student_data)) == 0:
            engine.execute("""
            INSERT INTO Student (record_book, full_name, email, phone) 
            VALUES ('{record_book}', '{full_name}', '{email}', '{phone}')"""
                           .format(record_book=form.record_book.data, full_name=form.full_name.data,
                                   email=form.email.data, phone=form.phone.data))
        else:
            engine.execute("""
                        UPDATE Student
                        SET full_name='{full_name}', email='{email}', phone='{phone}'
                        WHERE record_book='{record_book}'
                        """.format(full_name=form.full_name.data, email=form.email.data,
                                   phone=form.phone.data, record_book=form.record_book.data))
    students_list = engine.execute("SELECT * FROM Student ORDER BY record_book")
    return render_template('students.html', students=list(students_list), form=form)


@app.route('/resources', methods=['GET', 'POST'])
def resources():
    form = ResourceEditForm()
    if form.validate_on_submit():
        resource_data = engine.execute("SELECT * FROM resource WHERE resource_name='{resource_name}'"
                                      .format(resource_name=form.resource_name.data))
        if form.delete.data:
            engine.execute("""
            DELETE FROM resource WHERE resource_name='{resource_name}'"""
                           .format(resource_name=form.resource_name.data))
        elif len(list(resource_data)) == 0:
            engine.execute("""
             INSERT INTO resource (resource_name, label, content, rating) 
             VALUES ('{resource_name}', '{label}', '{content}', '{rating}')"""
                           .format(resource_name=form.resource_name.data, label=form.label.data,
                                   content=form.content.data, rating=form.rating.data))
        else:
            engine.execute("""
                        UPDATE resource
                        SET label='{label}', content='{content}', rating='{rating}'
                        WHERE resource_name='{resource_name}'
                        """.format(label=form.label.data, content=form.content.data,
                                   rating=form.rating.data, resource_name=form.resource_name.data))

    resource_list = engine.execute("SELECT * FROM resource")
    return render_template('resources.html', resources=list(resource_list), form=form)


@app.route('/laboratory', methods=['GET', 'POST'])
def laboratory():
    form = LaboratoryEditForm()
    if form.validate_on_submit():
        laboratory_data = engine.execute("SELECT * FROM laboratory WHERE number='{number}' AND variant='{variant}'"
                                       .format(number=form.number.data, variant=form.variant.data))
        if form.delete.data:
            engine.execute("""
            DELETE FROM laboratory WHERE number='{number}' AND variant='{variant}'"""
                           .format(number=form.number.data, variant=form.variant.data))
        elif len(list(laboratory_data)) == 0:
            engine.execute("""
             INSERT INTO laboratory (number, variant, task) 
             VALUES ('{number}', '{variant}', '{task}')"""
                           .format(number=form.number.data, variant=form.variant.data, task=form.task.data))
        else:
            engine.execute("""
                        UPDATE laboratory
                        SET task='{task}'
                        WHERE number='{number}' AND variant='{variant}'
                        """.format(number=form.number.data, variant=form.variant.data, task=form.task.data))
    laboratory_list = engine.execute("SELECT * FROM laboratory")
    return render_template('laboratory.html', laboratory=list(laboratory_list), form=form)


@app.route('/materials')
def materials():
    headlines = ['material_theme', 'subject', 'number', 'variant', 'label', 'content']
    materials_list = engine.execute("SELECT * FROM material")
    return render_template('table.html', entity='Material', data=list(materials_list), headlines=headlines)


@app.route('/clusters')
def clusters():
    headlines = ['label', 'name']
    cluster_list = engine.execute("SELECT * FROM cluster")
    return render_template('table.html', entity='Cluster', data=list(cluster_list), headlines=headlines)


@app.route('/works')
def works():
    headlines = ['attempt', 'record_book', 'number', 'variant', 'mark', 'test_result', 'content', 'operator_sequence',
                 'plagiary']
    work_list = engine.execute("SELECT * FROM work")
    return render_template('table.html', entity='Work', data=list(work_list), headlines=headlines)


@app.route('/tests')
def tests():
    headlines = ['test_name', 'number', 'variant', 'input_data', 'expected_result', 'on_fail_message']
    test_list = engine.execute("SELECT * FROM test")
    return render_template('table.html', entity='Test', data=list(test_list), headlines=headlines)


if __name__ == '__main__':
    app.run()
