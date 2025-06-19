from pydantic import BaseModel, Field, ConfigDict
from typing import Optional
from datetime import datetime
from enum import Enum

class PaymentMethod(str, Enum):
    """
    Enum for payment methods.
    """
    CASH = "Efectivo"
    BANK_TRANSFER = "Transferencia_bancaria"
    ON_CREDIT = "Crédito_en_tiempo"

class PaymentStatus(str, Enum):
    """
    Enum for payment statuses.
    """
    PENDING = "Pendiente"
    COMPLETED = "Completado"
    FAILED = "Fallido"
    REFUNDED = "Reembolsado"

class PaymentBase(BaseModel):
    """
    Base model for payments.
    """
    id: int = Field(..., description="Payment's unique identifier")
    user: int = Field(..., description="User associated with the payment")
    amount: Optional[float] = Field(None, description="Amount paid")
    method: PaymentMethod = Field(..., description="Payment method used")
    status: PaymentStatus = Field(..., description="Current status of the payment")

class Payment(PaymentBase):
    """
    Payment model for the API response.
    """
    created_at: datetime = Field(..., description="Timestamp when the payment was created")
    updated_at: datetime = Field(..., description="Timestamp when the payment was last updated")

    model_config: ConfigDict = ConfigDict(str_to_lower=True,
                                          str_strip_whitespace=True,
                                          use_enum_values=True,
                                          json_schema_extra={
                                              "example": {
                                                  "id": 1,
                                                  "user": 1,
                                                  "amount": 1000.00,
                                                  "method": "Efectivo",
                                                  "status": "Pendiente",
                                                  "created_at": "2023-01-01T00:00:00Z",
                                                  "updated_at": "2023-01-01T00:00:00Z"
                                              }
                                          },
                                          json_encoders={
                                              datetime: lambda v: v.isoformat()
                                          })
class Credit(Payment):
    """
    Credit model for the API response.
    """
    due_date: datetime = Field(..., description="Due date for the credit payment")
    interest_rate: float = Field(..., description="Interest rate applied to the credit")

    model_config: ConfigDict = ConfigDict(str_to_lower=True,
                                          str_strip_whitespace=True,
                                          use_enum_values=True,
                                          json_schema_extra={
                                              "example": {
                                                  "id": 1,
                                                  "user": 1,
                                                  "amount": 1000.00,
                                                  "method": "Crédito_en_tiempo",
                                                  "status": "Pendiente",
                                                  "due_date": "2023-12-31T00:00:00Z",
                                                  "interest_rate": 5.0,
                                                  "created_at": "2023-01-01T00:00:00Z",
                                                  "updated_at": "2023-01-01T00:00:00Z"
                                              }
                                          },
                                          json_encoders={
                                              datetime: lambda v: v.isoformat()
                                          })
class BankTransfer(Payment):
    """
    BankTransfer model for the API response.
    """
    account_number: str = Field(..., description="Account number for the bank transfer")


    model_config: ConfigDict = ConfigDict(str_to_lower=True,
                                          str_strip_whitespace=True,
                                          use_enum_values=True,
                                          json_schema_extra={
                                              "example": {
                                                  "id": 2,
                                                  "user": 1,
                                                  "amount": 500.00,
                                                  "method": "Transferencia_bancaria",
                                                  "status": "Completado",
                                                  "account_number": "1234567890",
                                                  "created_at": "2023-01-01T00:00:00Z",
                                                  "updated_at": "2023-01-01T00:00:00Z"
                                              }
                                          },
                                          json_encoders={
                                              datetime: lambda v: v.isoformat()
                                          })