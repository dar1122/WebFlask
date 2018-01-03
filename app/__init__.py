
from flask import Flask
from flask.ext.bootstrap import Bootstrap
from flask.ext.moment import Moment
from .main import forms




bootstrap = Bootstrap()
moment = Moment()


def create_app():
    app = Flask(__name__)
    bootstrap.init_app(app)
    moment.init_app(app)
    app.config['SECRET_KEY'] = 'go home'

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app

