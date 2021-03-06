import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from . import auth
from . import views


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        SQLALCHEMY_DATABASE_URI='mysql+pymysql://admin:pass1234@localhost/features',
        SQLALCHEMY_TRACK_MODIFICATIONS=False,
    )
    db = SQLAlchemy()
    db.init_app(app)

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    app.register_blueprint(auth.bp)
    app.register_blueprint(views.bp)
    app.add_url_rule('/', endpoint='index')

    return app
