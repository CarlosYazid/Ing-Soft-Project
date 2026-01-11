from typing import Optional, TYPE_CHECKING
from enum import Enum
from datetime import date

from sqlmodel import Relationship, Field

from models.abs import UserModel

if TYPE_CHECKING:
    from models.order import Order

class EmployeeRole(str, Enum):
    ADMIN = "Admin"
    EMPLOYEE = "Empleado"

class Employee(UserModel, table = True):

    role: EmployeeRole = Field(default=EmployeeRole.EMPLOYEE, description="Employee's role")
    birth_date: Optional[date] = Field(None, description="Employee's birth date")
    password: str = Field(..., description="Employee's password")

    orders: Optional[list['Order']] = Relationship(back_populates="employee", sa_relationship_kwargs={"lazy": "selectin"})