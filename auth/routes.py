from fastapi import APIRouter, HTTPException, Depends
from services.database_connection import SessionLocal
from auth import dto, repository, controllers
from fastapi.security import (
    OAuth2PasswordBearer,
    OAuth2PasswordRequestForm,
    SecurityScopes,
)
from auth import oauth2
from datetime import datetime, timedelta
from decouple import config


router = APIRouter(prefix="/auth")

# Dependency
def get_db():
    db = SessionLocal()
    try:
        return db
    finally:
        db.close()

@router.get('/')    
async def list_auth_users():
    session = get_db()
    auth_user_repository = repository.AuthUserRepository(session)
    response = await controllers.AuthUserController(auth_user_repository).get_all_auth_users()
    return response

@router.post('/')
async def post_auth_user(auth_user: dto.AuthUserCreate):
    session = get_db()
    auth_user_repository = repository.AuthUserRepository(session)
    response = await controllers.AuthUserController(auth_user_repository).create_auth_user(auth_user)
    return response

@router.post("/token", response_model=dto.Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    session = get_db()
    auth_user_repository = repository.AuthUserRepository(session)
    user = await controllers.AuthUserController(auth_user_repository).authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    access_token_expires = timedelta(minutes=int(config('FASTAPI_ACCESS_TOKEN_EXPIRE_MINUTES')))
    access_token = oauth2.create_access_token(
        data={"sub": user.username, "scopes": form_data.scopes},
        expires_delta=access_token_expires,
    )
    return {"access_token": access_token, "token_type": "bearer"}

@router.get("/me", response_model=dto.AuthUserResponse)
async def read_users_me(current_user: dto.AuthUserResponse = Depends(oauth2.get_current_user)):
    return current_user