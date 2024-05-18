from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from config import Config

#SQLAlchemy instance for the databse operation
db = SQLAlchemy()
migrate = Migrate()
login = LoginManager()
login.login_view = 'auth.login'

#creates and configures the fals application
def create_app(config_class=Config):
    app = Flask(__name__)
    """Loads the configuration setiings from
    configuration class
    """
    app.config.from_object(config_class)

    #binding instances
    db.init_app(app)
    migrate.init_app(app, db)
    login.init_app(app)


    #blueprint registration
    from app.main import bp as main_bp
    app.register_blueprint(main_bp)

    #import blueprint from the authentication module
    from app.auth import bp as auth_bp
    app.register_blueprint(auth_bp, url_prefix='/auth')


    return app


from app import models
