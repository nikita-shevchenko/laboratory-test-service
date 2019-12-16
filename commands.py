import click
from flask.cli import with_appcontext
from models import init_db, app
from populate import populate


@app.cli.command('create_tables')
@with_appcontext
def create_tables():
    init_db()


@app.cli.command('populate_tables')
@with_appcontext
def populate_tables():
    populate()
