from datetime import date

from fastapi import APIRouter, Request, Depends, UploadFile, File
from fastapi_pagination import Page
from fastapi_pagination.ext.sqlmodel import apaginate
from sqlmodel.ext.asyncio.session import AsyncSession
from botocore.client import BaseClient

from models import ProductCategory
from dtos import ProductCreate, ProductRead, ProductUpdate, ProductFilter, CategoryCreate, CategoryRead, CategoryUpdate, CategoryFilter
from crud import ProductCrud
from services import AuthService, ProductService
from core import get_e2_client
from db import get_session

router = APIRouter(prefix="/product")

@router.post("/", response_model = ProductRead)
async def create_product(request: Request,
                         product: ProductCreate,
                         db_session: AsyncSession = Depends(get_session)):
    """
    Create a product
    """
    return await ProductCrud.create_product(db_session, product)

@router.get("/{_id}", response_model = ProductRead)
async def read_product(request: Request, _id: int, db_session: AsyncSession = Depends(get_session)):
    """
    Retrieve a product by ID.
    """
    return await ProductCrud.read_product(db_session, _id)

@router.get("/", response_model = ProductRead)
async def read_product_2(request: Request, id: int, db_session: AsyncSession = Depends(get_session)):
    """
    Retrieve a product by ID.
    """
    return await ProductCrud.read_product(db_session, id)

@router.patch("/", response_model = ProductRead)
async def update_product(request: Request,
                         fields: ProductUpdate,
                         db_session: AsyncSession = Depends(get_session)):
    """
    Update an existing product by ID.
    """
    return await ProductCrud.update_product(db_session, fields)

@router.patch("/image/{_id}", response_model = ProductRead)
async def update_image(request: Request,
                       _id: int,
                       image: UploadFile = File(..., title="photo_product"),
                       storage_client: BaseClient = Depends(get_e2_client),
                       db_session: AsyncSession = Depends(get_session)):
    """
    Update the image of a product by ID.
    """
    return await ProductCrud.update_image(db_session, storage_client, _id, image)

@router.patch("/image/", response_model = ProductRead)
async def update_image_2(request: Request,
                         id: int,
                         image: UploadFile = File(..., title="photo_product"),
                         storage_client: BaseClient = Depends(get_e2_client),
                         db_session: AsyncSession = Depends(get_session)):
    """
    Update the image of a product by ID.
    """
    return await ProductCrud.update_image(db_session, storage_client, id, image)

@router.patch("/stock/{_id}/{stock}/{replace}", response_model = ProductRead)
async def update_product_stock(request: Request,
                               _id: int, 
                               stock: int,
                               replace: bool = True,
                               db_session: AsyncSession = Depends(get_session)):
    """
    Update the stock of a product by ID.
    """
    return await ProductCrud.update_stock(db_session, _id, stock, replace)

@router.patch("/stock/", response_model = ProductRead)
async def update_product_stock_2(request: Request, 
                                 id: int, 
                                 stock: int, 
                                 replace: bool = True,
                                 db_session: AsyncSession = Depends(get_session)):
    """
    Update the stock of a product by ID.
    """
    return await ProductCrud.update_stock(db_session, id, stock, replace)

@router.delete("/{_id}")
async def delete_product(request: Request,
                         _id: int,
                          storage_client: BaseClient = Depends(get_e2_client),
                          db_session: AsyncSession = Depends(get_session)):
    """
    Delete a product by ID.
    """
    return await ProductCrud.delete_product(db_session, storage_client, _id)

@router.delete("/")
async def delete_product_2(request: Request, 
                           id: int,
                           storage_client: BaseClient = Depends(get_e2_client),
                           db_session: AsyncSession = Depends(get_session)):
    """
    Delete a product by ID.
    """
    return await ProductCrud.delete_product(db_session, storage_client, id)

@router.post("/product-category", response_model = ProductCategory)
async def create_product_category(request: Request,
                                  category: ProductCategory,
                                  db_session: AsyncSession = Depends(get_session)):
    """
    Create a new product category.
    """
    return await ProductCrud.create_product_category(db_session, category)

@router.delete("/product-category/")
async def delete_product_category(request: Request,
                                  product_category: ProductCategory,
                                  db_session: AsyncSession = Depends(get_session)):
    """
    Delete a product category by ID.
    """
    return await ProductCrud.delete_product_category(db_session, product_category)

@router.post("/category", response_model = CategoryRead)
async def create_category(request: Request,
                          category: CategoryCreate,
                          db_session: AsyncSession = Depends(get_session)):
    """
    Create a new product category.
    """
    return await ProductCrud.create_category(db_session, category)

@router.get("/category/{_id}", response_model = CategoryRead)
async def read_category(request: Request, _id: int, db_session: AsyncSession = Depends(get_session)):
    """
    Retrieve a product category by ID.
    """
    return await ProductCrud.read_category(db_session, _id)

@router.get("/category/", response_model = CategoryRead)
async def read_category_2(request: Request, id: int, db_session: AsyncSession = Depends(get_session)):
    """
    Retrieve a product category by ID.
    """
    return await ProductCrud.read_category(db_session, id)

@router.patch("/category/", response_model = CategoryRead)
async def update_category(request: Request,
                            fields: CategoryUpdate,
                            db_session: AsyncSession = Depends(get_session)):
    """
    Update an existing product category by ID.
    """
    return await ProductCrud.update_category(db_session, fields)

@router.delete("/category/{_id}")
async def delete_category(request: Request, _id: int, db_session: AsyncSession = Depends(get_session)):
    """
    Delete a product category by ID.
    """
    return await ProductCrud.delete_category(db_session, _id)

@router.delete("/category/")
async def delete_category_2(request: Request, id: int, db_session: AsyncSession = Depends(get_session)):
    """
    Delete a product category by ID.
    """
    return await ProductCrud.delete_category(db_session, id)

@router.post("/search", response_model = Page[ProductRead])
async def search_products(request: Request,
                          filters: ProductFilter,
                          db_session: AsyncSession = Depends(get_session)):
    """
    Search category who meet the filters.
    """
    return await apaginate(db_session, ProductService.search_products(filters))

@router.get("/search/category/{category_id}", response_model = Page[ProductRead])
async def search_products_by_category(request: Request,
                                      category_id: int,
                                      db_session: AsyncSession = Depends(get_session)):
    """
    Get products by category.
    """
    return await apaginate(db_session, ProductService.search_products_by_category(category_id))

@router.get("/search/category/", response_model = Page[ProductRead])
async def search_products_by_category_2(request: Request,
                                        category_id: int,
                                        db_session: AsyncSession = Depends(get_session)):
    """
    Get products by category in base format.
    """
    return await apaginate(db_session, ProductService.search_products_by_category(category_id))

@router.get("/search/service/{service_id}", response_model = Page[ProductRead])
async def search_products_by_service(request: Request,
                                     service_id: int,
                                     db_session: AsyncSession = Depends(get_session)):
    """
    Get products by service.
    """
    return await apaginate(db_session, ProductService.search_products_by_service(service_id))

@router.get("/search/service/", response_model = Page[ProductRead])
async def search_products_by_service_2(request: Request,
                                     service_id: int,
                                     db_session: AsyncSession = Depends(get_session)):
    """
    Get products by service.
    """
    return await apaginate(db_session, ProductService.search_products_by_service(service_id))

@router.get("/search/low-stock", response_model = Page[ProductRead])
async def search_low_stock_products(request: Request,
                                    db_session: AsyncSession = Depends(get_session)):
    """
    Search products with low stock.
    """
    return await apaginate(db_session, ProductService.search_low_stock_products())

@router.get("/search/expired", response_model = Page[ProductRead])
async def search_expired_products(request: Request,
                                  db_session: AsyncSession = Depends(get_session)):
    """
    Search expired products.
    """
    return await apaginate(db_session, ProductService.search_expired_products())

@router.post("/category/search", response_model = Page[CategoryRead])
async def search_category(request: Request,
                          filters: CategoryFilter,
                          db_session: AsyncSession = Depends(get_session)):
    """
    Search category who meet the filters.
    """
    return await apaginate(db_session, ProductService.search_categories(filters))