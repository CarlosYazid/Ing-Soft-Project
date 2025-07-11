from fastapi import HTTPException
from datetime import date

from models import UserBase, EmployeeRole
from db import get_db_client
from core import SETTINGS

class UserService:
    
    FIELDS_USER_BASE = set(UserBase.__fields__.keys())
    
    @classmethod
    async def search_employees_by_name(cls, name: str) -> list[UserBase]:
        """Search employees by name."""

        client = await get_db_client()
            
        response = await client.table(SETTINGS.employee_table).select(*cls.FIELDS_USER_BASE).ilike("name", f"%{name}%").execute()

        if not bool(response.data):
            raise HTTPException(detail="No employees found with the given name", status_code=404)

        return [UserBase.model_validate(employee) for employee in response.data]

    @classmethod
    async def search_employees_by_birthday(cls, birthday: date) -> list[UserBase]:
        """Search employees by birthday."""

        client = await get_db_client()

        response = await client.table(SETTINGS.employee_table).select(*cls.FIELDS_USER_BASE).eq("birth_date", birthday.isoformat()).execute()

        if not bool(response.data):
            raise HTTPException(detail="No employees found with the given birthday", status_code=404)

        return [UserBase.model_validate(employee) for employee in response.data]

    @classmethod
    async def search_employees_by_status(cls, status: bool) -> list[UserBase]:
        """Search employees by status."""

        client = await get_db_client()

        response = await client.table(SETTINGS.employee_table).select(*cls.FIELDS_USER_BASE).eq("state", status).execute()

        if not bool(response.data):
            raise HTTPException(detail="No employees found with the given status", status_code=404)

        return [UserBase.model_validate(employee) for employee in response.data]

    @classmethod
    async def search_employees_by_role(cls, role: EmployeeRole) -> list[UserBase]:
        """Search employees by role."""

        client = await get_db_client()

        response = await client.table(SETTINGS.employee_table).select(*cls.FIELDS_USER_BASE).eq("role", role.capitalize()).execute()

        if not bool(response.data):
            raise HTTPException(detail="No employees found with the given role", status_code=404)

        return [UserBase.model_validate(employee) for employee in response.data]
    
    @classmethod
    async def search_employees_by_name_and_role(cls, name: str, role: EmployeeRole) -> list[UserBase]:
        """Search employees by name and role."""

        client = await get_db_client()

        response = await client.table(SETTINGS.employee_table).select(*cls.FIELDS_USER_BASE).ilike("name", f"%{name}%").eq("role", role.capitalize()).execute()

        if not bool(response.data):
            raise HTTPException(detail="No employees found with the given name and role", status_code=404)

        return [UserBase.model_validate(employee) for employee in response.data]
    
    @classmethod
    async def search_employees_by_name_and_status(cls, name: str, status: bool) -> list[UserBase]:
        """Search employees by name and status."""

        client = await get_db_client()

        response = await client.table(SETTINGS.employee_table).select(*cls.FIELDS_USER_BASE).ilike("name", f"%{name}%").eq("state", status).execute()

        if not bool(response.data):
            raise HTTPException(detail="No employees found with the given name and status", status_code=404)

        return [UserBase.model_validate(employee) for employee in response.data]
    
    @classmethod
    async def search_employees_by_name_and_birthday(cls, name: str, birthday: date) -> list[UserBase]:
        """Search employees by name and birthday."""

        client = await get_db_client()

        response = await client.table(SETTINGS.employee_table).select(*cls.FIELDS_USER_BASE).ilike("name", f"%{name}%").eq("birth_date", birthday.isoformat()).execute()

        if not bool(response.data):
            raise HTTPException(detail="No employees found with the given name and birthday", status_code=404)

        return [UserBase.model_validate(employee) for employee in response.data]
    
    @classmethod
    async def search_employees_by_role_and_status(cls, role: EmployeeRole, status: bool) -> list[UserBase]:
        """Search employees by role and status."""

        client = await get_db_client()

        response = await client.table(SETTINGS.employee_table).select(*cls.FIELDS_USER_BASE).eq("role", role.capitalize()).eq("state", status).execute()

        if not bool(response.data):
            raise HTTPException(detail="No employees found with the given role and status", status_code=404)

        return [UserBase.model_validate(employee) for employee in response.data]
    
    @classmethod
    async def search_clients_by_name(cls, name: str) -> list[UserBase]:
        """Search clients by name."""

        client = await get_db_client()

        response = await client.table(SETTINGS.client_table).select(*cls.FIELDS_USER_BASE).ilike("name", f"%{name}%").execute()

        if not bool(response.data):
            raise HTTPException(detail="No clients found with the given name", status_code=404)

        return [UserBase.model_validate(client) for client in response.data]
    
    @classmethod
    async def search_clients_by_status(cls, status: bool) -> list[UserBase]:
        """Search clients by status."""

        client = await get_db_client()

        response = await client.table(SETTINGS.client_table).select(*cls.FIELDS_USER_BASE).eq("state", status).execute()

        if not bool(response.data):
            raise HTTPException(detail="No clients found with the given status", status_code=404)

        return [UserBase.model_validate(client) for client in response.data]

    @classmethod
    async def search_clients_by_name_and_status(cls, name: str, status: bool) -> list[UserBase]:
        """Search clients by name and status."""

        client = await get_db_client()

        response = await client.table(SETTINGS.client_table).select(*cls.FIELDS_USER_BASE).ilike("name", f"%{name}%").eq("state", status).execute()

        if not bool(response.data):
            raise HTTPException(detail="No clients found with the given name and status", status_code=404)

        return [UserBase.model_validate(client) for client in response.data]