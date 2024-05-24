from app.models import User
from app import db  # Assuming db is the SQLAlchemy instance

class DB:
    def find_user_by(self, **kwargs) -> User:
        return User.query.filter_by(**kwargs).one()

    def add_user(self, email: str, hashed_password: str) -> User:
        user = User(email=email, hashed_password=hashed_password)
        db.session.add(user)
        db.session.commit()
        return user

    def update_user(self, user_id: int, **kwargs) -> None:
        user = User.query.get(user_id)
        for key, value in kwargs.items():
            setattr(user, key, value)
        db.session.commit()

    def get_user_by_id(self, user_id: int) -> User:
        return User.query.get(user_id)

