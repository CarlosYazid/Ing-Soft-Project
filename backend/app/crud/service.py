from fastapi import HTTPException

from db import get_db_client
from models import Service, ServiceCreate, ServiceInput, ServiceInputCreate, ServiceBasePlusID, ProductBasePlusID
from core import SETTINGS
from utils import ServiceUtils

class ServiceCrud:
    
    EXCLUDED_FIELDS_FOR_UPDATE = {"created_at"}
    ALLOWED_FIELDS_FOR_UPDATE = set(ServiceCreate.model_fields.keys()) - EXCLUDED_FIELDS_FOR_UPDATE
    EXCLUDED_FIELDS_FOR_UPDATE_INPUT = {"service_id"}
    ALLOWED_FIELDS_FOR_UPDATE_INPUT = set(ServiceInputCreate.model_fields.keys()) - EXCLUDED_FIELDS_FOR_UPDATE_INPUT

    FIELDS_SERVICE_BASE = set(ServiceBasePlusID.model_fields.keys())

    @classmethod
    async def create_service(cls, service: ServiceCreate) -> Service:
        """Create a new service."""

        client = await get_db_client()

        response = await client.table(SETTINGS.service_table).insert(service.model_dump(mode="json")).execute()

        if not bool(response.data):
            raise HTTPException(detail="Failed to create service", status_code=500)

        return Service.model_validate(response.data[0])
    
    @classmethod
    async def read_all_services(cls) -> list[Service]:
        """Retrieve all services."""

        client = await get_db_client()

        response = await client.table(SETTINGS.service_table).select("*").execute()

        if not bool(response.data):
            raise HTTPException(detail="No services found", status_code=404)

        return [Service.model_validate(service) for service in response.data]
    
    @classmethod
    async def read_all_services_base(cls) -> list[ServiceBasePlusID]:
        """Retrieve all services."""
        
        client = await get_db_client()

        response = await client.table(SETTINGS.service_table).select(*cls.FIELDS_SERVICE_BASE).execute()

        if not bool(response.data):
            raise HTTPException(detail="No services found", status_code=404)

        return [ServiceBasePlusID.model_validate(service) for service in response.data]
        
    @classmethod
    async def read_service(cls, service_id: int) -> Service:
        """Retrieve a service by ID."""

        client = await get_db_client()

        response = await client.table(SETTINGS.service_table).select("*").eq("id", service_id).execute()

        if not bool(response.data):
            raise HTTPException(detail="Service not found", status_code=404)

        return Service.model_validate(response.data[0])

    @classmethod
    async def read_service_base(cls, service_id: int) -> ServiceBasePlusID:
        """Retrieve a service by ID."""
        client = await get_db_client()

        response = await client.table(SETTINGS.service_table).select(*cls.FIELDS_SERVICE_BASE).eq("id", service_id).execute()

        if not bool(response.data):
            raise HTTPException(detail="Service not found", status_code=404)

        return ServiceBasePlusID.model_validate(response.data[0])

    @classmethod
    async def update_service(cls, service_id: int, fields: dict) -> Service:
        """Update an existing service."""
        
        # check if service exists
        if not await ServiceUtils.exist_service(service_id):
            raise HTTPException(detail="Service not found", status_code=404)
        
        if any(field in fields for field in cls.EXCLUDED_FIELDS_FOR_UPDATE):
            raise HTTPException(detail="Cannot update fields: " + ", ".join(cls.EXCLUDED_FIELDS_FOR_UPDATE), status_code=400)
        
        if not(set(fields.keys()) <= cls.ALLOWED_FIELDS_FOR_UPDATE):
            raise HTTPException(detail="Update attribute of service", status_code=400)

        client = await get_db_client()

        response = await client.table(SETTINGS.service_table).update(fields).eq("id", service_id).execute()

        if not bool(response.data):
            raise HTTPException(detail="Failed to update service", status_code=500)

        return Service.model_validate(response.data[0])

    @classmethod
    async def delete_service(cls, service_id: int) -> bool:
        """Delete a service by ID."""

        # check if service exists
        if not await ServiceUtils.exist_service(service_id):
            raise HTTPException(detail="Service not found", status_code=404)

        from utils import OrderUtils

        # Check if the service is associated with any orders
        if await OrderUtils.exist_service_in_orders(service_id):
            raise HTTPException(detail="Cannot delete service with active orders", status_code=400)

        #input_services = await cls.read_services_inputs_by_service(service_id)

        # Delete all inputs associated with the service
        #for input_service in input_services:
        #    await cls.delete_service_input(input_service.id)

        client = await get_db_client()

        response = await client.table(SETTINGS.service_table).delete().eq("id", service_id).execute()

        if not(bool(response.data)):
            raise HTTPException(detail="Failed to delete service", status_code=500)

        return True

    @classmethod
    async def create_service_input(cls, service_input: ServiceInputCreate) -> ServiceInput:
        """Create a new service input."""

        client = await get_db_client()

        response = await client.table(SETTINGS.service_inputs_table).insert(service_input.model_dump()).execute()

        if not bool(response.data):
            raise HTTPException(detail="Failed to create service input", status_code=500)

        return ServiceInput.model_validate(response.data[0])

    @classmethod
    async def read_service_input(cls, service_input_id: int) -> ServiceInput:
        """Retrieve a service input by ID."""

        client = await get_db_client()

        response = await client.table(SETTINGS.service_inputs_table).select("*").eq("id", service_input_id).execute()

        if not bool(response.data):
            raise HTTPException(detail="Service input not found", status_code=404)

        return ServiceInput.model_validate(response.data[0])
    
    @classmethod
    async def read_service_input_by_service_id_and_product_id(cls, service_id: int, product_id : int) -> ServiceInput:
        """Retrieve a service input by service ID and product ID."""

        client = await get_db_client()

        response = await client.table(SETTINGS.service_inputs_table).select("*").eq("service_id", service_id).eq("product_id", product_id).execute()

        if not(bool(response.data)):
            raise HTTPException(detail="Service input not found", status_code=404)

        return ServiceInput.model_validate(response.data[0])
    
    @classmethod
    async def read_services_inputs_by_product(cls, product_id: int) -> list[ServiceInput]:
        """Retrieve all service inputs for a specific product ID."""
        
        # check if product exists
        from utils import ProductUtils

        if not await ProductUtils.exist_product(product_id):
            raise HTTPException(detail="Product not found", status_code=404)

        client = await get_db_client()

        response = await client.table(SETTINGS.service_inputs_table).select("*").eq("product_id", product_id).execute()

        if not bool(response.data):
            raise HTTPException(detail="No service inputs found for this product", status_code=404)

        return [ServiceInput.model_validate(service_input) for service_input in response.data]

    @classmethod
    async def read_services_inputs_by_service(cls, service_id: int) -> list[ServiceInput]:
        """Retrieve all service inputs for a specific service ID."""

        if not await ServiceUtils.exist_service(service_id):
            raise HTTPException(detail="Service not found", status_code=404)

        client = await get_db_client()

        response = await client.table(SETTINGS.service_inputs_table).select("*").eq("service_id", service_id).execute()

        if not bool(response.data):
            raise HTTPException(detail="No service inputs found for this service", status_code=404)

        return [ServiceInput.model_validate(service_input) for service_input in response.data]
    
    @classmethod
    async def read_services_inputs_ids_by_service(cls, service_id: int) -> list[int]:
        """Retrieve all service input IDs for a specific service ID."""

        if not await ServiceUtils.exist_service(service_id):
            raise HTTPException(detail="Service not found", status_code=404)

        client = await get_db_client()

        response = await client.table(SETTINGS.service_inputs_table).select("id").eq("service_id", service_id).execute()

        if not bool(response.data):
            raise HTTPException(detail="No service inputs found for this service", status_code=404)

        return [int(item["id"]) for item in response.data]
    

    @classmethod
    async def update_service_input(cls, service_input_id: int, fields: dict) -> ServiceInput:
        """Update a service input by ID."""

        # check if service input exists
        if not await ServiceUtils.exist_service_input(service_input_id):
            raise HTTPException(detail="Service input not found", status_code=404)
        
        if any(field in fields for field in cls.EXCLUDED_FIELDS_FOR_UPDATE_INPUT):
            raise HTTPException(detail="Cannot update fields: " + ", ".join(cls.EXCLUDED_FIELDS_FOR_UPDATE_INPUT), status_code=400)

        if not(set(fields.keys()) <= cls.ALLOWED_FIELDS_FOR_UPDATE_INPUT):
            raise HTTPException(detail="Update attribute of input service", status_code=400)

        client = await get_db_client()

        response = await client.table(SETTINGS.service_inputs_table).update(fields).eq("id", service_input_id).execute()

        if not bool(response.data):
            raise HTTPException(detail="Failed to update service input", status_code=500)

        return ServiceInput.model_validate(response.data[0])


    @classmethod
    async def update_service_input_by_service_id_and_product_id(cls, service_id: int, product_id: int, fields: dict) -> ServiceInput:
        """Update an existing service input."""

        # check if service input exists
        if not await ServiceUtils.exist_service_input_by_service_id_and_product_id(service_id, product_id):
            raise HTTPException(detail="Service input not found", status_code=404)
        
        if any(field in fields for field in cls.EXCLUDED_FIELDS_FOR_UPDATE_INPUT):
            raise HTTPException(detail="Cannot update fields: " + ", ".join(cls.EXCLUDED_FIELDS_FOR_UPDATE_INPUT), status_code=400)

        if not(set(fields.keys()) <= cls.ALLOWED_FIELDS_FOR_UPDATE_INPUT):
            raise HTTPException(detail="Update attribute of input service", status_code=400)

        client = await get_db_client()

        response = await client.table(SETTINGS.service_inputs_table).update(fields).eq("service_id", service_id).eq("product_id", product_id).execute()

        if not bool(response.data):
            raise HTTPException(detail="Failed to update service input", status_code=500)

        return ServiceInput.model_validate(response.data[0])

    @classmethod
    async def delete_service_input(cls, service_input_id: int) -> bool:
        """Delete a service input by ID."""
        
        # check if service input exists
        if not await ServiceUtils.exist_service_input(service_input_id):
            raise HTTPException(detail="Service input not found", status_code=404)

        client = await get_db_client()

        response = await client.table(SETTINGS.service_inputs_table).delete().eq("id", service_input_id).execute()

        if not bool(response.data):
            raise HTTPException(detail="Failed to delete service input", status_code=500)

        return bool(response.data)

    @classmethod
    async def delete_service_input_by_service_id_and_product_id(cls, service_id: int, product_id: int) -> bool:
        """Delete a service input by service ID and product ID."""
        
        # check if service input exists
        if not await ServiceUtils.exist_service_input_by_service_id_and_product_id(service_id, product_id):
            raise HTTPException(detail="Service input not found", status_code=404)

        client = await get_db_client()

        response = await client.table(SETTINGS.service_inputs_table).delete().eq("service_id", service_id).eq("product_id", product_id).execute()

        if not bool(response.data):
            raise HTTPException(detail="Failed to delete service input", status_code=500)

        return bool(response.data)

    @classmethod
    async def read_products_by_service(cls, service_id: int) -> list[ProductBasePlusID]:
        """Retrieve all products for a specific service."""

        if not await ServiceUtils.exist_service(service_id):
            raise HTTPException(detail="Service not found", status_code=404)

        client = await get_db_client()

        response = await client.table(SETTINGS.service_inputs_table).select("product_id").eq("service_id", service_id).execute()

        if not bool(response.data):
            raise HTTPException(detail="No inputs found for this service", status_code=404)

        # Import ProductCrud directly from its file path
        from crud import ProductCrud

        return [await ProductCrud.read_product_base(int(item["product_id"])) for item in response.data]
