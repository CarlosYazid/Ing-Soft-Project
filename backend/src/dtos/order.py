from typing import Optional
from datetime import datetime

from sqlalchemy.sql.expression import Select
from pydantic import Field, ConfigDict

from models import OrderStatus, Order, OrderProduct, OrderService
from dtos.abs import BaseCreate, BaseRead, BaseUpdate, BaseFilter

class OrderCreate(BaseCreate):
    
    client_id: int = Field(..., description="User who placed the order", gt = 0)
    total_price: Optional[float] = Field(None, description="Total price of the order", gt = 0)
    status: OrderStatus = Field(default=OrderStatus.PENDING, description="Current status of the order")
    employee_id: int = Field(..., description="Employee assigned to the order", gt = 0)
    
    model_config: ConfigDict = ConfigDict(str_strip_whitespace=True,
                                          use_enum_values=True,
                                          json_schema_extra={
                                              "example": {
                                                  "client_id": 1,
                                                  "total_price": 59.99,
                                                  "status": "Pendiente",
                                                  "employee_id": 1
                                              }
                                          })
    
class OrderUpdate(BaseUpdate):

    id: int = Field(..., description="Order's unique identifier", gt = 0)
    total_price: Optional[float] = Field(None, description="Total price of the order", gt = 0)
    status: Optional[OrderStatus] = Field(None, description="Current status of the order")
    updated_at: datetime = Field(default_factory = datetime.now, description="Timestamp when the order was last updated")

    model_config: ConfigDict = ConfigDict(str_strip_whitespace=True,
                                          use_enum_values=True,
                                          json_schema_extra={
                                              "example": {
                                                  "id": 1,
                                                  "total_price": 3.5,
                                                  "status": "Completada",
                                                  "updated_at": "2023-01-01T00:00:00Z"
                                              }
                                          },
                                          json_encoders={
                                              datetime: lambda v: v.isoformat()
                                          })

class OrderRead(BaseRead):

    id: int = Field(..., description="Order's unique identifier")
    client_id: int = Field(..., description="User who placed the order")
    total_price: Optional[float] = Field(..., description="Total price of the order")
    status: OrderStatus = Field(..., description="Current status of the order")
    employee_id: int = Field(..., description="Employee assigned to the order")

    model_config: ConfigDict = ConfigDict(str_strip_whitespace=True,
                                          use_enum_values=True,
                                          json_schema_extra={
                                              "example": {
                                                  "id": 1,
                                                  "client_id": 1,
                                                  "total_price": 59.99,
                                                  "status": "Pendiente",
                                                  "employee_id": 1
                                              }
                                          })

class OrderServiceFilter(BaseFilter):
    
    order_id: Optional[int] = Field(None, ge = 0)
    service_id: Optional[int] = Field(None, ge = 0)

    def apply(self, query: Select) -> Select:
        
        if self.order_id:
            query = query.where(OrderService.order_id == self.order_id)
        
        if self.service_id:
            query = query.where(OrderService.service_id == self.service_id)
        
        return query

class OrderProductFilter(BaseFilter):
    
    order_id: Optional[int] = Field(None, ge = 0)
    product_id: Optional[int] = Field(None, ge = 0)
    
    def apply(self, query: Select) -> Select:
        
        if self.order_id:
            query = query.where(OrderProduct.order_id == self.order_id)
        
        if self.product_id:
            query = query.where(OrderProduct.product_id == self.product_id)
        
        return query

class OrderFilter(BaseFilter):
    
    status: Optional[OrderStatus] = Field(None, description="Current status of the order")
    client_id: Optional[int] = Field(None, ge = 0)
    employee_id: Optional[int] = Field(None, ge = 0)
    
    def apply(self, query: Select) -> Select:
        
        if self.status:
            query = query.where(Order.status == self.status)
        
        if self.client_id:
            query = query.where(Order.client_id == self.client_id)
        
        if self.employee_id:
            query = query.where(Order.employee_id == self.employee_id)
        
        return query