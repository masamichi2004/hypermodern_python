from app.repository.todo.todo import TodoRepo
from app.db_model.dataclass.db_config import MySQLClient
from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker


class TodoRepoImpl(TodoRepo):
    def __init__(self, client: MySQLClient):
        self.engine = create_engine(client.uri)
        
    def bulk_get(self):
        pass


def new_todo_repository(uri) -> TodoRepo:
    return TodoRepoImpl(uri)
