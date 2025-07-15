from db import get_db_client
from core import SETTINGS

class ProductUtils:
    
    @classmethod
    async def exist_product(cls, product_id: int) -> bool:
        """Check if a product exists by ID."""

        client = await get_db_client()

        response = await client.table(SETTINGS.product_table).select("id").eq("id", product_id).execute()

        return bool(response.data)
    
    @classmethod
    async def exist_category(cls, category_id: int) -> bool:
        """Check if a category exists by ID."""

        client = await get_db_client()

        response = await client.table(SETTINGS.category_table).select("id").eq("id", category_id).execute()

        return bool(response.data)
    
    @classmethod
    async def exist_product_category(cls, product_category_id: int) -> bool:
        """Check if a product category exists by ID."""

        client = await get_db_client()

        response = await client.table(SETTINGS.product_category_table).select("id").eq("id", product_category_id).execute()

        return bool(response.data)