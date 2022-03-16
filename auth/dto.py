from pydantic import BaseModel
from typing import List, Optional

class AuthUserCreate(BaseModel):
    username: str
    email: str
    password: str

    class Config:
        orm_mode = True


class AuthUserResponse(BaseModel):
    id: int
    username: str
    email: str
    password: str

    class Config:
        orm_mode = True
        

class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: Optional[str] = None
    scopes: List[str] = []


class User(BaseModel):
    username: str
    email: Optional[str] = None
    full_name: Optional[str] = None
    disabled: Optional[bool] = None


class UserInDB(User):
    hashed_password: str