from config import Config
from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate


app = Flask(__name__, static_folder='../static')
app.config.from_object(Config)
bootstrap = Bootstrap(app)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)
login.login_view = 'google.login'


from app.errors import bp as errors_bp
app.register_blueprint(errors_bp)

from app.auth import bp as auth_bp
app.register_blueprint(auth_bp)

from app.oauth import google_bp
app.register_blueprint(google_bp, url_prefix='/login')

from app import routes, models, oauth
