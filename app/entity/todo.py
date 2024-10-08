from pydantic import BaseModel


class Todo(BaseModel):
    title: str
    description: str
    done: bool
    user_id: str
