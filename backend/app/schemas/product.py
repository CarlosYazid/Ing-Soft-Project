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

class StationeryType(str, Enum):
    """
    Enum for stationery types.
    """

    GENERAL_STATIONERY = "Papelería_general"

    WRITING_AND_CORRECTION = "Escritura_y_corrección"

    MEASUREMENT_AND_DRAWING_TOOLS = "Medición_y_dibujo"

    ART_SUPPLIES = "Suministros_de_arte"

    SCHOOL_SUPPLIES = "Suministros_escolares"

    OFFICE_SUPPLIES = "Suministros_de_oficina"

    TECHNOLOGY_AND_ACCESSORIES = "Tecnología_y_accesorios"

class ConsumableType(str, Enum):
    """
    Enum for consumable product types.
    """

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
    id: int = Field(..., description="Product's unique identifier")
    name: str = Field(..., description="Product's name")
    short_description: Optional[str] = Field(None, description="Short description of the product")
    price: float = Field(..., description="Product's price")
    category: ProductCategory = Field(..., description="Category of the product")
    stock: int = Field(..., description="Available stock of the product")
    


class Product(ProductBase):
    """
    Product model for the API response.
    """
    description: Optional[str] = Field(None, description="Product's description")
    cost : float = Field(..., description="Cost of the product")
    created_at: datetime = Field(..., description="Timestamp when the product was created")
    updated_at: datetime = Field(..., description="Timestamp when the product was last updated")
    

class Stationery(Product):
    """
    Stationery model for the API response.
    """
    
    type: StationeryType = Field(..., description="Type of the stationery product")
    
    model_config: ConfigDict = ConfigDict(str_to_lower=True,
                                          str_strip_whitespace=True,
                                          use_enum_values=True,
                                          json_schema_extra={
                                              "example": {
                                                  "id": 1,
                                                  "name": "Example Stationery",
                                                  "short_description": "This is an example stationery product.",
                                                  "price": 9.99,
                                                  "category": "stationery",
                                                  "description": "Detailed description of the example stationery product.",
                                                  "cost": 5.00,
                                                  "stock": 50,
                                                  "created_at": "2023-01-01T00:00:00Z",
                                                  "updated_at": "2023-01-01T00:00:00Z",
                                                  "type": "general_stationery"
                                              }
                                          },
                                          json_encoders={
                                              datetime: lambda v: v.isoformat()
                                          })
class Consumable(Product):
    """
    Consumable model for the API response.
    """
    expiration_date: datetime = Field(..., description="Expiration date of the consumable product")
    type: ConsumableType = Field(..., description="Type of the consumable product")

    model_config: ConfigDict = ConfigDict(str_to_lower=True,
                                          str_strip_whitespace=True,
                                          use_enum_values=True,
                                          json_schema_extra={
                                              "example": {
                                                  "id": 1,
                                                  "name": "Example Consumable",
                                                  "short_description": "This is an example consumable product.",
                                                  "price": 19.99,
                                                  "category": "consumables",
                                                  "description": "Detailed description of the example consumable product.",
                                                  "cost": 10.00,
                                                  "stock": 100,
                                                  "created_at": "2023-01-01T00:00:00Z",
                                                  "updated_at": "2023-01-01T00:00:00Z",
                                                  "expiration_date": "2024-01-01T00:00:00Z",
                                                  "type": "chips_and_salty_snacks"
                                              }
                                          },
                                          json_encoders={
                                              datetime: lambda v: v.isoformat()
                                          })