import os
from flask import Flask
from .extensions import db, login_manager, bcrypt

__all__ = ['create_app']

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
    
    db.init_app(app)
    login_manager.init_app(app)
    bcrypt.init_app(app)

    # register blueprints here if available
    # from .users import routes as user_routes
    # app.register_blueprint(user_routes.bp)

    return app
