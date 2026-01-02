from fastapi import APIRouter, Request, Depends
from botocore.client import BaseClient
from sqlmodel.ext.asyncio import AsyncSession

from models import PaymentCreate, PaymentRead, PaymentUpdate, PaymentMethod, PaymentStatus
from crud import PaymentCrud
from services import AuthService, PaymentService, FileService
from core import get_e2_client
from db import get_session

router = APIRouter(prefix="/others")

@router.get("/files/{key:path}")
async def get_file(request: Request,
                   key: str,
                   storage_client: BaseClient = Depends(get_e2_client)):
    """
    Retrieve a file by name.
    """
    return await FileService.get_file(storage_client, key)

@router.post("/payment", response_model = PaymentRead)
async def create_payment(request: Request,
                         payment: PaymentCreate,
                         db_session: AsyncSession = Depends(get_session)):
    """
    Create a new payment.
    """
    return await PaymentCrud.create_payment(db_session, payment)

@router.get("/payment/all", response_model = list[PaymentRead])
async def read_all_payments(request: Request,
                            db_session: AsyncSession = Depends(get_session)):
    return await PaymentCrud.read_all_payments(db_session)

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


@router.put("/payment/", response_model = PaymentRead)
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

@router.get("/payment/search/client/{client_id}", response_model = list[PaymentRead])
async def search_payments_by_client(request: Request,
                                    client_id: int,
                                    db_session: AsyncSession = Depends(get_session)):
    """
    Retrieve payments by client ID.
    """
    return await PaymentService.search_payments_by_client_id(db_session, client_id)

@router.get("/payment/search/client/", response_model = list[PaymentRead])
async def search_payments_by_client_2(request: Request,
                                      client_id: int,
                                      db_session: AsyncSession = Depends(get_session)):
    """
    Retrieve payments by client ID.
    """
    return await PaymentService.search_payments_by_client_id(db_session, client_id)

@router.get("/payment/search/status/{status}", response_model = list[PaymentRead])
async def search_payments_by_status(request: Request,
                                    status: PaymentStatus,
                                    db_session: AsyncSession = Depends(get_session)):
    """
    Retrieve payments by status.
    """
    return await PaymentService.search_payments_by_status(db_session, status)

@router.get("/payment/search/status/", response_model = list[PaymentRead])
async def search_payments_by_status_2(request: Request,
                                      status: PaymentStatus,
                                      db_session: AsyncSession = Depends(get_session)):
    """
    Retrieve payments by status.
    """
    return await PaymentService.search_payments_by_status(db_session, status)

@router.get("/payment/search/method/{method}", response_model = list[PaymentRead])
async def search_payments_by_method(request : Request,
                                    method: PaymentMethod,
                                    db_session: AsyncSession = Depends(get_session)):
    """
    Retrieve payments by method.
    """
    return await PaymentService.search_payments_by_method(db_session, method)

@router.get("/payment/search/method/", response_model = list[PaymentRead])
async def search_payments_by_method_2(request: Request,
                                      method: PaymentMethod,
                                      db_session: AsyncSession = Depends(get_session)):
    """
    Retrieve payments by method.
    """
    return await PaymentService.search_payments_by_method(db_session, method)