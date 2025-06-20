from fastapi import HTTPException

from db import get_db_client
from models import Employee, Client
from core import SETTINGS

class UserCrud:
    """CRUD operations for users"""

    @classmethod
    async def get_all_employees(cls) -> list[Employee]:
        """Retrieve all employees."""

        client = await get_db_client()

        response = await client.table(SETTINGS.employee_table).select("*").execute()

        if not(bool(response.data)):
            raise HTTPException(detail="No employees found", status_code=404)

        return [Employee.model_validate(employee) for employee in response.data]
    
    
    @classmethod
    async def create_employee(cls, employee : Employee) -> Employee:
        """Create a new employee."""

        client = await get_db_client()

        response = await client.table(SETTINGS.employee_table).insert(employee.model_dump(mode="json")).execute()

        if not(bool(response.data)):
            raise HTTPException(detail="Employee creation failed", status_code=400)
        return Employee.model_validate(response.data[0])

    @classmethod
    async def update_employee_by_id(cls, _id: int, fields: dict) -> Employee:
        """Update an existing employee."""

        client = await get_db_client()

        response = await client.table(SETTINGS.employee_table).update(fields).eq("id", _id).execute()

        if not(bool(response.data)):

            if not cls.exist_employee_by_id(_id):
                raise HTTPException(detail="Employee not found", status_code=404)

            raise HTTPException(detail="Employee update failed", status_code=400)

        return Employee.model_validate(response.data[0])

    @classmethod
    async def update_employee_by_email(cls, email: str, fields: dict) -> Employee:
        """Update an existing employee by email."""

        client = await get_db_client()

        response = await client.table(SETTINGS.employee_table).update(fields).eq("email", email).execute()

        if not(bool(response.data)):

            if not cls.exist_employee_by_email(email):
                raise HTTPException(detail="Employee not found", status_code=404)

            raise HTTPException(detail="Employee update failed", status_code=400)

        return Employee.model_validate(response.data[0])

    @classmethod
    async def read_employee_by_id(cls, employee_id: int) -> Employee:
        """Retrieve an employee by ID."""

        client = await get_db_client()

        response = await client.table(SETTINGS.employee_table).select("*").eq("id", employee_id).execute()

        if not(bool(response.data)):

            raise HTTPException(detail="Employee not found", status_code=404)

        return Employee.model_validate(response.data[0])

    @classmethod
    async def read_employee_by_email(cls, email: str) -> Employee:
        """Retrieve an employee by email."""

        client = await get_db_client()

        response = await client.table(SETTINGS.employee_table).select("*").eq("email", email).execute()

        if not(bool(response.data)):
            raise HTTPException(detail="Employee not found", status_code=404)

        return Employee.model_validate(response.data[0])
    
    @classmethod
    async def exist_employee_by_email(cls, email: str) -> bool:
        """Check if an employee exists by email."""

        client = await get_db_client()

        response = await client.table(SETTINGS.employee_table).select("email").eq("email", email).execute()

        return bool(response.data)

    @classmethod
    async def exist_employee_by_id(cls, employee_id: int) -> bool:
        """Check if an employee exists by ID."""

        client = await get_db_client()

        response = await client.table(SETTINGS.employee_table).select("id").eq("id", employee_id).execute()

        return bool(response.data)

    @classmethod
    async def delete_employee_by_id(cls, employee_id: int) -> bool:
        """Delete an employee by ID."""

        client = await get_db_client()

        response = await client.table(SETTINGS.employee_table).delete().eq("id", employee_id).execute()

        if not(bool(response.data)):
            raise HTTPException(detail="Employee not found", status_code=404)

        return True
    @classmethod
    async def delete_employee_by_email(cls, email: str) -> bool:
        """Delete an employee by email."""

        client = await get_db_client()

        response = await client.table(SETTINGS.employee_table).delete().eq("email", email).execute()

        if not(bool(response.data)):
            raise HTTPException(detail="Employee not found", status_code=404)

        return True

    @classmethod
    async def get_all_clients(cls) -> list[Client]:
        """Retrieve all clients."""

        client = await get_db_client()

        response = await client.table(SETTINGS.client_table).select("*").execute()

        if not(bool(response.data)):
            raise HTTPException(detail="No clients found", status_code=404)

        return [Client.model_validate(client) for client in response.data]

    @classmethod
    async def create_client(cls, client: Client) -> Client:
        """Create a new client."""

        client = await get_db_client()

        response = await client.table(SETTINGS.client_table).insert(client.model_dump(mode="json")).execute()

        if not(bool(response.data)):
            raise HTTPException(detail="Client creation failed", status_code=400)
        return Client.model_validate(response.data[0])
    
    @classmethod
    async def update_client_by_id(cls, _id: int, fields: dict) -> Client:
        """Update an existing client."""

        client = await get_db_client()

        response = await client.table(SETTINGS.client_table).update(fields).eq("id", _id).execute()

        if not(bool(response.data)):

            if not cls.exist_client_by_id(_id):
                raise HTTPException(detail="Client not found", status_code=404)

            raise HTTPException(detail="Client update failed", status_code=400)

        return Client.model_validate(response.data[0])
    
    @classmethod
    async def update_client_by_email(cls, email: str, fields: dict) -> Client:
        """Update an existing client by email."""

        client = await get_db_client()

        response = await client.table(SETTINGS.client_table).update(fields).eq("email", email).execute()

        if not(bool(response.data)):

            if not cls.exist_client_by_email(email):
                raise HTTPException(detail="Client not found", status_code=404)

            raise HTTPException(detail="Client update failed", status_code=400)

        return Client.model_validate(response.data[0])
    
    @classmethod
    async def exist_client_by_email(cls, email: str) -> bool:
        """Check if a client exists by email."""

        client = await get_db_client()

        response = await client.table(SETTINGS.client_table).select("email").eq("email", email).execute()

        return bool(response.data)
    
    @classmethod
    async def exist_client_by_id(cls, _id: int) -> bool:
        """Check if a client exists by ID."""

        client = await get_db_client()

        response = await client.table(SETTINGS.client_table).select("id").eq("id", _id).execute()

        return bool(response.data)
    
    @classmethod
    async def read_client_by_id(cls, client_id: int) -> Client:
        """Retrieve a client by ID."""

        client = await get_db_client()

        response = await client.table(SETTINGS.client_table).select("*").eq("id", client_id).execute()

        if not(bool(response.data)):
            raise HTTPException(detail="Client not found", status_code=404)

        return Client.model_validate(response.data[0])
    
    @classmethod
    async def read_client_by_email(cls, email: str) -> Client:
        """Retrieve a client by email."""

        client = await get_db_client()

        response = await client.table(SETTINGS.client_table).select("*").eq("email", email).execute()

        if not(bool(response.data)):
            raise HTTPException(detail="Client not found", status_code=404)

        return Client.model_validate(response.data[0])
    
    @classmethod
    async def delete_client_by_id(cls, client_id: int) -> bool:
        """Delete a client by ID."""

        client = await get_db_client()

        response = await client.table(SETTINGS.client_table).delete().eq("id", client_id).execute()

        if not(bool(response.data)):
            raise HTTPException(detail="Client not found", status_code=404)

        return True
    
    @classmethod
    async def delete_client_by_email(cls, email: str) -> bool:
        """Delete a client by email."""

        client = await get_db_client()

        response = await client.table(SETTINGS.client_table).delete().eq("email", email).execute()

        if not(bool(response.data)):
            raise HTTPException(detail="Client not found", status_code=404)

        return True