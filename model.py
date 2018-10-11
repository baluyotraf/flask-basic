from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import sqlalchemy as sqla
from sqlalchemy import orm


db = SQLAlchemy()
ma = Marshmallow()


class User(db.Model):
    __tablename__ = 'users'

    id = sqla.Column(sqla.Integer, primary_key=True, autoincrement=True)
    username = sqla.Column(sqla.String(60), nullable=False, unique=True)
    password = sqla.Column(sqla.String(160), nullable=False)
    first_name = sqla.Column(sqla.String(60))
    last_name = sqla.Column(sqla.String(60))
    tickets = orm.relationship('Ticket', backref='user')


class Ticket(db.Model):
    __tablename__ = 'tickets'

    id = sqla.Column(sqla.Integer, primary_key=True, autoincrement=True)
    description = sqla.Column(sqla.String(60), nullable=False)
    user_id = sqla.Column(sqla.Integer, sqla.ForeignKey('users.id'))


class BasicUserSchema(ma.ModelSchema):
    class Meta:
        fields = ('id', 'username')


class DetailedUserSchema(ma.ModelSchema):
    class Meta:
        fields = ('id', 'username', 'first_name', 'last_name')


class TicketSchema(ma.ModelSchema):
    class Meta:
        fields = ('id', 'description')

