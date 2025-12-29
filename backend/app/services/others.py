from fastapi import HTTPException
from botocore.client import BaseClient
from starlette.responses import StreamingResponse
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlmodel import select

from models import Payment, PaymentMethod, PaymentStatus
from core import SETTINGS

class PaymentService:

    
    @classmethod
    async def search_payments_by_status(cls, db_session: AsyncSession, status: PaymentStatus) -> list[Payment]:
        """Retrieve payments by status."""
        
        try:
            
            response = await db_session.exec(select(Payment).where(Payment.status is status))
            payments = list(response.all())
            
            if not payments:
                raise HTTPException(detail="Payments not found", status_code=404)
            
            return payments
        
        except Exception as e:
            raise HTTPException(detail="Payment searching", status_code=500) from e
    
    @classmethod
    async def search_payments_by_method(cls, db_session: AsyncSession, method: PaymentMethod) -> list[Payment]:
        """Retrieve payments by method."""
        
        try:
            
            response = await db_session.exec(select(Payment).where(Payment.method is method))
            payments = list(response.all())
            
            if not payments:
                raise HTTPException(detail="Payments not found", status_code=404)
            
            return payments
        
        except Exception as e:
            raise HTTPException(detail="Failed", status_code=500) from e
    
    @classmethod
    async def search_payments_by_client_id(cls, db_session: AsyncSession, client_id: int) -> list[Payment]:
        """Retrieve payments by client ID."""
        
        try:
            
            response = await db_session.exec(select(Payment).where(Payment.client_id == client_id))
            payments = list(response.all())
            
            if not payments:
                raise HTTPException(detail="Payments not found", status_code= 404)
            
            return payments
        
        except Exception as e:
            raise HTTPException(detail="", status_code=500) from e
class FileService:
    
    @classmethod
    async def get_file(cls, storage_client: BaseClient, key: str):
        """Retrieve a file by name."""
        
        try:
        
            obj = await storage_client.get_object(Bucket=SETTINGS.bucket_name, Key=key)

            content_type = obj.get("ContentType", "application/octet-stream")

            return StreamingResponse(
                obj["Body"],
                media_type=content_type,
                headers={
                    "Content-Disposition": f'inline; filename="{key.split("/")[-1]}"'
                }
            )
        
        except Exception as e:
            raise HTTPException(detail="Retrieve file failed", status_code=500) from e
