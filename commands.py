import click
from flask.cli import with_appcontext
from models import init_db
from populate import populate


@click.command(name='create_tables')
@with_appcontext
def create_tables():
    init_db()


@app.cli.command('populate_tables')
@with_appcontext
def populate_tables():
    populate()


