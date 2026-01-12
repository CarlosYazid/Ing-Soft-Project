from fastapi import HTTPException
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlmodel import select, func
from sqlalchemy.sql.expression import Select

from models import Order, OrderStatus
from utils import OrderUtils

class OrderService:
    
    @staticmethod
    def read_all_orders() -> Select:
        """Query for retrieve all orders."""
        return select(Order)
    
    @staticmethod
    async def search_orders_services_by_order(db_session: AsyncSession, order_id: int) -> Select:
        """Query for search order services associated with an order."""
        
        if not await OrderUtils.exist_order(db_session, order_id):
            raise HTTPException(detail="Order not found", status_code=404)
        
        return select(OrderService).where(OrderService.order_id == order_id)
    
    @staticmethod
    async def search_orders_services_by_service(db_session: AsyncSession, service_id: int) -> Select:
        """Query for search all order service for a specific service."""

        from utils import ServiceUtils

        # Ensure the service_id exists before retrieving orders
        if not await ServiceUtils.exist_service(db_session, service_id):
            raise HTTPException(detail="Service not found", status_code=404)

        return select(OrderService).where(OrderService.service_id == service_id)
    
    @staticmethod
    async def search_orders_products_by_order(db_session: AsyncSession, order_id: int) -> Select:
        """Query for search all order products associated with an order."""
        
        if not await OrderUtils.exist_order(db_session, order_id):
            raise HTTPException(detail="Order not found", status_code=404)
        
        return select(OrderProduct).where(OrderProduct.order_id == order_id)
    
    @staticmethod
    async def search_orders_products_by_product(db_session: AsyncSession, product_id: int) -> Select:
        """Query for search all orders products for a specific product."""
        
        from utils import ProductUtils
        
        # Ensure the product_id exists before retrieving orders
        if not await ProductUtils.exist_product(db_session, product_id):
            raise HTTPException(detail="Product not found", status_code=404)
        
        return select(OrderProduct).where(OrderProduct.product_id == product_id)
    
    @staticmethod
    def search_orders_by_status(status: OrderStatus) -> Select:
        """Query for retrieve orders by status."""
        return select(Order).where(Order.status == status)

    @staticmethod
    async def search_orders_by_client(db_session: AsyncSession, client_id: int) -> Select:
        """Query for retrieve all orders for a specific client."""
        
        from utils import UserUtils
        
        # Ensure the client_id exists before retrieving orders
        if not await UserUtils.exist_client(db_session, client_id):
            raise HTTPException(detail="Client not found", status_code=404)
        
        return select(Order).where(Order.client_id == client_id)
    
    @staticmethod
    async def update_inventory(db_session: AsyncSession, order_id: int) -> bool:
        """Update inventory after an order is placed"""

        if not await OrderUtils.exist_order(db_session, order_id):
            raise HTTPException(detail="Order not found", status_code=404)

        try:

            result = await db_session.exec(await OrderService.search_orders_products_by_order(db_session, order_id))
            order_products = result.all()

            if not order_products:
                return True

            totals = {
                op.product_id: op.quantity for op in order_products
            }
        
            for product_id, qty in totals.items():
                stmt = (
                    update(Product)
                    .where(Product.id == product_id)
                    .values(stock=func.greatest(Product.stock - qty, 0))
                )
                await db_session.exec(stmt)

            await db_session.commit()
            
            return True
        
        except Exception as e:
            raise HTTPException(detail="Failed updating inventory", status_code=500)