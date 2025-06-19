from pydantic import BaseModel, Field, ConfigDict
from datetime import datetime
from enum import Enum


class OrderStatus(str, Enum):
    """
    Enum for order statuses.
    """
    PENDING = "Pendiente"
    COMPLETED = "Completada"
    CANCELLED = "Cancelada"
    REFUNDED = "Reembolsada"

class OrderProduct(BaseModel):
    """
    Model for products in an order.
    """
    id: int = Field(..., description="Order's unique identifier")
    order_id: int = Field(..., description="ID of the order")
    product_id: int = Field(..., description="ID of the product")
    quantity: int = Field(..., description="Quantity of the product")
    
    model_config: ConfigDict = ConfigDict(str_to_lower=True,
                                          str_strip_whitespace=True,
                                          json_schema_extra={
                                              "example": {
                                                  "id": 1,
                                                  "order_id": 1,
                                                  "product_id": 1,
                                                  "quantity": 2
                                              }
                                          })

class OrderService(BaseModel):
    """
    Model for services in an order.
    """
    id: int = Field(..., description="Order's unique identifier")
    order_id: int = Field(..., description="ID of the order")
    service_id: int = Field(..., description="ID of the service")
    quantity: int = Field(..., description="Quantity of the service")
    
    model_config: ConfigDict = ConfigDict(str_to_lower=True,
                                          str_strip_whitespace=True,
                                          json_schema_extra={
                                              "example": {
                                                  "id": 1,
                                                  "order_id": 1,
                                                  "service_id": 1,
                                                  "quantity": 1
                                              }
                                          })
class OrderBase(BaseModel):
    """
    Base model for orders.
    """
    id: int = Field(..., description="Order's unique identifier")
    user_id: int = Field(..., description="User who placed the order")
    total_price: float = Field(..., description="Total price of the order")
    status: OrderStatus = Field(..., description="Current status of the order")

class Order(OrderBase):
    """
    Order model for the API response.
    """
    employee: int = Field(None, description="Employee assigned to the order")
    created_at: datetime = Field(..., description="Timestamp when the order was created")
    updated_at: datetime = Field(..., description="Timestamp when the order was last updated")

    model_config: ConfigDict = ConfigDict(str_to_lower=True,
                                          str_strip_whitespace=True,
                                          use_enum_values=True,
                                          json_schema_extra={
                                              "example": {
                                                  "id": 1,
                                                  "user_id": 1,
                                                  "total_price": 59.99,
                                                  "status": "Pending",
                                                  "employee_id": 1,
                                                  "created_at": "2023-01-01T00:00:00Z",
                                                  "updated_at": "2023-01-01T00:00:00Z"
                                              }
                                          },
                                          json_encoders={
                                              datetime: lambda v: v.isoformat()
                                          })