from datetime import date

from fastapi import HTTPException
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlmodel import select
from sqlalchemy.sql.expression import Select

from models import Product, ProductCategory, Category, ServiceInput
from dtos import ProductFilter, CategoryFilter

class ProductService:
        
    QUERY_PRODUCT_BASE = select(Product)
    QUERY_CATEGORY_BASE = select(Category)
    
    @classmethod
    def search_products(cls, filters: ProductFilter) -> Select:
        """Query that searches for products who meet the filters."""
        return filters.apply(cls.QUERY_PRODUCT_BASE)
    
    @classmethod
    def search_products_by_category(cls, category_id: int) -> Select:
        """Query for search product by category"""
        return (cls.QUERY_PRODUCT_BASE
                .join(ProductCategory, Product.id == ProductCategory.product_id)
                .where(ProductCategory.category_id == category_id))
    
    @classmethod
    def search_products_by_service(cls, service_id: int) -> Select:
        """Query for search product by service"""
        return (
            cls.QUERY_PRODUCT_BASE
            .join(ServiceInput, ServiceInput.product_id == Product.id)
            .where(ServiceInput.service_id == service_id)
            .order_by(Product.id)
        )
    
    @classmethod
    def search_low_stock_products(cls) -> Select:
        """Query for search products with low stock."""
        return (cls.QUERY_PRODUCT_BASE
                .where(Product.stock <= Product.minimum_stock)
                .order_by(Product.stock))
    
    @classmethod
    def search_expired_products(cls) -> Select:
        """Query for search products that are expired."""
        return (cls.QUERY_PRODUCT_BASE
                .where(Product.expiration_date  < date.today())
                .order_by(Product.expiration_date))
    
    @classmethod
    def search_categories(cls, filters : CategoryFilter) -> Select:
        """Query for retrieve all product categories."""
        return filters.apply(cls.QUERY_CATEGORY_BASE)