from fastapi import HTTPException
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlmodel import select
from sqlalchemy.sql.expression import Select

from models import Service

class ServiceService:
    
    @staticmethod
    def read_all_services() -> Select:
        """Query for retrieve all services."""
        return select(Service)
    
    @staticmethod
    def search_services_by_name(name: str) -> Select:
        """Query for search services by name."""
        return select(Service).where(Service.name.ilike(f"%{name}%"))

    @staticmethod
    def search_services_by_price_range(min_price: float, max_price: float) -> Select:
        """Query for search services by price range."""
        return select(Service).where(Service.price >= min_price).where(Service.price <= max_price)
    
    @staticmethod
    def search_services_by_cost_range(min_cost: float, max_cost: float) -> Select:
        """Query for search services by cost range."""
        return select(Service).where(Service.cost >= min_cost).where(Service.cost <= max_cost)
    
    @staticmethod
    async def search_service_inputs_by_product(db_session: AsyncSession, product_id: int) -> Select:
        """Query for search all service inputs for a specific product ID."""
        
        # check if product exists
        from utils import ProductUtils

        if not await ProductUtils.exist_product(db_session, product_id):
            raise HTTPException(detail="Product not found", status_code=404)

        return select(ServiceInput).where(ServiceInput.product_id == product_id)
    
    @staticmethod
    async def search_service_inputs_by_service(db_session: AsyncSession, service_id: int) -> Select:
        """Query for search all service inputs for a specific service ID."""

        if not await ServiceUtils.exist_service(db_session, service_id):
            raise HTTPException(detail="Service not found", status_code=404)

        return select(ServiceInput).where(ServiceInput.service_id == service_id)