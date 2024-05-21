from typing import Union
from werkzeug.security import generate_password_hash, check_password_hash
from app.db import DB
#from user import User
from app.models import User

class Auth:
    def __init__(self):
        self._db = DB()

    def load_user(self, user_id):
        #load a user from the database based on user_id
        return self._db.get_user_by_id(user_id)

    def register_user(self, email: str, password: str) -> User:
        try:
            self._db.find_user_by(email=email)
        except NoResultFound:
            return self._db.add_user(email, self._hash_password(password))
        raise ValueError("User {} already exists".format(email))

    def valid_login(self, email: str, password: str) -> bool:
        try:
            user = self._db.find_user_by(email=email)
            return check_password_hash(user.hashed_password, password)
        except NoResultFound:
            return False

    def create_session(self, email: str) -> str:
        user = self._db.find_user_by(email=email)
        if not user:
            return None
        session_id = str(uuid4())
        self._db.update_user(user.id, session_id=session_id)
        return session_id

    def get_user_from_session_id(self, session_id: str) -> Union[User, None]:
        try:
            return self._db.find_user_by(session_id=session_id)
        except NoResultFound:
            return None

    def destroy_session(self, user_id: int) -> None:
        self._db.update_user(user_id, session_id=None)

    def get_reset_password_token(self, email: str) -> str:
        user = self._db.find_user_by(email=email)
        if not user:
            raise ValueError()
        reset_token = str(uuid4())
        self._db.update_user(user.id, reset_token=reset_token)
        return reset_token

    def update_password(self, reset_token: str, password: str) -> None:
        user = self._db.find_user_by(reset_token=reset_token)
        if not user:
            raise ValueError()
        hashed_password = self._hash_password(password)
        self._db.update_user(
            user.id,
            hashed_password=hashed_password,
            reset_token=None
        )

    @staticmethod
    def _hash_password(password: str) -> str:
        return generate_password_hash(password)

