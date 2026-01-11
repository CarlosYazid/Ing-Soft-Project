from typing import Optional, TYPE_CHECKING
from datetime import date

from sqlmodel import SQLModel, Relationship, Field

from models.abs import BaseModel

if TYPE_CHECKING:
    from models.service import ServiceInput
    from models.order import OrderProduct

class Product(BaseModel, table=True):
    """
    Product model for the database.
    """
    name: str = Field(..., description="Product's name")
    short_description: Optional[str] = Field(None, description="Short description of the product")
    price: float = Field(..., description="Product's price")
    cost: float = Field(..., description="Product's cost")
    stock: int = Field(..., description="Available stock of the product")
    minimum_stock: int = Field(..., description="Minimum stock level of the product")
    image_key: Optional[str] = Field(None, description="Key of the product image")
    expiration_date: Optional[date] = Field(None, description="Expiration date of the consumable product")

    service_inputs: Optional[list['ServiceInput']] = Relationship(back_populates="product", sa_relationship_kwargs={"lazy": "selectin"})
    product_categories: Optional[list['ProductCategory']] = Relationship(back_populates="product", sa_relationship_kwargs={"lazy": "selectin"})
    order_products: Optional[list['OrderProduct']] = Relationship(back_populates="product", sa_relationship_kwargs={"lazy": "selectin"})

    
class ProductCategory(SQLModel, table=True):
    """
    ProductCategory model for the database.
    """
    product_id: int = Field(foreign_key="product.id", primary_key=True, index = True)
    category_id: int = Field(foreign_key="category.id", primary_key=True, index = True)

    product: 'Product' = Relationship(back_populates="product_categories")
    category: 'Category' = Relationship(back_populates="product_categories")

class Category(BaseModel, table=True):
    """
    Category model for the database.
    """
    name: str = Field(..., description="Category's name")
    description: str = Field(..., description="Category's description")
    
    product_categories: Optional[list['ProductCategory']] = Relationship(back_populates="category", sa_relationship_kwargs={"lazy": "selectin"})