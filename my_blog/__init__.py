from flask_bcrypt import Bcrypt
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from my_blog.config import Config
from flask_bootstrap import Bootstrap


db = SQLAlchemy()
login_manager = LoginManager()
bcrypt = Bcrypt()


def create_app():
    app = Flask(__name__,
            static_url_path='',
            static_folder='static')
    app.config.from_object(Config)

    db.init_app(app)
    login_manager.init_app(app)
    bcrypt.init_app(app)

    from my_blog.main.routes import main
    from my_blog.users.routes import users
    from my_blog.blog.routes import blog
    from my_blog.portfolio.routes import portfolio
    app.register_blueprint(main)
    app.register_blueprint(users)
    app.register_blueprint(blog)
    app.register_blueprint(portfolio)
    bootstrap = Bootstrap(app)

    return app
