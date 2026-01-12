from datetime import date

from fastapi import HTTPException
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlmodel import select
from sqlalchemy.sql.expression import Select

from models import Product, ProductCategory, Category, ServiceInput

class ProductService:
        
    @staticmethod
    def read_all_products() -> Select:
        """Query for retrieve all products."""
        return select(Product)
    
    @staticmethod
    def search_products_by_category(category_id: int) -> Select:
        """Query for search product by category"""
        return (select(Product)
                .join(ProductCategory, Product.id == ProductCategory.product_id)
                .where(ProductCategory.category_id == category_id))

    @staticmethod
    def search_products_by_name(name: str) -> Select:
        """Query for search products by name."""
        return select(Product).where(Product.name.ilike(f"%{name}%"))

    @staticmethod
    def search_products_by_price_range(min_price: float, max_price: float) -> Select:
        """Query for search products by price range."""
        return select(Product).where(Product.price >= min_price).where(Product.price <= max_price)

    @staticmethod
    def search_products_by_stock_range(min_stock: int, max_stock: int) -> Select:
        """Query for search products by stock range."""
        return select(Product).where(Product.stock >= min_stock).where(Product.stock <= max_stock)
    
    @staticmethod
    def search_products_by_expiration_date(expiration_date: date) -> Select:
        """Query for search products by expiration date."""
        return select(Product).where(Product.expiration_date == expiration_date)
    
    @staticmethod
    def search_products_by_cost_range(min_cost: float, max_cost: float) -> Select:
        """Query for search products by cost range."""
        return select(Product).where(Product.cost >= min_cost).where(Product.cost <= max_cost)
    
    @staticmethod
    async def search_products_by_service(db_session: AsyncSession, service_id: int) -> Select:
        """Query for search product by service"""
        
        from utils import ServiceUtils

        if not await ServiceUtils.exist_service(db_session, service_id):
            raise HTTPException(status_code=404, detail="Service not found")

        return (
            select(Product)
            .join(ServiceInput, ServiceInput.product_id == Product.id)
            .where(ServiceInput.service_id == service_id)
            .order_by(Product.id)
        )
    
    @staticmethod
    def search_low_stock_products() -> Select:
        """Query for search products with low stock."""
        return (select(Product)
                .where(Product.stock <= Product.minimum_stock)
                .order_by(Product.stock))
    
    @staticmethod
    def search_expired_products() -> Select:
        """Query for search products that are expired."""
        return (select(Product)
                .where(Product.expiration_date  < date.today())
                .order_by(Product.expiration_date))
    
    @staticmethod
    def read_all_categories() -> Select:
        """Query for retrieve all product categories."""
        return select(Category)
    
    @staticmethod
    def search_category_by_name(category_name: str) -> Select:
        """Query for search products by category name."""
        return select(Category).where(Category.name.ilike(f"%{category_name}%"))