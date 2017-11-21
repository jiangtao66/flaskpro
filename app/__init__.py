from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .main import main as main_blueprint
from config import config
db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config.from_object(config)
    db.init_app(app)
    app.register_blueprint(main_blueprint)
    return app
