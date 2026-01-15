from fastapi import HTTPException
from botocore.client import BaseClient
from starlette.responses import StreamingResponse
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlmodel import select
from sqlalchemy.sql.expression import Select

from models import Payment, PaymentMethod, PaymentStatus
from core import SETTINGS
from dtos import PaymentFilter
from core import log_operation
class PaymentService:
    
    QUERY_PAYMENT_BASE = select(Payment)

    @classmethod
    def search_payments(cls, filters : PaymentFilter) -> Select:
        """Query that searches for payments who meet the filters."""
        return filters.apply(cls.QUERY_PAYMENT_BASE)
    
class FileService:
    
    @staticmethod
    @log_operation(True)
    async def get_file(storage_client: BaseClient, key: str):
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
