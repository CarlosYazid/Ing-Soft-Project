from datetime import date

from fastapi import HTTPException
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlmodel import select

from models import Product, ProductCategory, Category, ServiceInput

class ProductService:
    
    @classmethod
    async def search_products_by_category(cls, db_session: AsyncSession, category_id: int) -> list[Product]:
        """Search product by category"""
        
        try:
            
            statement = (
                select(Product)
                .join(ProductCategory, Product.id == ProductCategory.product_id)
                .where(ProductCategory.category_id == category_id)
            )

            result = await db_session.exec(statement)

            products = list(result.all())

            if not products:
                raise HTTPException(detail="No products found in this category", status_code=404)

            return products

        except Exception as e:
            raise HTTPException(detail="Product search failed", status_code=500) from e


    @classmethod
    async def search_products_by_name(cls, db_session: AsyncSession, name: str) -> list[Product]:
        """Search products by name."""
        
        try:
            
            response = await db_session.exec(select(Product).where(Product.name.ilike(f"%{name}%")))
            products = list(response.all())
            
            if not products:
                raise HTTPException(detail="No products found with this name", status_code=404)
            
            return products
        
        except Exception as e:
            raise HTTPException(detail="Product search failed", status_code=500) from e

    @classmethod
    async def search_products_by_price_range(cls, db_session: AsyncSession, min_price: float, max_price: float) -> list[Product]:
        """Search products by price range."""
        
        try:
            
            response = await db_session.exec(select(Product).where(Product.price >= min_price).where(Product.price <= max_price))
            products = list(response.all())
            
            if not products:
                raise HTTPException(detail="No products found in this price range", status_code=404)
            
            return products
        
        except Exception as e:
            raise HTTPException(detail="Product search failed", status_code=500) from e

    @classmethod
    async def search_products_by_stock_range(cls, db_session: AsyncSession, min_stock: int, max_stock: int) -> list[Product]:
        """Search products by stock range."""
        try:

            response = await db_session.exec(select(Product).where(Product.stock >= min_stock).where(Product.stock <= max_stock))
            products = list(response.all())

            if not products:
                raise HTTPException(detail="No products found in this stock range", status_code=404)

            return products

        except Exception as e:
            raise HTTPException(detail="Product search failed", status_code=500) from e
    
    @classmethod
    async def search_products_by_expiration_date(cls, db_session: AsyncSession, expiration_date: date) -> list[Product]:
        """Search products by expiration date."""
        
        try:

            response = await db_session.exec(select(Product).where(Product.expiration_date == expiration_date))
            products = list(response.all())

            if not products:
                raise HTTPException(detail="No products found with this expiration date", status_code=404)

            return products
        
        except Exception as e:
            raise HTTPException(detail="Product search failed", status_code=500) from e
        
    
    @classmethod
    async def search_products_by_cost_range(cls, db_session: AsyncSession, min_cost: float, max_cost: float) -> list[Product]:
        """Search products by cost range."""
        
        try:

            response = await db_session.exec(select(Product).where(Product.cost >= min_cost).where(Product.cost <= max_cost))
            products = list(response.all())

            if not products:
                raise HTTPException(detail="No products found in this cost range", status_code=404)

            return products

        except Exception as e:
            raise HTTPException(detail="Product search failed", status_code=500) from e
    
    @classmethod
    async def search_products_by_service(cls, db_session: AsyncSession, service_id: int) -> list[Product]:
        """Retrieve all products for a specific service."""

        from utils import ServiceUtils

        if not await ServiceUtils.exist_service(db_session, service_id):
            raise HTTPException(detail="Service not found", status_code=404)
        
        try:
            
            response = await db_session.exec(select(ServiceInput).where(ServiceInput.service_id == service_id))
            service_inputs = list(response.all())

            if not service_inputs:
                raise HTTPException(detail="No service inputs found for this service", status_code=404)

            from crud import ProductCrud

            return [await ProductCrud.read_product(db_session, item.product_id) for item in service_inputs]
        
        except Exception as e:
            raise HTTPException(detail="Service input search failed", status_code=500) from e
    
    @classmethod
    async def search_low_stock_products(cls, db_session: AsyncSession) -> list[Product]:
        """Search products with low stock."""
        
        try:
            
            response = await db_session.exec(select(Product)
                                             .where(Product.stock <= Product.minimum_stock)
                                             .order_by(Product.stock))
            products = list(response.all())
            
            if not products:
                raise HTTPException(detail="No low stock products found", status_code=404)
            
            return products
        
        except Exception as e:
            raise HTTPException(detail="Product search failed", status_code=500) from e
    
    @classmethod
    async def search_expired_products(cls, db_session: AsyncSession) -> list[Product]:
        """Search products that are expired."""
        
        try:

            response = await db_session.exec(select(Product)
                                             .where(Product.expiration_date  < date.today())
                                             .order_by(Product.expiration_date))
            products = list(response.all())

            if not products:
                raise HTTPException(detail="No expired products found", status_code=404)

            return products
        
        except Exception as e:
            raise HTTPException(detail="Product search failed", status_code=500) from e
        
    
    @classmethod
    async def search_category_by_name(cls, db_session: AsyncSession, category_name: str) -> list[Category]:
        """Search products by category name."""
        
        try:
            
            response = await db_session.exec(select(Category).where(Category.name.ilike(f"%{category_name}%")))
            categories = list(response.all())

            if not categories:
                raise HTTPException(detail="No categories found with this name", status_code=404)

            return categories
        
        except Exception as e:
            raise HTTPException(detail="Category search failed", status_code=500) from e