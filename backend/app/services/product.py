from fastapi import HTTPException
from datetime import date

from models import ProductBasePlusID, ProductCategory, Category
from db import get_db_client
from core import SETTINGS
from crud import ProductCrud

class ProductService:
    
    FIELDS_PRODUCT_BASE = set(ProductBasePlusID.model_fields.keys())
    
    @classmethod
    async def search_products_by_category(cls, category_id: int) -> list[ProductBasePlusID]:
        """Retrieve products by category."""
        
        client = await get_db_client()

        response = await client.table(SETTINGS.product_category_table).select("product_id").eq("category_id", category_id).execute()

        if not bool(response.data):
            raise HTTPException(detail="No products found in this category", status_code=404)
        
        # Retrieve product details using the product IDs
        return [await ProductCrud.read_product_base(int(product['product_id'])) for product in response.data]


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
    
    @classmethod
    async def search_category_by_name(cls, category_name: str) -> list[Category]:
        """Search products by category name."""

        client = await get_db_client()

        response = await client.table(SETTINGS.category_table).select("*").ilike("name", category_name).execute()

        if not bool(response.data):
            raise HTTPException(detail="No products found in this category", status_code=404)

        # Validate and return the categories
        return [Category.model_validate(category) for category in response.data]