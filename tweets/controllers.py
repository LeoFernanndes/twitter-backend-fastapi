import logging
from typing import List
from tweets.dto import TweetDto
from profiles.dto import Profile
from tweets.repository import TweetRepository
from services.utils import get_arroba_attributes, validate_arroba
from fastapi import HTTPException
from services.files_handler import save_local_user_tweets_csv


logging.basicConfig(level=logging.INFO, format='%(asctime)s %(name)s %(levelname)s:%(message)s')
logger = logging.getLogger(__name__)

class TweetController:
    def __init__(self, repository: TweetRepository):
        self._repository = repository

    async def list_tweets(self) -> List[TweetDto]:
        tweets = self._repository.get_all_tweets()
        tweets_response = [TweetDto(**tweet.__dict__) for tweet in tweets]
        return tweets_response

    async def list_tweets_by_user(self, user_screen_name:str) -> List[TweetDto]:
        tweets = self._repository.get_tweets_from_user(user_screen_name)
        tweets_response = [TweetDto(**tweet.__dict__) for tweet in tweets]
        return tweets_response
    
    async def download_list_tweets_by_user(self, user_screen_name:str) -> List[TweetDto]:
        tweets = self._repository.get_tweets_from_user(user_screen_name)
        tweets_response = [TweetDto(**tweet.__dict__) for tweet in tweets]
        logger.info(f'GET TweetControler.download_list_tweets_by_user user_screen_name {user_screen_name} got {len(tweets_response)} rows')
        save_local_user_tweets_csv(user_screen_name, tweets_response)
        return tweets_response[:100]
