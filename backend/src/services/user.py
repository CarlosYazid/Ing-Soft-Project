from datetime import date

from fastapi import HTTPException
from sqlmodel import select
from sqlalchemy.sql.expression import Select

from models import Employee, Client, EmployeeRole

class UserService:
    
    @classmethod
    def read_all_employees(cls) -> Select:
        """Query for retrieve all employees."""
        return select(Employee)
    
    @classmethod
    def search_employees_by_name(cls, name: str) -> Select:
        """Query for search employees by name."""
        return select(Employee).where(Employee.first_name.ilike(f"%{name}%"))

    @classmethod
    def search_employees_by_birthday(cls, birthday: date) -> Select:
        """Query for search employees by birthday."""
        return select(Employee).where(Employee.birth_date == birthday)

    @classmethod
    def search_employees_by_status(cls, status: bool) -> Select:
        """Query for search employees by status."""
        return select(Employee).where(Employee.status == status)

    @classmethod
    def search_employees_by_role(cls, role: EmployeeRole) -> Select:
        """Query for search employees by role."""
        return select(Employee).where(Employee.role == role.capitalize())
    
    @classmethod
    def search_employees_by_name_and_role(cls, name: str, role: EmployeeRole) -> Select:
        """Query for search employees by name and role."""
        return select(Employee).where(Employee.first_name.ilike(f"%{name}%")).where(Employee.role == role.capitalize())
    
    @classmethod
    def search_employees_by_name_and_status(cls, name: str, status: bool) -> Select:
        """Query for search employees by name and status."""
        return select(Employee).where(Employee.first_name.ilike(f"%{name}%")).where(Employee.status == status)
        
    @classmethod
    def search_employees_by_name_and_birthday(cls, name: str, birthday: date) -> Select:
        """Query for search employees by name and birthday."""
        return select(Employee).where(Employee.first_name.ilike(f"%{name}%")).where(Employee.birth_date == birthday)
        
    @classmethod
    def search_employees_by_role_and_status(cls, role: EmployeeRole, status: bool) -> Select:
        """Query for search employees by role and status."""
        return select(Employee).where(Employee.role == role.capitalize()).where(Employee.status == status)
    
    @classmethod
    def read_all_clients(cls) -> Select:
        """Query for retrieve all clients."""
        return select(Client)
    
    @classmethod
    def search_clients_by_name(cls, name: str) -> Select:
        """Query for search clients by name."""
        return select(Client).where(Client.first_name.ilike(f"%{name}%"))
    
    @classmethod
    def search_clients_by_status(cls, status: bool) -> Select:
        """Query for search clients by status."""
        return select(Client).where(Client.status == status)

    @classmethod
    def search_clients_by_name_and_status(cls, name: str, status: bool) -> Select:
        """Query for search clients by name and status."""
        return select(Client).where(Client.first_name.ilike(f"%{name}%")).where(Client.status == status)