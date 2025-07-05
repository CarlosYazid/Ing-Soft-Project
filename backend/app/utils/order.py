from core import SETTINGS
from db import get_db_client


class OrderUtils:

    @classmethod
    async def exist_order(cls, order_id: int) -> bool:
        """Check if an order exists by ID."""
        client = await get_db_client()

        response = await client.table(SETTINGS.order_table).select("id").eq("id", order_id).execute()

        return bool(response.data)
    
    @classmethod
    async def exist_orders_by_employee_id(cls, employee_id: int) -> bool:
        """Check if any orders exist for a specific employee."""
        client = await get_db_client()

        response = await client.table(SETTINGS.order_table).select("id").eq("employee_id", employee_id).execute()

        return bool(response.data)
    
    @classmethod
    async def exist_order_by_client_id(cls, client_id: int) -> bool:
        """Check if any orders exist for a specific client."""
        client = await get_db_client()

        response = await client.table(SETTINGS.order_table).select("id").eq("client_id", client_id).execute()

        return bool(response.data)

    @classmethod
    async def exist_order_service(cls, order_service_id: int) -> bool:
        """Check if an order service exists by ID."""
        client = await get_db_client()

        response = await client.table(SETTINGS.order_service_table).select("id").eq("id", order_service_id).execute()

        return bool(response.data)
    
    @classmethod
    async def exist_service_in_orders(cls, service_id: int) -> bool:
        """Check if a service is associated with any orders."""
        client = await get_db_client()

        response = await client.table(SETTINGS.order_service_table).select("id").eq("service_id", service_id).execute()

        return bool(response.data)

    @classmethod
    async def exist_order_product(cls, order_product_id: int) -> bool:
        """Check if an order product exists by ID."""
        client = await get_db_client()

        response = await client.table(SETTINGS.order_product_table).select("id").eq("id", order_product_id).execute()

        return bool(response.data)
    
    @classmethod
    async def exist_product_in_orders(cls, product_id: int) -> bool:
        """Check if a product is associated with any orders."""
        client = await get_db_client()

        response = await client.table(SETTINGS.order_product_table).select("id").eq("product_id", product_id).execute()

        return bool(response.data)