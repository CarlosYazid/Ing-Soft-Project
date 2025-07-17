from core import SETTINGS
from db import get_db_client
from models import OrderStatus

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
    async def exist_order_services_in_orders(cls, order_id : int) -> bool:
        """Check if at least one order service exists in a order"""
        client = await get_db_client()

        response = await client.table(SETTINGS.order_service_table).select("id").eq("order_id", order_id).execute()

        return bool(response.data)
    
    @classmethod
    async def exist_order_products_in_orders(cls, order_id : int) -> bool:
        """Check if at least one order service exists in a order"""
        client = await get_db_client()

        response = await client.table(SETTINGS.order_product_table).select("id").eq("order_id", order_id).execute()

        return bool(response.data)

    @classmethod
    async def order_product_in_order_completed(cls, order_product_id: int) -> bool:
        """Check if an order product exist in a order completed"""
        client = await get_db_client()

        response = await client.table(SETTINGS.order_product_table).select('order_id').eq("id", order_product_id).execute()

        if not bool(response.data):
            raise HTTPException(detail="No order found for this order product", status_code=404)
        
        from crud import OrderCrud

        return await OrderCrud.read_order_status(int(response.data[0]['order_id'])) is OrderStatus.COMPLETED

    @classmethod
    async def order_service_in_order_completed(cls, order_service_id: int) -> bool:
        """Check if an order service exist in a order completed"""
        client = await get_db_client()

        response = await client.table(SETTINGS.order_product_table).select('order_id').eq("id", order_service_id).execute()

        if not bool(response.data):
            raise HTTPException(detail="No order found for this order service", status_code=404)
        
        from crud import OrderCrud

        return await OrderCrud.read_order_status(int(response.data[0]['order_id'])) is OrderStatus.COMPLETED
    
    @classmethod
    async def exist_product_in_orders(cls, product_id: int) -> bool:
        """Check if a product is associated with any orders."""
        client = await get_db_client()

        response = await client.table(SETTINGS.order_product_table).select("id").eq("product_id", product_id).execute()

        return bool(response.data)