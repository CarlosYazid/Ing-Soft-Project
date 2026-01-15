from sqlmodel.ext.asyncio.session import AsyncSession
from sqlmodel import select
from fastapi import HTTPException

from models import OrderStatus, Order, OrderService, OrderProduct
from core import log_operation

class OrderUtils:

    @staticmethod
    @log_operation(True)
    async def exist_order(db_session: AsyncSession, order_id: int) -> bool:
        """Check if an order exists by ID."""
        
        try:
            
            response = await db_session.exec(select(Order).where(Order.id == order_id))
            
            return bool(response.first())
        
        except Exception as e:
            raise HTTPException(detail="Order existence check failed", status_code=500) from e
    
    @staticmethod
    @log_operation(True)
    async def exist_orders_by_employee(db_session: AsyncSession, employee_id: int) -> bool:
        """Check if any orders exist for a specific employee."""
        
        try:

            response = await db_session.exec(select(Order).where(Order.employee_id == employee_id))

            return bool(response.first())
        
        except Exception as e:
            raise HTTPException(detail="Order existence check failed", status_code=500) from e
    
    @staticmethod
    @log_operation(True)
    async def exist_order_by_client(db_session: AsyncSession, client_id: int) -> bool:
        """Check if any orders exist for a specific client."""
        
        try:

            response = await db_session.exec(select(Order).where(Order.client_id == client_id))

            return bool(response.first())
        
        except Exception as e:
            raise HTTPException(detail="Order existence check failed", status_code=500) from e

    @staticmethod
    @log_operation(True)
    async def exist_order_service(db_session: AsyncSession, order_service: OrderService) -> bool:
        """Check if an order service exists by ID."""
        
        try:
            
            response = await db_session.exec(select(OrderService).where(OrderService.service_id == order_service.service_id))

            return bool(response.first())
        
        except Exception as e:
            raise HTTPException(detail="Order service existence check failed", status_code=500) from e
    
    @staticmethod
    @log_operation(True)
    async def exist_service_in_orders(db_session: AsyncSession, service_id: int) -> bool:
        """Check if a service is associated with any orders."""
        
        try:
            
            response = await db_session.exec(select(OrderService).where(OrderService.service_id == service_id))
            
            return bool(response.first())
        
        except Exception as e:
            raise HTTPException(detail="Service existence check failed", status_code=500) from e

    @staticmethod
    @log_operation(True)
    async def exist_order_product(db_session: AsyncSession, order_product: OrderProduct) -> bool:
        """Check if an order product exists by ID."""
        
        try:
            
            response = await db_session.exec(select(OrderProduct).where(OrderProduct.product_id == order_product.product_id).where(OrderProduct.order_id == order_product.order_id))
            
            return bool(response.first())
        
        except Exception as e:
            raise HTTPException(detail="Order product existence check failed", status_code=500) from e
    
    @staticmethod
    @log_operation(True)
    async def exist_order_services_in_order(db_session: AsyncSession, order_id : int) -> bool:
        """Check if at least one order service exists in a order"""
        
        try:
            
            response = await db_session.exec(select(OrderService).where(OrderService.order_id == order_id))
            
            return bool(response.first())
        
        except Exception as e:
            raise HTTPException(detail="Order service existence check failed", status_code=500) from e
    
    @staticmethod
    @log_operation(True)
    async def exist_order_products_in_order(db_session: AsyncSession, order_id : int) -> bool:
        """Check if at least one order service exists in a order"""
        
        try:

            response = await db_session.exec(select(OrderProduct).where(OrderProduct.order_id == order_id))

            return bool(response.first())
        
        except Exception as e:
            raise HTTPException(detail="Order product existence check failed", status_code=500) from e

    @staticmethod
    @log_operation(True)
    async def order_product_in_order_completed(db_session: AsyncSession, order_product: OrderProduct) -> bool:
        """Check if an order product exist in a order completed"""
        
        if not await OrderUtils.exist_order_product(db_session, order_product):
            raise HTTPException(detail="Order product not found", status_code=404)
        
        try:
            
            response = await db_session.exec(select(Order).where(Order.id == order_product.order_id))

            return response.one().status == OrderStatus.COMPLETED
        
        except Exception as e:
            raise HTTPException(detail="Order product existence check failed", status_code=500) from e
        
    @staticmethod
    @log_operation(True)
    async def order_service_in_order_completed(db_session: AsyncSession, order_service: OrderService) -> bool:
        """Check if an order service exist in a order completed"""
        
        if not await OrderUtils.exist_order_service(db_session, order_service):
            raise HTTPException(detail="Order service not found", status_code=404)
        
        try:
            
            response = await db_session.exec(select(Order).where(Order.id == order_service.order_id))

            return response.one().status == OrderStatus.COMPLETED
        
        except Exception as e:
            raise HTTPException(detail="Order service existence check failed", status_code=500) from e
    
    @staticmethod
    @log_operation(True)
    async def exist_product_in_orders(db_session: AsyncSession, product_id: int) -> bool:
        """Check if a product is associated with any orders."""
        
        try:

            response = await db_session.exec(select(OrderProduct).where(OrderProduct.product_id == product_id))

            return bool(response.first())
        
        except Exception as e:
            raise HTTPException(detail="Product existence check failed", status_code=500) from e