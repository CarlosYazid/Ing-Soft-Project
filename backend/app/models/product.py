from pydantic import BaseModel, Field, ConfigDict
from typing import Optional
from datetime import datetime
from enum import Enum

class ProductCategory(str, Enum):
    """
    Enum for product categories.
    """

    CONSUMABLES = "Consumibles"
    
    STATIONERY = "Papelería"

class ProductTypes(str, Enum):
    """
    Enum for product types.
    """

    GENERAL_STATIONERY = "Papelería_general"

    WRITING_AND_CORRECTION = "Escritura_y_corrección"

    MEASUREMENT_AND_DRAWING_TOOLS = "Medición_y_dibujo"

    ART_SUPPLIES = "Suministros_de_arte"

    SCHOOL_SUPPLIES = "Suministros_escolares"

    OFFICE_SUPPLIES = "Suministros_de_oficina"

    TECHNOLOGY_AND_ACCESSORIES = "Tecnología_y_accesorios"

    CHIPS_AND_SALTY_SNACKS = "Chips_y_snacks_salados"
    
    COOKIES_AND_BISCUITS = "Galletas_y_bizcochos"
    
    CANDY_AND_GUM = "Dulces_y_chicles"
    
    CHOCOLATES_AND_BARS = "Chocolates_y_barras"
    
    BAKED_GOODS = "Panadería_y_bollería"
    
    JUICES_AND_FLAVORED_DRINKS = "Jugos_y_bebidas_saborizadas"
    
    SOFT_DRINKS = "Gaseosas_y_sodas"
    
    BOTTLED_WATER = "Agua_embotellada"
    
    DAIRY_AND_REFRIGERATED_SNACKS = "Lácteos_y_snacks_refrigerados"
    
    NUTS_AND_DRIED_FRUITS = "Nueces_y_frutas_secas"

class ProductBase(BaseModel):
    """
    Base model for product schemas.
    """
    name: str = Field(..., description="Product's name")
    short_description: Optional[str] = Field(None, description="Short description of the product")
    price: float = Field(..., description="Product's price")
    category: ProductCategory = Field(..., description="Category of the product")
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
                                                  "category": "Papelería",
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
    type: Optional[ProductTypes] = Field(None, description="Type of the product")
    
    model_config: ConfigDict = ConfigDict(str_strip_whitespace=True,
                                          use_enum_values=True,
                                          json_schema_extra={
                                              "example": {
                                                  "name": "Ejemplo de producto de papelería",
                                                  "short_description": "Este es un producto de papelería de ejemplo.",
                                                  "price": 9.99,
                                                  "category": "Papelería",
                                                  "stock": 50,
                                                  "minimum_stock" : 7,
                                                  "description": "Descripción detallada del producto de papelería de ejemplo.",
                                                  "cost": 5.00,
                                                  "created_at": "2023-01-01T00:00:00Z",
                                                  "updated_at": "2023-01-01T00:00:00Z",
                                                  "type": "Papelería_general",
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
                                                  "category": "Papelería",
                                                  "stock": 50,
                                                  "minimum_stock" : 20,
                                                  "description": "Descripción detallada del producto de papelería de ejemplo.",
                                                  "cost": 5.00,
                                                  "created_at": "2023-01-01T00:00:00Z",
                                                  "updated_at": "2023-01-01T00:00:00Z",
                                                  "type": "Papelería_general",
                                                  "image_url": "https://example.com/image.jpg",
                                              }
                                          },
                                          json_encoders={
                                              datetime: lambda v: v.isoformat()
                                          })