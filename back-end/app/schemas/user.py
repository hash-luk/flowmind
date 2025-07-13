from pydantic import BaseModel,EmailStr
from datetime import datetime
from typing import Optional

class UserBase(BaseModel):
    name: str
    email: EmailStr

class UserCreate(UserBase):
    password: str

class UserUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[EmailStr] = None
    
class UserOut(UserBase):
    id: int
    status: str
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode= True