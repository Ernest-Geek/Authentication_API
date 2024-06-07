from flask import Flask
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session

# Base class for declarative models
Base = declarative_base()

# Create a new SQLite database (or connect to an existing one)
engine = create_engine('sqlite:///users.db', echo=True)

# Configure the session factory with the engine
Session = sessionmaker(bind=engine)

# Create a scoped session for thread-safe database interactions
db_session = scoped_session(Session)

def create_app():
    """
    Creates and configures the Flask application.
    
    Sets up the database, initializes models, and registers routes.

    Returns:
        app (Flask): The configured Flask application instance.
    """
    app = Flask(__name__)

    with app.app_context():
        # Import models to create database tables
        from . import models
        Base.metadata.create_all(engine)

        # Import routes to register them with the app
        from . import routes

    @app.teardown_appcontext
    def shutdown_session_on_teardown(exception=None):
        """
        Removes the database session at the end of the request or when the application context ends.

        Args:
            exception (Exception, optional): The exception that triggered the teardown, if any.
        """
        db_session.remove()

    return app
