from flask import current_app, g
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy(current_app)


class User(db.Model):
    pass


class FeatureRequest(db.Model):
    pass
