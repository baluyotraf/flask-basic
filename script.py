import click
from flask.cli import FlaskGroup
from app import app, db


@click.group(cls=FlaskGroup, create_app=lambda: app)
def cli():
    """Management script for the flask application."""


@cli.command()
@click.argument('name')
def create_user(name):
    """Creates a user"""
    print("user created: ", name)


@cli.command()
def init_db():
    db.create_all()


if __name__ == '__main__':
    cli()

