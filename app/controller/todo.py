from fastapi import APIRouter
# from app.model.user import User
from app.service.hello_world_service import HelloWorldService
from pydantic import BaseModel

class SuccessMsg(BaseModel):
    message: str


router = APIRouter()
service = HelloWorldService()


@router.get("/", response_model=SuccessMsg)
async def root():
    return service.execute()

# @router.get("/todos", response_model=User)
# async def get_all_todos():
#     return todo_service.get_all()