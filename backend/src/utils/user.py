from fastapi import HTTPException
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlmodel import select

from models import Employee, Client
from core import log_operation

class UserUtils:
    
    @staticmethod
    @log_operation(True)
    async def exist_employee(db_session: AsyncSession, employee_id: int) -> bool:
        """Check if an employee exists by ID."""
        
        try:

            response = await db_session.exec(select(Employee).where(Employee.id == employee_id))

            return bool(response.first())
        
        except Exception as e:
            raise HTTPException(detail="Employee retrieval failed", status_code=500) from e

    @staticmethod
    @log_operation(True)
    async def exist_employee_by_email(db_session: AsyncSession, email: str) -> bool:
        """Check if an employee exists by email."""
        
        try:

            response = await db_session.exec(select(Employee).where(Employee.email == email))

            return bool(response.first())
        
        except Exception as e:
            raise HTTPException(detail="Employee retrieval failed", status_code=500) from e
    
    @staticmethod
    @log_operation(True)
    async def exist_employee_by_documentid(db_session: AsyncSession, document_id: int) -> bool:
        """Check if an employee exists by document ID."""
        
        try:
            
            response = await db_session.exec(select(Employee).where(Employee.documentid == document_id))
            
            return bool(response.first())
        
        except Exception as e:
            raise HTTPException(detail="Employee retrieval failed", status_code=500) from e
    
    @staticmethod
    @log_operation(True)
    async def translate_email_by_employee_id(db_session: AsyncSession, email: str) -> int:
        """Translate to email by employee id"""
        
        try:
            
            response = await db_session.exec(select(Employee).where(Employee.email == email))
            
            return int(response.one().id)
        
        except Exception as e:
            raise HTTPException(detail="Employee id retrieval failed", status_code=500) from e
    
    @staticmethod
    @log_operation(True)
    async def translate_documentid_by_employee_id(db_session: AsyncSession, documentid: int) -> int:
        """Translate to documentid by employee id"""
        
        try:
            
            response = await db_session.exec(select(Employee).where(Employee.documentid == documentid))
            
            return int(response.one().id)
        
        except Exception as e:
            raise HTTPException(detail="Employee id retrieval failed", status_code=500) from e
    
    @staticmethod
    @log_operation(True)
    async def exist_client(db_session: AsyncSession, _id: int) -> bool:
        """Check if a client exists by ID."""

        try:

            response = await db_session.exec(select(Client).where(Client.id == _id))

            return bool(response.first())

        except Exception as e:
            raise HTTPException(detail="Client retrieval failed", status_code=500) from e
    
    @staticmethod
    @log_operation(True)
    async def exist_client_by_email(db_session: AsyncSession, email: str) -> bool:
        """Check if a client exists by email."""
        
        try:

            response = await db_session.exec(select(Client).where(Client.email == email))

            return bool(response.first())
        
        except Exception as e:
            raise HTTPException(detail="Client retrieval failed", status_code=500) from e
    
    @staticmethod
    @log_operation(True)
    async def exist_client_by_documentid(db_session: AsyncSession, document_id: int) -> bool:
        """Check if a client exists by document ID."""
        
        try:

            response = await db_session.exec(select(Client).where(Client.documentid == document_id))

            return bool(response.first())
        
        except Exception as e:
            raise HTTPException(detail="Client retrieval failed", status_code=500) from e
    
    @staticmethod
    @log_operation(True)
    async def translate_email_by_client_id(db_session: AsyncSession, email: str) -> int:
        """Translate to email by client id"""
        
        try:
            
            response = await db_session.exec(select(Client).where(Client.email == email))
            
            return int(response.one().id)
        
        except Exception as e:
            raise HTTPException(detail="Client id retrieval failed", status_code=500) from e
    
    @staticmethod
    @log_operation(True)
    async def translate_documentid_by_client_id(db_session: AsyncSession, documentid: int) -> int:
        """Translate to documentid by client id"""
        
        try:
            
            response = await db_session.exec(select(Client).where(Client.documentid == documentid))
            
            return int(response.one().id)
        
        except Exception as e:
            raise HTTPException(detail="Client id retrieval failed", status_code=500) from e
    