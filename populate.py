from models import Student, Group, Task, Material, Resource, Label, Test, Implementation, Subject, Laboratory
from db import db


def populate():
    km62 = Group('KM-62', 2016)
    km61 = Group('KM-61', 2016)
    km63 = Group('KM-63', 2016)

    db.session.add(km62)
    db.session.add(km61)
    db.session.add(km63)

    richmound = Student('KM6202', 2016, 'KM-62', 'Richmound Tizard', 'rtizard1@arstechnica.com', '+64 958 599 9496')
    torrie = Student('KM6203', 2016, 'KM-62', 'Torrie Chinge', 'tchinge2@gov.uk', '+7 362 480 7692')
    becca = Student('KM6204', 2016, 'KM-62', 'Becca Parell', 'bparell3@yandex.ru', '+63 910 768 4564')

    db.session.add(richmound)
    db.session.add(torrie)
    db.session.add(becca)

    task1 = Task(2, 'Integral', 'Solve integral')
    task2 = Task(3, 'Integral', 'Solve Riman integral')
    task3 = Task(4, 'Integral', 'Solve Lebesgue integral')

    db.session.add(task1)
    db.session.add(task2)
    db.session.add(task3)

    integ = Material('Integral material', 'KPI FAM 1999', 1, 'Material about integral')
    rinteg = Material('Riman integral material', 'KPI FAM 1999', 1, 'Material about Riman integral')
    linteg = Material('Lebesgue integral material', 'KPI FAM 1999', 1, 'Material about Lebesgue integral')

    db.session.add(integ)
    db.session.add(rinteg)
    db.session.add(linteg)

    r1 = Resource('Wikipedia article about integrals', 'Wikipedia', 1, 'In mathematics, an integral assigns numbers to functions in a way that can describe displacement, area, volume, and other concepts that arise by combining infinitesimal data. Integration is one of the two main operations of calculus, with its inverse operation, differentiation, being the other. Given a function f of a real variable x and an interval [a, b] of the real line, the definite integral', 0)
    r2 = Resource('Definite Integrals MIT lection', 'MIT', 1, 'The following content is provided under a Creative Commons license. Your support will help MIT OpenCourseWare continue to offer high quality educational resources for free. To make a donation or to view additional materials from hundreds of MIT courses, visit MIT OpenCourseWare at ocw.mit.edu.', 0)
    r3 = Resource('Oxford integral lection', 'Oxford', 1, 'In these lectures we define a simple integral and study its properties; prove the Mean Value Theorem for Integrals and the Fundamental Theorem of Calculus. This gives us the tools to justify term-by-term differentiation of power series and deduce the elementary properties of the trigonometric functions.', 0)

    db.session.add(r1)
    db.session.add(r2)
    db.session.add(r3)

    l1 = Label(1, 'Integrals')
    l1.materials.append(integ)
    l1.materials.append(rinteg)
    l1.materials.append(linteg)
    l2 = Label(2, 'Integrals')
    l3 = Label(3, 'Integrals')

    db.session.add(l1)
    db.session.add(l2)
    db.session.add(l3)

    test1 = Test('Put string instead of integer as first param', 'input data', 'expected result', 'Input validation failed')
    test2 = Test('Put string instead of integer as second param', 'input data', 'expected result', 'Input validation failed')
    test3 = Test('Test correct answer', 'input data', 'expected result', 'Answer is incorrect')

    db.session.add(test1)
    db.session.add(test2)
    db.session.add(test3)

    imp1 = Implementation(1, 'KM6202', 2016, 'Integral', 8, 'Work content', 'Success', 'operator sequence', 13)
    imp2 = Implementation(1, 'KM6203', 2016, 'Integral', 2, 'Work content', 'Input validation failed', 'operator sequence', 22)
    imp3 = Implementation(2, 'KM6203', 2016, 'Integral', 4, 'Work content', 'Input validation failed', 'operator sequence', 26)

    db.session.add(imp1)
    db.session.add(imp2)
    db.session.add(imp3)

    lab1 = Laboratory('Integral', 'Calculus', 'Learn how to solve integrals', 1)
    lab1.tasks.append(task1)
    lab1.tasks.append(task2)
    lab1.tasks.append(task3)
    lab1.implementations.append(imp1)
    lab1.implementations.append(imp2)
    lab1.implementations.append(imp3)
    lab1.tests.append(test1)
    lab1.tests.append(test2)
    lab1.tests.append(test3)
    lab2 = Laboratory('Loop', 'Python', 'Learn how loop works', 3)
    lab3 = Laboratory('Postgres', 'DB', 'Learn how to postgres', 2)

    db.session.add(lab1)
    db.session.add(lab2)
    db.session.add(lab3)

    subj1 = Subject('Calculus')
    subj1.materials.append(integ)
    subj1.materials.append(rinteg)
    subj1.materials.append(linteg)
    subj1.laboratory.append(lab1)
    subj1.laboratory.append(lab2)
    subj1.laboratory.append(lab3)
    subj2 = Subject('Python')
    subj3 = Subject('DB')

    db.session.add(subj1)
    db.session.add(subj2)
    db.session.add(subj3)

    db.session.commit()
