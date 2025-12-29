from datetime import date

from fastapi import HTTPException
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlmodel import select


from models import Employee, Client, EmployeeRole

class UserService:
    
    @classmethod
    async def search_employees_by_name(cls, db_session: AsyncSession,  name: str) -> list[Employee]:
        """Search employees by name."""
        
        try:
            
            response = await db_session.exec(select(Employee).where(Employee.name.ilike(f"%{name}%")))
            employees = list(response.all())

            if employees:
                raise HTTPException(detail="No employees found with the given name", status_code=404)

            return employees
        
        except Exception as e:
            raise HTTPException(detail="Employee search failed", status_code=500) from e

    @classmethod
    async def search_employees_by_birthday(cls, db_session: AsyncSession, birthday: date) -> list[Employee]:
        """Search employees by birthday."""

        try:
            response = await db_session.exec(select(Employee).where(Employee.birth_date == birthday))
            employees = list(response.all())

            if not employees:
                raise HTTPException(detail="No employees found with the given birthday", status_code=404)

            return employees

        except Exception as e:
            raise HTTPException(detail="Employee search failed", status_code=500) from e

    @classmethod
    async def search_employees_by_status(cls,  db_session: AsyncSession, status: bool) -> list[Employee]:
        """Search employees by status."""

        try:
            response = await db_session.exec(select(Employee).where(Employee.status == status))
            employees = list(response.all())

            if not employees:
                raise HTTPException(detail="No employees found with the given status", status_code=404)

            return employees

        except Exception as e:
            raise HTTPException(detail="Employee search failed", status_code=500) from e

    @classmethod
    async def search_employees_by_role(cls, db_session: AsyncSession, role: EmployeeRole) -> list[Employee]:
        """Search employees by role."""

        try:
            
            response = await db_session.exec(select(Employee).where(Employee.role == role.capitalize()))
            employees = list(response.all())
            
            if not employees:
                raise HTTPException(detail="No employees found with the given role", status_code=404)

            return employees
        
        except Exception as e:
            raise HTTPException(detail="Employee search failed", status_code=500) from e
    
    @classmethod
    async def search_employees_by_name_and_role(cls, db_session: AsyncSession, name: str, role: EmployeeRole) -> list[Employee]:
        """Search employees by name and role."""
        
        try:

            response = await db_session.exec(select(Employee).where(Employee.name.ilike(f"%{name}%")).where(Employee.role == role.capitalize()))
            employees = list(response.all())
            
            if not employees:
                raise HTTPException(detail="No employees found with the given name and role", status_code=404)
            
            return employees
        
        except Exception as e:
            raise HTTPException(detail="Employee search failed", status_code=500) from e
    
    @classmethod
    async def search_employees_by_name_and_status(cls, db_session: AsyncSession, name: str, status: bool) -> list[Employee]:
        """Search employees by name and status."""

        try:

            response = await db_session.exec(select(Employee).where(Employee.name.ilike(f"%{name}%")).where(Employee.status == status))
            employees = list(response.all())

            if not employees:
                raise HTTPException(detail="No employees found with the given name and status", status_code=404)

            return employees

        except Exception as e:
            raise HTTPException(detail="Employee search failed", status_code=500) from e
    
    @classmethod
    async def search_employees_by_name_and_birthday(cls, db_session: AsyncSession, name: str, birthday: date) -> list[Employee]:
        """Search employees by name and birthday."""

        try:

            response = await db_session.exec(select(Employee).where(Employee.name.ilike(f"%{name}%")).where(Employee.birth_date == birthday))
            employees = list(response.all())

            if not employees:
                raise HTTPException(detail="No employees found with the given name and birthday", status_code=404)

            return employees

        except Exception as e:
            raise HTTPException(detail="Employee search failed", status_code=500) from e
    
    @classmethod
    async def search_employees_by_role_and_status(cls, db_session: AsyncSession, role: EmployeeRole, status: bool) -> list[Employee]:
        """Search employees by role and status."""
        
        try:
            
            response = await db_session.exec(select(Employee).where(Employee.role == role.capitalize()).where(Employee.status == status))
            employees = list(response.all())
            
            if not employees:
                raise HTTPException(detail="No employees found with the given role and status", status_code=404)
        
            return employees
    
        except Exception as e:
            raise HTTPException(detail="Employee search failed", status_code=500) from e
    
    @classmethod
    async def search_clients_by_name(cls, db_session: AsyncSession, name: str) -> list[Client]:
        """Search clients by name."""
        
        try:

            response = await db_session.exec(select(Client).where(Client.name.ilike(f"%{name}%")))
            clients = list(response.all())

            if not clients:
                raise HTTPException(detail="No clients found with the given name", status_code=404)

            return clients
        
        except Exception as e:
            raise HTTPException(detail="Client search failed", status_code=500) from e
        
    
    @classmethod
    async def search_clients_by_status(cls, db_session: AsyncSession, status: bool) -> list[Client]:
        """Search clients by status."""
        
        try:
            
            response = await db_session.exec(select(Client).where(Client.status == status))
            clients = list(response.all())

            if not clients:
                raise HTTPException(detail="No clients found with the given status", status_code=404)

            return clients
        
        except Exception as e:
            raise HTTPException(detail="Client search failed", status_code=500) from e

    @classmethod
    async def search_clients_by_name_and_status(cls, db_session: AsyncSession, name: str, status: bool) -> list[Client]:
        """Search clients by name and status."""

        try:

            response = await db_session.exec(select(Client).where(Client.name.ilike(f"%{name}%")).where(Client.status == status))
            clients = list(response.all())

            if not clients:
                raise HTTPException(detail="No clients found with the given name and status", status_code=404)

            return clients

        except Exception as e:
            raise HTTPException(detail="Client search failed", status_code=500) from e