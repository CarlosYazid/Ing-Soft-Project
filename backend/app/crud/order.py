from fastapi import HTTPException

from db import get_db_client
from models import Order, OrderStatus, OrderService, OrderProduct, OrderCreate, OrderServiceCreate, OrderProductCreate
from core import SETTINGS

class OrderCrud:

    @classmethod
    async def get_all_orders(cls) -> list[Order]:
        """Retrieve all orders."""
        client = await get_db_client()

        response = await client.table(SETTINGS.order_table).select("*").execute()

        if not(bool(response.data)):
            raise HTTPException(detail="No orders found", status_code=404)

        return [Order.model_validate(order) for order in response.data]

    @classmethod
    async def create_order(cls, order: OrderCreate) -> Order:
        """Create a new order."""
        client = await get_db_client()

        response = await client.table(SETTINGS.order_table).insert(order.model_dump(mode="json")).execute()

        if not(bool(response.data)):
            raise HTTPException(detail="Failed to create order", status_code=500)

        return Order.model_validate(response.data[0])

    @classmethod
    async def get_order_by_id(cls, order_id: int) -> Order:
        """Retrieve an order by ID."""
        client = await get_db_client()

        response = await client.table(SETTINGS.order_table).select("*").eq("id", order_id).execute()

        if not(bool(response.data)):
            raise HTTPException(detail="Order not found", status_code=404)

        return Order.model_validate(response.data[0])

    @classmethod
    async def update_order(cls, order_id: int, fields: dict) -> Order:
        """Update an existing order."""
        client = await get_db_client()
        
        if not(set(fields.keys()) < set(OrderCreate.__fields__.keys())):
            raise HTTPException(detail="Update attribute of order", status_code=400)

        response = await client.table(SETTINGS.order_table).update(fields).eq("id", order_id).execute()

        if not(bool(response.data)):
            raise HTTPException(detail="Failed to update order", status_code=500)

        return Order.model_validate(response.data[0])

    @classmethod
    async def delete_order(cls, order_id: int) -> None:
        """Delete an order by ID."""
        client = await get_db_client()

        response = await client.table(SETTINGS.order_table).delete().eq("id", order_id).execute()

        if not(bool(response.data)):
            raise HTTPException(detail="Failed to delete order", status_code=500)

        return bool(response.data)

    @classmethod
    async def get_orders_by_status(cls, status: OrderStatus) -> list[Order]:
        """Retrieve orders by status."""
        client = await get_db_client()

        response = await client.table(SETTINGS.order_table).select("*").eq("status", status.capitalize()).execute()

        if not(bool(response.data)):
            raise HTTPException(detail="No orders found with this status", status_code=404)

        return [Order.model_validate(order) for order in response.data]

    @classmethod
    async def add_service_to_order(cls, order_service: OrderServiceCreate) -> OrderService:
        """Add a service to an order."""
        client = await get_db_client()

        # Import ServiceCrud directly from its file path
        from crud.service import ServiceCrud

        # Ensure the order_id exists before adding the service
        if not await cls.exist_order_by_id(order_service.order_id):
            raise HTTPException(detail="Order not found", status_code=404)

        # Ensure the service_id exists before adding the service
        if not await ServiceCrud.exist_service_by_id(order_service.service_id):
            raise HTTPException(detail="Service not found", status_code=404)

        response = await client.table(SETTINGS.order_service_table).insert(order_service.model_dump(mode="json")).execute()

        if not(bool(response.data)):
            raise HTTPException(detail="Failed to add service to order", status_code=500)

        return OrderService.model_validate(response.data[0])

    @classmethod
    async def add_product_to_order(cls, order_product: OrderProductCreate) -> OrderProduct:
        """Add a product to an order."""
        client = await get_db_client()

        # Import ProductCrud directly from its file path
        from crud.product import ProductCrud

        # Ensure the order_id exists before adding the product
        if not await cls.exist_order_by_id(order_product.order_id):
            raise HTTPException(detail="Order not found", status_code=404)

        # Ensure the product_id exists before adding the product
        if not await ProductCrud.exist_product_by_id(order_product.product_id):
            raise HTTPException(detail="Product not found", status_code=404)

        response = await client.table(SETTINGS.order_product_table).insert(order_product.model_dump(mode="json")).execute()

        if not(bool(response.data)):
            raise HTTPException(detail="Failed to add product to order", status_code=500)

        return OrderProduct.model_validate(response.data[0])

    @classmethod
    async def get_order_services(cls, order_id: int) -> list[OrderService]:
        """Retrieve services associated with an order."""
        client = await get_db_client()

        response = await client.table(SETTINGS.order_service_table).select("*").eq("order_id", order_id).execute()

        if not(bool(response.data)):
            raise HTTPException(detail="No services found for this order", status_code=404)

        return [OrderService.model_validate(service) for service in response.data]

    @classmethod
    async def get_order_products(cls, order_id: int) -> list[OrderProduct]:
        """Retrieve products associated with an order."""
        client = await get_db_client()

        response = await client.table(SETTINGS.order_product_table).select("*").eq("order_id", order_id).execute()

        if not(bool(response.data)):
            raise HTTPException(detail="No products found for this order", status_code=404)

        return [OrderProduct.model_validate(product) for product in response.data]


    @classmethod
    async def get_order_service_by_id(cls, order_service_id: int) -> OrderService:
        """Retrieve an order service by ID."""
        client = await get_db_client()

        response = await client.table(SETTINGS.order_service_table).select("*").eq("id", order_service_id).execute()

        if not(bool(response.data)):
            raise HTTPException(detail="Order service not found", status_code=404)

        return OrderService.model_validate(response.data[0])


    @classmethod
    async def get_order_product_by_id(cls, order_product_id: int) -> OrderProduct:
        """Retrieve an order product by ID."""
        client = await get_db_client()
        response = await client.table(SETTINGS.order_product_table).select("*").eq("id", order_product_id).execute()

        if not(bool(response.data)):
            raise HTTPException(detail="Order product not found", status_code=404)

        return OrderProduct.model_validate(response.data[0])


    @classmethod
    async def update_order_service(cls, order_service_id: int, fields: dict) -> OrderService:
        """Update an existing order service."""
        client = await get_db_client()
        
        if not(set(fields.keys()) < set(OrderServiceCreate.__fields__.keys())):
            raise HTTPException(detail="Update attribute of order service", status_code=400)

        response = await client.table(SETTINGS.order_service_table).update(fields).eq("id", order_service_id).execute()

        if not(bool(response.data)):
            raise HTTPException(detail="Failed to update order service", status_code=500)

        return OrderService.model_validate(response.data[0])

    @classmethod
    async def update_order_product(cls, order_product_id: int, fields: dict) -> OrderProduct:
        """Update an existing order product."""
        client = await get_db_client()
        
        if not(set(fields.keys()) < set(OrderServiceCreate.__fields__.keys())):
            raise HTTPException(detail="Update attribute of order product", status_code=400)

        # Import ProductCrud directly from its file path
        from crud.product import ProductCrud

        if not await cls.exist_order_product_by_id(order_product_id):
            raise HTTPException(detail="Order product not found", status_code=404)
        if "order_id" in fields and not await cls.exist_order_by_id(fields["order_id"]):
            raise HTTPException(detail="Order not found", status_code=404)
        if "product_id" in fields and not await ProductCrud.exist_product_by_id(fields["product_id"]):
            raise HTTPException(detail="Product not found", status_code=404)

        response = await client.table(SETTINGS.order_product_table).update(fields).eq("id", order_product_id).execute()

        if not(bool(response.data)):
            raise HTTPException(detail="Failed to update order product", status_code=500)

        return OrderProduct.model_validate(response.data[0])

    @classmethod
    async def delete_order_service(cls, order_service_id: int) -> None:
        """Delete an order service by ID."""
        client = await get_db_client()

        # Check if the order service exists before attempting to delete
        if not await cls.exist_order_service_by_id(order_service_id):
            raise HTTPException(detail="Order service not found", status_code=404)

        response = await client.table(SETTINGS.order_service_table).delete().eq("id", order_service_id).execute()

        if not(bool(response.data)):
            raise HTTPException(detail="Failed to delete order service", status_code=500)

        return bool(response.data)

    @classmethod
    async def delete_order_product(cls, order_product_id: int) -> None:
        """Delete an order product by ID."""
        client = await get_db_client()

        # Check if the order product exists before attempting to delete
        if not await cls.exist_order_product_by_id(order_product_id):
            raise HTTPException(detail="Order product not found", status_code=404)

        response = await client.table(SETTINGS.order_product_table).delete().eq("id", order_product_id).execute()

        if not(bool(response.data)):
            raise HTTPException(detail="Failed to delete order product", status_code=500)

        return bool(response.data)

    @classmethod
    async def exist_order_by_id(cls, order_id: int) -> bool:
        """Check if an order exists by ID."""
        client = await get_db_client()

        response = await client.table(SETTINGS.order_table).select("id").eq("id", order_id).execute()

        return bool(response.data)

    @classmethod
    async def exist_order_service_by_id(cls, order_service_id: int) -> bool:
        """Check if an order service exists by ID."""
        client = await get_db_client()

        response = await client.table(SETTINGS.order_service_table).select("id").eq("id", order_service_id).execute()

        return bool(response.data)

    @classmethod
    async def exist_order_product_by_id(cls, order_product_id: int) -> bool:
        """Check if an order product exists by ID."""
        client = await get_db_client()

        response = await client.table(SETTINGS.order_product_table).select("id").eq("id", order_product_id).execute()

        return bool(response.data)

    @classmethod
    async def get_orders_by_client_id(cls, client_id: int) -> list[Order]:
        """Retrieve all orders for a specific client."""
        client = await get_db_client()

        response = await client.table(SETTINGS.order_table).select("*").eq("client_id", client_id).execute()

        if not(bool(response.data)):
            raise HTTPException(detail="No orders found for this client", status_code=404)

        return [Order.model_validate(order) for order in response.data]


    @classmethod
    async def get_orders_service_by_order_id(cls, order_id: int) -> list[OrderService]:
        """Retrieve all services for a specific order."""
        client = await get_db_client()

        response = await client.table(SETTINGS.order_service_table).select("*").eq("order_id", order_id).execute()

        if not(bool(response.data)):
            raise HTTPException(detail="No services found for this order", status_code=404)

        return [OrderService.model_validate(service) for service in response.data]

    @classmethod
    async def get_orders_product_by_order_id(cls, order_id: int) -> list[OrderProduct]:
        """Retrieve all products for a specific order."""
        client = await get_db_client()

        response = await client.table(SETTINGS.order_product_table).select("*").eq("order_id", order_id).execute()

        if not(bool(response.data)):
            raise HTTPException(detail="No products found for this order", status_code=404)

        return [OrderProduct.model_validate(product) for product in response.data]

    @classmethod
    async def get_orders_service_by_service_id(cls, service_id: int) -> list[OrderService]:
        """Retrieve all orders for a specific service."""
        client = await get_db_client()

        response = await client.table(SETTINGS.order_service_table).select("*").eq("service_id", service_id).execute()

        if not(bool(response.data)):
            raise HTTPException(detail="No orders found for this service", status_code=404)

        return [OrderService.model_validate(service) for service in response.data]

    @classmethod
    async def get_orders_product_by_product_id(cls, product_id: int) -> list[OrderProduct]:
        """Retrieve all orders for a specific product."""
        client = await get_db_client()

        response = await client.table(SETTINGS.order_product_table).select("*").eq("product_id", product_id).execute()

        if not(bool(response.data)):
            raise HTTPException(detail="No orders found for this product", status_code=404)

        return [OrderProduct.model_validate(product) for product in response.data]
