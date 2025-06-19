from models import OrderBase
from crud import OrderCrud

class OrderService:
    @classmethod
    async def get_all_orders_base(cls) -> list[OrderBase]:
        """Retrieve all orders."""
        orders = await OrderCrud.get_all_orders()
        return [OrderBase.model_validate({
            "id": order.id,
            "user_id": order.user_id,
            "total_price": order.total_price,
            "status": order.status,
        }) for order in orders]

    @classmethod
    async def get_order_base_by_id(cls, order_id: int) -> OrderBase:
        """Retrieve an order by ID."""
        order = await OrderCrud.get_order_by_id(order_id)
        return OrderBase.model_validate({
            "id": order.id,
            "user_id": order.user_id,
            "total_price": order.total_price,
            "status": order.status,
        })
        
    @classmethod
    async def get_orders_base_by_client_id(cls, client_id: int) -> list[OrderBase]:
        """Retrieve orders by client ID."""
        orders = await OrderCrud.get_orders_by_client_id(client_id)
        return [OrderBase.model_validate({
            "id": order.id,
            "user_id": order.user_id,
            "total_price": order.total_price,
            "status": order.status,
        }) for order in orders]
        
    @classmethod
    async def get_orders_base_by_status(cls, status: str) -> list[OrderBase]:
        """Retrieve orders by status."""
        orders = await OrderCrud.get_orders_by_status(status)
        return [OrderBase.model_validate({
            "id": order.id,
            "user_id": order.user_id,
            "total_price": order.total_price,
            "status": order.status,
        }) for order in orders]