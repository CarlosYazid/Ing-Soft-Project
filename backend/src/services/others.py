from fastapi import HTTPException
from botocore.client import BaseClient
from starlette.responses import StreamingResponse
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlmodel import select
from sqlalchemy.sql.expression import Select

from models import Payment, PaymentMethod, PaymentStatus
from core import SETTINGS

class PaymentService:

    @staticmethod
    def read_all_payments() -> Select:
        """Query for retrieve all payments."""
        return select(Payment)
    
    @staticmethod
    def search_payments_by_status(status: PaymentStatus) -> Select:
        """Query for retrieve payments by status."""
        return select(Payment).where(Payment.status is status)
    
    @staticmethod
    def search_payments_by_method(method: PaymentMethod) -> Select:
        """Query for retrieve payments by method."""
        return select(Payment).where(Payment.method is method)
    
    @staticmethod
    def search_payments_by_client(client_id: int) -> Select:
        """Query for retrieve payments by client."""
        return select(Payment).where(Payment.client_id == client_id)
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
