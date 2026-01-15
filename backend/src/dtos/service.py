from typing import Optional
from datetime import datetime

from sqlalchemy.sql.expression import Select
from pydantic import Field, ConfigDict

from dtos.abs import BaseCreate, BaseRead, BaseUpdate, BaseFilter
from models import Service, ServiceInput

class ServiceCreate(BaseCreate):
    
    name: str = Field(..., description="Name of the service")
    short_description: Optional[str] = Field(None, description="Short description of the service")
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

class ServiceUpdate(BaseUpdate):
    
    name: Optional[str] = Field(None, description="Name of the service")
    short_description: Optional[str] = Field(None, description="Short description of the service")
    price: Optional[float] = Field(None, description="Price of the service", gt = 0)
    description: Optional[str] = Field(None, description="Description of the service")
    cost: Optional[float] = Field(None, description="Cost of the service", gt = 0)
    
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

class ServiceRead(BaseRead):
    
    id: int = Field(..., description="Service's unique identifier")
    name: str = Field(..., description="Name of the service")
    short_description: Optional[str] = Field(None, description="Short description of the service")
    price : float = Field(..., description="Price of the service")
    description: str = Field(..., description="Description of the service")
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

class ServiceFilter(BaseFilter):
    
    name: Optional[str] = Field(None, description="Name of the service")
    max_price: Optional[float] = Field(None, description="Max price of the service", gt = 0)
    min_price: Optional[float] = Field(None, description="Min price of the service", gt = 0)
    max_cost: Optional[float] = Field(None, description="Max cost of the service", gt = 0)
    min_cost: Optional[float] = Field(None, description="Min cost of the service", gt = 0)
    
    def apply(self, query : Select) -> Select:
        
        if self.name:
            query = query.where(Service.name.ilike(f"%{self.name}%"))
        
        if self.max_price:
            query = query.where(Service.price <= self.max_price)
        
        if self.min_price:
            query = query.where(Service.price >= self.min_price)
        
        if self.max_cost:
            query = query.where(Service.cost <= self.max_cost)
        
        if self.min_cost:
            query = query.where(Service.cost >= self.min_cost)
        
        return query

class ServiceInputFilter(BaseFilter):
    
    product_id: Optional[int] = Field(None, ge = 0)
    service_id: Optional[int] = Field(None, ge = 0)
    
    def apply(self, query: Select) -> Select:
        
        if self.product_id:
            query = query.where(ServiceInput.product_id == self.product_id)
        
        if self.service_id:
            query = query.where(ServiceInput.service_id == self.service_id)
        
        return query