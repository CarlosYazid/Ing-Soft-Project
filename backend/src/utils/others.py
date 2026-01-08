from sqlmodel.ext.asyncio.session import AsyncSession
from sqlmodel import select
from fastapi import HTTPException

from models import Payment

class PaymentUtils:
    
    @classmethod
    async def exist_payment(cls, db_session: AsyncSession, payment_id: int) -> bool:
        """Check if a payment exists by ID."""
        
        try:
            
            response = await db_session.exec(select(Payment).where(Payment.id == payment_id))
            
            return bool(response.first())
        
        except Exception as e:
            raise HTTPException(detail="Payment existence check failed", status_code=500) from e