from fastapi import APIRouter, Request, Depends
from fastapi_pagination import Page
from fastapi_pagination.ext.sqlmodel import apaginate
from sqlmodel.ext.asyncio.session import AsyncSession

from models import OrderStatus, OrderService, OrderProduct
from dtos import OrderRead, OrderUpdate, OrderCreate, OrderFilter, OrderProductFilter, OrderServiceFilter
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

@router.patch("/", response_model=OrderRead)
async def update_order(request: Request,
                       fields : OrderUpdate,
                       db_session: AsyncSession = Depends(get_session)):
    """
    Update an existing order by ID.
    """
    return await OrderCrud.update_order(db_session, fields)

@router.patch('/status/{order_id}/{status}', response_model=OrderRead)
async def update_order_status(request: Request,
                              order_id: int,
                              status: OrderStatus,
                              db_session: AsyncSession = Depends(get_session)):
    """
    Update status of a order
    """
    return await OrderCrud.update_order_status(db_session, order_id, status)

@router.patch('/status/', response_model=OrderRead)
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

@router.patch("/service/", response_model=OrderService)
async def update_order_service(request: Request,
                               order_service: OrderService,
                               db_session: AsyncSession = Depends(get_session)):
    """
    Update a order service
    """
    return await OrderCrud.update_order_serivce(db_session, order_service)

@router.delete("/service/{_id}")
async def delete_order_service(request: Request,
                               order_service: OrderService,
                               db_session: AsyncSession = Depends(get_session)):
    """
    Delete an order service.
    """
    return await OrderCrud.delete_order_service(db_session, order_service)

@router.post("/product/", response_model=OrderProduct)
async def create_order_product(request: Request,
                               order_product: OrderProduct,
                               db_session: AsyncSession = Depends(get_session)):
    """
    Create a new order product.
    """
    return await OrderCrud.create_order_product(db_session, order_product)

@router.patch("/product/", response_model=OrderProduct)
async def update_order_product(request: Request,
                               order_product: OrderProduct,
                               db_session: AsyncSession = Depends(get_session)):
    """
    Update a order product
    """
    return await OrderCrud.update_order_product(db_session, order_product)

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

@router.post("/search", response_model=Page[OrderRead])
async def search_orders(request: Request,
                        filters: OrderFilter,
                        db_session: AsyncSession = Depends(get_session)):
    """
    Search orders who meet the filters.
    """
    return await apaginate(db_session, OrderServiceService.search_orders(filters))

@router.post("/service/search", response_model=Page[OrderService])
async def search_order_services(request: Request,
                                 filters: OrderServiceFilter,
                                 db_session: AsyncSession = Depends(get_session)):
    """
    Search orders services who meet the filters.
    """
    return await apaginate(db_session, OrderServiceService.search_order_services(filters))


@router.post("/product/search", response_model=Page[OrderProduct])
async def search_order_products(request: Request,
                                filters: OrderProductFilter,
                                db_session: AsyncSession = Depends(get_session)):
    """
    Search orders products who meet the filters.
    """
    return await apaginate(db_session, OrderServiceService.search_order_products(filters))