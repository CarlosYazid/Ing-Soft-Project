from fastapi import APIRouter, Request, Depends, UploadFile, File, Form
from typing import Optional
from datetime import datetime

from models import Product, ProductCategory, ProductTypes
from crud import ProductCrud
from services import AuthService, ProductService

router = APIRouter(prefix="/products")

@router.get("/all")
async def get_products(request: Request):
    return await ProductCrud.get_all_products()

@router.get("/base/all")
async def get_products_base(request: Request):
    """
    Retrieve all products in base format.
    """
    return await ProductService.get_all_products_base()

@router.get("/{_id}")
async def get_product_by_id(request: Request, _id: int):
    """
    Retrieve a product by ID.
    """
    return await ProductCrud.get_product_by_id(_id)

@router.get("/")
async def get_product_by_id_2(request: Request, id: int):
    """
    Retrieve a product by ID.
    """
    return await ProductCrud.get_product_by_id(id)

@router.get("/base/{_id}")
async def get_product_base_by_id(request: Request, _id: int):
    """
    Get a product base by ID.
    """
    return await ProductService.get_product_base_by_id(_id)

@router.get("/base/")
async def get_product_base_by_id_2(request: Request, id: int):
    """
    Get a product base by ID.
    """
    return await ProductService.get_product_base_by_id(id)

@router.post("/")
async def create_product(request: Request, product: Product):
    
    return await ProductCrud.create_product(product)


@router.post("/{_id}")
async def update_product_by_id(request: Request, _id: int, fields: dict):
    """
    Update an existing product by ID.
    """
    return await ProductCrud.update_product(_id, fields)


@router.post("/image/{_id}")
async def update_product_image(request: Request, _id: int, image: UploadFile = File(...)):
    """ Update the image of a product by ID."""
    return await ProductCrud.upload_image(_id, image)

@router.post("/image/")
async def update_product_image_2(request: Request, id: int, image: UploadFile = File(...)):
    """ Update the image of a product by ID."""
    return await ProductCrud.upload_image(id, image)


@router.delete("/{_id}")
async def delete_product_by_id(request: Request, _id: int):
    """
    Delete a product by ID.
    """
    return await ProductCrud.delete_product(_id)

@router.delete("/")
async def delete_product_by_id_2(request: Request, id: int):
    """
    Delete a product by ID.
    """
    return await ProductCrud.delete_product(id)

@router.get("/category/{category}")
async def get_products_by_category(request: Request, category: str):
    """
    Get products by category.
    """
    return await ProductCrud.get_products_by_category(category)

@router.get("/type/{product_type}")
async def get_products_by_type(request: Request, product_type: str):
    """
    Get products by type.
    """
    return await ProductCrud.get_products_by_type(product_type)


@router.get("/base/category/{category}")
async def get_products_base_by_category(category: str):
    """
    Get products by category in base format.
    """
    return await ProductService.get_products_base_by_category(category)

@router.get("/base/type/{product_type}")
async def get_products_base_by_type(request : Request,product_type: str):
    """
    Get products by type in base format.
    """
    return await ProductService.get_products_base_by_type(product_type)
@router.get("/base/category/")
async def get_products_base_by_category_2(request: Request, category: str):
    """
    Get products by category in base format.
    """
    return await ProductService.get_products_base_by_category(category)

@router.get("/base/type/")
async def get_products_base_by_type_2(request: Request, product_type: str):
    """
    Get products by type in base format.
    """
    return await ProductService.get_products_base_by_type(product_type)
