from enum import unique
from sqlalchemy import Column, String, Integer
from services.database_connection import Base


class AuthUser(Base):
    __tablename__ = 'authuser'
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(255), unique=True)
    email = Column(String(255), unique=True)
    password = Column(String(255))