from pydantic import BaseModel, Field, ConfigDict
from typing import Optional
from datetime import datetime

class ProductBase(BaseModel):
    """
    Base model for product schemas.
    """
    name: str = Field(..., description="Product's name")
    short_description: Optional[str] = Field(None, description="Short description of the product")
    price: float = Field(..., description="Product's price")
    stock: int = Field(..., description="Available stock of the product")
    minimum_stock: int = Field(..., description="Minimum stock level of the product")
    image_url: Optional[str] = Field(None, description="URL of the product image")
    



class ProductBasePlusID(ProductBase):
    """
    Base model for product schemas with ID.
    """
    id: int = Field(..., description="Product's unique identifier")
    
    model_config: ConfigDict = ConfigDict(str_strip_whitespace=True,
                                          use_enum_values=True,
                                          json_schema_extra={
                                              "example": {
                                                  "id": 1,
                                                  "name": "Ejemplo de producto de papelería",
                                                  "short_description": "Este es un producto de papelería de ejemplo.",
                                                  "price": 9.99,
                                                  "stock": 50,
                                                  "minimum_stock" : 10,
                                                  "image_url": "https://example.com/image.jpg",
                                              }
                                          })


class ProductCreate(ProductBase):
    """
    Product model for the API request.
    """
    description: Optional[str] = Field(None, description="Product's description")
    cost: float = Field(..., description="Cost of the product")
    created_at: datetime = Field(..., description="Timestamp when the product was created")
    updated_at: datetime = Field(..., description="Timestamp when the product was last updated")
    expiration_date: Optional[datetime] = Field(None, description="Expiration date of the consumable product")
    
    model_config: ConfigDict = ConfigDict(str_strip_whitespace=True,
                                          use_enum_values=True,
                                          json_schema_extra={
                                              "example": {
                                                  "name": "Ejemplo de producto de papelería",
                                                  "short_description": "Este es un producto de papelería de ejemplo.",
                                                  "price": 9.99,
                                                  "stock": 50,
                                                  "minimum_stock" : 7,
                                                  "description": "Descripción detallada del producto de papelería de ejemplo.",
                                                  "cost": 5.00,
                                                  "created_at": "2023-01-01T00:00:00Z",
                                                  "updated_at": "2023-01-01T00:00:00Z",
                                                  "image_url": "https://example.com/image.jpg",
                                              }
                                          },
                                          json_encoders={
                                              datetime: lambda v: v.isoformat()
                                          })

class Product(ProductCreate):
    """
    Product model for the API response.
    """
    id: int = Field(..., description="Product's unique identifier")
    
    model_config: ConfigDict = ConfigDict(str_strip_whitespace=True,
                                          use_enum_values=True,
                                          json_schema_extra={
                                              "example": {
                                                  "id": 1,
                                                  "name": "Ejemplo de producto de papelería",
                                                  "short_description": "Este es un producto de papelería de ejemplo.",
                                                  "price": 9.99,
                                                  "stock": 50,
                                                  "minimum_stock" : 20,
                                                  "description": "Descripción detallada del producto de papelería de ejemplo.",
                                                  "cost": 5.00,
                                                  "created_at": "2023-01-01T00:00:00Z",
                                                  "updated_at": "2023-01-01T00:00:00Z",
                                                  "image_url": "https://example.com/image.jpg",
                                              }
                                          },
                                          json_encoders={
                                              datetime: lambda v: v.isoformat()
                                          })

class ProductCategoryBase(BaseModel):
    """
    Base model for product category schemas.
    """
    product_id: int = Field(..., description="ID of the product")
    category_id: int = Field(..., description="ID of the category")

    model_config: ConfigDict = ConfigDict(str_strip_whitespace=True,
                                          use_enum_values=True,
                                          json_schema_extra={
                                              "example": {
                                                  "name": "Papelería"
                                              }
                                          })

class ProductCategoryCreate(ProductCategoryBase):
    """
    Product category model for the API request.
    """
    created_at: datetime = Field(default=datetime.now(), description="Timestamp when the product category was created")
    
    model_config: ConfigDict = ConfigDict(str_strip_whitespace=True,
                                          use_enum_values=True,
                                          json_schema_extra={
                                              "example": {
                                                  "product_id": 1,
                                                  "category_id": 1
                                              }
                                          },
                                          json_encoders={
                                              datetime: lambda v: v.isoformat()
                                          })

class ProductCategory(ProductCategoryCreate):
    """
    Product category model for the API response.
    """
    id: int = Field(..., description="Product category's unique identifier")
    
    model_config: ConfigDict = ConfigDict(str_strip_whitespace=True,
                                          use_enum_values=True,
                                          json_schema_extra={
                                              "example": {
                                                  "id": 1,
                                                  "product_id": 1,
                                                  "category_id": 1,
                                                  "created_at": "2023-01-01T00:00:00Z"
                                              }
                                          },
                                          json_encoders={
                                              datetime: lambda v: v.isoformat()
                                          })

class ProductCategoryPlusID(ProductCategoryBase):
    """
    Product category model with ID for the API response.
    """
    id: int = Field(..., description="Product category's unique identifier")
    
    model_config: ConfigDict = ConfigDict(str_strip_whitespace=True,
                                          use_enum_values=True,
                                          json_schema_extra={
                                              "example": {
                                                  "id": 1,
                                                  "product_id": 1,
                                                  "category_id": 1,
                                                  "created_at": "2023-01-01T00:00:00Z"
                                              }
                                          },
                                          json_encoders={
                                              datetime: lambda v: v.isoformat()
                                          })

class CategoryBase(BaseModel):
    """
    Base model for category schemas.
    """
    name: str = Field(..., description="Category's name")
    
    model_config: ConfigDict = ConfigDict(str_strip_whitespace=True,
                                          use_enum_values=True,
                                          json_schema_extra={
                                              "example": {
                                                  "name": "Papelería"
                                              }
                                          })

class CategoryCreate(CategoryBase):
    """
    Category model for the API request.
    """
    description: str = Field(None, description="Category's description")
    created_at: datetime = Field(default=datetime.now(), description="Timestamp when the category was created")
    
    model_config: ConfigDict = ConfigDict(str_strip_whitespace=True,
                                          use_enum_values=True,
                                          json_schema_extra={
                                              "example": {
                                                  "name": "Papelería",
                                                  "created_at": "2023-01-01T00:00:00Z"
                                              }
                                          },
                                          json_encoders={
                                              datetime: lambda v: v.isoformat()
                                          })
class Category(CategoryCreate):
    """
    Category model for the API response.
    """
    id: int = Field(..., description="Category's unique identifier")
    
    model_config: ConfigDict = ConfigDict(str_strip_whitespace=True,
                                          use_enum_values=True,
                                          json_schema_extra={
                                              "example": {
                                                  "id": 1,
                                                  "name": "Papelería",
                                                  "description": "Categoría de productos de papelería.",
                                                  "created_at": "2023-01-01T00:00:00Z"
                                              }
                                          },
                                          json_encoders={
                                              datetime: lambda v: v.isoformat()
                                          })

class CategoryPlusID(CategoryBase):
    """
    Category model with ID for the API response.
    """
    id: int = Field(..., description="Category's unique identifier")
    
    model_config: ConfigDict = ConfigDict(str_strip_whitespace=True,
                                          use_enum_values=True,
                                          json_schema_extra={
                                              "example": {
                                                  "id": 1,
                                                  "name": "Papelería",
                                                  "created_at": "2023-01-01T00:00:00Z"
                                              }
                                          },
                                          json_encoders={
                                              datetime: lambda v: v.isoformat()
                                          })