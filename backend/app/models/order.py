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

class OrderProductCreate(BaseModel):
    """
    Model for creating products in an order.
    """
    order_id: int = Field(..., description="ID of the order")
    product_id: int = Field(..., description="ID of the product")
    quantity: int = Field(..., description="Quantity of the product")
    
    model_config: ConfigDict = ConfigDict(str_strip_whitespace=True,
                                          json_schema_extra={
                                              "example": {
                                                  "order_id": 1,
                                                  "product_id": 1,
                                                  "quantity": 2
                                              }
                                          })

class OrderProduct(OrderProductCreate):
    """
    Model for products in an order.
    """
    id: int = Field(..., description="Order's unique identifier")
    
    model_config: ConfigDict = ConfigDict(str_strip_whitespace=True,
                                          json_schema_extra={
                                              "example": {
                                                  "id": 1,
                                                  "order_id": 1,
                                                  "product_id": 1,
                                                  "quantity": 2
                                              }
                                          })


class OrderServiceCreate(BaseModel):
    """
    Model for creating services in an order.
    """
    order_id: int = Field(..., description="ID of the order")
    service_id: int = Field(..., description="ID of the service")
    quantity: int = Field(..., description="Quantity of the service")
    
    model_config: ConfigDict = ConfigDict(str_strip_whitespace=True,
                                          json_schema_extra={
                                              "example": {
                                                  "order_id": 1,
                                                  "service_id": 1,
                                                  "quantity": 1
                                              }
                                          })

class OrderService(OrderServiceCreate):
    """
    Model for services in an order.
    """
    id: int = Field(..., description="Order's unique identifier")
    
    model_config: ConfigDict = ConfigDict(str_strip_whitespace=True,
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
    client_id: int = Field(..., description="User who placed the order")
    total_price: float = Field(..., description="Total price of the order")
    status: OrderStatus = Field(..., description="Current status of the order")


class OrderBasePlusID(OrderBase):
    """
    Base model for orders with ID.
    """
    id: int = Field(..., description="Order's unique identifier")

    model_config: ConfigDict = ConfigDict(str_strip_whitespace=True,
                                          use_enum_values=True,
                                          json_schema_extra={
                                              "example": {
                                                  "id": 1,
                                                  "client_id": 1,
                                                  "total_price": 59.99,
                                                  "status": "Pendiente"
                                              }
                                          })


class OrderCreate(OrderBase):
    """
    Order model for the API request.
    """
    employee_id: int = Field(..., description="Employee assigned to the order")
    created_at: datetime = Field(..., description="Timestamp when the order was created")
    updated_at: datetime = Field(..., description="Timestamp when the order was last updated")

    model_config: ConfigDict = ConfigDict(str_strip_whitespace=True,
                                          use_enum_values=True,
                                          json_schema_extra={
                                              "example": {
                                                  "client_id": 1,
                                                  "total_price": 59.99,
                                                  "status": "Pendiente",
                                                  "employee_id": 1,
                                                  "created_at": "2023-01-01T00:00:00Z",
                                                  "updated_at": "2023-01-01T00:00:00Z"
                                              }
                                          },
                                          json_encoders={
                                              datetime: lambda v: v.isoformat()
                                          })


class Order(OrderCreate):
    """
    Order model for the API response.
    """
    id: int = Field(..., description="Order's unique identifier")
    invoice_link: str = Field(..., description="Invoice link to PDF")

    model_config: ConfigDict = ConfigDict(str_strip_whitespace=True,
                                          use_enum_values=True,
                                          json_schema_extra={
                                              "example": {
                                                  "id": 1,
                                                  "client_id": 1,
                                                  "total_price": 59.99,
                                                  "status": "Pendiente",
                                                  "employee_id": 1,
                                                  "created_at": "2023-01-01T00:00:00Z",
                                                  "updated_at": "2023-01-01T00:00:00Z",
                                                  "invoice_link": "https://example.com/invoice.pdf"
                                              }
                                          },
                                          json_encoders={
                                              datetime: lambda v: v.isoformat()
                                          })
