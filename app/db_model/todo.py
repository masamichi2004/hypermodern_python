from sqlalchemy import Column, Integer, String, TIMESTAMP, Text, func
from app.config.db import Base


class Todo(Base):
    __tablename__ = "todo"

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(255), nullable=False)
    description = Column(Text, nullable=True)
    created_at = Column(TIMESTAMP, server_default=func.now())
    updated_at = Column(TIMESTAMP, server_default=func.now(), onupdate=func.now())
    is_completed = Column(Integer, nullable=False)
    user_id = Column(Integer, nullable=False)
