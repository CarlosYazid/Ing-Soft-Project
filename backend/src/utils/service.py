from fastapi import HTTPException
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlmodel import select

from models import Service, ServiceInput
from core import log_operation

class ServiceUtils:
    
    @staticmethod
    @log_operation(True)
    async def exist_service(db_session: AsyncSession, service_id: int) -> bool:
        """Check if a service exists by ID."""
        
        try:
            
            response = await db_session.exec(select(Service).where(Service.id == service_id))
            
            return bool(response.first())
        
        except Exception as e:
            raise HTTPException(detail="Service search failed", status_code=500) from e
    
    @staticmethod
    @log_operation(True)
    async def exist_service_input(db_session: AsyncSession, service_input: ServiceInput) -> bool:
        """Check if a service input exists by ID."""
        
        try:
            
            response = await db_session.exec(select(ServiceInput).where(ServiceInput.service_id == service_input.service_id).where(ServiceInput.product_id == service_input.product_id))

            return bool(response.first())
        
        except Exception as e:
            raise HTTPException(detail="Service input search failed", status_code=500) from e