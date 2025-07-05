from fastapi import HTTPException

from models import ServiceBasePlusID
from core import SETTINGS
from db import get_db_client

class ServiceService:
    
    @classmethod
    async def search_services_by_name(cls, name: str) -> list[ServiceBasePlusID]:
        """Search services by name."""

        client = await get_db_client()

        response = await client.table(SETTINGS.service_table).select("id", "name", "short_description", "price").ilike("name", f"%{name}%").execute()

        if not bool(response.data):
            raise HTTPException(detail="No services found with this name", status_code=404)

        return [ServiceBasePlusID.model_validate(service) for service in response.data]

    @classmethod
    async def search_services_by_price_range(cls, min_price: float, max_price: float) -> list[ServiceBasePlusID]:
        """Search services by price range."""

        client = await get_db_client()

        response = await client.table(SETTINGS.service_table).select("id", "name", "short_description", "price").gte("price", min_price).lte("price", max_price).execute()

        if not bool(response.data):
            raise HTTPException(detail="No services found in this price range", status_code=404)

        return [ServiceBasePlusID.model_validate(service) for service in response.data]
    
    @classmethod
    async def search_services_by_cost_range(cls, min_cost: float, max_cost: float) -> list[ServiceBasePlusID]:
        """Search services by cost range."""

        client = await get_db_client()

        response = await client.table(SETTINGS.service_table).select("id", "name", "short_description", "price").gte("cost", min_cost).lte("cost", max_cost).execute()

        if not bool(response.data):
            raise HTTPException(detail="No services found in this cost range", status_code=404)

        return [ServiceBasePlusID.model_validate(service) for service in response.data]