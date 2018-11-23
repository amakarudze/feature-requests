import os

from flask import Flask

from . import auth
from . import features


def create_app(test_config=None):
    # create and configure our app
    app = Flask(__name__, instance_relative_config=True)
    db_path = os.path.join(app.instance_path, 'feature_request.db'),
    db_uri = 'sqlite:///{}'.format(db_path)
    app.config.from_mapping(
        SECRET_KEY='dev',
        SQLALCHEMY_DATABASE_URI=db_uri,
    )

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
    app.register_blueprint(features.bp)
    app.add_url_rule('/', endpoint='index')

    return app
