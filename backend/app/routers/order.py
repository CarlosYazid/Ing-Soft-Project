from fastapi import APIRouter, Request, Depends

from models import OrderCreate, OrderStatus, OrderServiceCreate, OrderProductCreate
from crud import OrderCrud
from services import AuthService, OrderService


router = APIRouter(prefix="/order")

@router.get("/all")
async def get_orders(request: Request):
    return await OrderCrud.get_all_orders()

@router.get("/base/all")
async def get_orders_base(request: Request):
    """
    Retrieve all orders in base format.
    """
    return await OrderService.get_all_orders_base()

@router.get("/{_id}")
async def get_order_by_id(request: Request, _id: int):
    """
    Retrieve an order by ID.
    """
    return await OrderCrud.get_order_by_id(_id)

@router.get("/")
async def get_order_by_id_2(request: Request, id: int):
    """
    Retrieve an order by ID.
    """
    return await OrderCrud.get_order_by_id(id)

@router.get("/base/{_id}")
async def get_order_base_by_id(request: Request, _id: int):
    """
    Get an order base by ID.
    """
    return await OrderService.get_order_base_by_id(_id)

@router.get("/base/")
async def get_order_base_by_id_2(request: Request, id: int):
    """
    Get an order base by ID.
    """
    return await OrderService.get_order_base_by_id(id)

@router.post("/")
async def create_order(request: Request, order: OrderCreate):
    """
    Create a new order.
    """
    return await OrderCrud.create_order(order)

@router.put("/{_id}")
async def update_order_by_id(request: Request, _id: int, fields: dict):
    """
    Update an existing order by ID.
    """
    return await OrderCrud.update_order(_id, fields)

@router.delete("/{_id}")
async def delete_order_by_id(request: Request, _id: int):
    """
    Delete an order by ID.
    """
    return await OrderCrud.delete_order(_id)

@router.delete("/")
async def delete_order_by_id_2(request: Request, id: int):
    """
    Delete an order by ID.
    """
    return await OrderCrud.delete_order(id)

@router.get("/client/{client_id}")
async def get_orders_by_client_id(request: Request, client_id: int):
    """
    Retrieve orders by client ID.
    """
    return await OrderCrud.get_orders_by_client_id(client_id)

@router.get("/client/")
async def get_orders_by_client_id_2(request: Request, client_id: int):
    """
    Retrieve orders by client ID.
    """
    return await OrderCrud.get_orders_by_client_id(client_id)

@router.get("/client/base/{client_id}")
async def get_orders_base_by_client_id(request: Request, client_id: int):
    """
    Retrieve orders by client ID in base format.
    """
    return await OrderService.get_orders_base_by_client_id(client_id)

@router.get("/client/base/")
async def get_orders_base_by_client_id_2(request: Request, client_id: int):
    """
    Retrieve orders by client ID in base format.
    """
    return await OrderService.get_orders_base_by_client_id(client_id)

@router.get("/status/{status}")
async def get_orders_by_status(request: Request, status: OrderStatus):
    """
    Retrieve orders by status.
    """
    return await OrderCrud.get_orders_by_status(status)

@router.get("/status/")
async def get_orders_by_status_2(request: Request, status: OrderStatus):
    """
    Retrieve orders by status.
    """
    return await OrderCrud.get_orders_by_status(status)

@router.get("/status/base/{status}")
async def get_orders_base_by_status(request: Request, status: OrderStatus):
    """
    Retrieve orders by status in base format.
    """
    return await OrderService.get_orders_base_by_status(status)

@router.get("/status/base/")
async def get_orders_base_by_status_2(request: Request, status: OrderStatus):
    """
    Retrieve orders by status in base format.
    """
    return await OrderService.get_orders_base_by_status(status)

@router.get("/exists/{_id}")
async def exist_order_by_id(request: Request, _id: int):
    """
    Check if an order exists by ID.
    """
    return await OrderCrud.exist_order_by_id(_id)

@router.get("/exists/")
async def exist_order_by_id_2(request: Request, id: int):
    """
    Check if an order exists by ID.
    """
    return await OrderCrud.exist_order_by_id(id)

@router.get("/services/{order_service_id}")
async def get_order_service_by_id(request: Request, order_service_id: int):
    """
    Retrieve an order service by ID.
    """
    return await OrderCrud.get_order_services(order_service_id)

@router.get("/services/")
async def get_order_service_by_id_2(request: Request, order_service_id: int):
    """
    Retrieve an order service by ID.
    """
    return await OrderCrud.get_order_services(order_service_id)

@router.post("/services/")
async def create_order_service(request: Request, order_service: OrderServiceCreate):
    """
    Create a new order service.
    """
    return await OrderCrud.add_service_to_order(order_service)

@router.put("/services/{_id}")
async def update_order_service_by_id(request: Request, _id: int, fields: dict):
    """
    Update an existing order service by ID.
    """
    return await OrderCrud.update_order_service(_id, fields)

@router.delete("/services/{_id}")
async def delete_order_service_by_id(request: Request, _id: int):
    """
    Delete an order service by ID.
    """
    return await OrderCrud.delete_order_service(_id)

@router.delete("/services/")
async def delete_order_service_by_id_2(request: Request, id: int):
    """
    Delete an order service by ID.
    """
    return await OrderCrud.delete_order_service(id)

@router.get("/services/orders/{order_id}")
async def get_orders_services_by_order_id(request: Request, order_id: int):
    """
    Retrieve order services by order ID.
    """
    return await OrderCrud.get_orders_service_by_order_id(order_id)

@router.get("/services/orders/")
async def get_orders_services_by_order_id_2(request: Request, order_id: int):
    """
    Retrieve order services by order ID.
    """
    return await OrderCrud.get_orders_service_by_order_id(order_id)


@router.get("/services/exist/{_id}")
async def exist_order_service_by_id(request: Request, _id: int):
    """
    Check if an order service exists by ID.
    """
    return await OrderCrud.exist_order_service_by_id(_id)


@router.get("/services/exist/")
async def exist_order_service_by_id_2(request: Request, id: int):
    """
    Check if an order service exists by ID.
    """
    return await OrderCrud.exist_order_service_by_id(id)


@router.get("/products/{_id}")
async def get_order_product_by_id(request: Request, _id: int):
    """
    Retrieve an order product by ID.
    """
    return await OrderCrud.get_order_product_by_id(_id)

@router.get("/products/")
async def get_order_product_by_id_2(request: Request, id: int):
    """
    Retrieve an order product by ID.
    """
    return await OrderCrud.get_order_product_by_id(id)

@router.post("/products/")
async def create_order_product(request: Request, order_product: OrderProductCreate):
    """
    Create a new order product.
    """
    return await OrderCrud.add_product_to_order(order_product)

@router.put("/products/{_id}")
async def update_order_product_by_id(request: Request, _id: int, fields: dict):
    """
    Update an existing order product by ID.
    """
    return await OrderCrud.update_order_product(_id, fields)

@router.delete("/products/{_id}")
async def delete_order_product_by_id(request: Request, _id: int):
    """
    Delete an order product by ID.
    """
    return await OrderCrud.delete_order_product(_id)

@router.delete("/products/")
async def delete_order_product_by_id_2(request: Request, id: int):
    """
    Delete an order product by ID.
    """
    return await OrderCrud.delete_order_product(id)

@router.get("/products/exist/{_id}")
async def exist_order_product_by_id(request: Request, _id: int):
    """
    Check if an order product exists by ID.
    """
    return await OrderCrud.exist_order_product_by_id(_id)

@router.get("/products/exist/")
async def exist_order_product_by_id_2(request: Request, id: int):
    """
    Check if an order product exists by ID.
    """
    return await OrderCrud.exist_order_product_by_id(id)


@router.get("/products/orders/{order_id}")
async def get_orders_products_by_order_id(request: Request, order_id: int):
    """
    Retrieve order products by order ID.
    """
    return await OrderCrud.get_orders_product_by_order_id(order_id)

@router.get("/products/orders/")
async def get_order_products_by_order_id_2(request: Request, order_id: int):
    """
    Retrieve order products by order ID.
    """
    return await OrderCrud.get_orders_product_by_order_id(order_id)