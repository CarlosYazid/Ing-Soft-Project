from fastapi import HTTPException

from models import ServiceBasePlusID
from core import SETTINGS
from db import get_db_client

class ServiceService:
    
    FIELDS_SERVICE_BASE = set(ServiceBasePlusID.__fields__.keys())
    
    @classmethod
    async def search_services_by_name(cls, name: str) -> list[ServiceBasePlusID]:
        """Search services by name."""

        client = await get_db_client()

        response = await client.table(SETTINGS.service_table).select(*cls.FIELDS_SERVICE_BASE).ilike("name", f"%{name}%").execute()

        if not bool(response.data):
            raise HTTPException(detail="No services found with this name", status_code=404)

        return [ServiceBasePlusID.model_validate(service) for service in response.data]

    @classmethod
    async def search_services_by_price_range(cls, min_price: float, max_price: float) -> list[ServiceBasePlusID]:
        """Search services by price range."""

        client = await get_db_client()

        response = await client.table(SETTINGS.service_table).select(*cls.FIELDS_SERVICE_BASE).gte("price", min_price).lte("price", max_price).execute()

        if not bool(response.data):
            raise HTTPException(detail="No services found in this price range", status_code=404)

        return [ServiceBasePlusID.model_validate(service) for service in response.data]
    
    @classmethod
    async def search_services_by_cost_range(cls, min_cost: float, max_cost: float) -> list[ServiceBasePlusID]:
        """Search services by cost range."""

        client = await get_db_client()

        response = await client.table(SETTINGS.service_table).select(*cls.FIELDS_SERVICE_BASE).gte("cost", min_cost).lte("cost", max_cost).execute()

        if not bool(response.data):
            raise HTTPException(detail="No services found in this cost range", status_code=404)

        return [ServiceBasePlusID.model_validate(service) for service in response.data]