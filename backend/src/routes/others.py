from fastapi import APIRouter, Request, Depends
from fastapi_pagination import Page
from fastapi_pagination.ext.sqlmodel import apaginate
from sqlmodel.ext.asyncio.session import AsyncSession

from models import PaymentMethod, PaymentStatus
from schemas import PaymentCreate, PaymentRead, PaymentUpdate
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

@router.get("/payment/all/", response_model = Page[PaymentRead])
async def read_all_payments(request: Request,
                            db_session: AsyncSession = Depends(get_session)):
    return await apaginate(db_session, PaymentService.read_all_payments())

@router.get("/payment/search/client/{client_id}", response_model = Page[PaymentRead])
async def search_payments_by_client(request: Request,
                                    client_id: int,
                                    db_session: AsyncSession = Depends(get_session)):
    """
    Retrieve payments by client ID.
    """
    return await apaginate(db_session, PaymentService.search_payments_by_client(client_id))

@router.get("/payment/search/client/", response_model = Page[PaymentRead])
async def search_payments_by_client_2(request: Request,
                                      client_id: int,
                                      db_session: AsyncSession = Depends(get_session)):
    """
    Retrieve payments by client ID.
    """
    return await apaginate(db_session, PaymentService.search_payments_by_client(client_id))

@router.get("/payment/search/status/{status}", response_model = Page[PaymentRead])
async def search_payments_by_status(request: Request,
                                    status: PaymentStatus,
                                    db_session: AsyncSession = Depends(get_session)):
    """
    Retrieve payments by status.
    """
    return await apaginate(db_session, PaymentService.search_payments_by_status(status))

@router.get("/payment/search/status/", response_model = Page[PaymentRead])
async def search_payments_by_status_2(request: Request,
                                      status: PaymentStatus,
                                      db_session: AsyncSession = Depends(get_session)):
    """
    Retrieve payments by status.
    """
    return await apaginate(db_session, PaymentService.search_payments_by_status(status))

@router.get("/payment/search/method/{method}", response_model = Page[PaymentRead])
async def search_payments_by_method(request : Request,
                                    method: PaymentMethod,
                                    db_session: AsyncSession = Depends(get_session)):
    """
    Retrieve payments by method.
    """
    return await apaginate(db_session, PaymentService.search_payments_by_method(method))

@router.get("/payment/search/method/", response_model = Page[PaymentRead])
async def search_payments_by_method_2(request: Request,
                                      method: PaymentMethod,
                                      db_session: AsyncSession = Depends(get_session)):
    """
    Retrieve payments by method.
    """
    return await apaginate(db_session, PaymentService.search_payments_by_method(method))