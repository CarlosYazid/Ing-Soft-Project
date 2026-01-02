from fastapi import HTTPException, UploadFile
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlmodel import select
from botocore.client import BaseClient

from models import Product, ProductCreate, ProductUpdate, ProductCategory, Category, CategoryCreate, CategoryUpdate
from utils import ProductUtils

class ProductCrud:
    
    EXCLUDED_FIELDS_FOR_UPDATE = {"id"}

    @classmethod
    async def create_product(cls, db_session: AsyncSession, storage_client: BaseClient, product: ProductCreate) -> Product:
        """Create a new product."""
        
        image_url = None
        
        if product.image:

            image_key = await ProductUtils.upload_image(storage_client, product.image)
        
            
        try:
            
            product_data : dict = product.model_dump(exclude_unset=True)
            product_data["image_key"] = image_key
            
            async with db_session.begin():
            
                new_product = Product(**product_data)
                
                db_session.add(new_product)
                await db_session.refresh(new_product)
                
            return new_product
        
        except Exception as e:

            if image_url:
                await ProductUtils.delete_image(storage_client, image_url)

            raise HTTPException(status_code=500, detail="Service creation failed") from e
        
    
    @classmethod
    async def read_all_products(cls, db_session: AsyncSession) -> list[Product]:
        """Retrieve all products."""
        
        try:

            response = await db_session.exec(select(Product))
            products = list(response.all())

            if not products:
                raise HTTPException(detail="No products found", status_code=404)

            return products

        except Exception as e:
            raise HTTPException(detail="Product search failed", status_code=500) from e
    
    @classmethod
    async def read_product(cls, db_session: AsyncSession, product_id: int) -> Product:
        """Retrieve a product by ID."""
        
        try:
            
            response = await db_session.exec(select(Product).where(Product.id == product_id))
            product = response.first()
            
            if not product:
                raise HTTPException(detail="Product not found", status_code=404)
            
            return product
        
        except Exception as e:
            raise HTTPException(detail="Product search failed", status_code=500) from e
    
    @classmethod
    async def update_product(cls, db_session: AsyncSession, fields: ProductUpdate) -> Product:
        """Update an existing product."""
        
        # Check if the product exists before attempting to update
        if not await ProductUtils.exist_product(db_session, fields.id):
            raise HTTPException(detail="Product not found", status_code=404)
        
        try:
            
            async with db_session.begin():

                response = await db_session.exec(select(Product).where(Product.id == fields.id))
                product = response.one()

                for key, value in fields.model_dump(exclude_unset=True).items():
                    
                    if key in cls.EXCLUDED_FIELDS_FOR_UPDATE:
                        continue
                    
                    setattr(product, key, value)

                db_session.add(product)
                await db_session.refresh(product)
                
            return product
            
        except Exception as e:
            raise HTTPException(detail="Product update failed", status_code=500) from e
    
    @classmethod
    async def update_stock(cls, db_session: AsyncSession, product_id: int, new_stock: int, replace: bool = True) -> Product:
        """Update the stock of a product by ID."""

        # Check if the product exists before attempting to update stock
        if not await ProductUtils.exist_product(db_session, product_id):
            raise HTTPException(detail="Product not found", status_code=404)
        try:

            async with db_session.begin():

                response = await db_session.exec(select(Product).where(Product.id == product_id))
                product = response.one()

                if replace:
                    product.stock = new_stock
                else:
                    product.stock += new_stock

                if product.stock < 0:
                    product.stock = 0

                db_session.add(product)
                await db_session.refresh(product)
            
            return product
        
        except Exception as e:
            raise HTTPException(detail="Stock update failed", status_code=500) from e
    
    @classmethod
    async def update_image(cls, db_session: AsyncSession, storage_client: BaseClient, product_id: int, image: UploadFile) -> Product:
        """Update the image of a product by ID."""

        # Check if the product exists before attempting to update the image
        if not await ProductUtils.exist_product(db_session, product_id):
            raise HTTPException(detail="Product not found", status_code=404)
        
        try:

            async with db_session.begin():

                response = await db_session.exec(select(Product).where(Product.id == product_id))
                product = response.one()

                if product.image_key:
                    await ProductUtils.delete_image(storage_client, product.image_key)

                image_key = await ProductUtils.upload_image(storage_client, image)

                product.image_key = image_key

                db_session.add(product)
                await db_session.refresh(product)

            return product
    
        except Exception as e:
            raise HTTPException(detail="Image update failed", status_code=500) from e
    
    @classmethod
    async def delete_product(cls, db_session: AsyncSession, storage_client: BaseClient, product_id: int) -> bool:
        """Delete a product by ID."""

        # Check if the product exists before attempting to delete
        if not await ProductUtils.exist_product(db_session, product_id):
            raise HTTPException(detail="Product not found", status_code=404)
        
        from utils import OrderUtils
        
        # Check if the product is associated with any orders
        if await OrderUtils.exist_product_in_orders(db_session, product_id):
            raise HTTPException(detail="Cannot delete product associated with orders", status_code=400)
        
        try:

            async with db_session.begin():

                response = await db_session.exec(select(Product).where(Product.id == product_id))
                product = response.one()

                if product.image_key:
                    await ProductUtils.delete_image(storage_client, product.image_key)

                await db_session.delete(product)
            
            return True
        
        except Exception as e:
            raise HTTPException(detail="Product deletion failed", status_code=500) from e
    
    @classmethod
    async def create_product_category(cls, db_session: AsyncSession, product_category: ProductCategory) -> ProductCategory:
        """Create a new product category."""
        
        if not await ProductUtils.exist_product(db_session, product_category.product_id):
            raise HTTPException(detail="Product not found", status_code=404)
        
        if not await ProductUtils.exist_category(db_session, product_category.category_id):
            raise HTTPException(detail="Category not found", status_code=404)

        try:

            async with db_session.begin():

                db_session.add(product_category)
                await db_session.refresh(product_category)
            
            return product_category
        
        except Exception as e:
            raise HTTPException(detail="Failed to create product category", status_code=500) from e
    
    @classmethod
    async def read_all_product_categories(cls, db_session: AsyncSession) -> list[ProductCategory]:
        """Retrieve all product categories."""
        
        try:
            
            response = await db_session.exec(select(ProductCategory))
            product_categories = list(response.all())
            
            if not product_categories:
                raise HTTPException(detail="No product categories found", status_code=404)
            
            return product_categories
        
        except Exception as e:
            raise HTTPException(detail="Failed to retrieve product categories", status_code=500) from e

    @classmethod
    async def delete_product_category(cls, db_session: AsyncSession, product_category: ProductCategory) -> bool:
        """Delete a product category by ID."""

        # Check if the category exists before attempting to delete
        if not await ProductUtils.exist_product_category(db_session, product_category):
            raise HTTPException(detail="Product Category not found", status_code=404)
        
        try:

            async with db_session.begin():

                response = await db_session.exec(select(ProductCategory).where(ProductCategory.product_id == product_category.product_id, ProductCategory.category_id == product_category.category_id))
                product_category = response.one()

                await db_session.delete(product_category)

            return True

        except Exception as e:
            raise HTTPException(detail="Product category deletion failed", status_code=500) from e

    @classmethod
    async def create_category(cls, db_session: AsyncSession, category: CategoryCreate) -> Category:
        """Create a new product category."""
        
        try:
            
            async with db_session.begin():

                new_category = Category(**category.model_dump(exclude_unset=True))

                db_session.add(new_category)
                await db_session.refresh(new_category)
            
            return new_category
        
        except Exception as e:
            raise HTTPException(detail="Failed to create category", status_code=500) from e
    
    @classmethod
    async def read_all_categories(cls, db_session: AsyncSession) -> list[Category]:
        """Retrieve all product categories."""
        
        try:
            
            response = await db_session.exec(select(Category))
            categories = list(response.all())

            if not categories:
                raise HTTPException(detail="No categories found", status_code=404)

            return categories
        
        except Exception as e:
            raise HTTPException(detail="Failed to retrieve categories", status_code=500) from e
    
    @classmethod
    async def read_category(cls, db_session: AsyncSession, category_id: int) -> Category:
        """Retrieve a product category by ID."""
        
        try:
            
            response = await db_session.exec(select(Category).where(Category.id == category_id))
            category = response.first()

            if not category:
                raise HTTPException(detail="Category not found", status_code=404)

            return category
        
        except Exception as e:
            raise HTTPException(detail="Failed to retrieve category", status_code=500) from e
    
    @classmethod
    async def update_category(cls, db_session: AsyncSession, fields: CategoryUpdate) -> Category:
        """Update an existing product category."""
        
        # Check if the category exists before attempting to update
        if not await ProductUtils.exist_category(db_session, fields.id):
            raise HTTPException(detail="Category not found", status_code=404)
        
        try:

            async with db_session.begin():

                response = await db_session.exec(select(Category).where(Category.id ==fields.id))
                category = response.one()

                for key, value in fields.model_dump(exclude_unset=True).items():
                    
                    if key in cls.EXCLUDED_FIELDS_FOR_UPDATE:
                        continue

                    setattr(category, key, value)

                db_session.add(category)
                await db_session.refresh(category)

            return category
        
        except Exception as e:
            raise HTTPException(detail="Failed to update category", status_code=500) from e
    
    @classmethod
    async def delete_category(cls, db_session: AsyncSession, category_id: int) -> bool:
        """Delete a product category by ID."""

        # Check if the category exists before attempting to delete
        if not await ProductUtils.exist_category(db_session, category_id):
            raise HTTPException(detail="Category not found", status_code=404)
        
        try:
            
            async with db_session.begin():

                response = await db_session.exec(select(Category).where(Category.id == category_id))
                category = response.one()

                await db_session.delete(category)
            
            return True
        
        except Exception as e:
            raise HTTPException(detail="Failed to delete category", status_code=500) from e