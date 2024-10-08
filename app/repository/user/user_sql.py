from app.repository.user.user import UserRepo
from app.db_model.dataclass.db_config import MySQLClient
from sqlalchemy import create_engine


class UserRepoImpl(UserRepo):
    def __init__(self, client: MySQLClient):
        self.engine = create_engine(client.uri)

    def bulk_get(self):
        pass

    def get_by_id(self, id):
        pass

    def create(self, user):
        pass

    def bulk_create(self, users):
        pass

    def update(self, user):
        pass

    def delete(self, id):
        pass


def new_user_repository(client: MySQLClient) -> UserRepo:
    return UserRepoImpl(client)
