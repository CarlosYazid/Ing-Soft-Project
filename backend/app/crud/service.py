from fastapi import HTTPException

from db import get_db_client
from models import Service, Product
from core import SETTINGS
from crud import ProductCrud

class ServiceCrud:
    @classmethod
    async def get_all_services(cls) -> list[Service]:
        """Retrieve all services."""
        
        client = await get_db_client()

        response = await client.table(SETTINGS.service_table).select("*").execute()

        if not(bool(response.data)):
            raise HTTPException(detail="No services found", status_code=404)

        return [Service.model_validate(service) for service in response.data]

    @classmethod
    async def get_service_by_id(cls, service_id: int) -> Service:
        """Retrieve a service by ID."""
        
        client = await get_db_client()

        response = await client.table(SETTINGS.service_table).select("*").eq("id", service_id).execute()

        if not(bool(response.data)):
            raise HTTPException(detail="Service not found", status_code=404)

        return Service.model_validate(response.data[0])
    
    @classmethod
    async def create_service(cls, service_data: Service) -> Service:
        """Create a new service."""
        
        client = await get_db_client()

        response = await client.table(SETTINGS.service_table).insert(service_data.model_dump()).execute()

        if not(bool(response.data)):
            raise HTTPException(detail="Failed to create service", status_code=500)

        return Service.model_validate(response.data[0])
    
    @classmethod
    async def update_service(cls, service_id: int, fields: dict) -> Service:
        """Update an existing service."""
        
        client = await get_db_client()

        response = await client.table(SETTINGS.service_table).update(fields).eq("id", service_id).execute()

        if not(bool(response.data)):
            raise HTTPException(detail="Failed to update service", status_code=500)

        return Service.model_validate(response.data[0])
    
    @classmethod
    async def delete_service(cls, service_id: int) -> bool:
        """Delete a service by ID."""
        
        client = await get_db_client()

        response = await client.table(SETTINGS.service_table).delete().eq("id", service_id).execute()

        if not(bool(response.data)):
            raise HTTPException(detail="Failed to delete service", status_code=500)

        return True
    
    
    @classmethod
    async def exist_service_by_id(cls, service_id: int) -> bool:
        """Check if a service exists by ID."""
        
        client = await get_db_client()

        response = await client.table(SETTINGS.service_table).select("id").eq("id", service_id).execute()

        return not(bool(response.data))
    
    @classmethod
    async def get_input_services_by_service(cls, service_id: int) -> list[Product]:
        """Retrieve all inputs for a specific service."""
        
        client = await get_db_client()

        response = await client.table(SETTINGS.service_inputs_table).select("service_id","product_id").eq("service_id", service_id).execute()

        if not(bool(response.data)):
            raise HTTPException(detail="No inputs found for this service", status_code=404)

        return [ProductCrud.get_product_by_id(service_input_id) for service_input_id in response.data[0].get("service_inputs", [])]