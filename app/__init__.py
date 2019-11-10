from config import Config
from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()
login = LoginManager()
login.login_view = 'auth.login'
bootstrap = Bootstrap()


def create_app(config_class=Config):
    app = Flask(__name__, static_folder='../static')
    app.config.from_object(config_class)

    db.init_app(app)
    migrate.init_app(app, db)
    login.init_app(app)
    bootstrap.init_app(app)

    from app.errors import bp as errors_bp

    app.register_blueprint(errors_bp)

    from app.auth import bp as auth_bp

    app.register_blueprint(auth_bp)

    from app.frontend import bp as frontend_bp

    app.register_blueprint(frontend_bp)

    from app.oauth import google_bp

    app.register_blueprint(google_bp, url_prefix='/login')

    from .frontend.nav import nav, init_custom_nav_renderer

    nav.init_app(app)
    init_custom_nav_renderer(app)

    return app


from app import models
