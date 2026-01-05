from typing import Optional, TYPE_CHECKING
from datetime import datetime

from pydantic import BaseModel, Field, ConfigDict
from sqlmodel import SQLModel, Relationship
from sqlmodel import Field as FieldDB

if TYPE_CHECKING:
    from models.order import OrderService
    from models.product import Product

class Service(SQLModel, table=True):
    """
    Service model for the database.
    """
    id: Optional[int] = FieldDB(primary_key=True, index=True)
    name: str = FieldDB(..., description="Name of the service")
    short_description: Optional[str] = FieldDB(None, description="Short description of the service")
    price: float = FieldDB(..., description="Price of the service")
    description: str = FieldDB(..., description="Description of the service")
    cost: float = FieldDB(..., description="Cost of the service")
    created_at: datetime = FieldDB(default_factory = datetime.now, description="Timestamp when the service was created")
    updated_at: datetime = FieldDB(default_factory = datetime.now, description="Timestamp when the service was last updated")

    service_inputs: Optional[list['ServiceInput']] = Relationship(back_populates="service", sa_relationship_kwargs={"lazy": "selectin"})
    order_services: Optional[list['OrderService']] = Relationship(back_populates="service", sa_relationship_kwargs={"lazy": "selectin"})

class ServiceCreate(BaseModel):
    
    name: str = Field(..., description="Name of the service")
    price: float = Field(..., description="Price of the service", gt = 0)
    description: str = Field(..., description="Description of the service")
    cost: float = Field(..., description="Cost of the service", gt = 0)
    
    model_config: ConfigDict = ConfigDict(str_strip_whitespace=True,
                                          json_schema_extra={
                                              "example": {
                                                  "name": "Ejemplo de Servicio",
                                                  "price": 49.99,
                                                  "description": "Descripción detallada del servicio de ejemplo.",
                                                  "cost": 30.00,
                                              }
                                          })

class ServiceUpdate(BaseModel):
    
    id: Optional[int] = Field(None, description="Service's unique identifier")
    name: Optional[str] = Field(None, description="Name of the service")
    short_description: Optional[str] = Field(None, description="Short description of the service")
    price: Optional[float] = Field(None, description="Price of the service", gt = 0)
    description: Optional[str] = Field(None, description="Description of the service")
    cost: Optional[float] = Field(None, description="Cost of the service", gt = 0)
    updated_at: datetime = Field(default_factory = datetime.now, description="Timestamp when the service was last updated")
    
    model_config: ConfigDict = ConfigDict(str_strip_whitespace=True,
                                          json_schema_extra={
                                              "example": {
                                                  "id": 1,
                                                  "name": "Ejemplo de Servicio",
                                                  "short_description": "Esta es un servicio de ejemplo.",
                                                  "price": 49.99,
                                                  "description": "Descripción detallada del servicio de ejemplo.",
                                                  "cost": 30.00,
                                                  "updated_at": "2023-01-01T00:00:00Z"
                                              }
                                          },
                                          json_encoders={
                                              datetime: lambda v: v.isoformat()
                                          })

class ServiceRead(BaseModel):
    
    id: int = Field(..., description="Service's unique identifier")
    name: str = Field(..., description="Name of the service")
    short_description: Optional[str] = Field(None, description="Short description of the service")
    price : float = Field(..., description="Price of the service")
    cost : float = Field(..., description="Cost of the service")
    
    model_config: ConfigDict = ConfigDict(str_strip_whitespace=True,
                                          json_schema_extra={
                                              "example": {
                                                  "id": 1,
                                                  "name": "Ejemplo de Servicio",
                                                  "short_description": "Esta es un servicio de ejemplo.",
                                                  "price": 49.99,
                                                  "description": "Descripción detallada del servicio de ejemplo.",
                                                  "cost": 30.00
                                              }
                                          })


class ServiceInput(SQLModel, table = True):
    
    service_id: int = FieldDB(..., description="ID of the service that requires the product", foreign_key = "service.id", primary_key = True)
    product_id: int = FieldDB(..., description="ID of the product required for the service", foreign_key = "product.id", primary_key = True)

    service: 'Service' = Relationship(back_populates="service_inputs")
    product: 'Product' = Relationship(back_populates="service_inputs")
    
    model_config: ConfigDict = ConfigDict(str_strip_whitespace=True,
                                          json_schema_extra={
                                              "example": {
                                                  "service_id": 1,
                                                  "product_id": 1
                                              }
                                          })