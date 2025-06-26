from fastapi import HTTPException

from db import get_db_client
from models import Service, ServiceCreate, ServiceInput, ServiceInputCreate, Product
from core import SETTINGS

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
    async def create_service(cls, service_data: ServiceCreate) -> Service:
        """Create a new service."""

        client = await get_db_client()

        response = await client.table(SETTINGS.service_table).insert(service_data.model_dump(mode="json")).execute()

        if not(bool(response.data)):
            raise HTTPException(detail="Failed to create service", status_code=500)

        return Service.model_validate(response.data[0])

    @classmethod
    async def update_service(cls, service_id: int, fields: dict) -> Service:
        """Update an existing service."""

        client = await get_db_client()

        # check if service exists
        if not await cls.exist_service_by_id(service_id):
            raise HTTPException(detail="Service not found", status_code=404)
        
        if not(set(fields.keys()) < set(ServiceCreate.__fields__.keys())):
            raise HTTPException(detail="Update attribute of service", status_code=400)

        response = await client.table(SETTINGS.service_table).update(fields).eq("id", service_id).execute()

        if not(bool(response.data)):
            raise HTTPException(detail="Failed to update service", status_code=500)

        return Service.model_validate(response.data[0])

    @classmethod
    async def delete_service(cls, service_id: int) -> bool:
        """Delete a service by ID."""

        client = await get_db_client()

        # check if service exists
        if not await cls.exist_service_by_id(service_id):
            raise HTTPException(detail="Service not found", status_code=404)

        response = await client.table(SETTINGS.service_table).delete().eq("id", service_id).execute()

        if not(bool(response.data)):
            raise HTTPException(detail="Failed to delete service", status_code=500)

        return True


    @classmethod
    async def exist_service_by_id(cls, service_id: int) -> bool:
        """Check if a service exists by ID."""

        client = await get_db_client()

        response = await client.table(SETTINGS.service_table).select("id").eq("id", service_id).execute()


        return bool(response.data)

    @classmethod
    async def get_input_services_by_service(cls, service_id: int) -> list[Product]:
        """Retrieve all inputs for a specific service."""

        client = await get_db_client()

        response = await client.table(SETTINGS.service_inputs_table).select("service_id","product_id").eq("service_id", service_id).execute()

        if not(bool(response.data)):
            raise HTTPException(detail="No inputs found for this service", status_code=404)

        # Import ProductCrud directly from its file path
        from crud.product import ProductCrud

        return [await ProductCrud.get_product_by_id(item["product_id"]) for item in response.data]

    @classmethod
    async def create_service_input(cls, service_input_data: ServiceInputCreate) -> ServiceInput:
        """Create a new service input."""

        client = await get_db_client()

        response = await client.table(SETTINGS.service_inputs_table).insert(service_input_data.model_dump()).execute()

        if not(bool(response.data)):
            raise HTTPException(detail="Failed to create service input", status_code=500)

        return ServiceInput.model_validate(response.data[0])

    @classmethod
    async def update_service_input(cls, service_id: int, product_id: int, fields: dict) -> ServiceInput:
        """Update an existing service input."""

        client = await get_db_client()

        # check if service input exists
        if not await cls.exist_service_input_by_service_id_and_product_id(service_id, product_id):
            raise HTTPException(detail="Service input not found", status_code=404)
        
        if not(set(fields.keys()) < set(ServiceInputCreate.__fields__.keys())):
            raise HTTPException(detail="Update attribute of input service", status_code=400)

        response = await client.table(SETTINGS.service_inputs_table).update(fields).eq("service_id", service_id).eq("product_id", product_id).execute()

        if not(bool(response.data)):
            raise HTTPException(detail="Failed to update service input", status_code=500)

        return ServiceInput.model_validate(response.data[0])

    @classmethod
    async def get_service_input_by_id(cls, service_input_id: int) -> ServiceInput:
        """Retrieve a service input by ID."""

        client = await get_db_client()

        response = await client.table(SETTINGS.service_inputs_table).select("*").eq("id", service_input_id).execute()

        if not(bool(response.data)):
            raise HTTPException(detail="Service input not found", status_code=404)

        return ServiceInput.model_validate(response.data[0])

    @classmethod
    async def update_service_input_by_id(cls, service_input_id: int, fields: dict) -> ServiceInput:
        """Update a service input by ID."""

        client = await get_db_client()

        # check if service input exists
        if not await cls.exist_service_input_by_id(service_input_id):
            raise HTTPException(detail="Service input not found", status_code=404)
        
        if not(set(fields.keys()) < set(ServiceInputCreate.__fields__.keys())):
            raise HTTPException(detail="Update attribute of input service", status_code=400)

        response = await client.table(SETTINGS.service_inputs_table).update(fields).eq("id", service_input_id).execute()

        if not(bool(response.data)):
            raise HTTPException(detail="Failed to update service input", status_code=500)

        return ServiceInput.model_validate(response.data[0])

    @classmethod
    async def get_service_input_by_service_id_and_product_id(cls, service_id: int, product_id : int) -> ServiceInput:
        """Retrieve a service input by service ID and product ID."""

        client = await get_db_client()

        response = await client.table(SETTINGS.service_inputs_table).select("*").eq("service_id", service_id).eq("product_id", product_id).execute()

        if not(bool(response.data)):
            raise HTTPException(detail="Service input not found", status_code=404)

        return ServiceInput.model_validate(response.data[0])

    @classmethod
    async def delete_service_input_by_service_id_and_product_id(cls, service_id: int, product_id: int) -> bool:
        """Delete a service input by service ID and product ID."""

        client = await get_db_client()

        # check if service input exists
        if not await cls.exist_service_input_by_service_id_and_product_id(service_id, product_id):
            raise HTTPException(detail="Service input not found", status_code=404)

        response = await client.table(SETTINGS.service_inputs_table).delete().eq("service_id", service_id).eq("product_id", product_id).execute()

        if not(bool(response.data)):
            raise HTTPException(detail="Failed to delete service input", status_code=500)

        return True

    @classmethod
    async def delete_service_input_by_id(cls, service_input_id: int) -> bool:
        """Delete a service input by ID."""

        client = await get_db_client()

        # check if service input exists
        if not await cls.exist_service_input_by_id(service_input_id):
            raise HTTPException(detail="Service input not found", status_code=404)

        response = await client.table(SETTINGS.service_inputs_table).delete().eq("id", service_input_id).execute()

        if not(bool(response.data)):
            raise HTTPException(detail="Failed to delete service input", status_code=500)

        return True

    @classmethod
    async def exist_service_input_by_service_id_and_product_id(cls, service_id: int, product_id: int) -> bool:
        """Check if a service input exists by service ID and product ID."""

        client = await get_db_client()
        
        print(service_id, product_id)

        response = await client.table(SETTINGS.service_inputs_table).select("*").eq("service_id", service_id).eq("product_id", product_id).execute()

        print(response.data)

        return bool(response.data)

    @classmethod
    async def exist_service_input_by_id(cls, service_input_id: int) -> bool:
        """Check if a service input exists by ID."""

        client = await get_db_client()

        response = await client.table(SETTINGS.service_inputs_table).select("id").eq("id", service_input_id).execute()


        return bool(response.data)
