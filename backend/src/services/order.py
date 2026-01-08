from fastapi import HTTPException
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlmodel import select

from models import Order, OrderStatus
from utils import OrderUtils

class OrderService:
    
    @classmethod
    async def search_orders_by_status(cls, db_session: AsyncSession, status: OrderStatus) -> list[Order]:
        """Retrieve orders by status."""
        
        try:
            
            response = await db_session.exec(select(Order).where(Order.status == status))
            orders = list(response.all())
            
            if not orders:
                raise HTTPException(detail="No orders found with this status", status_code=404)
            
            return orders
        
        except Exception as e:
            raise HTTPException(detail="Order search by status failed", status_code=500) from e

    @classmethod
    async def search_orders_by_client(cls, db_session: AsyncSession, client_id: int) -> list[Order]:
        """Retrieve all orders for a specific client."""
        
        from utils import UserUtils
        
        # Ensure the client_id exists before retrieving orders
        if not await UserUtils.exist_client(db_session, client_id):
            raise HTTPException(detail="Client not found", status_code=404)
        
        try:

            response = await db_session.exec(select(Order).where(Order.client_id == client_id))
            orders = list(response.all())

            if not orders:
                raise HTTPException(detail="No orders found for this client", status_code=404)

            return orders
        
        except Exception as e:
            raise HTTPException(detail="Order search by client failed", status_code=500) from e
    
    @classmethod
    async def update_inventory(cls, db_session: AsyncSession, order_id: int) -> bool:
        """Update inventory after an order is placed."""
        
        from crud import OrderCrud, ProductCrud

        if (await OrderUtils.exist_order_products_in_order(db_session, order_id)):
            order_products = await OrderCrud.read_orders_products_by_order(db_session, order_id)
        else:
            order_products = []

        for order_product in order_products:
            await ProductCrud.update_stock(order_product.product_id, -order_product.quantity, False)
        
        return True
