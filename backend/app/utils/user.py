from fastapi import HTTPException

from core import SETTINGS
from db import get_db_client

class UserUtils:
    
    @classmethod
    async def exist_employee(cls, employee_id: int) -> bool:
        """Check if an employee exists by ID."""

        client = await get_db_client()

        response = await client.table(SETTINGS.employee_table).select("id").eq("id", employee_id).execute()

        return bool(response.data)

    @classmethod
    async def exist_employee_by_email(cls, email: str) -> bool:
        """Check if an employee exists by email."""

        client = await get_db_client()

        response = await client.table(SETTINGS.employee_table).select("email").eq("email", email).execute()

        return bool(response.data)
    
    @classmethod
    async def exist_employee_by_documentid(cls, document_id: int) -> bool:
        """Check if an employee exists by document ID."""

        client = await get_db_client()

        response = await client.table(SETTINGS.employee_table).select("documentid").eq("documentid", document_id).execute()

        return bool(response.data)
    
    @classmethod
    async def translate_email_by_employee_id(cls, email: str) -> int:
        """Translate email to employee ID."""
        
        if not await cls.exist_employee_by_email(email):
            raise HTTPException(detail="Employee not found", status_code=404)

        client = await get_db_client()

        response = await client.table(SETTINGS.employee_table).select("email", "id").eq("email", email).execute()

        if not bool(response.data):
            raise HTTPException(detail="Failed to retrieve employee ID", status_code=500)

        return int(response.data[0]["id"])
    
    @classmethod
    async def translate_documentid_by_employee_id(cls, document_id: int) -> int:
        """Translate document ID to employee ID."""
        
        if not await cls.exist_employee_by_documentid(document_id):
            raise HTTPException(detail="Employee not found", status_code=404)

        client = await get_db_client()

        response = await client.table(SETTINGS.employee_table).select("documentid", "id").eq("documentid", document_id).execute()

        if not bool(response.data):
            raise HTTPException(detail="Failed to retrieve employee ID", status_code=500)

        return int(response.data[0]["id"])
    
    @classmethod
    async def exist_client(cls, _id: int) -> bool:
        """Check if a client exists by ID."""

        client = await get_db_client()

        response = await client.table(SETTINGS.client_table).select("id").eq("id", _id).execute()

        return bool(response.data)
    
    @classmethod
    async def exist_client_by_email(cls, email: str) -> bool:
        """Check if a client exists by email."""

        client = await get_db_client()

        response = await client.table(SETTINGS.client_table).select("email").eq("email", email).execute()

        return bool(response.data)
    
    @classmethod
    async def exist_client_by_documentid(cls, document_id: int) -> bool:
        """Check if a client exists by document ID."""

        client = await get_db_client()

        response = await client.table(SETTINGS.client_table).select("documentid").eq("documentid", document_id).execute()

        return bool(response.data)
    
    @classmethod
    async def translate_email_by_client_id(cls, email: str) -> int:
        """Translate email to client ID."""
        
        if not await cls.exist_client_by_email(email):
            raise HTTPException(detail="Client not found", status_code=404)

        client = await get_db_client()

        response = await client.table(SETTINGS.client_table).select("email", "id").eq("email", email).execute()

        if not bool(response.data):
            raise HTTPException(detail="Failed to retrieve client ID", status_code=500)

        return int(response.data[0]["id"])
    
    @classmethod
    async def translate_documentid_by_client_id(cls, document_id: int) -> int:
        """Translate document ID to client ID."""
        
        if not await cls.exist_client_by_documentid(document_id):
            raise HTTPException(detail="Client not found", status_code=404)

        client = await get_db_client()

        response = await client.table(SETTINGS.client_table).select("documentid", "id").eq("documentid", document_id).execute()

        if not bool(response.data):
            raise HTTPException(detail="Failed to retrieve client ID", status_code=500)

        return int(response.data[0]["id"])