from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt

# extension instances for use by application

db = SQLAlchemy()
login_manager = LoginManager()
bcrypt = Bcrypt()
