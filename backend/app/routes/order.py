from fastapi import APIRouter, Request, Depends

from models import OrderCreate, OrderStatus, OrderServiceCreate, OrderProductCreate
from crud import OrderCrud
from services import AuthService, OrderService


router = APIRouter(prefix="/order")

@router.post("/")
async def create_order(request: Request, order: OrderCreate):
    """
    Create a new order.
    """
    return await OrderCrud.create_order(order)

@router.get("/all")
async def read_all_orders(request: Request):
    """
    Retrieve all orders.
    """
    return await OrderCrud.read_all_orders()

@router.get("/base/all")
async def read_all_orders_base(request: Request):
    """
    Retrieve all orders in base format.
    """
    return await OrderCrud.read_all_orders_base()

@router.get("/{_id}")
async def read_order(request: Request, _id: int):
    """
    Retrieve an order by ID.
    """
    return await OrderCrud.read_order(_id)

@router.get("/")
async def read_order_2(request: Request, id: int):
    """
    Retrieve an order by ID.
    """
    return await OrderCrud.read_order(id)

@router.get("/base/{_id}")
async def read_order_base(request: Request, _id: int):
    """
    Get an order base by ID.
    """
    return await OrderCrud.read_order_base(_id)

@router.get("/base/")
async def read_order_base_2(request: Request, id: int):
    """
    Get an order base by ID.
    """
    return await OrderCrud.read_order_base(id)

@router.put("/{_id}")
async def update_order(request: Request, _id: int, fields: dict):
    """
    Update an existing order by ID.
    """
    return await OrderCrud.update_order(_id, fields)

@router.put('/status/{_id}/{status}')
async def update_order_status(request: Request, order_id: int, status: OrderStatus):
    """
    Update status of a order
    """
    return await OrderCrud.update_order_status(order_id, status)

@router.put('/status/')
async def update_order_status(request: Request, order_id: int, status: OrderStatus):
    """
    Update status of a order
    """
    return await OrderCrud.update_order_status(order_id, status)

@router.delete("/{_id}")
async def delete_order(request: Request, _id: int):
    """
    Delete an order by ID.
    """
    return await OrderCrud.delete_order(_id)

@router.delete("/")
async def delete_order_2(request: Request, id: int):
    """
    Delete an order by ID.
    """
    return await OrderCrud.delete_order(id)

@router.post("/service/")
async def create_order_service(request: Request, order_service: OrderServiceCreate):
    """
    Create a new order service.
    """
    return await OrderCrud.create_order_service(order_service)

@router.get("/service/{order_service_id}")
async def read_order_service(request: Request, order_service_id: int):
    """
    Retrieve an order service by ID.
    """
    return await OrderCrud.read_order_service(order_service_id)

@router.get("/service/")
async def read_order_service_2(request: Request, order_service_id: int):
    """
    Retrieve an order service by ID.
    """
    return await OrderCrud.read_order_service(order_service_id)

@router.get("/service/order/{order_id}")
async def read_orders_services_by_order_id(request: Request, order_id: int):
    """
    Retrieve order services by order ID.
    """
    return await OrderCrud.read_orders_services_by_order_id(order_id)

@router.get("/service/order/")
async def read_orders_services_by_order_id_2(request: Request, order_id: int):
    """
    Retrieve order services by order ID.
    """
    return await OrderCrud.read_orders_services_by_order_id(order_id)

@router.put("/service/{_id}")
async def update_order_service(request: Request, _id: int, fields: dict):
    """
    Update an existing order service by ID.
    """
    return await OrderCrud.update_order_service(_id, fields)

@router.delete("/service/{_id}")
async def delete_order_service(request: Request, _id: int):
    """
    Delete an order service by ID.
    """
    return await OrderCrud.delete_order_service(_id)

@router.delete("/service/")
async def delete_order_service_2(request: Request, id: int):
    """
    Delete an order service by ID.
    """
    return await OrderCrud.delete_order_service(id)


@router.post("/product/")
async def create_order_product(request: Request, order_product: OrderProductCreate):
    """
    Create a new order product.
    """
    return await OrderCrud.create_order_product(order_product)

@router.get("/product/{_id}")
async def read_order_product(request: Request, _id: int):
    """
    Retrieve an order product by ID.
    """
    return await OrderCrud.read_order_product(_id)

@router.get("/product/")
async def read_order_product_2(request: Request, id: int):
    """
    Retrieve an order product by ID.
    """
    return await OrderCrud.read_order_product(id)

@router.put("/product/{_id}")
async def update_order_product(request: Request, _id: int, fields: dict):
    """
    Update an existing order product by ID.
    """
    return await OrderCrud.update_order_product(_id, fields)

@router.delete("/product/{_id}")
async def delete_order_product(request: Request, _id: int):
    """
    Delete an order product by ID.
    """
    return await OrderCrud.delete_order_product(_id)

@router.delete("/product/")
async def delete_order_product_2(request: Request, id: int):
    """
    Delete an order product by ID.
    """
    return await OrderCrud.delete_order_product(id)


@router.get("/product/order/{order_id}")
async def read_orders_products_by_order_id(request: Request, order_id: int):
    """
    Retrieve order products by order ID.
    """
    return await OrderCrud.read_orders_products_by_order_id(order_id)

@router.get("/product/order/")
async def read_order_products_by_order_id_2(request: Request, order_id: int):
    """
    Retrieve order products by order ID.
    """
    return await OrderCrud.read_orders_products_by_order_id(order_id)

@router.get("/client/{client_id}")
async def search_orders_by_client_id(request: Request, client_id: int):
    """
    Retrieve orders by client ID.
    """
    return await OrderService.search_orders_by_client_id(client_id)

@router.get("/client/")
async def search_orders_by_client_id_2(request: Request, client_id: int):
    """
    Retrieve orders by client ID.
    """
    return await OrderService.search_orders_by_client_id(client_id)

@router.get("/status/{status}")
async def search_orders_by_status(request: Request, status: OrderStatus):
    """
    Retrieve orders by status.
    """
    return await OrderService.search_orders_by_status(status)

@router.get("/status/")
async def search_orders_by_status_2(request: Request, status: OrderStatus):
    """
    Retrieve orders by status.
    """
    return await OrderService.search_orders_by_status(status)
