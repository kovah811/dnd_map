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

from app import routes, models, oauth
app.register_blueprint(oauth.blueprint, url_prefix='/login')
