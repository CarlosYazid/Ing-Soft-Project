from enum import Enum
from typing import Optional, TYPE_CHECKING

from pydantic import ConfigDict
from sqlmodel import SQLModel, Field, Relationship

from models.abs import BaseModel

if TYPE_CHECKING:
    from models.product import Product
    from models.service import Service
    from models.client import Client
    from models.employee import Employee

class OrderProduct(SQLModel, table=True):
    """
    Model for products in an order.
    """
    order_id: int = Field(foreign_key="order.id", index=True, primary_key=True)
    product_id: int = Field(foreign_key="product.id", index=True, primary_key=True)
    quantity: int = Field(..., description="Quantity of the product")

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
    order_id: int = Field(foreign_key="order.id", index=True, primary_key=True)
    service_id: int = Field(foreign_key="service.id", index=True, primary_key=True)
    quantity: int = Field(..., description="Quantity of the service")

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

class Order(BaseModel, table=True):
    """
    Model for orders.
    """
    client_id: int = Field(foreign_key="client.id", description="User who placed the order", index = True)
    total_price: Optional[float] = Field(..., description="Total price of the order")
    status: OrderStatus = Field(default=OrderStatus.PENDING, description="Current status of the order")
    employee_id: int = Field(foreign_key="employee.id", description="Employee assigned to the order", index = True)
    
    order_products: Optional[list['OrderProduct']] = Relationship(back_populates="order", sa_relationship_kwargs={"lazy": "selectin"})
    order_services: Optional[list['OrderService']] = Relationship(back_populates="order", sa_relationship_kwargs={"lazy": "selectin"})

    client: 'Client' = Relationship(back_populates="orders")
    employee: 'Employee' = Relationship(back_populates="orders")