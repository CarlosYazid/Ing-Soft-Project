from fastapi import HTTPException

from db import get_db_client
from models import Order, OrderService, OrderProduct, OrderCreate, OrderServiceCreate, OrderProductCreate, OrderBasePlusID, OrderStatus
from core import SETTINGS
from utils import OrderUtils

class OrderCrud:
    
    EXCLUDED_FIELDS_FOR_UPDATE = {"created_at", "client_id"}
    ALLOWED_FIELDS_FOR_UPDATE = set(OrderCreate.model_fields.keys()) - EXCLUDED_FIELDS_FOR_UPDATE
    
    EXCLUDED_FIELDS_FOR_UPDATE_SERVICE = {"order_id", "service_id"}
    ALLOWED_FIELDS_FOR_UPDATE_SERVICE = set(OrderServiceCreate.model_fields.keys()) - EXCLUDED_FIELDS_FOR_UPDATE_SERVICE

    EXCLUDED_FIELDS_FOR_UPDATE_PRODUCT = {"order_id", "product_id"}
    ALLOWED_FIELDS_FOR_UPDATE_PRODUCT = set(OrderProductCreate.model_fields.keys()) - EXCLUDED_FIELDS_FOR_UPDATE_PRODUCT

    FIELDS_ORDER_BASE = set(OrderBasePlusID.model_fields.keys())

    @classmethod
    async def create_order(cls, order: OrderCreate) -> Order:
        """Create a new order."""
        client = await get_db_client()

        response = await client.table(SETTINGS.order_table).insert(order.model_dump(mode="json")).execute()

        if not bool(response.data):
            raise HTTPException(detail="Failed to create order", status_code=500)
        
        if order.status is OrderStatus.COMPLETED:
            
            from services import OrderService

            await OrderService.update_inventory(order.id)

        return Order.model_validate(response.data[0])

    @classmethod
    async def read_all_orders(cls) -> list[Order]:
        """Retrieve all orders."""
        client = await get_db_client()

        response = await client.table(SETTINGS.order_table).select("*").execute()

        if not bool(response.data):
            raise HTTPException(detail="No orders found", status_code=404)

        return [Order.model_validate(order) for order in response.data]

    @classmethod
    async def read_all_orders_base(cls) -> list[OrderBasePlusID]:
        """Retrieve all orders."""
        client = await get_db_client()

        response = await client.table(SETTINGS.order_table).select(*cls.FIELDS_ORDER_BASE).execute()
        
        if not bool(response.data):
            raise HTTPException(detail="No orders found", status_code=404)
        
        return [OrderBasePlusID.model_validate(order) for order in response.data]

    @classmethod
    async def read_order(cls, order_id: int) -> Order:
        """Retrieve an order by ID."""
        client = await get_db_client()

        response = await client.table(SETTINGS.order_table).select("*").eq("id", order_id).execute()

        if not bool(response.data):
            raise HTTPException(detail="Order not found", status_code=404)

        return Order.model_validate(response.data[0])

    @classmethod
    async def read_order_base(cls, order_id: int) -> OrderBasePlusID:
        """Retrieve an order by ID."""
        client = await get_db_client()

        response = await client.table(SETTINGS.order_table).select(*cls.FIELDS_ORDER_BASE).eq("id", order_id).execute()

        if not bool(response.data):
            raise HTTPException(detail="Order not found", status_code=404)

        return OrderBasePlusID.model_validate(response.data[0])

    
    @classmethod
    async def read_order_status(cls, order_id: int) -> OrderStatus:
        """Retrieve the status of an order."""

        if not await OrderUtils.exist_order(order_id):
            raise HTTPException(detail="Order not found", status_code=404)
        
        client = await get_db_client()

        response = await client.table(SETTINGS.order_table).select("status").eq("id", order_id).execute()

        if not bool(response.data):
            raise HTTPException(detail="Failed to retrieve order status", status_code=500)

        return OrderStatus(response.data[0]["status"])

    @classmethod
    async def update_order(cls, order_id: int, fields: dict) -> Order:
        """Update an existing order."""

        if not await OrderUtils.exist_order(order_id):
            raise HTTPException(detail="Order not found", status_code=404)
        
        if any(field in fields for field in cls.EXCLUDED_FIELDS_FOR_UPDATE):
            raise HTTPException(detail="Cannot update fields: " + ", ".join(cls.EXCLUDED_FIELDS_FOR_UPDATE), status_code=400)

        if not(set(fields.keys()) <= cls.ALLOWED_FIELDS_FOR_UPDATE):
            raise HTTPException(detail="Update attribute of order", status_code=400)

        client = await get_db_client()

        response = await client.table(SETTINGS.order_table).update(fields).eq("id", order_id).execute()

        if not bool(response.data):
            raise HTTPException(detail="Failed to update order", status_code=500)

        if "status" in fields and OrderStatus(fields["status"]) is OrderStatus.COMPLETED:
            from services import OrderService
            
            await OrderService.update_inventory(order_id)

        return Order.model_validate(response.data[0])

    @classmethod
    async def update_order_status(cls, order_id: int, status: OrderStatus) -> Order:
        """Update the status of an order."""

        if not await OrderUtils.exist_order(order_id):
            raise HTTPException(detail="Order not found", status_code=404)

        client = await get_db_client()

        response = await client.table(SETTINGS.order_table).update({"status": status.capitalize()}).eq("id", order_id).execute()

        if not bool(response.data):
            raise HTTPException(detail="Failed to update order status", status_code=500)
        
        if status is OrderStatus.COMPLETED:
            
            from services import OrderService
            
            await OrderService.update_inventory(order_id)

        return Order.model_validate(response.data[0])
    
    @classmethod
    async def delete_order(cls, order_id: int) -> None:
        """Delete an order by ID."""
        
        # Check if the order exists before attempting to delete
        if not await OrderUtils.exist_order(order_id):
            raise HTTPException(detail="Order not found", status_code=404)
        
        # Ensure the order is not completed before deleting
        if await cls.read_order_status(order_id) is OrderStatus.COMPLETED:
            raise HTTPException(detail="Cannot delete a completed order", status_code=400)
        
        order_products = await cls.read_orders_products_by_order_id(order_id)
        order_services = await cls.read_orders_services_by_order_id(order_id)

        # Delete associated order products
        for order_product in order_products:
            await cls.delete_order_product(order_product.id)
        
        # Delete associated order services
        for order_service in order_services:
            await cls.delete_order_service(order_service.id)
            
        client = await get_db_client()
        
        # Finally, delete the order itself
        response = await client.table(SETTINGS.order_table).delete().eq("id", order_id).execute()

        if not bool(response.data):
            raise HTTPException(detail="Failed to delete order", status_code=500)

        return bool(response.data)

    @classmethod
    async def create_order_service(cls, order_service: OrderServiceCreate) -> OrderService:
        """Add a service to an order."""

        # Ensure the order_id exists before adding the service
        if not await OrderUtils.exist_order(order_service.order_id):
            raise HTTPException(detail="Order not found", status_code=404)

        if await cls.read_order_status(order_service.order_id) is OrderStatus.COMPLETED:
            raise HTTPException(detail="Cannot add service to a completed order", status_code=400)

        # Import ServiceCrud directly from its file path
        from utils import ServiceUtils

        # Ensure the service_id exists before adding the service
        if not await ServiceUtils.exist_service(order_service.service_id):
            raise HTTPException(detail="Service not found", status_code=404)
        
        client = await get_db_client()

        response = await client.table(SETTINGS.order_service_table).insert(order_service.model_dump(mode="json")).execute()

        if not bool(response.data):
            raise HTTPException(detail="Failed to add service to order", status_code=500)

        return OrderService.model_validate(response.data[0])
    
    @classmethod
    async def read_order_service(cls, order_service_id: int) -> OrderService:
        """Retrieve an order service by ID."""
        client = await get_db_client()

        response = await client.table(SETTINGS.order_service_table).select("*").eq("id", order_service_id).execute()

        if not bool(response.data):
            raise HTTPException(detail="Order service not found", status_code=404)

        return OrderService.model_validate(response.data[0])
    
    @classmethod
    async def read_orders_services_by_order_id(cls, order_id: int) -> list[OrderService]:
        """Retrieve services associated with an order."""
        
        if not await OrderUtils.exist_order(order_id):
            raise HTTPException(detail="Order not found", status_code=404)
        
        client = await get_db_client()

        response = await client.table(SETTINGS.order_service_table).select("*").eq("order_id", order_id).execute()

        if not bool(response.data):
            raise HTTPException(detail="No services found for this order", status_code=404)

        return [OrderService.model_validate(service) for service in response.data]
    
    @classmethod
    async def read_orders_services_ids_by_order_id(cls, order_id: int) -> list[int]:
        """Retrieve service IDs associated with an order."""
        if not await OrderUtils.exist_order(order_id):
            raise HTTPException(detail="Order not found", status_code=404)
        
        client = await get_db_client()

        response = await client.table(SETTINGS.order_service_table).select("id").eq("order_id", order_id).execute()

        if not bool(response.data):
            raise HTTPException(detail="No services found for this order", status_code=404)

        return [int(service["id"]) for service in response.data]
    
    @classmethod
    async def read_orders_services_by_service_id(cls, service_id: int) -> list[OrderService]:
        """Retrieve all orders for a specific service."""
        
        from utils import ServiceUtils
        
        # Ensure the service_id exists before retrieving orders
        if not await ServiceUtils.exist_service(service_id):
            raise HTTPException(detail="Service not found", status_code=404)

        client = await get_db_client()

        response = await client.table(SETTINGS.order_service_table).select("*").eq("service_id", service_id).execute()

        if not bool(response.data):
            raise HTTPException(detail="No orders found for this service", status_code=404)

        return [OrderService.model_validate(service) for service in response.data]
    
    @classmethod
    async def update_order_service(cls, order_service_id: int, fields: dict) -> OrderService:
        """Update an existing order service."""
        client = await get_db_client()
        
        if not await OrderUtils.exist_order_service(order_service_id):
            raise HTTPException(detail="Order service not found", status_code=404)
        
        if any(field in fields for field in cls.EXCLUDED_FIELDS_FOR_UPDATE_SERVICE):
            raise HTTPException(detail="Cannot update fields: " + ", ".join(cls.EXCLUDED_FIELDS_FOR_UPDATE_SERVICE), status_code=400)
        
        if not(set(fields.keys()) <= cls.ALLOWED_FIELDS_FOR_UPDATE_SERVICE):
            raise HTTPException(detail="Update attribute of order service", status_code=400)
        
        if cls.read_order_status(cls.read_order_service(order_service_id).order_id) is OrderStatus.COMPLETED:
            raise HTTPException(detail="Cannot update service in a completed order", status_code=400)

        response = await client.table(SETTINGS.order_service_table).update(fields).eq("id", order_service_id).execute()

        if not(bool(response.data)):
            raise HTTPException(detail="Failed to update order service", status_code=500)

        return OrderService.model_validate(response.data[0])
    
    @classmethod
    async def delete_order_service(cls, order_service_id: int) -> bool:
        """Delete an order service by ID."""
        client = await get_db_client()

        # Check if the order service exists before attempting to delete
        if not await OrderUtils.exist_order_service(order_service_id):
            raise HTTPException(detail="Order service not found", status_code=404)
        
        if await OrderUtils.order_service_in_order_completed(order_service_id):
            raise HTTPException(detail="Order service in order completed", status_code=404)

        response = await client.table(SETTINGS.order_service_table).delete().eq("id", order_service_id).execute()

        if not bool(response.data):
            raise HTTPException(detail="Failed to delete order service", status_code=500)

        return bool(response.data)
    
    @classmethod
    async def create_order_product(cls, order_product: OrderProductCreate) -> OrderProduct:
        """Add a product to an order."""

        # Ensure the order_id exists before adding the product
        if not await OrderUtils.exist_order(order_product.order_id):
            raise HTTPException(detail="Order not found", status_code=404)

        if await cls.read_order_status(order_product.order_id) is OrderStatus.COMPLETED:
            raise HTTPException(detail="Cannot add product to a completed order", status_code=400)

        # Import ProductUtils directly from its file path
        from utils import ProductUtils

        # Ensure the product_id exists before adding the product
        if not await ProductUtils.exist_product(order_product.product_id):
            raise HTTPException(detail="Product not found", status_code=404)
        
        client = await get_db_client()
        
        response = await client.table(SETTINGS.order_product_table).insert(order_product.model_dump(mode="json")).execute()

        if not bool(response.data):
            raise HTTPException(detail="Failed to add product to order", status_code=500)

        return OrderProduct.model_validate(response.data[0])
    
    @classmethod
    async def read_order_product(cls, order_product_id: int) -> OrderProduct:
        """Retrieve an order product by ID."""
        
        client = await get_db_client()
        
        response = await client.table(SETTINGS.order_product_table).select("*").eq("id", order_product_id).execute()

        if not bool(response.data):
            raise HTTPException(detail="Order product not found", status_code=404)

        return OrderProduct.model_validate(response.data[0])
    
    @classmethod
    async def read_orders_products_by_order_id(cls, order_id: int) -> list[OrderProduct]:
        """Retrieve orders products associated with an order."""
        
        if not await OrderUtils.exist_order(order_id):
            raise HTTPException(detail="Order not found", status_code=404)
        
        client = await get_db_client()

        response = await client.table(SETTINGS.order_product_table).select("*").eq("order_id", order_id).execute()

        if not bool(response.data):
            raise HTTPException(detail="No products found for this order", status_code=404)

        return [OrderProduct.model_validate(product) for product in response.data]
    
    @classmethod
    async def read_orders_products_ids_by_order_id(cls, order_id: int) -> list[int]:
        """Retrieve product IDs associated with an order."""
        
        if not await OrderUtils.exist_order(order_id):
            raise HTTPException(detail="Order not found", status_code=404)
        
        client = await get_db_client()

        response = await client.table(SETTINGS.order_product_table).select("id").eq("order_id", order_id).execute()

        if not bool(response.data):
            raise HTTPException(detail="No products found for this order", status_code=404)

        return [int(product["id"]) for product in response.data]
    
    @classmethod
    async def read_orders_products_by_product_id(cls, product_id: int) -> list[OrderProduct]:
        """Retrieve all orders for a specific product."""
        
        from utils import ProductUtils
        
        # Ensure the product_id exists before retrieving orders
        if not await ProductUtils.exist_product(product_id):
            raise HTTPException(detail="Product not found", status_code=404)

        client = await get_db_client()

        response = await client.table(SETTINGS.order_product_table).select("*").eq("product_id", product_id).execute()

        if not bool(response.data):
            raise HTTPException(detail="No orders found for this product", status_code=404)

        return [OrderProduct.model_validate(product) for product in response.data]

    @classmethod
    async def update_order_product(cls, order_product_id: int, fields: dict) -> OrderProduct:
        """Update an existing order product."""
        client = await get_db_client()
        
        if not await OrderUtils.exist_order_product(order_product_id):
            raise HTTPException(detail="Order product not found", status_code=404)
        
        if any(field in fields for field in cls.EXCLUDED_FIELDS_FOR_UPDATE_PRODUCT):
            raise HTTPException(detail="Cannot update fields: " + ", ".join(cls.EXCLUDED_FIELDS_FOR_UPDATE_PRODUCT), status_code=400)
        
        if not(set(fields.keys()) <= cls.ALLOWED_FIELDS_FOR_UPDATE_PRODUCT):
            raise HTTPException(detail="Update attribute of order product", status_code=400)
        
        if cls.read_order_status(cls.read_order_product(order_product_id).order_id) is OrderStatus.COMPLETED:
            raise HTTPException(detail="Cannot update product in a completed order", status_code=400)

        response = await client.table(SETTINGS.order_product_table).update(fields).eq("id", order_product_id).execute()

        if not(bool(response.data)):
            raise HTTPException(detail="Failed to update order product", status_code=500)

        return OrderProduct.model_validate(response.data[0])
    
    @classmethod
    async def delete_order_product(cls, order_product_id: int) -> None:
        """Delete an order product by ID."""
        client = await get_db_client()

        # Check if the order product exists before attempting to delete
        if not await OrderUtils.exist_order_product(order_product_id):
            raise HTTPException(detail="Order product not found", status_code=404)

        if await OrderUtils.order_product_in_order_completed(order_product_id):
            raise HTTPException(detail="Order product in order completed", status_code=404)

        response = await client.table(SETTINGS.order_product_table).delete().eq("id", order_product_id).execute()

        if not(bool(response.data)):
            raise HTTPException(detail="Failed to delete order product", status_code=500)

        return bool(response.data)