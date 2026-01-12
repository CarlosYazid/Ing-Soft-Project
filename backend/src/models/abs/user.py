from typing import Optional

from sqlmodel import Field
from pydantic import EmailStr

from models.abs.base import BaseModel

class UserModel(BaseModel):
    
    documentid: Optional[int] = Field(None, description="User's document ID")
    email: EmailStr = Field(..., description="User's email address")
    phone: Optional[str] = Field(None, description="User's phone number")
    first_name: Optional[str] = Field(None, description="User's firstname")
    last_name: Optional[str] = Field(None, description="User's lastname")
    status: bool = Field(default=True, description="Is the user active?")
    
    class Config:
        from_attributes = True
        arbitrary_types_allowed = True