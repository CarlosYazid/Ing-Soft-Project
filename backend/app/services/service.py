from fastapi import HTTPException
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlmodel import select

from models import Service

class ServiceService:
    
    @classmethod
    async def search_services_by_name(cls, db_session: AsyncSession, name: str) -> list[Service]:
        """Search services by name."""
        
        try:
            
            result = await db_session.exec(select(Service).where(Service.name.ilike(f"%{name}%")))
            services = list(result.all())
            
            if not services:
                raise HTTPException(detail="No services found with the given name", status_code=404)
            
            return services
        
        except Exception as e:
            raise HTTPException(status_code=500, detail="Service search failed") from e

    @classmethod
    async def search_services_by_price_range(cls, db_session: AsyncSession, min_price: float, max_price: float) -> list[Service]:
        """Search services by price range."""
        
        try:
            
            result = await db_session.exec(select(Service).where(Service.price >= min_price).where(Service.price <= max_price))
            services = list(result.all())
            
            if not services:
                raise HTTPException(detail="No services found in this price range", status_code=404)
            
            return services
        
        except Exception as e:
            raise HTTPException(status_code=500, detail="Service search failed") from e
    
    @classmethod
    async def search_services_by_cost_range(cls, db_session: AsyncSession, min_cost: float, max_cost: float) -> list[Service]:
        """Search services by cost range."""
        
        try:

            result = await db_session.exec(select(Service).where(Service.cost >= min_cost).where(Service.cost <= max_cost))
            services = list(result.all())

            if not services:
                raise HTTPException(detail="No services found in this cost range", status_code=404)

            return services

        except Exception as e:
            raise HTTPException(status_code=500, detail="Service search failed") from e