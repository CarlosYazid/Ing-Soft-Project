from datetime import date

from fastapi import APIRouter, Request, Depends, UploadFile, File
from sqlmodel.ext.asyncio.session import AsyncSession
from botocore.client import BaseClient

from models import ProductCreate, ProductRead, ProductUpdate, ProductCategory, CategoryCreate, CategoryRead, CategoryUpdate
from crud import ProductCrud
from services import AuthService, ProductService
from core import get_e2_client
from db import get_session

router = APIRouter(prefix="/product")

@router.post("/", response_model = ProductRead)
async def create_product(request: Request,
                         product: ProductCreate,
                         storage_client: BaseClient = Depends(get_e2_client),
                         db_session: AsyncSession = Depends(get_session)):
    """
    Create a product
    """
    return await ProductCrud.create_product(db_session, storage_client, product)

@router.get("/all", response_model = list[ProductRead])
async def read_all_products(request: Request, db_session: AsyncSession = Depends(get_session)):
    """
    Retrieve all products
    """
    return await ProductCrud.read_all_products(db_session)

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

@router.put("/", response_model = ProductRead)
async def update_product(request: Request,
                         fields: ProductUpdate,
                         db_session: AsyncSession = Depends(get_session)):
    """
    Update an existing product by ID.
    """
    return await ProductCrud.update_product(db_session, fields)

@router.put("/image/{_id}", response_model = ProductRead)
async def update_image(request: Request,
                       _id: int,
                       image: UploadFile = File(..., title="photo_product"),
                       storage_client: BaseClient = Depends(get_e2_client),
                       db_session: AsyncSession = Depends(get_session)):
    """
    Update the image of a product by ID.
    """
    return await ProductCrud.update_image(db_session, storage_client, _id, image)

@router.put("/image/", response_model = ProductRead)
async def update_image_2(request: Request,
                         id: int,
                         image: UploadFile = File(..., title="photo_product"),
                         storage_client: BaseClient = Depends(get_e2_client),
                         db_session: AsyncSession = Depends(get_session)):
    """
    Update the image of a product by ID.
    """
    return await ProductCrud.update_image(db_session, storage_client, id, image)

@router.put("/stock/{_id}/{stock}/{replace}", response_model = ProductRead)
async def update_product_stock(request: Request,
                               _id: int, 
                               stock: int,
                               replace: bool = True,
                               db_session: AsyncSession = Depends(get_session)):
    """
    Update the stock of a product by ID.
    """
    return await ProductCrud.update_stock(db_session, _id, stock, replace)

@router.put("/stock/", response_model = ProductRead)
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

@router.post("/product_category", response_model = ProductCategory)
async def create_product_category(request: Request,
                                  category: ProductCategory,
                                  db_session: AsyncSession = Depends(get_session)):
    """
    Create a new product category.
    """
    return await ProductCrud.create_product_category(db_session, category)

@router.get("/product_category/all", response_model = list[ProductCategory])
async def read_all_product_categories(request: Request, db_session: AsyncSession = Depends(get_session)):
    """
    Retrieve all product categories.
    """
    return await ProductCrud.read_all_product_categories(db_session)

@router.delete("/product_category/")
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

@router.get("/category/all", response_model = list[CategoryRead])
async def read_all_categories(request: Request, db_session: AsyncSession = Depends(get_session)):
    """
    Retrieve all product categories.
    """
    return await ProductCrud.read_all_categories(db_session)

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

@router.put("/category/", response_model = CategoryRead)
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

@router.get("/search/category/{category_id}", response_model = list[ProductRead])
async def search_products_by_category(request: Request,
                                      category_id: int,
                                      db_session: AsyncSession = Depends(get_session)):
    """
    Get products by category.
    """
    return await ProductService.search_products_by_category(db_session, category_id)

@router.get("/search/category/", response_model = list[ProductRead])
async def search_products_by_category_2(request: Request,
                                        category_id: int,
                                        db_session: AsyncSession = Depends(get_session)):
    """
    Get products by category in base format.
    """
    return await ProductService.search_products_by_category(db_session, category_id)

@router.get("/search/name/{name}", response_model = list[ProductRead])
async def search_products_by_name(request: Request,
                                  name: str,
                                  db_session: AsyncSession = Depends(get_session)):
    """
    Search products by name.
    """
    return await ProductService.search_products_by_name(db_session, name)

@router.get("/search/name/", response_model = list[ProductRead])
async def search_products_by_name_2(request: Request,
                                    name: str,
                                    db_session: AsyncSession = Depends(get_session)):
    """
    Search products by name in base format.
    """
    return await ProductService.search_products_by_name(db_session, name)

@router.get("/search/price/{min_price}/{max_price}", response_model = list[ProductRead])
async def search_products_by_price_range(request: Request,
                                         min_price: float,
                                         max_price: float,
                                         db_session: AsyncSession = Depends(get_session)):
    """
    Search products by price range.
    """
    return await ProductService.search_products_by_price_range(db_session, min_price, max_price)

@router.get("/search/price/", response_model = list[ProductRead])
async def search_products_by_price_range_2(request: Request,
                                           min_price: float,
                                           max_price: float,
                                           db_session: AsyncSession = Depends(get_session)):
    """
    Search products by price range in base format.
    """
    return await ProductService.search_products_by_price_range(db_session, min_price, max_price)

@router.get("/search/stock/{min_stock}/{max_stock}", response_model = list[ProductRead])
async def search_products_by_stock_range(request: Request,
                                         min_stock: int,
                                         max_stock: int,
                                         db_session: AsyncSession = Depends(get_session)):
    """
    Search products by stock range.
    """
    return await ProductService.search_products_by_stock_range(db_session, min_stock, max_stock)

@router.get("/search/stock/", response_model = list[ProductRead])
async def search_products_by_stock_range_2(request: Request,
                                           min_stock: int,
                                           max_stock: int,
                                           db_session: AsyncSession = Depends(get_session)):
    """
    Search products by stock range in base format.
    """
    return await ProductService.search_products_by_stock_range(db_session, min_stock, max_stock)

@router.get("/search/expiration/{expiration_date}", response_model = list[ProductRead])
async def search_products_by_expiration_date(request: Request,
                                             expiration_date: date,
                                             db_session: AsyncSession = Depends(get_session)):
    """
    Search products by expiration date.
    """
    return await ProductService.search_products_by_expiration_date(db_session, expiration_date)

@router.get("/search/expiration/", response_model = list[ProductRead])
async def search_products_by_expiration_date_2(request: Request,
                                               expiration_date: date,
                                               db_session: AsyncSession = Depends(get_session)):
    """
    Search products by expiration date in base format.
    """
    return await ProductService.search_products_by_expiration_date(db_session, expiration_date)

@router.get("/search/cost/{min_cost}/{max_cost}", response_model = list[ProductRead])
async def search_products_by_cost_range(request: Request,
                                        min_cost: float,
                                        max_cost: float,
                                        db_session: AsyncSession = Depends(get_session)):
    """
    Search products by cost range.
    """
    return await ProductService.search_products_by_cost_range(db_session, min_cost, max_cost)

@router.get("/search/cost/", response_model = list[ProductRead])
async def search_products_by_cost_range_2(request: Request,
                                          min_cost: float,
                                          max_cost: float, 
                                          db_session: AsyncSession = Depends(get_session)):
    """
    Search products by cost range in base format.
    """
    return await ProductService.search_products_by_cost_range(db_session, min_cost, max_cost)

@router.get("/search/low-stock", response_model = list[ProductRead])
async def search_low_stock_products(request: Request,
                                    db_session: AsyncSession = Depends(get_session)):
    """
    Search products with low stock.
    """
    return await ProductService.search_low_stock_products(db_session)

@router.get("/search/expired", response_model = list[ProductRead])
async def search_expired_products(request: Request,
                                  db_session: AsyncSession = Depends(get_session)):
    """
    Search expired products.
    """
    return await ProductService.search_expired_products(db_session)

@router.get("/search/category/name/{category_name}", response_model = list[ProductRead])
async def search_category_by_name(request: Request,
                                  category_name: str,
                                  db_session: AsyncSession = Depends(get_session)):
    """
    Search products by category name.
    """
    return await ProductService.search_category_by_name(db_session, category_name)

@router.get("/search/category/name/", response_model = list[ProductRead])
async def search_category_by_name_2(request: Request,
                                    category_name: str,
                                    db_session: AsyncSession = Depends(get_session)):
    """
    Search products by category name in base format.
    """
    return await ProductService.search_category_by_name(db_session, category_name)