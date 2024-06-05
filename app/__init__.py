from flask import Flask
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session

Base = declarative_base()
engine = create_engine('sqlite:///users.db', echo=True)
Session = sessionmaker(bind=engine)
db_session = scoped_session(Session)

def create_app():
    app = Flask(__name__)

    with app.app_context():
        from . import models
        Base.metadata.create_all(engine)

        from . import routes

    @app.teardown_appcontext
    def shutdown_session_on_teardown(exception=None):
        db_session.remove()

    return app
