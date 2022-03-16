from auth import models, dto
from sqlalchemy.orm import Session
from passlib.context import CryptContext
from typing import List


class AuthUserRepository:
    def __init__(self, sql_alchemy_session: Session):
        self.__sql_alchemy_session = sql_alchemy_session         

    def create_auth_user(self, auth_user: dto.AuthUserCreate) -> models.AuthUser:
        auth_user_create = auth_user.dict()
        hashed_password = CryptContext(schemes=["bcrypt"], deprecated="auto").hash(auth_user_create['password'])
        auth_user_create['password'] = hashed_password        
        db_auth_user = models.AuthUser(**auth_user_create)      
        self.__sql_alchemy_session.add(db_auth_user)
        self.__sql_alchemy_session.commit()
        self.__sql_alchemy_session.refresh(db_auth_user)
        return db_auth_user
    
    def get_all_auth_users(self) -> List[models.AuthUser]:
        return self.__sql_alchemy_session.query(models.AuthUser).all()
    
    def retrieve_auth_users(self, username: str) -> models.AuthUser:
        return self.__sql_alchemy_session.query(models.AuthUser).filter(models.AuthUser.username == username).first()
    