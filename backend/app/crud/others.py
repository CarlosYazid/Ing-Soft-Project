from fastapi import HTTPException
from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession

from models import Payment, PaymentCreate, PaymentUpdate
from utils import PaymentUtils

class PaymentCrud:
    
    EXCLUDED_FIELDS_FOR_UPDATE = {"id"}
    
    @classmethod
    async def create_payment(cls, db_session: AsyncSession, payment: PaymentCreate) -> Payment:
        """Create a new payment."""
        
        try:
            
            async with db_session as session:

                # Create the payment
                new_payment = Payment(**payment.model_dump(exclude_unset=True))
                session.add(new_payment)
            
            await session.refresh(new_payment)
            return new_payment
        
        except Exception as e:
            raise HTTPException(detail="Failed to create payment", status_code=500) from e
    
    @classmethod
    async def read_all_payments(cls, db_session: AsyncSession) -> list[Payment]:
        """Retrieve all payments."""
        
        try:
            
            response = await db_session.exec(select(Payment))
            payments = list(response.all())
            
            if not payments:
                raise HTTPException(detail="No payments found", status_code=404)
            
            return payments
        
        except Exception as e:
            raise HTTPException(detail="Failed to retrieve payments", status_code=500) from e

    @classmethod
    async def read_payment(cls, db_session: AsyncSession, payment_id: int) -> Payment:
        """Retrieve a payment by ID."""
        try:

            response = await db_session.exec(select(Payment).where(Payment.id == payment_id))
            payment = response.first()

            if payment is None:
                raise HTTPException(detail="Payment not found", status_code=404)

            return payment

        except Exception as e:
            raise HTTPException(detail="Failed to retrieve payment", status_code=500) from e
    
    @classmethod
    async def update_payment(cls, db_session: AsyncSession, fields: PaymentUpdate) -> Payment:
        """Update an existing payment."""
        
        if fields.id is None:
            raise HTTPException(detail="Payment ID is required", status_code=400)

        # check if payment exists
        if not await PaymentUtils.exist_payment(db_session, fields.id):
            raise HTTPException(detail="Payment not found", status_code=404)
        
        try:
            
            response = await db_session.exec(select(Payment).where(Payment.id == fields.id))
            payment = response.one()
            
            for key, value in fields.model_dump(exclude_unset=True).items():
                    
                if key in cls.EXCLUDED_FIELDS_FOR_UPDATE:
                    continue
                    
                setattr(payment, key, value)

            db_session.add(payment)
            await db_session.commit()
            
            await db_session.refresh(payment)
            return payment
        
        except Exception as e:
            await db_session.rollback()
            raise HTTPException(detail="Failed to update payment", status_code=500) from e
    
    @classmethod
    async def delete_payment(cls, db_session: AsyncSession, payment_id: int) -> bool:
        """Delete a payment by ID."""
        
        if not await PaymentUtils.exist_payment(db_session, payment_id):
            raise HTTPException(detail="Payment not found", status_code=404)
        
        try:
            
            response = await db_session.exec(select(Payment).where(Payment.id == payment_id))

            await db_session.delete(response.one())
            await db_session.commit()
            
            return True
        
        except Exception as e:
            await db_session.rollback()
            raise HTTPException(detail="Failed to delete payment", status_code=500) from e