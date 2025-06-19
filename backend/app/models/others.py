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
    user_id: int = Field(..., description="User associated with the payment")
    amount: Optional[float] = Field(None, description="Amount paid")
    method: PaymentMethod = Field(..., description="Payment method used")
    status: PaymentStatus = Field(..., description="Current status of the payment")

class Payment(PaymentBase):
    """
    Payment model for the API response.
    """
    created_at: datetime = Field(..., description="Timestamp when the payment was created")
    updated_at: datetime = Field(..., description="Timestamp when the payment was last updated")
    due_date: Optional[datetime] = Field(None, description="Due date for the credit payment")
    interest_rate: Optional[float] = Field(None, description="Interest rate applied to the credit")
    account_number: Optional[str] = Field(None, description="Account number for the bank transfer")

    model_config: ConfigDict = ConfigDict(str_to_lower=True,
                                          str_strip_whitespace=True,
                                          use_enum_values=True,
                                          json_schema_extra={
                                              "example": {
                                                  "id": 1,
                                                  "user_id": 1,
                                                  "amount": 1000.00,
                                                  "method": "Crédito_en_tiempo",
                                                  "status": "Pendiente",
                                                  "created_at": "2023-01-01T00:00:00Z",
                                                  "updated_at": "2023-01-01T00:00:00Z",
                                                  "due_date": "2023-02-01T00:00:00Z",
                                                  "interest_rate": 5.0
                                              }
                                          },
                                          json_encoders={
                                              datetime: lambda v: v.isoformat()
                                          })