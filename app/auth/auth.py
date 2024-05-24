from app.models import User
from app.db import DB
from sqlalchemy.orm.exc import NoResultFound
from werkzeug.security import generate_password_hash, check_password_hash
from uuid import uuid4
from typing import Union

db = DB()  # Initialize the database instance

def load_user(user_id):
    # Load a user from the database based on user_id
    return db.get_user_by_id(user_id)

class Auth:
    def __init__(self):
        self._db = db

    def register_user(self, email: str, password: str) -> User:
        try:
            self._db.find_user_by(email=email)
            raise ValueError(f"User {email} already exists")
        except NoResultFound:
            hashed_password = generate_password_hash(password)
            return self._db.add_user(email, hashed_password)

    def valid_login(self, email: str, password: str) -> bool:
        try:
            user = self._db.find_user_by(email=email)
            return check_password_hash(user.hashed_password, password)
        except NoResultFound:
            return False

    def create_session(self, email: str) -> Union[str, None]:
        try:
            user = self._db.find_user_by(email=email)
            session_id = str(uuid4())
            self._db.update_user(user.id, session_id=session_id)
            return session_id
        except NoResultFound:
            return None

    def get_user_from_session_id(self, session_id: str) -> Union[User, None]:
        try:
            return self._db.find_user_by(session_id=session_id)
        except NoResultFound:
            return None

    def destroy_session(self, user_id: int) -> None:
        self._db.update_user(user_id, session_id=None)

