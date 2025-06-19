from pydantic import BaseModel, Field, ConfigDict
from typing import Optional
from datetime import datetime


class ServiceBase(BaseModel):
    """
    Base model for services.
    """
    id: int = Field(..., description="Service's unique identifier")
    name: str = Field(..., description="Name of the service")
    short_description: Optional[str] = Field(None, description="Short description of the service")
    price: float = Field(..., description="Price of the service")
    
class Service(ServiceBase):
    """
    Service model for the API response.
    """
    description: Optional[str] = Field(None, description="Description of the service")
    cost: float = Field(..., description="Cost of the service")
    created_at: datetime = Field(..., description="Timestamp when the service was created")
    updated_at: datetime = Field(..., description="Timestamp when the service was last updated")
    
    model_config: ConfigDict = ConfigDict(str_to_lower=True,
                                          str_strip_whitespace=True,
                                          use_enum_values=True,
                                          json_schema_extra={
                                              "example": {
                                                  "id": 1,
                                                  "name": "Ejemplo de Servicio",
                                                  "short_description": "Esta es un servicio de ejemplo.",
                                                  "price": 49.99,
                                                  "description": "Descripción detallada del servicio de ejemplo.",
                                                  "cost": 30.00,
                                                  "created_at": "2023-01-01T00:00:00Z",
                                                  "updated_at": "2023-01-01T00:00:00Z"
                                              }
                                          },
                                          json_encoders={
                                              datetime: lambda v: v.isoformat()
                                          })

class ServiceInput(BaseModel):
    """
    Model for service input.
    """
    id: int = Field(..., description="Service input's unique identifier")
    service_id: int = Field(..., description="ID of the service that requires the product")
    product_id: int = Field(..., description="ID of the product required for the service")
    quantity: int = Field(..., description="Quantity of the product required for the service")
    
    model_config: ConfigDict = ConfigDict(str_to_lower=True,
                                          str_strip_whitespace=True,
                                          json_schema_extra={
                                              "example": {
                                                  "id": 1,
                                                  "service_id": 1,
                                                  "product_id": 1,
                                                  "quantity": 2
                                              }
                                          })