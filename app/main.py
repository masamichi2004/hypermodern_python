from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.controller import todo
import app.config.env as env
from app.db_model.dataclass.db_config import DBConfig, MySQLClient
from app.repository.todo.todo_sql import new_todo_repository
from app.repository.user.user_sql import new_user_repository
from app.repository.user.user import UserRepo
from app.repository.todo.todo import TodoRepo
from app.service.todo import TodoService
from app.service.user import UserService


app = FastAPI()


def new_mysql_client() -> MySQLClient:
    db_config = DBConfig(
        user=env.DB_USER,
        password=env.DB_PASSWORD,
        host=env.DB_HOST,
        port=env.DB_PORT,
        db=env.DB_NAME,
    )
    client = MySQLClient(db_config)
    return client


todo_repo: TodoRepo = new_todo_repository(new_mysql_client())
user_repo: UserRepo = new_user_repository(new_mysql_client())
todo_service = TodoService(todo_repo)
user_service = UserService(user_repo)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(todo.router, prefix="/v1", dependencies=todo_service)
