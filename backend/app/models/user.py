from pydantic import BaseModel, EmailStr, Field, ConfigDict
from typing import Optional
from datetime import datetime
from abc import ABC
from enum import Enum

class EmployeeRole(str, Enum):
    ADMIN = "Admin"
    EMPLOYEE = "Empleado"

class AbstractUser(ABC, BaseModel):
    
    email: EmailStr = Field(..., description="User's email address")
    name: str = Field(..., description="User's name")
    phone: Optional[str] = Field(None, description="User's phone number")
    
class UserBase(AbstractUser):
    """
    User model for the API response.
    """
    
    created_at: datetime = Field(..., description="Timestamp when the user was created")
    updated_at: Optional[datetime] = Field(None, description="Timestamp when the user was last updated")
    state : bool = Field(default=True, description="Is the user active?")
    documentid: int = Field(..., description="User's document ID")


class ClientCreate(UserBase):
    
    """
    Client model for the API response.
    """
         

    model_config: ConfigDict = ConfigDict(str_strip_whitespace=True,
                                          use_enum_values=True,
                                          json_schema_extra={
                                              "example": {
                                                  "email": "client@example.com",
                                                  "name": "Jane Doe",
                                                  "phone": "987-654-3210",
                                                  "created_at": "2023-01-01T00:00:00Z",
                                                  "updated_at": "2023-01-02T00:00:00Z",
                                                  "state": True,
                                                  "documentid": 987654321,
                                              }
                                          },
                                          json_encoders={
                                              datetime: lambda v: v.isoformat()
                                          })

class Client(ClientCreate):
    """
    Client model for the API response.
    """
    id: int = Field(..., description="User's unique identifier")

    model_config: ConfigDict = ConfigDict(str_strip_whitespace=True,
                                          use_enum_values=True,
                                          json_schema_extra={
                                              "example": {
                                                  "id": 1,
                                                  "email": "client@example.com",
                                                  "name": "Jane Doe",
                                                  "phone": "987-654-3210",
                                                  "created_at": "2023-01-01T00:00:00Z",
                                                  "updated_at": "2023-01-02T00:00:00Z",
                                                  "state": True,
                                                  "documentid": 987654321,
                                              }
                                          },
                                          json_encoders={
                                              datetime: lambda v: v.isoformat()
                                          })
    

class EmployeeCreate(UserBase):
    """
    Employee model for the API request.
    """
    birth_date: datetime = Field(..., description="User's birth date")
    first_name: str = Field(..., description="User's first name")
    last_name: str = Field(..., description="User's last name")
    role : EmployeeRole = Field(..., description="User's role in the system")
    
    model_config: ConfigDict = ConfigDict(str_strip_whitespace=True,
                                            use_enum_values=True,
                                            json_schema_extra={
                                                "example": {
                                                    "email": "doro@example.com",
                                                    "name": "Dorotea Hernandez",
                                                    "phone": "555-555-5555",
                                                    "created_at": "2023-01-01T00:00:00Z",
                                                    "updated_at": "2023-01-02T00:00:00Z",
                                                    "state": True,
                                                    "documentid": 123456789,
                                                    "birth_date": "1990-01-01T00:00:00Z",
                                                    "first_name": "Dorotea",
                                                    "last_name": "Hernandez",
                                                    "role": "Empleado",
                                                    
                                                }
                                            },
                                            json_encoders={
                                                datetime: lambda v: v.isoformat()
                                            })

class Employee(EmployeeCreate):
    """
    Employee model for the API response.
    """
    id: int = Field(..., description="User's unique identifier")
    
    model_config: ConfigDict = ConfigDict(str_strip_whitespace=True,
                                            use_enum_values=True,
                                            json_schema_extra={
                                                "example": {
                                                    "id": 1,
                                                    "email": "doro@example.com",
                                                    "name": "Dorotea Hernandez",
                                                    "phone": "555-555-5555",
                                                    "created_at": "2023-01-01T00:00:00Z",
                                                    "updated_at": "2023-01-02T00:00:00Z",
                                                    "state": True,
                                                    "documentid": 123456789,
                                                    "birth_date": "1990-01-01T00:00:00Z",
                                                    "first_name": "Dorotea",
                                                    "last_name": "Hernandez",
                                                    "role": "Empleado",
                                                    
                                                }
                                            },
                                            json_encoders={
                                                datetime: lambda v: v.isoformat()
                                            })