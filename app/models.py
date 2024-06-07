from sqlalchemy import Column, Integer, String
from . import Base

class User(Base):
    """
    User model representing a user in the database.
    
    Attributes:
        id (int): The primary key for the user.
        name (str): The first name of the user.
        surname (str): The surname of the user.
        email (str): The email address of the user, must be unique.
        password (str): The password for the user's account.
    """
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    surname = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
