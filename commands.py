import click
from flask.cli import with_appcontext
from db import db
from models import Student, Group, Task, Material, Resource, Label, Test, Implementation, Subject, Laboratory
from populate import populate


@click.command(name='create_tables')
@with_appcontext
def create_tables():
    db.create_all()


@click.command(name='populate_tables')
@with_appcontext
def populate_tables():
    populate()


