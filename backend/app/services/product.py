from models import ProductBase
from crud import ProductCrud

class ProductService:
    @classmethod
    async def get_all_products_base(cls) -> list[ProductBase]:
        """Retrieve all products."""
        products = await ProductCrud.get_all_products()
        return [ProductBase.model_validate(
            {"id": product.id,
             "name": product.name,
             "short_description": product.short_description,
             "price": product.price,
             "category": product.category,
             "stock": product.stock,
             "image_url": product.image_url,
            }) for product in products]
    
    @classmethod
    async def get_product_base_by_id(cls, product_id: int) -> ProductBase:
        """Retrieve a product by ID."""
        product = await ProductCrud.get_product_by_id(product_id)
        return ProductBase.model_validate(
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
    async def get_products_base_by_category(cls, category: str) -> list[ProductBase]:
        """Retrieve products by category."""
        products = await ProductCrud.get_products_by_category(category)
        return [ProductBase.model_validate(
            {"id": product.id,
             "name": product.name,
             "short_description": product.short_description,
             "price": product.price,
             "category": product.category,
             "stock": product.stock,
             "image_url": product.image_url,
            }) for product in products]
        
    @classmethod
    async def get_products_base_by_type(cls, product_type: str) -> list[ProductBase]:
        """Retrieve products by type."""
        products = await ProductCrud.get_products_by_type(product_type)
        return [ProductBase.model_validate(
            {"id": product.id,
             "name": product.name,
             "short_description": product.short_description,
             "price": product.price,
             "category": product.category,
             "stock": product.stock,
             "image_url": product.image_url,
            }) for product in products]