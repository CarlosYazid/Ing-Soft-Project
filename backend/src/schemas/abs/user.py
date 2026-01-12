from typing import Optional
from datetime import datetime

from pydantic import EmailStr, Field

from schemas.abs.base import BaseCreate, BaseUpdate, BaseRead

class UserCreate(BaseCreate):
    
    documentid: Optional[int] = Field(None, description="User's document ID", gt = 0)
    email: EmailStr = Field(..., description="User's email address")
    phone: Optional[str] = Field(None, description="User's phone number")
    first_name: str = Field(..., description="User's firstname")
    last_name: str = Field(..., description="User's lastname")
class UserUpdate(BaseUpdate):

    id: Optional[int] = Field(None, description="User's ID", gt = 0)
    email: Optional[EmailStr] = Field(None, description="User's email address")
    documentid: Optional[int] = Field(None, description="User's document ID", gt = 0)
    phone: Optional[str] = Field(None, description="User's phone number")
    first_name: str = Field(..., description="User's firstname")
    last_name: str = Field(..., description="User's lastname")
    status: Optional[bool] = Field(None, description="Is the user active?")
    updated_at: datetime = Field(default_factory = datetime.now, description="Timestamp when the client was last updated")

class UserRead(BaseRead):
    
    id: int = Field(..., description="User's ID")
    documentid: int = Field(..., description="User's document ID")
    email: EmailStr = Field(..., description="User's email address")
    phone: Optional[str] = Field(None, description="User's phone number")
    first_name: str = Field(..., description="User's firstname")
    last_name: str = Field(..., description="User's lastname")
    status: bool = Field(..., description="Is the user active?")