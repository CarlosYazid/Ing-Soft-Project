from fastapi import UploadFile
from typing import Optional, TYPE_CHECKING
from datetime import datetime, date

from pydantic import BaseModel, Field, ConfigDict
from sqlmodel import Field as FieldDB, SQLModel, Relationship

if TYPE_CHECKING:
    from models.service import ServiceInput
    from models.products import ProductCategory
    from models.order import OrderProduct

class Product(SQLModel, table=True):
    """
    Product model for the database.
    """
    id: Optional[int] = FieldDB(primary_key=True, index=True)
    name: str = FieldDB(..., description="Product's name")
    short_description: Optional[str] = FieldDB(None, description="Short description of the product")
    price: float = FieldDB(..., description="Product's price")
    cost: float = FieldDB(..., description="Product's cost")
    stock: int = FieldDB(..., description="Available stock of the product")
    minimum_stock: int = FieldDB(..., description="Minimum stock level of the product")
    image_key: Optional[str] = FieldDB(None, description="Key of the product image")
    expiration_date: Optional[date] = FieldDB(None, description="Expiration date of the consumable product")
    created_at: datetime = FieldDB(default_factory = datetime.now, description="Timestamp when the product was created")
    updated_at: datetime = FieldDB(default_factory = datetime.now, description="Timestamp when the product was last updated")

    service_inputs: Optional[list['ServiceInput']] = Relationship(back_populates="product", sa_relationship_kwargs={"lazy": "selectin"})
    product_categories: Optional[list['ProductCategory']] = Relationship(back_populates="product", sa_relationship_kwargs={"lazy": "selectin"})
    order_products: Optional[list['OrderProduct']] = Relationship(back_populates="product", sa_relationship_kwargs={"lazy": "selectin"})

class ProductCreate(BaseModel):
    
    name: str = Field(..., description="Product's name")
    short_description: Optional[str] = Field(None, description="Short description of the product")
    price: float = Field(..., description="Product's price", gt = 0)
    image: UploadFile = Field(..., description="Image of the product")
    cost: float = Field(..., description="Product's cost", gt = 0)
    stock: int = Field(..., description="Available stock of the product", gt = 0)
    minimum_stock: int = Field(..., description="Minimum stock level of the product", gt = 0)
    expiration_date: Optional[date] = Field(None, description="Expiration date of the consumable product")
    
    model_config: ConfigDict = ConfigDict(str_strip_whitespace=True,
                                          json_schema_extra={
                                              "example": {
                                                  "name": "Ejemplo de producto de papelería",
                                                  "short_description": "Este es un producto de papelería de ejemplo.",
                                                  "price": 9.99,
                                                  "stock": 50,
                                                  "minimum_stock" : 7,
                                                  "expiration_date": "2023-12-31"
                                              }
                                          },
                                          json_encoders={
                                              datetime: lambda v: v.isoformat()
                                          })
    

class ProductRead(BaseModel):
    """
    Product model for the API response.
    """
    id: int = Field(..., description="Product's unique identifier")
    name: str = Field(..., description="Product's name")
    short_description: Optional[str] = Field(None, description="Short description of the product")
    price: float = Field(..., description="Product's price")
    cost: float = Field(..., description="Product's cost")
    stock: int = Field(..., description="Available stock of the product")
    minimum_stock: int = Field(..., description="Minimum stock level of the product")
    image_key: Optional[str] = Field(None, description="URL of the product image")
    expiration_date: Optional[date] = Field(None, description="Expiration date of the consumable product")

    model_config: ConfigDict = ConfigDict(str_strip_whitespace=True,
                                          json_schema_extra={
                                              "example": {
                                                  "id": 1,
                                                  "name": "Ejemplo de producto de papelería",
                                                  "short_description": "Este es un producto de papelería de ejemplo.",
                                                  "price": 9.99,
                                                  "stock": 50,
                                                  "minimum_stock" : 7,
                                                  "image_url": "https://example.com/image.jpg",
                                                  "expiration_date": "2023-12-31"
                                              }
                                          },
                                          json_encoders={
                                              datetime: lambda v: v.isoformat()
                                          })
    

class ProductUpdate(BaseModel):
    """
    Product model for the API request.
    """
    id: int = Field(..., description="Product's unique identifier")
    name: Optional[str] = Field(None, description="Product's name")
    short_description: Optional[str] = Field(None, description="Short description of the product")
    price: Optional[float] = Field(None, description="Product's price", gt = 0)
    cost: Optional[float] = Field(None, description="Product's cost", gt = 0)
    minimum_stock: Optional[int] = Field(None, description="Minimum stock level of the product", gt = 0)
    expiration_date: Optional[date] = Field(None, description="Expiration date of the consumable product")
    updated_at: datetime = Field(default_factory = datetime.now, description="Timestamp when the product was last updated")

    model_config: ConfigDict = ConfigDict(str_strip_whitespace=True,
                                          json_schema_extra={
                                              "example": {
                                                  "name": "Ejemplo de producto de papelería",
                                                  "short_description": "Este es un producto de papelería de ejemplo.",
                                                  "price": 9.99,
                                                  "cost": 5.99,
                                                  "stock": 50,
                                                  "minimum_stock" : 7,
                                                  "expiration_date": "2023-12-31",
                                                  "updated_at" : "2023-12-31T00:00:00Z"
                                              }
                                          },
                                          json_encoders={
                                              datetime: lambda v: v.isoformat()
                                          })
    
class ProductCategory(SQLModel, table=True):
    """
    ProductCategory model for the database.
    """
    product_id: int = FieldDB(foreign_key="product.id", primary_key=True)
    category_id: int = FieldDB(foreign_key="category.id", primary_key=True)

    product: 'Product' = Relationship(back_populates="product_categories")
    category: 'Category' = Relationship(back_populates="product_categories")

class Category(SQLModel, table=True):
    """
    Category model for the database.
    """
    id: Optional[int] = FieldDB(primary_key=True, index=True)
    name: str = FieldDB(..., description="Category's name")
    description: str = FieldDB(..., description="Category's description")
    created_at: datetime = FieldDB(default_factory = datetime.now, description="Timestamp when the category was created")
    updated_at: datetime = FieldDB(default_factory = datetime.now, description="Timestamp when the category was last updated")

    product_categories: Optional[list['ProductCategory']] = Relationship(back_populates="category", sa_relationship_kwargs={"lazy": "selectin"})

class CategoryCreate(BaseModel):
    """
    Category model for the API request.
    """
    name: str = Field(..., description="Category's name")
    description: str = Field(..., description="Category's description")

    model_config: ConfigDict = ConfigDict(str_strip_whitespace=True,
                                          use_enum_values=True,
                                          json_schema_extra={
                                              "example": {
                                                  "name": "Ejemplo de categoría",
                                                  "description": "Descripción de la categoría de ejemplo."
                                              }
                                          })

class CategoryRead(BaseModel):
    """
    Category model for the API response.
    """
    id: int = Field(..., description="Category's unique identifier")
    name: str = Field(..., description="Category's name")
    description: str = Field(..., description="Category's description")

    model_config: ConfigDict = ConfigDict(str_strip_whitespace=True,
                                          use_enum_values=True,
                                          json_schema_extra={
                                              "example": {
                                                  "id": 1,
                                                  "name": "Ejemplo de categoría",
                                                  "description": "Descripción de la categoría de ejemplo."
                                              }
                                          })

class CategoryUpdate(BaseModel):
    """
    Category model for the API request.
    """
    id: int = Field(..., description="Category's unique identifier")
    name: Optional[str] = Field(None, description="Category's name")
    description: Optional[str] = Field(None, description="Category's description")
    update_at: datetime = Field(default_factory = datetime.now, description="Timestamp when the category was last updated")

    model_config: ConfigDict = ConfigDict(str_strip_whitespace=True,
                                          use_enum_values=True,
                                          json_schema_extra={
                                              "example": {
                                                  "name": "Ejemplo de categoría",
                                                  "description": "Descripción de la categoría de ejemplo.",
                                                  "update_at": "2023-12-31T00:00:00Z"
                                              }
                                          })