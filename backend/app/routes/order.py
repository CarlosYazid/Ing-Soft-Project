from fastapi import APIRouter, Request, Depends
from sqlmodel.ext.asyncio import AsyncSession

from models import OrderRead, OrderUpdate, OrderCreate, OrderStatus, OrderService, OrderProduct
from crud import OrderCrud
from services import AuthService, OrderService as OrderServiceService
from db import get_session


router = APIRouter(prefix="/order")

@router.post("/", response_model=OrderRead)
async def create_order(request: Request,
                       order: OrderCreate,
                       db_session: AsyncSession = Depends(get_session)):
    """
    Create a new order.
    """
    return await OrderCrud.create_order(db_session, order)

@router.get("/all", response_model=list[OrderRead])
async def read_all_orders(request: Request,
                          db_session: AsyncSession = Depends(get_session)):
    """
    Retrieve all orders.
    """
    return await OrderCrud.read_all_orders(db_session)

@router.get("/{_id}", response_model=OrderRead)
async def read_order(request: Request,
                     _id: int,
                     db_session: AsyncSession = Depends(get_session)):
    """
    Retrieve an order by ID.
    """
    return await OrderCrud.read_order(db_session, _id)

@router.get("/", response_model=OrderRead)
async def read_order_2(request: Request,
                       id: int,
                       db_session: AsyncSession = Depends(get_session)):
    """
    Retrieve an order by ID.
    """
    return await OrderCrud.read_order(db_session, id)

@router.put("/", response_model=OrderRead)
async def update_order(request: Request,
                       fields : OrderUpdate,
                       db_session: AsyncSession = Depends(get_session)):
    """
    Update an existing order by ID.
    """
    return await OrderCrud.update_order(db_session, fields)

@router.put('/status/{order_id}/{status}', response_model=OrderRead)
async def update_order_status(request: Request,
                              order_id: int,
                              status: OrderStatus,
                              db_session: AsyncSession = Depends(get_session)):
    """
    Update status of a order
    """
    return await OrderCrud.update_order_status(db_session, order_id, status)

@router.put('/status/', response_model=OrderRead)
async def update_order_status_2(request: Request,
                                order_id: int,
                                status: OrderStatus,
                                db_session: AsyncSession = Depends(get_session)):
    """
    Update status of a order
    """
    return await OrderCrud.update_order_status(db_session, order_id, status)

@router.delete("/{_id}")
async def delete_order(request: Request,
                       _id: int,
                       db_session: AsyncSession = Depends(get_session)):
    """
    Delete an order by ID.
    """
    return await OrderCrud.delete_order(db_session, _id)

@router.delete("/", response_model=OrderRead)
async def delete_order_2(request: Request,
                         id: int,
                         db_session: AsyncSession = Depends(get_session)):
    """
    Delete an order by ID.
    """
    return await OrderCrud.delete_order(db_session, id)

@router.post("/service/", response_model=OrderService)
async def create_order_service(request: Request,
                               order_service: OrderService,
                               db_session: AsyncSession = Depends(get_session)):
    """
    Create a new order service.
    """
    return await OrderCrud.create_order_service(db_session, order_service)

@router.get("/service/order/{order_id}", response_model=list[OrderService])
async def read_orders_services_by_order(request: Request,
                                        order_id: int,
                                        db_session: AsyncSession = Depends(get_session)):
    """
    Retrieve order services by order ID.
    """
    return await OrderCrud.read_orders_services_by_order(db_session, order_id)

@router.get("/service/order/", response_model=list[OrderService])
async def read_orders_services_by_order_2(request: Request,
                                          order_id: int,
                                          db_session: AsyncSession = Depends(get_session)):
    """
    Retrieve order services by order ID.
    """
    return await OrderCrud.read_orders_services_by_order(db_session, order_id)

@router.delete("/service/{_id}", response_model=OrderService)
async def delete_order_service(request: Request, 
                               _id: int,
                               db_session: AsyncSession = Depends(get_session)):
    """
    Delete an order service by ID.
    """
    return await OrderCrud.delete_order_service(db_session, _id)

@router.delete("/service/", response_model=OrderService)
async def delete_order_service_2(request: Request,
                                 id: int,
                                 db_session: AsyncSession = Depends(get_session)):
    """
    Delete an order service by ID.
    """
    return await OrderCrud.delete_order_service(db_session, id)

@router.post("/product/", response_model=OrderProduct)
async def create_order_product(request: Request,
                               order_product: OrderProduct,
                               db_session: AsyncSession = Depends(get_session)):
    """
    Create a new order product.
    """
    return await OrderCrud.create_order_product(db_session, order_product)

@router.get("/product/{_id}", response_model=OrderProduct)
async def read_order_product(request: Request,
                             _id: int,
                             db_session: AsyncSession = Depends(get_session)):
    """
    Retrieve an order product by ID.
    """
    return await OrderCrud.read_order_product(db_session, _id)

@router.get("/product/", response_model=OrderProduct)
async def read_order_product_2(request: Request,
                               id: int,
                               db_session: AsyncSession = Depends(get_session)):
    """
    Retrieve an order product by ID.
    """
    return await OrderCrud.read_order_product(db_session, id)

@router.delete("/product/{_id}")
async def delete_order_product(request: Request,
                               order_product: OrderProduct,
                               db_session: AsyncSession = Depends(get_session)):
    """
    Delete an order product by ID.
    """
    return await OrderCrud.delete_order_product(db_session, order_product)

@router.delete("/product/")
async def delete_order_product_2(request: Request,
                                 order_product: OrderProduct,
                                 db_session: AsyncSession = Depends(get_session)):
    """
    Delete an order product by ID.
    """
    return await OrderCrud.delete_order_product(db_session, order_product)


@router.get("/product/order/{order_id}", response_model=list[OrderProduct])
async def read_orders_products_by_order(request: Request,
                                        order_id: int,
                                        db_session: AsyncSession = Depends(get_session)):
    """
    Retrieve order products by order ID.
    """
    return await OrderCrud.read_orders_products_by_order(db_session, order_id)

@router.get("/product/order/")
async def read_order_products_by_order_2(request: Request,
                                         order_id: int,
                                         db_session: AsyncSession = Depends(get_session)):
    """
    Retrieve order products by order ID.
    """
    return await OrderCrud.read_orders_products_by_order(db_session, order_id)

@router.get("/client/{client_id}", response_model=list[OrderRead])
async def search_orders_by_client_id(request: Request,
                                     client_id: int,
                                     db_session: AsyncSession = Depends(get_session)):
    """
    Retrieve orders by client ID.
    """
    return await OrderServiceService.search_orders_by_client(db_session, client_id)

@router.get("/client/", response_model=list[OrderRead])
async def search_orders_by_client_id_2(request: Request,
                                       client_id: int,
                                       db_session: AsyncSession = Depends(get_session)):
    """
    Retrieve orders by client ID.
    """
    return await OrderServiceService.search_orders_by_client(db_session, client_id)

@router.get("/status/{status}", response_model=list[OrderRead])
async def search_orders_by_status(request: Request,
                                  status: OrderStatus,
                                  db_session: AsyncSession = Depends(get_session)):
    """
    Retrieve orders by status.
    """
    return await OrderServiceService.search_orders_by_status(db_session, status)

@router.get("/status/", response_model=list[OrderRead])
async def search_orders_by_status_2(request: Request,
                                    status: OrderStatus,
                                    db_session: AsyncSession = Depends(get_session)):
    """
    Retrieve orders by status.
    """
    return await OrderServiceService.search_orders_by_status(db_session, status)
