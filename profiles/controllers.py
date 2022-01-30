from typing import List
from profiles.dto import Profile
from profiles.repository import UserRepository
from services.utils import get_arroba_attributes, validate_arroba
from fastapi import HTTPException

class UserController:
    def __init__(self, user_repository: UserRepository):
        self._user_repository = user_repository

    async def create_user(self, profile: Profile):
        if not validate_arroba(profile.arroba):
            raise HTTPException(status_code=400, detail="Profile not found.")
        twitter_profile_data = get_arroba_attributes(profile.arroba)
        twitter_profile_data_id_str = twitter_profile_data._json.get('id_str')
        if self._user_repository.get_by_twitter_id(twitter_profile_data_id_str):
            raise HTTPException(status_code=400, detail="Profile already created.")
        return self._user_repository.create_profile(profile)

    async def list_users(self) -> List[Profile]:
        users = self._user_repository.get_all_profiles()
        return users

    async def get_user_by_twitter_id(self, twitter_id):
        user = self._user_repository.get_by_twitter_id(twitter_id)
        return user

    async def get_user_by_arroba(self, arroba):
        user = self._user_repository.get_by_arroba(arroba)
        return user
    
    async def get_all_arrobas(self):
        users = self._user_repository.get_all_arrobas()
        return users