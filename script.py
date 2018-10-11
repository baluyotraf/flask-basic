import click
from flask.cli import FlaskGroup
from app import app, db


@click.group(cls=FlaskGroup, create_app=lambda: app)
def cli():
    """Management script for the flask application."""


@cli.command()
def init_db():
    """Creates database tables"""
    db.create_all()


@cli.command()
def delete_db():
    """Deletes all database tables"""
    db.drop_all()


if __name__ == '__main__':
    cli()

