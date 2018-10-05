import click
from flask.cli import FlaskGroup
from app import app


@click.group(cls=FlaskGroup, create_app=lambda: app)
def cli():
    """Management script for the flask application."""


@cli.command()
@click.argument('name')
def create_user(name):
    """Creates a user"""
    print("user created: ", name)


if __name__ == '__main__':
    cli()

