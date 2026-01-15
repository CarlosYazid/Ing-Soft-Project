from typing import Optional
from datetime import date

from sqlalchemy.sql.expression import Select
from pydantic import ConfigDict, Field

from models import EmployeeRole, Employee
from dtos.abs import UserCreate, UserRead, UserUpdate, UserFilter

class EmployeeCreate(UserCreate):

    role: EmployeeRole = Field(default=EmployeeRole.EMPLOYEE, description="Employee's role")
    birth_date: Optional[date] = Field(..., description="Employee's birth date")
    password: str = Field(..., description="Password employee")
    
    model_config: ConfigDict = ConfigDict(str_strip_whitespace=True,
                                            use_enum_values=True,
                                            json_schema_extra={
                                                "example": {
                                                    "documentid": 123456789,
                                                    "email": "doro@example.com",
                                                    "phone": "555-555-5555",
                                                    "role": "Empleado",
                                                    "birth_date": "1990-01-01",
                                                    "first_name": "Dorotea",
                                                    "last_name": "Hernandez",
                                                    "password": "92f728fh0fah98fh"
                                                }
                                            },
                                            json_encoders={
                                                date: lambda v: v.isoformat()
                                            })

class EmployeeUpdate(UserUpdate):

    role: Optional[EmployeeRole] = Field(None, description="Employee's role")
    password: Optional[str] = Field(..., description="Password employee")
    
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
                                                    "password": "92fh2hf9haf9f",
                                                    "updated_at": "2023-01-02T00:00:00Z"
                                                }
                                            },
                                            json_encoders={
                                                date: lambda v: v.isoformat()
                                            })

class EmployeeRead(UserRead):

    role: EmployeeRole = Field(..., description="Employee's role")
    
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

class EmployeeFilter(UserFilter):
    
    role: Optional[EmployeeRole] = Field(None, description="Employee's role")
    min_birth_date: Optional[date] = Field(None, description="Min employee's birth date")
    max_birth_date: Optional[date] = Field(None, description="Max employee's birth date")
    
    def apply(self, query: Select) -> Select:
        
        if self.first_name:
            query = query.where(Employee.first_name.ilike(f"%{self.first_name}%"))
        
        if self.last_name:
            query = query.where(Employee.last_name.ilike(f"%{self.last_name}"))
        
        if not self.status is None:
            query = query.where(Employee.status == self.status)
        
        if self.role:
            query = query.where(Employee.role == self.role)
        
        if self.min_birth_date:
            query = query.where(Employee.birth_date >= self.min_birth_date)
        
        if self.max_birth_date:
            query = query.where(Employee.birth_date <= self.max_birth_date)
        
        return query