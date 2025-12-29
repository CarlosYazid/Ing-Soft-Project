from __future__ import annotations
from typing import Optional
from datetime import datetime
from enum import Enum

from pydantic import BaseModel, EmailStr, ConfigDict, Field
from sqlmodel import SQLModel, Relationship, Field as FieldDB

class Client(SQLModel, table = True):
    
    id : Optional[int] = FieldDB(primary_key=True, index = True)
    documentid: int = FieldDB(..., description="Client's document ID", index = True)
    email: EmailStr = FieldDB(..., description="Client's email address", index = True)
    phone: Optional[str] = FieldDB(None, description="Client's phone number", index = True)
    name: str = FieldDB(..., description="Client's name")
    status : bool = FieldDB(default=True, description="Is the client active?")
    created_at: datetime = FieldDB(default_factory=datetime.now, description="Timestamp when the client was created")
    updated_at: datetime = FieldDB(default_factory=datetime.now, description="Timestamp when the client was last updated")
    
    orders: list["Order"] = Relationship(back_populates="client")
    payments: list["Payment"] = Relationship(back_populates="client")


class ClientCreate(BaseModel):
    
    documentid: int = Field(..., description="Client's document ID", gt = 0)
    email: EmailStr = Field(..., description="Client's email address")
    phone: Optional[str] = Field(None, description="Client's phone number")
    name: str = Field(..., description="Client's name")
    
    model_config: ConfigDict = ConfigDict(str_strip_whitespace=True,
                                            json_schema_extra={
                                                "example": {
                                                    "documentid": 1234567890,
                                                    "email": "doro@example.com",
                                                    "phone": "555-555-5555",
                                                    "name": "Dorotea Hernandez",
                                                }
                                            })
    
class ClientUpdate(BaseModel):

    id: Optional[int] = Field(None, description="Client's ID", gt = 0)
    email: Optional[EmailStr] = Field(None, description="Client's email address")
    documentid: Optional[int] = Field(None, description="Client's document ID", gt = 0)
    phone: Optional[str] = Field(None, description="Client's phone number")
    name: Optional[str] = Field(None, description="Client's name")
    status: Optional[bool] = Field(None, description="Is the client active?")
    updated_at: datetime = Field(default_factory=datetime.now, description="Timestamp when the client was last updated")
    
    model_config: ConfigDict = ConfigDict(str_strip_whitespace=True,
                                            json_schema_extra={
                                                "example": {
                                                    "id": 1,
                                                    "email": "doro@example.com",
                                                    "phone": "555-555-5555",
                                                    "name": "Dorotea Hernandez",
                                                    "status": True,
                                                    "updated_at": datetime.now()
                                                }
                                            })

class ClientRead(BaseModel):

    id: int = Field(..., description="Client's ID")
    documentid: int = Field(..., description="Client's document ID")
    email: EmailStr = Field(..., description="Client's email address")
    phone: Optional[str] = Field(None, description="Client's phone number")
    name: str = Field(..., description="Client's name")
    status: bool = Field(..., description="Is the client active?")
    
    model_config: ConfigDict = ConfigDict(str_strip_whitespace=True,
                                            json_schema_extra={
                                                "example": {
                                                    "id": 1,
                                                    "documentid": 1234567890,
                                                    "email": "doro@example.com",
                                                    "phone": "555-555-5555",
                                                    "name": "Dorotea Hernandez",
                                                    "status": True,
                                                }
                                            })

class EmployeeRole(str, Enum):
    ADMIN = "Admin"
    EMPLOYEE = "Empleado"

class Employee(SQLModel, table = True):

    id : Optional[int] = FieldDB(primary_key=True, index = True)
    documentid: int = FieldDB(..., description="Employee's document ID", index = True)
    email: EmailStr = FieldDB(..., description="Employee's email address", index = True)
    phone: Optional[str] = FieldDB(None, description="Employee's phone number", index = True)
    role: EmployeeRole = FieldDB(..., description="Employee's role")
    birth_date: datetime = FieldDB(..., description="Employee's birth date")
    first_name: str = FieldDB(..., description="Employee's first name")
    last_name: str = FieldDB(..., description="Employee's last name")
    status : bool = FieldDB(default=True, description="Is the employee active?")
    created_at: datetime = FieldDB(default_factory=datetime.now, description="Timestamp when the employee was created")
    updated_at: datetime = FieldDB(default_factory=datetime.now, description="Timestamp when the employee was last updated")
    
    orders: list["Order"] = Relationship(back_populates="employee")
    
class EmployeeCreate(BaseModel):

    documentid: int = Field(..., description="Employee's document ID", gt = 0)
    email: EmailStr = Field(..., description="Employee's email address")
    phone: Optional[str] = Field(None, description="Employee's phone number")
    role: EmployeeRole = Field(..., description="Employee's role")
    birth_date: datetime = Field(..., description="Employee's birth date")
    first_name: str = Field(..., description="Employee's first name")
    last_name: str = Field(..., description="Employee's last name")
    
    model_config: ConfigDict = ConfigDict(str_strip_whitespace=True,
                                            use_enum_values=True,
                                            json_schema_extra={
                                                "example": {
                                                    "documentid": 123456789,
                                                    "email": "doro@example.com",
                                                    "phone": "555-555-5555",
                                                    "role": "Empleado",
                                                    "birth_date": "1990-01-01T00:00:00Z",
                                                    "first_name": "Dorotea",
                                                    "last_name": "Hernandez",
                                                }
                                            },
                                            json_encoders={
                                                datetime: lambda v: v.isoformat()
                                            })

class EmployeeUpdate(BaseModel):

    id: Optional[int] = Field(None, description="Employee's ID", gt = 0)
    email: Optional[EmailStr] = Field(None, description="Employee's email address")
    documentid: Optional[int] = Field(None, description="Employee's document ID", gt = 0)
    phone: Optional[str] = Field(None, description="Employee's phone number")
    role: Optional[EmployeeRole] = Field(None, description="Employee's role")
    first_name: Optional[str] = Field(None, description="Employee's first name")
    last_name: Optional[str] = Field(None, description="Employee's last name")
    status: Optional[bool] = Field(None, description="Is the employee active?")
    updated_at: datetime = Field(default_factory=datetime.now, description="Timestamp when the employee was last updated")

    model_config: ConfigDict = ConfigDict(str_strip_whitespace=True,
                                            use_enum_values=True,
                                            json_schema_extra={
                                                "example": {
                                                    "id": 1,
                                                    "email": "doro@example.com",
                                                    "phone": "555-555-5555",
                                                    "role": "Empleado",
                                                    "first_name": "Dorotea",
                                                    "last_name": "Hernandez",
                                                    "status": True,
                                                    "updated_at": "2023-01-02T00:00:00Z"
                                                }
                                            },
                                            json_encoders={
                                                datetime: lambda v: v.isoformat()
                                            })

class EmployeeRead(BaseModel):

    id: int = Field(..., description="Employee's ID")
    documentid: int = Field(..., description="Employee's document ID")
    email: EmailStr = Field(..., description="Employee's email address")
    phone: Optional[str] = Field(None, description="Employee's phone number")
    role: EmployeeRole = Field(..., description="Employee's role")
    first_name: str = Field(..., description="Employee's first name")
    last_name: str = Field(..., description="Employee's last name")
    status: bool = Field(..., description="Is the employee active?")
    
    model_config: ConfigDict = ConfigDict(str_strip_whitespace=True,
                                            use_enum_values=True,
                                            json_schema_extra={
                                                "example": {
                                                    "id": 1,
                                                    "documentid": 1234567890,
                                                    "email": "doro@example.com",
                                                    "phone": "555-555-5555",
                                                    "role": "Empleado",
                                                    "first_name": "Dorotea",
                                                    "last_name": "Hernandez",
                                                    "status": True,
                                                }
                                            })