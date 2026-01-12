from typing import Optional, TYPE_CHECKING

from pydantic import ConfigDict
from sqlmodel import SQLModel, Relationship, Field

from models.abs import BaseModel

if TYPE_CHECKING:
    from models.order import OrderService
    from models.product import Product

class Service(BaseModel, table=True):
    """
    Service model for the database.
    """
    
    name: str = Field(..., description="Name of the service")
    short_description: Optional[str] = Field(None, description="Short description of the service")
    price: float = Field(..., description="Price of the service")
    description: str = Field(..., description="Description of the service")
    cost: float = Field(..., description="Cost of the service")
    
    service_inputs: Optional[list['ServiceInput']] = Relationship(back_populates="service", sa_relationship_kwargs={"lazy": "selectin"})
    order_services: Optional[list['OrderService']] = Relationship(back_populates="service", sa_relationship_kwargs={"lazy": "selectin"})


class ServiceInput(SQLModel, table = True):
    
    service_id: int = Field(..., description="ID of the service that requires the product", foreign_key = "service.id", primary_key = True, index = True)
    product_id: int = Field(..., description="ID of the product required for the service", foreign_key = "product.id", primary_key = True, index = True)

    service: 'Service' = Relationship(back_populates="service_inputs")
    product: 'Product' = Relationship(back_populates="service_inputs")
    
    model_config: ConfigDict = ConfigDict(str_strip_whitespace=True,
                                          json_schema_extra={
                                              "example": {
                                                  "service_id": 1,
                                                  "product_id": 1
                                              }
                                          })