from pydantic import BaseModel, Field, ConfigDict
from typing import Optional
from datetime import datetime
from enum import Enum

class OrderStatus(str, Enum):
    """
    Enum for order statuses.
    """
    PENDING = "Pending"
    COMPLETED = "Completed"
    CANCELLED = "Cancelled"

class OrderBase(BaseModel):
    """
    Base model for orders.
    """
    id: int = Field(..., description="Order's unique identifier")
    user: int = Field(..., description="User who placed the order")
    products: dict[int, int] = Field(..., description="Products in the order with their quantities")
    services : dict[int, int] = Field(..., description="Services in the order with their quantities")
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
                                                  "user": 1,
                                                  "products": {1: 2, 2: 1},
                                                  "services": {1: 1},
                                                  "total_price": 59.99,
                                                  "status": "Pending",
                                                  "employee": 1,
                                                  "created_at": "2023-01-01T00:00:00Z",
                                                  "updated_at": "2023-01-01T00:00:00Z"
                                              }
                                          },
                                          json_encoders={
                                              datetime: lambda v: v.isoformat()
                                          })

class OrdersHistory(BaseModel):
    """
    Model for orders history.
    """
    user : int = Field(..., description="User whose order history is being retrieved")
    orders: list[int] = Field(..., description="List of orders in the history")

    model_config: ConfigDict = ConfigDict(str_to_lower=True,
                                          str_strip_whitespace=True,
                                          use_enum_values=True,
                                          json_schema_extra={
                                              "example": {
                                                  "user": 1,
                                                  "orders": [1, 2, 3, 4, 5]
                                              }
                                          })