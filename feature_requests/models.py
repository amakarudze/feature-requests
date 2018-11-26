from datetime import datetime

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return '<User %r>' % self.username


class FeatureRequest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, nullable=False)
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'), nullable=False)
    priority_id = db.Column(db.Integer, db.ForeignKey('priority.id'))
    target_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    product_area_id = db.Column(db.Integer, db.ForeignKey('product_area.id'))
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    closed = db.Column(db.Boolean, default=False)
    customer = db.relationship('Customer', backref=db.backref('customer', lazy=True))
    priority = db.relationship('Priority', backref=db.backref('priority', lazy=True))
    product_area = db.relationship('ProductArea', backref=db.backref('product_area', lazy=True))

    def __repr__(self):
        return '<Feature Request %r>' % self.title


class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)

    def __repr__(self):
        return '<Client %r>' % self.name


class Priority(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    priority_level = db.Column(db.String(30), unique=True, nullable=False)

    def __repr__(self):
        return '<Priority %r>' % self.level


class ProductArea(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), unique=True, nullable=False)

    def __repr__(self):
        return '<Product Area %r>' % self.name
