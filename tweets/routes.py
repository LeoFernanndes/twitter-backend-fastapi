import logging
from typing import List
from fastapi import APIRouter, HTTPException
from tweets.dto import TweetDto
from tweets.controllers import TweetController
from services.database_connection import SessionLocal
from tweets.repository import TweetRepository

import logging
from logging.config import dictConfig
from fastapi import FastAPI


logger = logging.getLogger(__name__)

router = APIRouter(prefix="/tweets")

# Dependency
def get_db():
    db = SessionLocal()
    try:
        return db
    finally:
        db.close()

@router.get('/')    
async def list_tweets() -> List[TweetDto]:
    session = get_db()
    repository = TweetRepository(session)
    response = await TweetController(repository).list_tweets()
    return response

@router.get('/{user_screen_name}', response_model=List[TweetDto])    
async def list_tweets_by_user(user_screen_name: str) -> List[TweetDto]:
    session = get_db()
    repository = TweetRepository(session)
    response = await TweetController(repository).list_tweets_by_user(user_screen_name)
    return response

@router.get('/{user_screen_name}/download')    
async def list_tweets_by_user(user_screen_name: str) -> List[TweetDto]:
    logger.info(f'GET list_tweets_by_user user_screen_name {user_screen_name}')
    session = get_db()
    repository = TweetRepository(session)
    await TweetController(repository).download_list_tweets_by_user(user_screen_name)
    return {"detail": "CSV file already saved"}
