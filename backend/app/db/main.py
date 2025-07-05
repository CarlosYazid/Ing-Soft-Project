from supabase import acreate_client, AsyncClient
from core import SETTINGS

async def get_db_client() -> AsyncClient:
    return await acreate_client(SETTINGS.db_url, SETTINGS.db_key.get_secret_value())

