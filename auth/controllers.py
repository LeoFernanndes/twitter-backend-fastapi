from auth import repository, dto, oauth2

class AuthUserController:
    def __init__(self, auth_user_repository: repository.AuthUserRepository):
        self.__auth_user_repository = auth_user_repository
        
    async def create_auth_user(self, auth_user: dto.AuthUserCreate):
        return self.__auth_user_repository.create_auth_user(auth_user)        
    
    async def get_all_auth_users(self):
        return self.__auth_user_repository.get_all_auth_users()
    
    async def authenticate_user(self, username: str, password: str):
        user = self.__auth_user_repository.retrieve_auth_users(username)
        if not user:
            return False
        if not oauth2.verify_password(password, user.password):
            return False
        return user  
   