from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from my_blog.config import Config
from flask_bootstrap import Bootstrap


db = SQLAlchemy()
login_manager = LoginManager()


def create_app():
    app = Flask(__name__,
            static_url_path='',
            static_folder='static')
    app.config.from_object(Config)

    db.init_app(app)
    login_manager.init_app(app)

    from my_blog.main.routes import main
    app.register_blueprint(main)
    bootstrap = Bootstrap(app)

    return app
