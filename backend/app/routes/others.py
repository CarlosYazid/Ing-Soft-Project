from fastapi import APIRouter, Request, Depends

from models import PaymentCreate, PaymentMethod, PaymentStatus
from crud import PaymentCrud
from services import AuthService, PaymentService


router = APIRouter(prefix="/payment")

@router.post("/")
async def create_payment(request: Request, payment: PaymentCreate):
    """
    Create a new payment.
    """
    return await PaymentCrud.create_payment(payment)

@router.get("/all")
async def read_all_payments(request: Request):
    return await PaymentCrud.read_all_payments()

@router.get("/base/all")
async def read_all_payments_base(request: Request):
    """
    Retrieve all payments in base format.
    """
    return await PaymentCrud.read_all_payments_base()

@router.get("/{_id}")
async def read_payment(request: Request, _id: int):
    """
    Retrieve a payment by ID.
    """
    return await PaymentCrud.read_payment(_id)

@router.get("/")
async def read_payment_2(request: Request, id: int):
    """
    Retrieve a payment by ID.
    """
    return await PaymentCrud.read_payment(id)

@router.get("/base/{_id}")
async def read_payment_base(request: Request, _id: int):
    """
    Get a payment base by ID.
    """
    return await PaymentCrud.read_payment_base(_id)

@router.get("/base/")
async def read_payment_base_2(request: Request, id: int):
    """
    Get a payment base by ID.
    """
    return await PaymentCrud.read_payment_base(id)

@router.put("/{_id}")
async def update_payment(request: Request, _id: int, fields: dict):
    """
    Update an existing payment by ID.
    """
    return await PaymentCrud.update_payment(_id, fields)

@router.delete("/{_id}")
async def delete_payment(request: Request, _id: int):
    """
    Delete a payment by ID.
    """
    return await PaymentCrud.delete_payment(_id)

@router.delete("/")
async def delete_payment_2(request: Request, id: int):
    """
    Delete a payment by ID.
    """
    return await PaymentCrud.delete_payment(id)

@router.get("/search/client/{client_id}")
async def search_payments_by_client(request: Request, client_id: int):
    """
    Retrieve payments by client ID.
    """
    return await PaymentService.search_payments_by_client_id(client_id)

@router.get("/search/client/")
async def search_payments_by_client_2(request: Request, client_id: int):
    """
    Retrieve payments by client ID.
    """
    return await PaymentService.search_payments_by_client_id(client_id)

@router.get("/search/status/{status}")
async def search_payments_by_status(request: Request, status: PaymentStatus):
    """
    Retrieve payments by status.
    """
    return await PaymentService.search_payments_by_status(status)

@router.get("/search/status/")
async def search_payments_by_status_2(request: Request, status: PaymentStatus):
    """
    Retrieve payments by status.
    """
    return await PaymentService.search_payments_by_status(status)

@router.get("/search/method/{method}")
async def search_payments_by_method(request : Request, method: PaymentMethod):
    """
    Retrieve payments by method.
    """
    return await PaymentService.search_payments_by_method(method)

@router.get("/search/method/")
async def search_payments_by_method_2(request: Request, method: PaymentMethod):
    """
    Retrieve payments by method.
    """
    return await PaymentService.search_payments_by_method(method)