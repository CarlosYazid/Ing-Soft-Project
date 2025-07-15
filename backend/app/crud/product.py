from fastapi import HTTPException, UploadFile

from db import get_db_client
from models import Product, ProductCreate, ProductBasePlusID, ProductCategory, Category, ProductCategoryCreate, CategoryPlusID, CategoryCreate
from core import SETTINGS
from utils import ProductUtils

class ProductCrud:

    ALLOWED_IMAGE_TYPES = {"image/png", "image/jpeg", "image/webp"}
    EXCLUDED_FIELDS_FOR_UPDATE = {"id", "image_url", "created_at", "stock"}
    ALLOWED_FIELDS_FOR_UPDATE = set(ProductCreate.model_fields.keys()) - EXCLUDED_FIELDS_FOR_UPDATE
    EXCLUDED_FIELDS_FOR_CATEGORY_UPDATE = {"id", "created_at"}
    ALLOWED_FIELDS_FOR_CATEGORY_UPDATE = set(ProductCategoryCreate.model_fields.keys()) - EXCLUDED_FIELDS_FOR_CATEGORY_UPDATE
    EXCLUDED_FIELDS_FOR_PRODUCT_CATEGORY_UPDATE = {"id", "created_at", "product_id"}
    ALLOWED_FIELDS_FOR_PRODUCT_CATEGORY_UPDATE = set(ProductCategoryCreate.model_fields.keys()) - EXCLUDED_FIELDS_FOR_PRODUCT_CATEGORY_UPDATE

    FIELDS_PRODUCT_BASE = set(ProductBasePlusID.model_fields.keys())
    FIELDS_CATEGORY_BASE = set(CategoryPlusID.model_fields.keys())

    @classmethod
    async def create_product(cls, product: ProductCreate) -> Product:
        """Create a new product."""
        
        client = await get_db_client()

        names = await client.table(SETTINGS.product_table).select("name").execute()


        if bool(names.data):

            names = [n['name'].lower() for n in names.data]

            if product.name.lower() in names:
                raise HTTPException(status_code=404, detail="The product already exists")
        
        product.image_url = None  # Initialize image_url to None

        from services.gen_ai import GenAIService

        product.short_description = await GenAIService.gen_short_description(product.description)
            
        response = await client.table(SETTINGS.product_table).insert(product.model_dump(mode="json")).execute()
        
        if not response.data:
            raise HTTPException(status_code=500, detail="Failed to create product")
        
        return Product.model_validate(response.data[0])
    
    @classmethod
    async def read_all_products(cls) -> list[Product]:
        """Retrieve all products."""

        client = await get_db_client()

        response = await client.table(SETTINGS.product_table).select("*").execute()

        if not bool(response.data):
            raise HTTPException(detail="No products found", status_code=404)

        return [Product.model_validate(product) for product in response.data]
    
    @classmethod
    async def read_all_products_base(cls) -> list[ProductBasePlusID]:
        """Retrieve all products."""
        
        client = await get_db_client()

        response = await client.table(SETTINGS.product_table).select(*cls.FIELDS_PRODUCT_BASE).execute()

        if not bool(response.data):
            raise HTTPException(detail="No products found", status_code=404)
        
        return [ProductBasePlusID.model_validate(product) for product in response.data]
    
    @classmethod
    async def read_product(cls, product_id: int) -> Product:
        """Retrieve a product by ID."""

        client = await get_db_client()

        response = await client.table(SETTINGS.product_table).select("*").eq("id", product_id).execute()

        if not bool(response.data):
            raise HTTPException(detail="Product not found", status_code=404)

        return Product.model_validate(response.data[0])
    
    @classmethod
    async def read_product_base(cls, product_id: int) -> ProductBasePlusID:
        """Retrieve a product by ID."""
        
        client = await get_db_client()

        response = await client.table(SETTINGS.product_table).select(*cls.FIELDS_PRODUCT_BASE).eq("id", product_id).execute()

        if not bool(response.data):
            raise HTTPException(detail="Product not found", status_code=404)

        return ProductBasePlusID.model_validate(response.data[0])
    
    @classmethod
    async def update_product(cls, product_id: int, fields: dict) -> Product:
        """Update an existing product."""
        
        # Check if the product exists before attempting to update
        if not await ProductUtils.exist_product(product_id):
            raise HTTPException(detail="Product not found", status_code=404)
        
        if any(field in fields for field in cls.EXCLUDED_FIELDS_FOR_UPDATE):
            raise HTTPException(detail=f"Cannot update fields: {', '.join(cls.EXCLUDED_FIELDS_FOR_UPDATE)}", status_code=400)

        if not(set(fields.keys()) <= cls.ALLOWED_FIELDS_FOR_UPDATE):
            raise HTTPException(detail="Update attribute of product", status_code=400)

        client = await get_db_client()

        response = await client.table(SETTINGS.product_table).update(fields).eq("id", product_id).execute()

        if not bool(response.data):
            raise HTTPException(detail="Failed to update product", status_code=500)

        return Product.model_validate(response.data[0])
    
    @classmethod
    async def upload_image(cls, product_id: int, image: UploadFile) -> str:
        """Upload an image for a product and return the URL."""

        if image.content_type not in cls.ALLOWED_IMAGE_TYPES:
            raise HTTPException(
                status_code=400,
                detail=f"Invalid image type: {image.content_type}. Allowed types are: {', '.join(cls.ALLOWED_IMAGE_TYPES)}",
            )
        
        # Check if the product exists before attempting to upload an image
        if not await ProductUtils.exist_product(product_id):
            raise HTTPException(status_code=404, detail="Product not found")

        name, ext = image.filename.split(".")[-2:]
        
        client = await get_db_client()
        
        last_image = await client.table(SETTINGS.product_table).select("image_url").eq("id", product_id).execute()

        filename = f"products/{product_id}_{name.replace(' ', '_').lower()}.{ext}"

        if bool(last_image.data) and bool(last_image.data[0]["image_url"]):
            last_image = "products/" + last_image.data[0]["image_url"].split("/")[-1]
            await client.storage.from_(SETTINGS.bucket_name).remove([last_image, filename])
        else:
            await client.storage.from_(SETTINGS.bucket_name).remove([filename])

        file_content = await image.read()

        response = await client.storage.from_(SETTINGS.bucket_name).upload(
            path=filename,
            file=file_content,
            file_options={"content-type": image.content_type})

        if not bool(response):
            raise HTTPException(status_code=500, detail="Failed to upload image")

        image_url = f"{SETTINGS.db_url}/storage/v1/object/public/{SETTINGS.bucket_name}/{filename}"
        
        response = await client.table(SETTINGS.product_table).update({"image_url": image_url}).eq("id", product_id).execute()

        if not bool(response.data):
            raise HTTPException(status_code=500, detail="Failed to update product with image URL")

        return image_url
    
    @classmethod
    async def update_stock(cls, product_id: int, new_stock: int, replace: bool = True) -> Product:
        """Update the stock of a product by ID."""

        # Check if the product exists before attempting to update stock
        if not await ProductUtils.exist_product(product_id):
            raise HTTPException(detail="Product not found", status_code=404)
        
        client = await get_db_client()

        if not replace:
            
            current_stock_response = await client.table(SETTINGS.product_table).select("stock").eq("id", product_id).execute()

            if not bool(current_stock_response.data):
                raise HTTPException(detail="The product has no stock, better replace it.", status_code=404)

            new_stock += int(current_stock_response.data[0]["stock"])
        
        if new_stock < 0:
            new_stock = 0

        response = await client.table(SETTINGS.product_table).update({"stock": new_stock}).eq("id", product_id).execute()

        if not bool(response.data):
            raise HTTPException(detail="Failed to update product stock", status_code=500)

        return Product.model_validate(response.data[0])
    
    @classmethod
    async def delete_product(cls, product_id: int) -> None:
        """Delete a product by ID."""

        # Check if the product exists before attempting to delete
        if not await ProductUtils.exist_product(product_id):
            raise HTTPException(detail="Product not found", status_code=404)
        
        from utils import OrderUtils
        
        # Check if the product is associated with any orders
        if await OrderUtils.exist_product_in_orders(product_id):
            raise HTTPException(detail="Cannot delete product associated with orders", status_code=400)
        
        client = await get_db_client()

        response = await client.table(SETTINGS.product_table).delete().eq("id", product_id).execute()

        if not bool(response.data):
            raise HTTPException(detail="Failed to delete product", status_code=500)
        
        return bool(response.data)
    
    @classmethod
    async def create_product_category(cls, category: ProductCategoryCreate) -> ProductCategory:
        """Create a new product category."""
        
        if not await ProductUtils.exist_product(category.product_id):
            raise HTTPException(detail="Product not found", status_code=404)
        
        if not await ProductUtils.exist_category(category.category_id):
            raise HTTPException(detail="Category not found", status_code=404)

        client = await get_db_client()

        response = await client.table(SETTINGS.product_category_table).insert(category.model_dump(mode="json")).execute()

        if not bool(response.data):
            raise HTTPException(detail="Failed to create product category", status_code=500)

        return ProductCategory.model_validate(response.data[0])
    
    @classmethod
    async def read_all_product_categories(cls) -> list[ProductCategory]:
        """Retrieve all product categories."""

        client = await get_db_client()

        response = await client.table(SETTINGS.product_category_table).select("*").execute()

        if not bool(response.data):
            raise HTTPException(detail="No product categories found", status_code=404)

        return [ProductCategory.model_validate(category) for category in response.data]
    
    @classmethod
    async def read_product_category(cls, category_id: int) -> ProductCategory:
        """Retrieve a product category by ID."""

        client = await get_db_client()

        response = await client.table(SETTINGS.product_category_table).select("*").eq("id", category_id).execute()

        if not bool(response.data):
            raise HTTPException(detail="Product category not found", status_code=404)

        return ProductCategory.model_validate(response.data[0])

    @classmethod
    async def update_product_category(cls, product_category_id: int, fields: dict) -> ProductCategory:
        """Update an existing product category."""

        # Check if the category exists before attempting to update
        if not await ProductUtils.exist_product_category(product_category_id):
            raise HTTPException(detail="Category not found", status_code=404)
        
        if any(field in fields for field in cls.EXCLUDED_FIELDS_FOR_PRODUCT_CATEGORY_UPDATE):
            raise HTTPException(detail=f"Cannot update fields: {', '.join(cls.EXCLUDED_FIELDS_FOR_PRODUCT_CATEGORY_UPDATE)}", status_code=400)
        
        if not(set(fields.keys()) <= cls.ALLOWED_FIELDS_FOR_PRODUCT_CATEGORY_UPDATE):
            print(fields.keys(), cls.ALLOWED_FIELDS_FOR_PRODUCT_CATEGORY_UPDATE)
            raise HTTPException(detail="Update attribute of product category", status_code=400)
        
        client = await get_db_client()

        response = await client.table(SETTINGS.product_category_table).update(fields).eq("id", product_category_id).execute()

        if not bool(response.data):
            raise HTTPException(detail="Failed to update category", status_code=500)

        return ProductCategory.model_validate(response.data[0])

    @classmethod
    async def delete_product_category(cls, category_id: int) -> None:
        """Delete a product category by ID."""

        # Check if the category exists before attempting to delete
        if not await ProductUtils.exist_category(category_id):
            raise HTTPException(detail="Category not found", status_code=404)

        client = await get_db_client()

        response = await client.table(SETTINGS.product_category_table).delete().eq("id", category_id).execute()

        if not bool(response.data):
            raise HTTPException(detail="Failed to delete category", status_code=500)
        
        return bool(response.data)

    @classmethod
    async def create_category(cls, category: CategoryCreate) -> Category:
        """Create a new product category."""

        client = await get_db_client()

        response = await client.table(SETTINGS.category_table).insert(category.model_dump(mode="json")).execute()

        if not bool(response.data):
            raise HTTPException(detail="Failed to create category", status_code=500)

        return Category.model_validate(response.data[0])
    
    @classmethod
    async def read_all_categories(cls) -> list[Category]:
        """Retrieve all product categories."""

        client = await get_db_client()

        response = await client.table(SETTINGS.category_table).select("*").execute()

        if not bool(response.data):
            raise HTTPException(detail="No categories found", status_code=404)

        return [Category.model_validate(category) for category in response.data]
    
    @classmethod
    async def read_category(cls, category_id: int) -> Category:
        """Retrieve a product category by ID."""

        client = await get_db_client()

        response = await client.table(SETTINGS.category_table).select("*").eq("id", category_id).execute()

        if not bool(response.data):
            raise HTTPException(detail="Category not found", status_code=404)

        return Category.model_validate(response.data[0])
    
    @classmethod
    async def read_category_base(cls, category_id: int) -> CategoryPlusID:
        """Retrieve a product category by ID."""
        
        client = await get_db_client()

        response = await client.table(SETTINGS.category_table).select(*cls.FIELDS_CATEGORY_BASE).eq("id", category_id).execute()

        if not bool(response.data):
            raise HTTPException(detail="Category not found", status_code=404)

        return CategoryPlusID.model_validate(response.data[0])
    
    @classmethod
    async def read_all_categories_base(cls) -> list[CategoryPlusID]:
        """Retrieve all product categories."""
        
        client = await get_db_client()

        response = await client.table(SETTINGS.category_table).select(*cls.FIELDS_CATEGORY_BASE).execute()

        if not bool(response.data):
            raise HTTPException(detail="No categories found", status_code=404)

        return [CategoryPlusID.model_validate(category) for category in response.data]
    
    @classmethod
    async def update_category(cls, category_id: int, fields: dict) -> Category:
        """Update an existing product category."""
        
        # Check if the category exists before attempting to update
        if not await ProductUtils.exist_category(category_id):
            raise HTTPException(detail="Category not found", status_code=404)
        
        if any(field in fields for field in cls.EXCLUDED_FIELDS_FOR_CATEGORY_UPDATE):
            raise HTTPException(detail=f"Cannot update fields: {', '.join(cls.EXCLUDED_FIELDS_FOR_CATEGORY_UPDATE)}", status_code=400)
        
        if not(set(fields.keys()) <= cls.ALLOWED_FIELDS_FOR_CATEGORY_UPDATE):
            raise HTTPException(detail="Update attribute of category", status_code=400)

        client = await get_db_client()

        response = await client.table(SETTINGS.category_table).update(fields).eq("id", category_id).execute()

        if not bool(response.data):
            raise HTTPException(detail="Failed to update category", status_code=500)

        return Category.model_validate(response.data[0])
    
    @classmethod
    async def delete_category(cls, category_id: int) -> None:
        """Delete a product category by ID."""

        # Check if the category exists before attempting to delete
        if not await ProductUtils.exist_category(category_id):
            raise HTTPException(detail="Category not found", status_code=404)

        client = await get_db_client()

        response = await client.table(SETTINGS.category_table).delete().eq("id", category_id).execute()

        if not bool(response.data):
            raise HTTPException(detail="Failed to delete category", status_code=500)
        
        return bool(response.data)