from fastapi import HTTPException, UploadFile

from db import get_db_client
from models import Product, ProductCategory, ProductTypes
from core import SETTINGS


class ProductCrud:
    
    @classmethod
    async def get_all_products(cls) -> list[Product]:
        """Retrieve all products."""

        client = await get_db_client()

        response = await client.table(SETTINGS.product_table).select("*").execute()

        if not(bool(response.data)):
            raise HTTPException(detail="No products found", status_code=404)

        return [Product.model_validate(product) for product in response.data]
    
    @classmethod
    async def get_product_by_id(cls, product_id: int) -> Product:
        """Retrieve a product by ID."""

        client = await get_db_client()

        response = await client.table(SETTINGS.product_table).select("*").eq("id", product_id).execute()

        if not(bool(response.data)):
            raise HTTPException(detail="Product not found", status_code=404)

        return Product.model_validate(response.data[0])
    
    @classmethod
    async def get_products_by_category(cls, category: ProductCategory) -> list[Product]:
        """Retrieve products by category."""

        client = await get_db_client()

        response = await client.table(SETTINGS.product_table).select("*").eq("category", category).execute()

        if not(bool(response.data)):
            raise HTTPException(detail="No products found in this category", status_code=404)

        return [Product.model_validate(product) for product in response.data]
    
    
    @classmethod
    async def get_products_by_type(cls, product_type: ProductTypes) -> list[Product]:
        """Retrieve products by type."""

        client = await get_db_client()

        response = await client.table(SETTINGS.product_table).select("*").eq("type", product_type).execute()

        if not(bool(response.data)):
            raise HTTPException(detail="No products found of this type", status_code=404)

        return [Product.model_validate(product) for product in response.data]
    
    @classmethod
    async def create_product(cls, product: Product) -> Product:
        """Create a new product."""
        
        client = await get_db_client()
        
        product.image_url = None  # Initialize image_url to None
            
        response = await client.table(SETTINGS.product_table).insert(product.model_dump(mode="json")).execute()
        
        if not response.data:
            raise HTTPException(status_code=500, detail="Failed to create product")
        
        return Product.model_validate(response.data[0])

    
    @classmethod
    async def upload_image(cls, product_id: int, image: UploadFile) -> str:
        """Upload an image for a product and return the URL."""
        
        client = await get_db_client()

        name, ext = image.filename.split(".")[-2:]
        
        last_image = await client.table(SETTINGS.product_table).select("image_url").eq("id", product_id).execute()
        
        if not bool(last_image.data):
            raise HTTPException(status_code=404, detail="Product not found")

        last_image = "products/" + last_image.data[0]["image_url"].split("/")[-1]
        filename = f"products/{product_id}_{name.replace(' ', '_').lower()}.{ext}"
        file_content = await image.read()

        await client.storage.from_(SETTINGS.bucket_name).remove([last_image, filename])

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
    async def update_product(cls, product_id: int, fields: dict) -> Product:
        """Update an existing product."""

        client = await get_db_client()
        
        if "image_url" in fields:
            fields.pop("image_url")
            

        response = await client.table(SETTINGS.product_table).update(fields).eq("id", product_id).execute()

        if not(bool(response.data)):
            raise HTTPException(detail="Failed to update product", status_code=500)

        return Product.model_validate(response.data[0])
    
    @classmethod
    async def delete_product(cls, product_id: int) -> None:
        """Delete a product by ID."""

        client = await get_db_client()

        response = await client.table(SETTINGS.product_table).delete().eq("id", product_id).execute()

        if not(bool(response.data)):
            raise HTTPException(detail="Failed to delete product", status_code=500)
        
        return None
    
    @classmethod
    async def exist_product_by_id(cls, product_id: int) -> bool:
        """Check if a product exists by ID."""

        client = await get_db_client()

        response = await client.table(SETTINGS.product_table).select("id").eq("id", product_id).execute()

        return not(bool(response.data))