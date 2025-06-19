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
    service_inputs : dict[int, int] = Field(..., description="Inputs required for the service, mapping product to quantity")
    
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
                                                  "name": "Example Service",
                                                  "short_description": "This is an example service.",
                                                  "price": 49.99,
                                                  "service_inputs": {
                                                      1: 2, # Example product ID to quantity mapping
                                                      2: 1
                                                  },
                                                  "description": "Detailed description of the example service.",
                                                  "cost": 30.00,
                                                  "created_at": "2023-01-01T00:00:00Z",
                                                  "updated_at": "2023-01-01T00:00:00Z"
                                              }
                                          },
                                          json_encoders={
                                              datetime: lambda v: v.isoformat()
                                          })