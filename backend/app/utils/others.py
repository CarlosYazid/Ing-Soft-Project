from db import get_db_client
from core import SETTINGS

class PaymentUtils:
    
    @classmethod
    async def exist_payment(cls, payment_id: int) -> bool:
        """Check if a payment exists by ID."""
        client = await get_db_client()

        response = await client.table(SETTINGS.payment_table).select("id").eq("id", payment_id).execute()

        return bool(response.data)