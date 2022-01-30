from sqlite3 import sqlite_version
from typing import List
from profiles import models, dto
from sqlalchemy.orm import Session
from services.utils import get_arroba_attributes

class TweetRepository:
    def __init__(self, sql_alchemy_session: Session):
        self._sql_alchemy_session = sql_alchemy_session
         

    
    def get_all_tweets(self):
        return self._sql_alchemy_session.query(models.Tweet).all()[:100]
    
    def get_tweets_from_user(self, user_screen_name: str):
        return self._sql_alchemy_session.query(models.Tweet).filter(models.Tweet.user_screen_name == user_screen_name)


    # def get_by_twitter_id(self, twitter_id):
    #     return self._sql_alchemy_session.query(models.Profile).filter(models.Profile.id_str == twitter_id).first()

    # def get_by_arroba(self, arroba):
    #     return self._sql_alchemy_session.query(models.Profile).filter(models.Profile.screen_name == arroba).first()
    
    # def get_all_arrobas(self):
    #     complete_users = self._sql_alchemy_session.query(models.Profile).all()
    #     users = [user.screen_name for user in complete_users]
    #     return users
