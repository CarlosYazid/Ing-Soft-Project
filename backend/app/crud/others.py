from fastapi import HTTPException

from db import get_db_client
from models import Payment, PaymentStatus, PaymentMethod
from core import SETTINGS

class PaymentCrud:
    @classmethod
    async def create_payment(cls, payment: Payment) -> Payment:
        """Create a new payment."""
        client = await get_db_client()

        response = await client.table(SETTINGS.payment_table).insert(payment.model_dump()).execute()

        if not(bool(response.data)):
            raise HTTPException(detail="Failed to create payment", status_code=500)

        return Payment.model_validate(response.data[0])

    @classmethod
    async def get_payment_by_id(cls, payment_id: int) -> Payment:
        """Retrieve a payment by ID."""
        client = await get_db_client()

        response = await client.table(SETTINGS.payment_table).select("*").eq("id", payment_id).execute()

        if not(bool(response.data)):
            raise HTTPException(detail="Payment not found", status_code=404)

        return Payment.model_validate(response.data[0])
    
    @classmethod
    async def update_payment(cls, payment_id: int, fields: dict) -> Payment:
        """Update an existing payment."""
        client = await get_db_client()

        response = await client.table(SETTINGS.payment_table).update(fields).eq("id", payment_id).execute()

        if not(bool(response.data)):
            raise HTTPException(detail="Failed to update payment", status_code=500)

        return Payment.model_validate(response.data[0])
    
    @classmethod
    async def delete_payment(cls, payment_id: int) -> None:
        """Delete a payment by ID."""
        client = await get_db_client()

        response = await client.table(SETTINGS.payment_table).delete().eq("id", payment_id).execute()

        if not(bool(response.data)):
            raise HTTPException(detail="Failed to delete payment", status_code=500)
        
    @classmethod
    async def get_payments_by_status(cls, status: PaymentStatus) -> list[Payment]:
        """Retrieve payments by status."""
        client = await get_db_client()

        response = await client.table(SETTINGS.payment_table).select("*").eq("status", status).execute()

        if not(bool(response.data)):
            raise HTTPException(detail="No payments found for this status", status_code=404)

        return [Payment.model_validate(payment) for payment in response.data]
    
    @classmethod
    async def get_payments_by_method(cls, method: PaymentMethod) -> list[Payment]:
        """Retrieve payments by method."""
        client = await get_db_client()

        response = await client.table(SETTINGS.payment_table).select("*").eq("method", method).execute()

        if not(bool(response.data)):
            raise HTTPException(detail="No payments found for this method", status_code=404)

        return [Payment.model_validate(payment) for payment in response.data]
    
    @classmethod
    async def get_payments_by_user(cls, user_id: int) -> list[Payment]:
        """Retrieve payments by user ID."""
        client = await get_db_client()

        response = await client.table(SETTINGS.payment_table).select("*").eq("user_id", user_id).execute()

        if not(bool(response.data)):
            raise HTTPException(detail="No payments found for this user", status_code=404)

        return [Payment.model_validate(payment) for payment in response.data]
    
    @classmethod
    async def get_all_payments(cls) -> list[Payment]:
        """Retrieve all payments."""
        client = await get_db_client()

        response = await client.table(SETTINGS.payment_table).select("*").execute()

        if not(bool(response.data)):
            raise HTTPException(detail="No payments found", status_code=404)

        return [Payment.model_validate(payment) for payment in response.data]