from app.repository.user.user import UserRepo

class UserRepoImpl(UserRepo):
    def __init__(self, uri: str):
        self.uri = uri
    
    def get_user(self, user_id: int) -> dict:
        pass

    def get_users(self) -> list:
        pass

    def create_user(self, user: dict) -> dict:
        pass

    def update_user(self, user_id: int, user: dict) -> dict:
        pass

    def delete_user(self, user_id: int) -> dict:
        pass
    
def newUserRepo(uri: str) -> UserRepo:
    return UserRepoImpl(uri)