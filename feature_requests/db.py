from flask import current_app
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy(current_app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username


class FeatureRequest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, nullable=False)
    client_id = db.Column(db.Integer, db.ForeignKey('client.id'), nullable=False)
    priority_id = db.Column(db.Integer, db.ForeignKey('priority.id'))
    target_date = db.column(db.DateTime, nullable=False)

    client = db.relationship('Client', backref=db.backref('clients', lazy=True))
    priority = db.relationship('Priority', backref=db.backref('priority', lazy=True))

    def __repr__(self):
        return '<Feature Request %r>' % self.title


class Client(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)

    def __repr__(self):
        return '<Client %r>' % self.name


class Priority(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    level = db.Column(db.String(30), unique=True, nullable=False)

    def __repr__(self):
        return '<Priority %r>' % self.level
