import logging
from fastapi import APIRouter, HTTPException
from profiles.controllers import UserController
from profiles.dto import Profile
from services.database_connection import SessionLocal
from profiles import repository
from services.utils import validate_arroba

router = APIRouter(prefix="/profiles")

# Dependency
def get_db():
    db = SessionLocal()
    try:
        return db
    finally:
        db.close()

@router.get('/')    
async def list_profiles():
    session = get_db()
    user_repository = repository.UserRepository(session)
    response = await UserController(user_repository).list_users()
    return response

@router.get('/twitter_ids/{twitter_id}')
async def list_profiles(twitter_id: str):
    session = get_db()
    user_repository = repository.UserRepository(session)
    response = await UserController(user_repository).get_user_by_twitter_id(twitter_id)
    return response

@router.get('/arrobas/{arroba}')
async def list_profiles(arroba: str):
    session = get_db()
    user_repository = repository.UserRepository(session)
    response = await UserController(user_repository).get_user_by_arroba(arroba)
    return response

@router.get('/arrobas/')
async def list_profiles():
    session = get_db()
    user_repository = repository.UserRepository(session)
    response = await UserController(user_repository).get_all_arrobas()
    return response

@router.post('/')
async def post_profile(profile: Profile):
    session = get_db()
    user_repository = repository.UserRepository(session)
    response = await UserController(user_repository).create_user(profile)
    return response
