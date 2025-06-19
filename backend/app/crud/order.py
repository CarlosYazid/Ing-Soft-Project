from fastapi import HTTPException

from db import get_db_client
from models import Order, OrderStatus, OrderService, OrderProduct
from core import SETTINGS

class OrderCrud:
    @classmethod
    async def create_order(cls, order: Order) -> Order:
        """Create a new order."""
        client = await get_db_client()

        response = await client.table(SETTINGS.order_table).insert(order.model_dump()).execute()

        if response.data is None or len(response.data) == 0:
            raise HTTPException(detail="Failed to create order", status_code=500)

        return Order.model_validate(response.data[0])

    @classmethod
    async def get_order_by_id(cls, order_id: int) -> Order:
        """Retrieve an order by ID."""
        client = await get_db_client()

        response = await client.table(SETTINGS.order_table).select("*").eq("id", order_id).execute()

        if response.data is None or len(response.data) == 0:
            raise HTTPException(detail="Order not found", status_code=404)

        return Order.model_validate(response.data[0])
    
    @classmethod
    async def update_order(cls, order_id: int, fields: dict) -> Order:
        """Update an existing order."""
        client = await get_db_client()

        response = await client.table(SETTINGS.order_table).update(fields).eq("id", order_id).execute()

        if response.data is None or len(response.data) == 0:
            raise HTTPException(detail="Failed to update order", status_code=500)

        return Order.model_validate(response.data[0])
    
    @classmethod
    async def delete_order(cls, order_id: int) -> None:
        """Delete an order by ID."""
        client = await get_db_client()

        response = await client.table(SETTINGS.order_table).delete().eq("id", order_id).execute()

        if response.data is None or len(response.data) == 0:
            raise HTTPException(detail="Failed to delete order", status_code=500)
        
    @classmethod
    async def get_orders_by_status(cls, status: OrderStatus) -> list[Order]:
        """Retrieve orders by status."""
        client = await get_db_client()

        response = await client.table(SETTINGS.order_table).select("*").eq("status", status).execute()

        if response.data is None or len(response.data) == 0:
            raise HTTPException(detail="No orders found with this status", status_code=404)

        return [Order.model_validate(order) for order in response.data]
    
    @classmethod
    async def add_service_to_order(cls, order_service: OrderService) -> OrderService:
        """Add a service to an order."""
        client = await get_db_client()

        response = await client.table(SETTINGS.order_service_table).insert(order_service.model_dump()).execute()

        if response.data is None or len(response.data) == 0:
            raise HTTPException(detail="Failed to add service to order", status_code=500)

        return OrderService.model_validate(response.data[0])
    
    @classmethod
    async def add_product_to_order(cls, order_product: OrderProduct) -> OrderProduct:
        """Add a product to an order."""
        client = await get_db_client()

        response = await client.table(SETTINGS.order_product_table).insert(order_product.model_dump()).execute()

        if response.data is None or len(response.data) == 0:
            raise HTTPException(detail="Failed to add product to order", status_code=500)

        return OrderProduct.model_validate(response.data[0])
    
    @classmethod
    async def get_order_services(cls, order_id: int) -> list[OrderService]:
        """Retrieve services associated with an order."""
        client = await get_db_client()

        response = await client.table(SETTINGS.order_service_table).select("*").eq("order_id", order_id).execute()

        if response.data is None or len(response.data) == 0:
            raise HTTPException(detail="No services found for this order", status_code=404)

        return [OrderService.model_validate(service) for service in response.data]
    
    @classmethod
    async def get_order_products(cls, order_id: int) -> list[OrderProduct]:
        """Retrieve products associated with an order."""
        client = await get_db_client()

        response = await client.table(SETTINGS.order_product_table).select("*").eq("order_id", order_id).execute()

        if response.data is None or len(response.data) == 0:
            raise HTTPException(detail="No products found for this order", status_code=404)

        return [OrderProduct.model_validate(product) for product in response.data]
    
    @classmethod
    async def update_order_service(cls, order_service_id: int, fields: dict) -> OrderService:
        """Update an existing order service."""
        client = await get_db_client()

        response = await client.table(SETTINGS.order_service_table).update(fields).eq("id", order_service_id).execute()

        if response.data is None or len(response.data) == 0:
            raise HTTPException(detail="Failed to update order service", status_code=500)

        return OrderService.model_validate(response.data[0])
    
    @classmethod
    async def update_order_product(cls, order_product_id: int, fields: dict) -> OrderProduct:
        """Update an existing order product."""
        client = await get_db_client()

        response = await client.table(SETTINGS.order_product_table).update(fields).eq("id", order_product_id).execute()

        if response.data is None or len(response.data) == 0:
            raise HTTPException(detail="Failed to update order product", status_code=500)

        return OrderProduct.model_validate(response.data[0])
    
    @classmethod
    async def delete_order_service(cls, order_service_id: int) -> None:
        """Delete an order service by ID."""
        client = await get_db_client()

        response = await client.table(SETTINGS.order_service_table).delete().eq("id", order_service_id).execute()

        if response.data is None or len(response.data) == 0:
            raise HTTPException(detail="Failed to delete order service", status_code=500)

    @classmethod
    async def delete_order_product(cls, order_product_id: int) -> None:
        """Delete an order product by ID."""
        client = await get_db_client()

        response = await client.table(SETTINGS.order_product_table).delete().eq("id", order_product_id).execute()

        if response.data is None or len(response.data) == 0:
            raise HTTPException(detail="Failed to delete order product", status_code=500)