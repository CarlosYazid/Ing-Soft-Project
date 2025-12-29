from fastapi import HTTPException
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlmodel import select

from models import Employee, Client

class UserUtils:
    
    @classmethod
    async def exist_employee(cls, db_session: AsyncSession, employee_id: int) -> bool:
        """Check if an employee exists by ID."""
        
        try:

            response = await db_session.exec(select(Employee).where(Employee.id == employee_id))

            return bool(response.first())
        
        except Exception as e:
            raise HTTPException(detail="Employee retrieval failed", status_code=500) from e

    @classmethod
    async def exist_employee_by_email(cls, db_session: AsyncSession, email: str) -> bool:
        """Check if an employee exists by email."""
        
        try:

            response = await db_session.exec(select(Employee).where(Employee.email == email))

            return bool(response.first())
        
        except Exception as e:
            raise HTTPException(detail="Employee retrieval failed", status_code=500) from e
    
    @classmethod
    async def exist_employee_by_documentid(cls, db_session: AsyncSession, document_id: int) -> bool:
        """Check if an employee exists by document ID."""
        
        try:
            
            response = await db_session.exec(select(Employee).where(Employee.documentid == document_id))
            
            return bool(response.first())
        
        except Exception as e:
            raise HTTPException(detail="Employee retrieval failed", status_code=500) from e
    
    @classmethod
    async def translate_email_by_employee_id(cls, db_session: AsyncSession, email: str) -> int:
        """Translate email to employee ID."""
        
        if not await cls.exist_employee_by_email(db_session, email):
            raise HTTPException(detail="Employee not found", status_code=404)
        
        try:

            response = await db_session.exec(select(Employee).where(Employee.email == email))

            return int(response.one().id)

        except Exception as e:
            raise HTTPException(detail="Failed to retrieve employee ID", status_code=500) from e
    
    @classmethod
    async def translate_documentid_by_employee_id(cls, db_session: AsyncSession, document_id: int) -> int:
        """Translate document ID to employee ID."""
        
        if not await cls.exist_employee_by_documentid(db_session, document_id):
            raise HTTPException(detail="Employee not found", status_code=404)

        try:

            response = await db_session.exec(select(Employee).where(Employee.document_id == document_id))

            return int(response.one().id)

        except Exception as e:
            raise HTTPException(detail="Failed to retrieve employee ID", status_code=500) from e
    
    @classmethod
    async def exist_client(cls, db_session: AsyncSession, _id: int) -> bool:
        """Check if a client exists by ID."""

        try:

            response = await db_session.exec(select(Client).where(Client.id == _id))

            return bool(response.first())

        except Exception as e:
            raise HTTPException(detail="Client retrieval failed", status_code=500) from e
        
    
    @classmethod
    async def exist_client_by_email(cls, db_session: AsyncSession, email: str) -> bool:
        """Check if a client exists by email."""
        
        try:

            response = await db_session.exec(select(Client).where(Client.email == email))

            return bool(response.first())
        
        except Exception as e:
            raise HTTPException(detail="Client retrieval failed", status_code=500) from e
    
    @classmethod
    async def exist_client_by_documentid(cls, db_session: AsyncSession, document_id: int) -> bool:
        """Check if a client exists by document ID."""
        
        try:

            response = await db_session.exec(select(Client).where(Client.documentid == document_id))

            return bool(response.first())
        
        except Exception as e:
            raise HTTPException(detail="Client retrieval failed", status_code=500) from e
    
    @classmethod
    async def translate_email_by_client_id(cls, db_session: AsyncSession, email: str) -> int:
        """Translate email to client ID."""
        
        if not await cls.exist_client_by_email(db_session, email):
            raise HTTPException(detail="Client not found", status_code=404)
        
        try:

            response = await db_session.exec(select(Client).where(Client.email == email))

            return int(response.one().id)
        
        except Exception as e:
            raise HTTPException(detail="Failed to retrieve client ID", status_code=500) from e
    
    @classmethod
    async def translate_documentid_by_client_id(cls, db_session: AsyncSession, document_id: int) -> int:
        """Translate document ID to client ID."""
        
        if not await cls.exist_client_by_documentid(db_session, document_id):
            raise HTTPException(detail="Client not found", status_code=404)
        
        try:

            response = await db_session.exec(select(Client).where(Client.documentid == document_id))

            return int(response.one().id)
        
        except Exception as e:
            raise HTTPException(detail="Failed to retrieve client ID", status_code=500) from e