from fastapi import HTTPException

from db import get_db_client
from models import Payment, PaymentCreate, PaymentBasePlusID
from core import SETTINGS
from utils import PaymentUtils

class PaymentCrud:
    
    EXCLUDED_FIELDS_FOR_UPDATE = {"client_id", "created_at"}
    ALLOWED_FIELDS_FOR_UPDATE = set(PaymentCreate.__fields__.keys()) - EXCLUDED_FIELDS_FOR_UPDATE
    
    FIELDS_PAYMENT_BASE = set(PaymentBasePlusID.__fields__.keys())
    
    @classmethod
    async def create_payment(cls, payment: PaymentCreate) -> Payment:
        """Create a new payment."""
        client = await get_db_client()

        response = await client.table(SETTINGS.payment_table).insert(payment.model_dump(mode="json")).execute()

        if not bool(response.data):
            raise HTTPException(detail="Failed to create payment", status_code=500)

        return Payment.model_validate(response.data[0])
    
    @classmethod
    async def read_all_payments(cls) -> list[Payment]:
        """Retrieve all payments."""
        client = await get_db_client()

        response = await client.table(SETTINGS.payment_table).select("*").execute()

        if not bool(response.data):
            raise HTTPException(detail="No payments found", status_code=404)

        return [Payment.model_validate(payment) for payment in response.data]

    @classmethod
    async def read_all_payments_base(cls) -> list[PaymentBasePlusID]:
        """Retrieve all payments."""
        
        client = await get_db_client()
        
        response = await client.table(SETTINGS.payment_table).select(*cls.FIELDS_PAYMENT_BASE).execute()

        if not bool(response.data):
            raise HTTPException(detail="No payments found", status_code=404)

        return [PaymentBasePlusID.model_validate(payment) for payment in response.data]

    @classmethod
    async def read_payment(cls, payment_id: int) -> Payment:
        """Retrieve a payment by ID."""
        client = await get_db_client()

        response = await client.table(SETTINGS.payment_table).select("*").eq("id", payment_id).execute()

        if not bool(response.data):
            raise HTTPException(detail="Payment not found", status_code=404)

        return Payment.model_validate(response.data[0])
    
    @classmethod
    async def read_payment_base(cls, payment_id: int) -> PaymentBasePlusID:
        """Retrieve a payment by ID."""
        
        client = await get_db_client()

        response = await client.table(SETTINGS.payment_table).select(*cls.FIELDS_PAYMENT_BASE).eq("id", payment_id).execute()

        if not bool(response.data):
            raise HTTPException(detail="Payment not found", status_code=404)

        return PaymentBasePlusID.model_validate(response.data[0])
    
    @classmethod
    async def update_payment(cls, payment_id: int, fields: dict) -> Payment:
        """Update an existing payment."""

        # check if payment exists
        if not await PaymentUtils.exist_payment(payment_id):
            raise HTTPException(detail="Payment not found", status_code=404)
        
        if any(field in fields for field in cls.EXCLUDED_FIELDS_FOR_UPDATE):
            raise HTTPException(detail=f"Cannot update: {', '.join(cls.EXCLUDED_FIELDS_FOR_UPDATE)}", status_code=400)

        if not(set(fields.keys()) < cls.ALLOWED_FIELDS_FOR_UPDATE):
            raise HTTPException(detail="Update attribute of payment", status_code=400)
        
        client = await get_db_client()

        response = await client.table(SETTINGS.payment_table).update(fields).eq("id", payment_id).execute()

        if not bool(response.data):
            raise HTTPException(detail="Failed to update payment", status_code=500)

        return Payment.model_validate(response.data[0])
    
    @classmethod
    async def delete_payment(cls, payment_id: int) -> None:
        """Delete a payment by ID."""
        
        if not await PaymentUtils.exist_payment(payment_id):
            raise HTTPException(detail="Payment not found", status_code=404)
        
        client = await get_db_client()

        response = await client.table(SETTINGS.payment_table).delete().eq("id", payment_id).execute()

        if not bool(response.data):
            raise HTTPException(detail="Failed to delete payment", status_code=500)
        
        return bool(response.data)