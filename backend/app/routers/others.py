from fastapi import APIRouter, Request, Depends

from models import PaymentCreate, PaymentMethod, PaymentStatus
from crud import PaymentCrud
from services import AuthService, PaymentService


router = APIRouter(prefix="/payment")

@router.get("/all")
async def get_payments(request: Request):
    return await PaymentCrud.get_all_payments()

@router.get("/base/all")
async def get_payments_base(request: Request):
    """
    Retrieve all payments in base format.
    """
    return await PaymentService.get_all_payments_base()

@router.get("/{_id}")
async def get_payment_by_id(request: Request, _id: int):
    """
    Retrieve a payment by ID.
    """
    return await PaymentCrud.get_payment_by_id(_id)

@router.get("/")
async def get_payment_by_id_2(request: Request, id: int):
    """
    Retrieve a payment by ID.
    """
    return await PaymentCrud.get_payment_by_id(id)

@router.get("/base/{_id}")
async def get_payment_base_by_id(request: Request, _id: int):
    """
    Get a payment base by ID.
    """
    return await PaymentService.get_payment_base_by_id(_id)

@router.get("/base/")
async def get_payment_base_by_id_2(request: Request, id: int):
    """
    Get a payment base by ID.
    """
    return await PaymentService.get_payment_base_by_id(id)

@router.post("/")
async def create_payment(request: Request, payment: PaymentCreate):
    """
    Create a new payment.
    """
    return await PaymentCrud.create_payment(payment)

@router.put("/{_id}")
async def update_payment_by_id(request: Request, _id: int, fields: dict):
    """
    Update an existing payment by ID.
    """
    return await PaymentCrud.update_payment(_id, fields)

@router.get("/user/{user_id}")
async def get_payments_by_user(request: Request, user_id: int):
    """
    Retrieve payments by user ID.
    """
    return await PaymentCrud.get_payments_by_user(user_id)

@router.get("/base/user/{user_id}")
async def get_payments_base_by_user(request: Request, user_id: int):
    """
    Retrieve payments by user ID in base format.
    """
    return await PaymentService.get_payments_base_by_user(user_id)

@router.get("/user/")
async def get_payments_by_user_2(request: Request, user_id: int):
    """
    Retrieve payments by user ID.
    """
    return await PaymentCrud.get_payments_by_user(user_id)

@router.get("/base/user/")
async def get_payments_base_by_user_2(request: Request, user_id: int):
    """
    Retrieve payments by user ID in base format.
    """
    return await PaymentService.get_payments_base_by_user(user_id)

@router.get("/status/{status}")
async def get_payments_by_status(request: Request, status: PaymentStatus):
    """
    Retrieve payments by status.
    """
    return await PaymentCrud.get_payments_by_status(status)

@router.get("/base/status/{status}")
async def get_payments_base_by_status(request: Request, status: PaymentStatus):
    """
    Retrieve payments by status in base format.
    """
    return await PaymentService.get_payments_base_by_status(status)

@router.get("/method/{method}")
async def get_payments_by_method(request : Request, method: PaymentMethod):
    """
    Retrieve payments by method.
    """
    return await PaymentCrud.get_payments_by_method(method)

@router.get("/base/method/{method}")
async def get_payments_base_by_method(request : Request, method: PaymentMethod):
    """
    Retrieve payments by method in base format.
    """
    return await PaymentService.get_payments_base_by_method(method)

@router.delete("/{_id}")
async def delete_payment_by_id(request: Request, _id: int):
    """
    Delete a payment by ID.
    """
    return await PaymentCrud.delete_payment(_id)

@router.delete("/")
async def delete_payment_by_id_2(request: Request, id: int):
    """
    Delete a payment by ID.
    """
    return await PaymentCrud.delete_payment(id)

@router.get("/status/")
async def get_payments_by_status_2(request: Request, status: PaymentStatus):
    """
    Retrieve payments by status.
    """
    return await PaymentCrud.get_payments_by_status(status)

@router.get("/base/status/")
async def get_payments_base_by_status_2(request: Request, status: PaymentStatus):
    """
    Retrieve payments by status in base format.
    """
    return await PaymentService.get_payments_base_by_status(status)

@router.get("/method/")
async def get_payments_by_method_2(request: Request, method: PaymentMethod):
    """
    Retrieve payments by method.
    """
    return await PaymentCrud.get_payments_by_method(method)

@router.get("/base/method/")
async def get_payments_base_by_method_2(request: Request, method: PaymentMethod):
    """
    Retrieve payments by method in base format.
    """
    return await PaymentService.get_payments_base_by_method(method)