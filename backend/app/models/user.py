from pydantic import BaseModel, EmailStr, Field, ConfigDict
from typing import Optional
from datetime import datetime
from abc import ABC
from enum import Enum

class EmployeeRole(str, Enum):
    ADMIN = "admin"
    EMPLOYEE = "employee"

class AbstractUser(ABC, BaseModel):
    id: int = Field(..., description="User's unique identifier")
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
    documentID: int = Field(..., description="User's document ID", alias="documentid")

class Client(UserBase):
    
    """
    Client model for the API response.
    """
         

    model_config: ConfigDict = ConfigDict(str_to_lower=True,
                                          str_strip_whitespace=True,
                                          use_enum_values=True,
                                          json_schema_extra={
                                              "example": {
                                                  "id": 1,
                                                  "email": "client@example.com",
                                                  "name": "Jane Doe",
                                                  "phone": "987-654-3210",
                                                  "created_at": "2023-01-01T00:00:00Z",
                                                  "updated_at": "2023-01-02T00:00:00Z",
                                                  "documentID": 987654321,
                                                  "state": True
                                              }
                                          },
                                          json_encoders={
                                              datetime: lambda v: v.isoformat()
                                          })

class Employee(UserBase):
    """
    Employee model for the API response.
    """
    birth_date: datetime = Field(..., description="User's birth date")
    first_name: str = Field(..., description="User's first name")
    last_name: str = Field(..., description="User's last name")
    role : EmployeeRole = Field(..., description="User's role in the system")
    
    model_config: ConfigDict = ConfigDict(str_to_lower=True,
                                            str_strip_whitespace=True,
                                            use_enum_values=True,
                                            json_schema_extra={
                                                "example": {
                                                    "id": 1,
                                                    "email": "employee@example.com",
                                                    "username": "employeedoe",
                                                    "name": "Employee Doe",
                                                    "phone": "555-555-5555",
                                                    "created_at": "2023-01-01T00:00:00Z",
                                                    "birth_date": "1990-01-01T00:00:00Z",
                                                    "documentID": 123456789,
                                                    "first_name": "Employee",
                                                    "last_name": "Doe",
                                                    "role": "employee",
                                                    "state": True
                                                }
                                            },
                                            json_encoders={
                                                datetime: lambda v: v.isoformat()
                                            })