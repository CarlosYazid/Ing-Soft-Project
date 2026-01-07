from datetime import datetime, date
from enum import Enum
from typing import Optional, TYPE_CHECKING

from pydantic import BaseModel, Field, ConfigDict
from sqlmodel import SQLModel, Field as FieldDB, Relationship

if TYPE_CHECKING:
    from models.product import Product
    from models.service import Service
    from models.user import Client, Employee

class OrderProduct(SQLModel, table=True):
    """
    Model for products in an order.
    """
    order_id: int = FieldDB(foreign_key="order.id", index=True, primary_key=True)
    product_id: int = FieldDB(foreign_key="product.id", index=True, primary_key=True)
    quantity: int = FieldDB(..., description="Quantity of the product")

    order: 'Order' = Relationship(back_populates="order_products")
    product: 'Product' = Relationship(back_populates="order_products")

    model_config: ConfigDict = ConfigDict(str_strip_whitespace=True,
                                          json_schema_extra={
                                              "example": {
                                                  "order_id": 1,
                                                  "product_id": 1,
                                                  "quantity": 2
                                              }
                                          })

class OrderService(SQLModel, table=True):
    """
    Model for services in an order.
    """
    order_id: int = FieldDB(foreign_key="order.id", index=True, primary_key=True)
    service_id: int = FieldDB(foreign_key="service.id", index=True, primary_key=True)
    quantity: int = FieldDB(..., description="Quantity of the service")

    order: 'Order' = Relationship(back_populates="order_services")
    service: 'Service' = Relationship(back_populates="order_services")

    model_config: ConfigDict = ConfigDict(str_strip_whitespace=True,
                                          json_schema_extra={
                                              "example": {
                                                  "order_id": 1,
                                                  "service_id": 1,
                                                  "quantity": 2
                                              }
                                          })

class OrderStatus(str, Enum):
    """
    Enum for order statuses.
    """
    PENDING = "Pendiente"
    COMPLETED = "Completada"
    CANCELLED = "Cancelada"
    REFUNDED = "Reembolsada"


class Order(SQLModel, table=True):
    """
    Model for orders.
    """
    id: Optional[int] = FieldDB(primary_key=True, description="Order's unique identifier")
    client_id: int = FieldDB(foreign_key="client.id", description="User who placed the order")
    total_price: Optional[float] = FieldDB(..., description="Total price of the order")
    status: OrderStatus = FieldDB(default=OrderStatus.PENDING, description="Current status of the order")
    employee_id: int = FieldDB(foreign_key="employee.id", description="Employee assigned to the order")
    created_at: datetime = FieldDB(default_factory = datetime.now, description="Timestamp when the order was created")
    updated_at: datetime = FieldDB(default_factory = datetime.now, description="Timestamp when the order was last updated")

    order_products: Optional[list['OrderProduct']] = Relationship(back_populates="order", sa_relationship_kwargs={"lazy": "selectin"})
    order_services: Optional[list['OrderService']] = Relationship(back_populates="order", sa_relationship_kwargs={"lazy": "selectin"})

    client: 'Client' = Relationship(back_populates="orders")
    employee: 'Employee' = Relationship(back_populates="orders")
    
class OrderCreate(BaseModel):
    
    client_id: int = Field(..., description="User who placed the order", gt = 0)
    total_price: Optional[float] = Field(None, description="Total price of the order", gt = 0)
    status: OrderStatus = Field(..., description="Current status of the order")
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
                                          },
                                          json_encoders={
                                              datetime: lambda v: v.isoformat()
                                          })
    
class OrderUpdate(BaseModel):

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

class OrderRead(BaseModel):

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
                                          },
                                          json_encoders={
                                              datetime: lambda v: v.isoformat()
                                          })
