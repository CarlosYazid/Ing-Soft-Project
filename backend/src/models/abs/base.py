from typing import Optional
from datetime import datetime

from sqlmodel import SQLModel, Field

class BaseModel(SQLModel):
    
    id: Optional[int] = Field(default=None, primary_key=True)
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)
    
    class Config:
        from_attributes = True
        arbitrary_types_allowed = True
        
    def __repr__(self):
        return f"<{self.__class__.__name__} id={self.id}>"
    