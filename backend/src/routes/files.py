from fastapi import APIRouter, Request, Depends
from botocore.client import BaseClient

from services import AuthService, PaymentService, FileService
from core import get_e2_client

router = APIRouter(prefix="/files")

@router.get("/{key:path}")
async def get_file(request: Request,
                   key: str,
                   storage_client: BaseClient = Depends(get_e2_client)):
    """
    Retrieve a file by name.
    """
    return await FileService.get_file(storage_client, key)