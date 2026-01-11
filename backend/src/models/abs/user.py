from typing import Optional

from sqlmodel import Field
from pydantic import EmailStr

from models.abs.base import BaseModel

class UserModel(BaseModel):
    
    documentid: Optional[int] = Field(None, description="User's document ID")
    email: EmailStr = Field(..., description="User's email address")
    phone: Optional[str] = Field(None, description="User's phone number")
    name: str = Field(..., description="User's name")
    status: bool = Field(default=True, description="Is the user active?")
    
    class Config:
        orm_mode = True
        arbitrary_types_allowed = True