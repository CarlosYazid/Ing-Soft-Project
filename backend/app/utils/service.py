from fastapi import HTTPException
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlmodel import select

from models import Service, ServiceInput

class ServiceUtils:
    
    @classmethod
    async def exist_service(cls, db_session: AsyncSession, service_id: int) -> bool:
        """Check if a service exists by ID."""
        
        try:
            
            response = await db_session.exec(select(Service).where(Service.id == service_id))
            
            return bool(response.first())
        
        except Exception as e:
            raise HTTPException(detail="Service search failed", status_code=500) from e
    
    @classmethod
    async def exist_service_input(cls, db_session: AsyncSession, service_input: ServiceInput) -> bool:
        """Check if a service input exists by ID."""
        
        try:
            
            response = await db_session.exec(select(ServiceInput).where(ServiceInput.service_id == service_input.service_id).where(ServiceInput.product_id == service_input.product_id))

            return bool(response.first())
        
        except Exception as e:
            raise HTTPException(detail="Service input search failed", status_code=500) from e