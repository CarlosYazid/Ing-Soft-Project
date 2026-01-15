from datetime import datetime

from sqlalchemy.sql.expression import Select
from pydantic import ConfigDict

from dtos.abs import UserCreate, UserRead, UserUpdate, UserFilter
from models import Client

class ClientCreate(UserCreate):
    
    model_config: ConfigDict = ConfigDict(str_strip_whitespace=True,
                                          json_schema_extra={
                                                "example": {
                                                    "documentid": 1234567890,
                                                    "email": "doro@example.com",
                                                    "phone": "555-555-5555",
                                                    "first_name": "Dorotea",
                                                    "last_name": "Hernandez",
                                                }
                                            })
    
class ClientUpdate(UserUpdate):
    
    model_config: ConfigDict = ConfigDict(str_strip_whitespace=True,
                                          json_schema_extra={
                                                "example": {
                                                    "id": 1,
                                                    "email": "doro@example.com",
                                                    "phone": "555-555-5555",
                                                    "first_name": "Dorotea",
                                                    "last_name": "Hernandez",
                                                    "status": True,
                                                    "updated_at": datetime.now()
                                                }
                                            })

class ClientRead(UserRead):
    
    model_config: ConfigDict = ConfigDict(str_strip_whitespace=True,
                                            json_schema_extra={
                                                "example": {
                                                    "id": 1,
                                                    "documentid": 1234567890,
                                                    "email": "doro@example.com",
                                                    "phone": "555-555-5555",
                                                    "first_name": "Dorotea",
                                                    "last_name": "Hernandez",
                                                    "status": True,
                                                }
                                            })

class ClientFilter(UserFilter):
    
    def apply(self, query: Select) -> Select:
        
        if self.first_name:
            query = query.where(Client.first_name.ilike(f"%{self.first_name}%"))
        
        if self.last_name:
            query = query.where(Client.last_name.ilike(f"%{self.last_name}"))
        
        if not self.status is None:
            query = query.where(Client.status == self.status)
        
        return query