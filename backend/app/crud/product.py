from fastapi import HTTPException, UploadFile

from db import get_db_client
from models import Product, ProductCategory, ProductTypes, ProductCreate
from core import SETTINGS

class ProductCrud:

    ALLOWED_IMAGE_TYPES = {"image/png", "image/jpeg", "image/webp"}
    
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

        response = await client.table(SETTINGS.product_table).select("*").eq("category", category.capitalize()).execute()

        if not(bool(response.data)):
            raise HTTPException(detail="No products found in this category", status_code=404)

        return [Product.model_validate(product) for product in response.data]
    
    
    @classmethod
    async def get_products_by_type(cls, product_type: ProductTypes) -> list[Product]:
        """Retrieve products by type."""

        client = await get_db_client()

        response = await client.table(SETTINGS.product_table).select("*").eq("type", product_type.capitalize()).execute()

        if not(bool(response.data)):
            raise HTTPException(detail="No products found of this type", status_code=404)

        return [Product.model_validate(product) for product in response.data]
    
    @classmethod
    async def create_product(cls, product: ProductCreate) -> Product:
        """Create a new product."""
        
        client = await get_db_client()

        names = await client.table(SETTINGS.product_table).select("name").execute()

        if bool(names.data):
            if product.name.lower() in names.data:
                raise HTTPException(status_code=404, detail="The product already exists")
        
        product.image_url = None  # Initialize image_url to None

        from services.gen_ai import GenAIService

        product.short_description = await GenAIService.gen_short_description(product.description)
            
        response = await client.table(SETTINGS.product_table).insert(product.model_dump(mode="json")).execute()
        
        if not response.data:
            raise HTTPException(status_code=500, detail="Failed to create product")
        
        return Product.model_validate(response.data[0])

    
    @classmethod
    async def upload_image(cls, product_id: int, image: UploadFile) -> str:
        """Upload an image for a product and return the URL."""

        if image.content_type not in cls.ALLOWED_IMAGE_TYPES:
            raise HTTPException(
                status_code=400,
                detail=f"Tipo de archivo no permitido: {image.content_type}. Debe ser PNG, JPEG o WEBP.",
            )
        
        client = await get_db_client()
        
        # Check if the product exists before attempting to upload an image
        if not(cls.exist_product_by_id(product_id)):
            raise HTTPException(status_code=404, detail="Product not found")

        name, ext = image.filename.split(".")[-2:]
        
        last_image = await client.table(SETTINGS.product_table).select("image_url").eq("id", product_id).execute()
        
        if not bool(last_image.data):
            raise HTTPException(status_code=404, detail="Product not found")

        filename = f"products/{product_id}_{name.replace(' ', '_').lower()}.{ext}"

        if bool(last_image.data[0]["image_url"]):
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
    async def update_product(cls, product_id: int, fields: dict) -> Product:
        """Update an existing product."""

        client = await get_db_client()
        
        # Check if the product exists before attempting to update
        if not(cls.exist_product_by_id(product_id)):
            raise HTTPException(detail="Product not found", status_code=404)
        
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

        # Check if the product exists before attempting to delete
        if not await cls.exist_product_by_id(product_id):
            raise HTTPException(detail="Product not found", status_code=404)


        response = await client.table(SETTINGS.product_table).delete().eq("id", product_id).execute()

        if not(bool(response.data)):
            raise HTTPException(detail="Failed to delete product", status_code=500)
        
        return bool(response.data)
    
    @classmethod
    async def exist_product_by_id(cls, product_id: int) -> bool:
        """Check if a product exists by ID."""

        client = await get_db_client()

        response = await client.table(SETTINGS.product_table).select("id").eq("id", product_id).execute()

        return bool(response.data)