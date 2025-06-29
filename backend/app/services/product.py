from datetime import date

from models import ProductBasePlusID, ProductCategory, ProductTypes
from crud import ProductCrud

class ProductService:
    @classmethod
    async def get_all_products_base(cls) -> list[ProductBasePlusID]:
        """Retrieve all products."""
        products = await ProductCrud.get_all_products()
        return [ProductBasePlusID.model_validate(
            {"id": product.id,
             "name": product.name,
             "short_description": product.short_description,
             "price": product.price,
             "category": product.category,
             "stock": product.stock,
             "image_url": product.image_url,
            }) for product in products]
    
    @classmethod
    async def get_product_base_by_id(cls, product_id: int) -> ProductBasePlusID:
        """Retrieve a product by ID."""
        product = await ProductCrud.get_product_by_id(product_id)
        return ProductBasePlusID.model_validate(
            {"id": product.id,
             "name": product.name,
             "short_description": product.short_description,
             "price": product.price,
             "category": product.category,
             "stock": product.stock,
             "image_url": product.image_url,
            }
        )
    
    @classmethod
    async def get_products_base_by_category(cls, category: str) -> list[ProductBasePlusID]:
        """Retrieve products by category."""
        products = await ProductCrud.get_products_by_category(category)
        return [ProductBasePlusID.model_validate(
            {"id": product.id,
             "name": product.name,
             "short_description": product.short_description,
             "price": product.price,
             "category": product.category,
             "stock": product.stock,
             "image_url": product.image_url,
            }) for product in products]
        
    @classmethod
    async def get_products_base_by_type(cls, product_type: str) -> list[ProductBasePlusID]:
        """Retrieve products by type."""
        products = await ProductCrud.get_products_by_type(product_type)
        return [ProductBasePlusID.model_validate(
            {"id": product.id,
             "name": product.name,
             "short_description": product.short_description,
             "price": product.price,
             "category": product.category,
             "stock": product.stock,
             "image_url": product.image_url,
            }) for product in products]
    
    @classmethod
    async def search_products_by_name(cls, name: str) -> list[ProductBasePlusID]:
        """Search products by name."""
        products = await ProductCrud.search_product_by_name(name)
        return [ProductBasePlusID.model_validate(
            {"id": product.id,
             "name": product.name,
             "short_description": product.short_description,
             "price": product.price,
             "category": product.category,
             "stock": product.stock,
             "image_url": product.image_url,
            }) for product in products]
        

    @classmethod
    async def search_products_by_price_range(cls, min_price: float, max_price: float) -> list[ProductBasePlusID]:
        """Search products by price range."""
        products = await ProductCrud.search_product_by_price_range(min_price, max_price)
        return [ProductBasePlusID.model_validate(
            {"id": product.id,
             "name": product.name,
             "short_description": product.short_description,
             "price": product.price,
             "category": product.category,
             "stock": product.stock,
             "image_url": product.image_url,
            }) for product in products]
        
    @classmethod
    async def search_products_by_stock_range(cls, min_stock: int, max_stock: int) -> list[ProductBasePlusID]:
        """Search products by stock range."""
        products = await ProductCrud.search_product_by_stock_range(min_stock, max_stock)
        return [ProductBasePlusID.model_validate(
            {"id": product.id,
             "name": product.name,
             "short_description": product.short_description,
             "price": product.price,
             "category": product.category,
             "stock": product.stock,
             "image_url": product.image_url,
            }) for product in products]
    
    @classmethod
    async def search_products_by_expiration_date(cls, expiration_date: date) -> list[ProductBasePlusID]:
        """Search products by expiration date."""
        products = await ProductCrud.search_product_by_expiration_date(expiration_date)
        return [ProductBasePlusID.model_validate(
            {"id": product.id,
             "name": product.name,
             "short_description": product.short_description,
             "price": product.price,
             "category": product.category,
             "stock": product.stock,
             "image_url": product.image_url,
            }) for product in products]
        
    
    @classmethod
    async def search_product_by_cost_range(cls, min_cost: float, max_cost: float) -> list[ProductBasePlusID]:
        """Search products by cost range."""
        products = await ProductCrud.search_product_by_cost_range(min_cost, max_cost)
        return [ProductBasePlusID.model_validate(
            {"id": product.id,
             "name": product.name,
             "short_description": product.short_description,
             "price": product.price,
             "category": product.category,
             "stock": product.stock,
             "image_url": product.image_url,
            }) for product in products]