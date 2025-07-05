from fastapi import HTTPException

from db import get_db_client
from core import SETTINGS

class ServiceUtils:
    
    @classmethod
    async def exist_service(cls, service_id: int) -> bool:
        """Check if a service exists by ID."""

        client = await get_db_client()

        response = await client.table(SETTINGS.service_table).select("id").eq("id", service_id).execute()

        return bool(response.data)
    
    @classmethod
    async def exist_service_input(cls, service_input_id: int) -> bool:
        """Check if a service input exists by ID."""

        client = await get_db_client()

        response = await client.table(SETTINGS.service_inputs_table).select("id").eq("id", service_input_id).execute()

        return bool(response.data)

    @classmethod
    async def exist_service_input_by_service_id_and_product_id(cls, service_id: int, product_id: int) -> bool:
        """Check if a service input exists by service ID and product ID."""
        
        if not await cls.exist_service(service_id):
            raise HTTPException(detail="Service not found", status_code=404)
        
        from .product import ProductUtils

        if not await ProductUtils.exist_product(product_id):
            raise HTTPException(detail="Product not found", status_code=404)
        
        client = await get_db_client()

        response = await client.table(SETTINGS.service_inputs_table).select("*").eq("service_id", service_id).eq("product_id", product_id).execute()

        return bool(response.data)