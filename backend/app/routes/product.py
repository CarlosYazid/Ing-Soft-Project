from fastapi import APIRouter, Request, Depends, UploadFile, File, Form
from datetime import date

from models import ProductCreate, ProductCategoryCreate
from crud import ProductCrud
from services import AuthService, ProductService

router = APIRouter(prefix="/product")

@router.post("/")
async def create_product(request: Request, product: ProductCreate):
    
    return await ProductCrud.create_product(product)

@router.get("/all")
async def read_all_products(request: Request):
    return await ProductCrud.read_all_products()

@router.get("/base/all")
async def read_all_products_base(request: Request):
    """
    Retrieve all products in base format.
    """
    return await ProductCrud.read_all_products_base()

@router.get("/{_id}")
async def read_product(request: Request, _id: int):
    """
    Retrieve a product by ID.
    """
    return await ProductCrud.read_product(_id)

@router.get("/")
async def read_product_2(request: Request, id: int):
    """
    Retrieve a product by ID.
    """
    return await ProductCrud.read_product(id)

@router.get("/base/{_id}")
async def read_product_base(request: Request, _id: int):
    """
    Get a product base by ID.
    """
    return await ProductCrud.read_product_base(_id)

@router.get("/base/")
async def read_product_base_2(request: Request, id: int):
    """
    Get a product base by ID.
    """
    return await ProductCrud.read_product_base(id)

@router.put("/{_id}")
async def update_product(request: Request, _id: int, fields: dict):
    """
    Update an existing product by ID.
    """
    return await ProductCrud.update_product(_id, fields)

@router.put("/image/{_id}")
async def upload_image(request: Request, _id: int, image: UploadFile = File(..., title="photo_product")):
    """ Update the image of a product by ID."""
    return await ProductCrud.upload_image(_id, image)

@router.put("/image/")
async def upload_image_2(request: Request, id: int, image: UploadFile = File(..., title="photo_product")):
    """ Update the image of a product by ID."""
    return await ProductCrud.upload_image(id, image)

@router.put("/stock/{_id}/{stock}/{replace}")
async def update_product_stock(request: Request, _id: int, stock: int, replace: bool = True):
    """
    Update the stock of a product by ID.
    """
    return await ProductCrud.update_stock(_id, stock, replace)

@router.put("/stock/")
async def update_product_stock_2(request: Request, id: int, stock: int, replace: bool = True):
    """
    Update the stock of a product by ID.
    """
    return await ProductCrud.update_stock(id, stock, replace)

@router.delete("/{_id}")
async def delete_product(request: Request, _id: int):
    """
    Delete a product by ID.
    """
    return await ProductCrud.delete_product(_id)

@router.delete("/")
async def delete_product_2(request: Request, id: int):
    """
    Delete a product by ID.
    """
    return await ProductCrud.delete_product(id)

@router.post("/product_category")
async def create_product_category(request: Request, category: ProductCategoryCreate):
    """
    Create a new product category.
    """
    return await ProductCrud.create_product_category(category)

@router.get("/product_category/all")
async def read_all_product_categories(request: Request):
    """
    Retrieve all product categories.
    """
    return await ProductCrud.read_all_product_categories()

@router.get("/product_category/{_id}")
async def read_product_category(request: Request, _id: int):
    """
    Retrieve a product category by ID.
    """
    return await ProductCrud.read_product_category(_id)

@router.get("/product_category/")
async def read_product_category_2(request: Request, id: int):
    """
    Retrieve a product category by ID.
    """
    return await ProductCrud.read_product_category(id)

@router.put("/product_category/{_id}")
async def update_product_category(request: Request, _id: int, fields: dict):
    """
    Update an existing product category by ID.
    """
    return await ProductCrud.update_product_category(_id, fields)

@router.put("/product_category/")
async def update_product_category_2(request: Request, id: int, fields: dict):
    """
    Update an existing product category by ID.
    """
    return await ProductCrud.update_product_category(id, fields)

@router.delete("/product_category/{_id}")
async def delete_product_category(request: Request, _id: int):
    """
    Delete a product category by ID.
    """
    return await ProductCrud.delete_product_category(_id)

@router.delete("/product_category/")
async def delete_product_category_2(request: Request, id: int):
    """
    Delete a product category by ID.
    """
    return await ProductCrud.delete_product_category(id)

@router.post("/category")
async def create_category(request: Request, category: ProductCategoryCreate):
    """
    Create a new product category.
    """
    return await ProductCrud.create_category(category)

@router.get("/category/all")
async def read_all_categories(request: Request):
    """
    Retrieve all product categories.
    """
    return await ProductCrud.read_all_categories()

@router.get("/category/base/all")
async def read_all_categories_base(request: Request):
    """
    Retrieve all product categories in base format.
    """
    return await ProductCrud.read_all_categories_base()

@router.get("/category/{_id}")
async def read_category(request: Request, _id: int):
    """
    Retrieve a product category by ID.
    """
    return await ProductCrud.read_category(_id)

@router.get("/category/")
async def read_category_2(request: Request, id: int):
    """
    Retrieve a product category by ID.
    """
    return await ProductCrud.read_category(id)

@router.get("/category/base/{_id}")
async def read_category_base(request: Request, _id: int):
    """
    Get a product category base by ID.
    """
    return await ProductCrud.read_category_base(_id)

@router.get("/category/base/")
async def read_category_base_2(request: Request, id: int):
    """
    Get a product category base by ID.
    """
    return await ProductCrud.read_category_base(id)

@router.put("/category/{_id}")
async def update_category(request: Request, _id: int, fields: dict):
    """
    Update an existing product category by ID.
    """
    return await ProductCrud.update_category(_id, fields)


@router.put("/category/")
async def update_category_2(request: Request, id: int, fields: dict):
    """
    Update an existing product category by ID.
    """
    return await ProductCrud.update_category(id, fields)


@router.delete("/category/{_id}")
async def delete_category(request: Request, _id: int):
    """
    Delete a product category by ID.
    """
    return await ProductCrud.delete_category(_id)

@router.delete("/category/")
async def delete_category_2(request: Request, id: int):
    """
    Delete a product category by ID.
    """
    return await ProductCrud.delete_category(id)

@router.get("/search/category/{category_id}")
async def search_products_by_category(request: Request, category_id: int):
    """
    Get products by category.
    """
    return await ProductService.search_products_by_category(category_id)

@router.get("/search/category/")
async def search_products_by_category_2(request: Request, category_id: int):
    """
    Get products by category in base format.
    """
    return await ProductService.search_products_by_category(category_id)


@router.get("/search/name/{name}")
async def search_products_by_name(request: Request, name: str):
    """
    Search products by name.
    """
    return await ProductService.search_products_by_name(name)

@router.get("/search/name/")
async def search_products_by_name_2(request: Request, name: str):
    """
    Search products by name in base format.
    """
    return await ProductService.search_products_by_name(name)

@router.get("/search/price/{min_price}/{max_price}")
async def search_products_by_price_range(request: Request, min_price: float, max_price: float):
    """
    Search products by price range.
    """
    return await ProductService.search_products_by_price_range(min_price, max_price)

@router.get("/search/price/")
async def search_products_by_price_range_2(request: Request, min_price: float, max_price: float):
    """
    Search products by price range in base format.
    """
    return await ProductService.search_products_by_price_range(min_price, max_price)

@router.get("/search/stock/{min_stock}/{max_stock}")
async def search_products_by_stock_range(request: Request, min_stock: int, max_stock: int):
    """
    Search products by stock range.
    """
    return await ProductService.search_products_by_stock_range(min_stock, max_stock)


@router.get("/search/stock/")
async def search_products_by_stock_range_2(request: Request, min_stock: int, max_stock: int):
    """
    Search products by stock range in base format.
    """
    return await ProductService.search_products_by_stock_range(min_stock, max_stock)

@router.get("/search/expiration/{expiration_date}")
async def search_products_by_expiration_date(request: Request, expiration_date: date):
    """
    Search products by expiration date.
    """
    return await ProductService.search_products_by_expiration_date(expiration_date)

@router.get("/search/expiration/")
async def search_products_by_expiration_date_2(request: Request, expiration_date: date):
    """
    Search products by expiration date in base format.
    """
    return await ProductService.search_products_by_expiration_date(expiration_date)

@router.get("/search/cost/{min_cost}/{max_cost}")
async def search_products_by_cost_range(request: Request, min_cost: float, max_cost: float):
    """
    Search products by cost range.
    """
    return await ProductService.search_products_by_cost_range(min_cost, max_cost)

@router.get("/search/cost/")
async def search_products_by_cost_range_2(request: Request, min_cost: float, max_cost: float):
    """
    Search products by cost range in base format.
    """
    return await ProductService.search_products_by_cost_range(min_cost, max_cost)

@router.get("/search/low-stock")
async def search_low_stock_products(request: Request):
    """
    Search products with low stock.
    """
    return await ProductService.search_low_stock_products()

@router.get("/search/expired")
async def search_expired_products(request: Request):
    """
    Search expired products.
    """
    return await ProductService.search_expired_products()

@router.get("/search/category/name/{category_name}")
async def search_category_by_name(request: Request, category_name: str):
    """
    Search products by category name.
    """
    return await ProductService.search_category_by_name(category_name)

@router.get("/search/category/name/")
async def search_category_by_name_2(request: Request, category_name: str):
    """
    Search products by category name in base format.
    """
    return await ProductService.search_category_by_name(category_name)
