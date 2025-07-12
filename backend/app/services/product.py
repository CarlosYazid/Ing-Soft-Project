from fastapi import HTTPException
from datetime import date

from models import ProductBasePlusID, ProductCategory, ProductTypes
from db import get_db_client
from core import SETTINGS
class ProductService:
    
    FIELDS_PRODUCT_BASE = set(ProductBasePlusID.__fields__.keys())
    
    @classmethod
    async def search_products_by_category(cls, category: ProductCategory) -> list[ProductBasePlusID]:
        """Retrieve products by category."""
        
        client = await get_db_client()

        response = await client.table(SETTINGS.product_table).select(*cls.FIELDS_PRODUCT_BASE).eq("category", category.capitalize()).execute()

        if not bool(response.data):
            raise HTTPException(detail="No products found in this category", status_code=404)

        return [ProductBasePlusID.model_validate(product) for product in response.data]


    @classmethod
    async def search_products_by_type(cls, product_type: ProductTypes) -> list[ProductBasePlusID]:
        """Retrieve products by type."""
        client = await get_db_client()

        response = await client.table(SETTINGS.product_table).select(*cls.FIELDS_PRODUCT_BASE).eq("type", product_type.capitalize()).execute()

        if not bool(response.data):
            raise HTTPException(detail="No products found of this type", status_code=404)

        return [ProductBasePlusID.model_validate(product) for product in response.data]


    @classmethod
    async def search_products_by_name(cls, name: str) -> list[ProductBasePlusID]:
        """Search products by name."""

        client = await get_db_client()

        response = await client.table(SETTINGS.product_table).select(*cls.FIELDS_PRODUCT_BASE).ilike("name", f"%{name}%").execute()

        if not bool(response.data):
            raise HTTPException(detail="No products found with this name", status_code=404)

        return [ProductBasePlusID.model_validate(product) for product in response.data]

    @classmethod
    async def search_products_by_price_range(cls, min_price: float, max_price: float) -> list[ProductBasePlusID]:
        """Search products by price range."""

        client = await get_db_client()

        response = await client.table(SETTINGS.product_table).select(*cls.FIELDS_PRODUCT_BASE).gte("price", min_price).lte("price", max_price).execute()

        if not bool(response.data):
            raise HTTPException(detail="No products found in this price range", status_code=404)

        return [ProductBasePlusID.model_validate(product) for product in response.data]

    @classmethod
    async def search_products_by_stock_range(cls, min_stock: int, max_stock: int) -> list[ProductBasePlusID]:
        """Search products by stock range."""

        client = await get_db_client()

        response = await client.table(SETTINGS.product_table).select(*cls.FIELDS_PRODUCT_BASE).gte("stock", min_stock).lte("stock", max_stock).execute()

        if not bool(response.data):
            raise HTTPException(detail="No products found in this stock range", status_code=404)

        return [ProductBasePlusID.model_validate(product) for product in response.data]
    
    @classmethod
    async def search_products_by_expiration_date(cls, expiration_date: date) -> list[ProductBasePlusID]:
        """Search products by expiration date."""

        client = await get_db_client()

        response = await client.table(SETTINGS.product_table).select(*cls.FIELDS_PRODUCT_BASE).eq("expiration_date", expiration_date).execute()

        if not bool(response.data):
            raise HTTPException(detail="No products found with this expiration date", status_code=404)

        return [ProductBasePlusID.model_validate(product) for product in response.data]
    
    @classmethod
    async def search_products_by_cost_range(cls, min_cost: float, max_cost: float) -> list[ProductBasePlusID]:
        """Search products by cost range."""

        client = await get_db_client()

        response = await client.table(SETTINGS.product_table).select(*cls.FIELDS_PRODUCT_BASE).gte("cost", min_cost).lte("cost", max_cost).execute()

        if not bool(response.data):
            raise HTTPException(detail="No products found in this cost range", status_code=404)

        return [ProductBasePlusID.model_validate(product) for product in response.data]
    
    @classmethod
    async def search_low_stock_products(cls) -> list[ProductBasePlusID]:
        """Search products with low stock."""

        client = await get_db_client()

        response = await client.table(SETTINGS.low_stock_products_view).select(*cls.FIELDS_PRODUCT_BASE).execute()

        if not bool(response.data):
            raise HTTPException(detail="No low stock products found", status_code=404)

        return [ProductBasePlusID.model_validate(product) for product in response.data]
    
    @classmethod
    async def search_expired_products(cls) -> list[ProductBasePlusID]:
        """Search products that are expired."""

        client = await get_db_client()

        response = await client.table(SETTINGS.expired_products_view).select(*cls.FIELDS_PRODUCT_BASE).execute()

        if not bool(response.data):
            raise HTTPException(detail="No expired products found", status_code=404)

        return [ProductBasePlusID.model_validate(product) for product in response.data]