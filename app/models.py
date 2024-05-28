from app.db import db  # Ensure this imports db correctly
from flask_login import UserMixin

class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(128), unique=True, nullable=False)
    hashed_password = db.Column(db.String(128), nullable=False)
    session_id = db.Column(db.String(128), nullable=True)
    reset_token = db.Column(db.String(128), nullable=True)

    def __repr__(self):
        return f'<User {self.email}>'

