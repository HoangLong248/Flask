from flask import render_template, Flask

from flask_bootstrap import Bootstrap
from flask_moment import Moment

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import config

bootstrap = Bootstrap()
moment = Moment()
db = SQLAlchemy()
migrate  = Migrate()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    bootstrap.init_app(app)
    moment.init_app(app)
    db.init_app(app)

    from .main import main as main_blueprint

    app.register_blueprint(main_blueprint)

    # attach routes and custom error pages here
    
    return app 