from sqlalchemy import Column, Integer,String,DateTime,func
from app.db.base import Base

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    email=Column(String, unique=True, nullable=False)
    name=Column(String, nullable=True)
    hashed_password=Column(String, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True), server_default=func.now(),onupdate=func.now(), nullable=False)