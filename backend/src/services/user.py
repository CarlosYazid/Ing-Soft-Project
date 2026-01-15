from datetime import date

from fastapi import HTTPException
from sqlmodel import select
from sqlalchemy.sql.expression import Select

from models import Employee, Client, EmployeeRole

from dtos import EmployeeFilter, ClientFilter

class UserService:
    
    QUERY_EMPLOYEE_BASE = select(Employee)
    QUERY_CLIENT_BASE = select(Client)
    
    @classmethod
    def search_employees(cls, filters : EmployeeFilter) -> Select:
        """Query that searches for employees who meet the filters."""
        return filters.apply(cls.QUERY_EMPLOYEE_BASE)
    
    @classmethod
    def search_clients(cls, filters: ClientFilter) -> Select:
        """Query that searches for clients who meet the filters.."""
        return filters.apply(cls.QUERY_CLIENT_BASE)
    