from pydantic import BaseModel, EmailStr, Field, ConfigDict
from typing import Optional
from datetime import datetime
from abc import ABC


class AbstractUser(ABC, BaseModel):
    id: int = Field(..., description="User's unique identifier")
    email: EmailStr = Field(..., description="User's email address")
    name: str = Field(..., description="User's name")
    phone: Optional[str] = Field(None, description="User's phone number")

class UserBase(AbstractUser):
    """
    Base model for users.
    """
    username: Optional[str] = Field(None, description="User's username")
    password: str = Field(..., description="User's password")
    

class User(UserBase):
    """
    User model for the API response.
    """
    

    created_at: datetime = Field(..., description="Timestamp when the user was created")
    state : bool = Field(default=True, description="Is the user active?")
    
    model_config: ConfigDict = ConfigDict(str_to_lower=True,
                                          str_strip_whitespace=True,
                                          use_enum_values=True,
                                          json_schema_extra={
                                              "example": {
                                                  "id": 1,
                                                  "email": "user@example.com",
                                                  "username": "johndoe",
                                                  "name": "John Doe",
                                                  "phone": "123-456-7890",
                                                  "created_at": "2023-01-01T00:00:00Z",
                                                  "birth_date": "1990-01-01T00:00:00Z",
                                                  "password": "hashed_password",
                                                  "state": True,
                                                  "first_name": "John",
                                                  "last_name": "Doe"
                                              }
                                          },
                                          json_encoders={
                                              datetime: lambda v: v.isoformat()
                                          })

class Client(AbstractUser):
    
    """
    Client model for the API response.
    """
    
    created_at: datetime = Field(..., description="Timestamp when the client was created")
    birth_date: datetime = Field(..., description="Client's birth date")
    state : bool = Field(default=True, description="Is the client active?")
    documentID: int = Field(..., description="User's document ID")
    

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
                                                  "birth_date": "1995-01-01T00:00:00Z",
                                                  "documentID": 987654321,
                                                  "state": True,
                                                  "role": "client",

                                              }
                                          },
                                          json_encoders={
                                              datetime: lambda v: v.isoformat()
                                          })

class Employee(User):
    """
    Employee model for the API response.
    """
    
    birth_date: datetime = Field(..., description="User's birth date")
    sales: list[int] = Field(..., description="List of sales made by the employee")
    documentID: int = Field(..., description="User's document ID")
    first_name: str = Field(..., description="User's first name")
    last_name: str = Field(..., description="User's last name")
    
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
                                                    "sales": [1, 2, 3],
                                                    "first_name": "Employee",
                                                    "last_name": "Doe"
                                                }
                                            },
                                            json_encoders={
                                                datetime: lambda v: v.isoformat()
                                            })
class Admin(User):
    """
    Admin model for the API response.
    """
    
    permissions: list[str] = Field(..., description="List of permissions granted to the admin")
    
    model_config: ConfigDict = ConfigDict(str_to_lower=True,
                                          str_strip_whitespace=True,
                                          use_enum_values=True,
                                          json_schema_extra={
                                              "example": {
                                                  "id": 1,
                                                  "email": "admin@example.com",
                                                  "username": "admindoe",
                                                  "name": "Admin Doe",
                                                  "phone": "555-555-5555",
                                                  "created_at": "2023-01-01T00:00:00Z",
                                                  "documentID": 123456789,
                                                  "permissions": ["manage_users", "view_reports"],
                                              }
                                          },
                                          json_encoders={
                                              datetime: lambda v: v.isoformat()
                                          })