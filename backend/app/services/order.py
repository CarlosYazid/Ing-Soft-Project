from models import OrderBasePlusID
from crud import OrderCrud

class OrderService:
    @classmethod
    async def get_all_orders_base(cls) -> list[OrderBasePlusID]:
        """Retrieve all orders."""
        orders = await OrderCrud.get_all_orders()
        return [OrderBasePlusID.model_validate({
            "id": order.id,
            "client_id": order.client_id,
            "total_price": order.total_price,
            "status": order.status,
        }) for order in orders]

    @classmethod
    async def get_order_base_by_id(cls, order_id: int) -> OrderBasePlusID:
        """Retrieve an order by ID."""
        order = await OrderCrud.get_order_by_id(order_id)
        return OrderBasePlusID.model_validate({
            "id": order.id,
            "client_id": order.client_id,
            "total_price": order.total_price,
            "status": order.status,
        })
        
    @classmethod
    async def get_orders_base_by_client_id(cls, client_id: int) -> list[OrderBasePlusID]:
        """Retrieve orders by client ID."""
        orders = await OrderCrud.get_orders_by_client_id(client_id)
        return [OrderBasePlusID.model_validate({
            "id": order.id,
            "client_id": order.client_id,
            "total_price": order.total_price,
            "status": order.status,
        }) for order in orders]
        
    @classmethod
    async def get_orders_base_by_status(cls, status: str) -> list[OrderBasePlusID]:
        """Retrieve orders by status."""
        orders = await OrderCrud.get_orders_by_status(status)
        return [OrderBasePlusID.model_validate({
            "id": order.id,
            "client_id": order.client_id,
            "total_price": order.total_price,
            "status": order.status,
        }) for order in orders]