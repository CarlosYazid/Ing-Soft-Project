from fastapi import HTTPException

from models import PaymentBasePlusID, PaymentMethod, PaymentStatus
from core import SETTINGS
from db import get_db_client

class PaymentService:
    
    @classmethod
    async def search_payments_by_status(cls, status: PaymentStatus) -> list[PaymentBasePlusID]:
        """Retrieve payments by status."""
        
        client = await get_db_client()

        response = await client.table(SETTINGS.payment_table).select("id", "user_id", "amount", "method", "status").eq("status", status.capitalize()).execute()

        if not bool(response.data):
            raise HTTPException(detail="No payments found for this status", status_code=404)

        return [PaymentBasePlusID.model_validate(payment) for payment in response.data]
    
    @classmethod
    async def search_payments_by_method(cls, method: PaymentMethod) -> list[PaymentBasePlusID]:
        """Retrieve payments by method."""
        client = await get_db_client()

        response = await client.table(SETTINGS.payment_table).select("id", "user_id", "amount", "method", "status").eq("method", method.capitalize()).execute()

        if not bool(response.data):
            raise HTTPException(detail="No payments found for this method", status_code=404)

        return [PaymentBasePlusID.model_validate(payment) for payment in response.data]
    
    @classmethod
    async def search_payments_by_user_id(cls, user_id: int) -> list[PaymentBasePlusID]:
        """Retrieve payments by user ID."""
        client = await get_db_client()

        response = await client.table(SETTINGS.payment_table).select("id", "user_id", "amount", "method", "status").eq("user_id", user_id).execute()

        if not bool(response.data):
            raise HTTPException(detail="No payments found for this user", status_code=404)

        return [PaymentBasePlusID.model_validate(payment) for payment in response.data]