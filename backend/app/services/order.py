from fastapi import HTTPException

from models import OrderBasePlusID, OrderStatus
from core import SETTINGS
from db import get_db_client
from utils import OrderUtils

class OrderService:
    
    FIELDS_ORDER_BASE = set(OrderBasePlusID.model_fields.keys())
    
    @classmethod
    async def search_orders_by_status(cls, status: OrderStatus) -> list[OrderBasePlusID]:
        """Retrieve orders by status."""
        
        client = await get_db_client()

        response = await client.table(SETTINGS.order_table).select(*cls.FIELDS_ORDER_BASE).eq("status", status.capitalize()).execute()

        if not bool(response.data):
            raise HTTPException(detail="No orders found with this status", status_code=404)

        return [OrderBasePlusID.model_validate(order) for order in response.data]

    @classmethod
    async def search_orders_by_client_id(cls, client_id: int) -> list[OrderBasePlusID]:
        """Retrieve all orders for a specific client."""
        
        from utils import UserUtils
        
        # Ensure the client_id exists before retrieving orders
        if not await UserUtils.exist_client(client_id):
            raise HTTPException(detail="Client not found", status_code=404)

        client = await get_db_client()

        response = await client.table(SETTINGS.order_table).select(*cls.FIELDS_ORDER_BASE).eq("client_id", client_id).execute()

        if not bool(response.data):
            raise HTTPException(detail="No orders found for this client", status_code=404)

        return [OrderBasePlusID.model_validate(order) for order in response.data]
    
    @classmethod
    async def update_inventory(cls, order_id: int) -> bool:
        """Update inventory after an order is placed."""
        
        from crud import OrderCrud, ProductCrud

        if (await OrderUtils.exist_order_products_in_orders(order_id)):
            order_products = await OrderCrud.read_orders_products_by_order_id(order_id)
        else:
            order_products = []

        for order_product in order_products:
            await ProductCrud.update_stock(order_product.product_id, -order_product.quantity, False)
        
        return True
