from sqlite3 import sqlite_version
from typing import List
from profiles import models, dto
from sqlalchemy.orm import Session
from services.utils import get_arroba_attributes

class UserRepository:
    def __init__(self, sql_alchemy_session: Session):
        self._sql_alchemy_session = sql_alchemy_session
         

    def create_profile(self, profile: dto.Profile):
        arroba = get_arroba_attributes(validated_user=profile.arroba)
        db_profile = models.Profile(
            id_str = arroba._json.get('id_str'),
            name = arroba._json.get('name'),
            screen_name = arroba._json.get('screen_name'),
            location = arroba._json.get('location'),
            profile_location = arroba._json.get('profile_location'),
            description = arroba._json.get('profile_location'),
            url = arroba._json.get('url'),
            protected = arroba._json.get('protected'),
            followers_count = arroba._json.get('followers_count'),
            listed_count = arroba._json.get('listed_count'),
            created_at = arroba._json.get('created_at'),
            favourites_count = arroba._json.get('favourites_count'),
            time_zone = arroba._json.get('time_zone'),
            geo_enabled = arroba._json.get('geo_enabled'),
            verified = arroba._json.get('verified'),
            statuses_count = arroba._json.get('statuses_count'),
            lang = arroba._json.get('lang'),
        )
      
        self._sql_alchemy_session.add(db_profile)
        self._sql_alchemy_session.commit()
        self._sql_alchemy_session.refresh(db_profile)
        return db_profile

    def get_all_profiles(self):
        return self._sql_alchemy_session.query(models.Profile).all()

    def get_by_twitter_id(self, twitter_id):
        return self._sql_alchemy_session.query(models.Profile).filter(models.Profile.id_str == twitter_id).first()

    def get_by_arroba(self, arroba):
        return self._sql_alchemy_session.query(models.Profile).filter(models.Profile.screen_name == arroba).first()
    
    def get_all_arrobas(self):
        complete_users = self._sql_alchemy_session.query(models.Profile).all()
        users = [user.screen_name for user in complete_users]
        return users
