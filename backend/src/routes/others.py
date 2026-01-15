from fastapi import APIRouter, Request, Depends
from fastapi_pagination import Page
from fastapi_pagination.ext.sqlmodel import apaginate
from sqlmodel.ext.asyncio.session import AsyncSession

from models import PaymentMethod, PaymentStatus
from dtos import PaymentCreate, PaymentRead, PaymentUpdate, PaymentFilter
from crud import PaymentCrud
from services import AuthService, PaymentService
from db import get_session

router = APIRouter(prefix="/others")

@router.post("/payment", response_model = PaymentRead)
async def create_payment(request: Request,
                         payment: PaymentCreate,
                         db_session: AsyncSession = Depends(get_session)):
    """
    Create a new payment.
    """
    return await PaymentCrud.create_payment(db_session, payment)

@router.get("/payment/{_id}", response_model = PaymentRead)
async def read_payment(request: Request,
                       _id: int,
                       db_session: AsyncSession = Depends(get_session)):
    """
    Retrieve a payment by ID.
    """
    return await PaymentCrud.read_payment(db_session, _id)

@router.get("/payment/", response_model = PaymentRead)
async def read_payment_2(request: Request,
                         id: int,
                         db_session: AsyncSession = Depends(get_session)):
    """
    Retrieve a payment by ID.
    """
    return await PaymentCrud.read_payment(db_session, id)

@router.patch("/payment/", response_model = PaymentRead)
async def update_payment(request: Request,
                         fields: PaymentUpdate,
                         db_session: AsyncSession = Depends(get_session)):
    """
    Update an existing payment by ID.
    """
    return await PaymentCrud.update_payment(db_session, fields)

@router.delete("/payment/{_id}")
async def delete_payment(request: Request,
                         _id: int,
                         db_session: AsyncSession = Depends(get_session)):
    """
    Delete a payment by ID.
    """
    return await PaymentCrud.delete_payment(db_session, _id)

@router.delete("/payment/")
async def delete_payment_2(request: Request,
                           id: int,
                           db_session: AsyncSession = Depends(get_session)):
    """
    Delete a payment by ID.
    """
    return await PaymentCrud.delete_payment(db_session, id)

@router.post("/payment/search", response_model = Page[PaymentRead])
async def search_payments(request: Request,
                          filters: PaymentFilter,
                          db_session: AsyncSession = Depends(get_session)):
    """
    Search payments who meet the filters.
    """
    return await apaginate(db_session, PaymentService.search_payments(filters))