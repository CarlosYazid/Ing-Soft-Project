from typing import Optional
from datetime import datetime, date

from sqlalchemy.sql.expression import Select
from pydantic import Field, ConfigDict

from models import PaymentMethod, PaymentStatus, Payment
from dtos.abs import BaseCreate, BaseRead, BaseUpdate, BaseFilter

class PaymentCreate(BaseCreate):
    
    client_id: int = Field(..., description="Client associated with the payment", gt = 0)
    amount: float = Field(..., description="Amount paid", gt = 0)
    method: PaymentMethod = Field(default=PaymentMethod.CASH, description="Payment method used")
    status: PaymentStatus = Field(default=PaymentStatus.PENDING, description="Current status of the payment")
    due_date: Optional[date] = Field(None, description="Due date for the credit payment")
    interest_rate: Optional[float] = Field(None, description="Interest rate applied to the credit", gt = 0)
    account_number: Optional[str] = Field(None, description="Account number for the bank transfer", gt = 0)
    
    model_config : ConfigDict = ConfigDict(str_strip_whitespace=True,
                                          use_enum_values=True,
                                          json_schema_extra={
                                              "example": {
                                                  "client_id": 1,
                                                  "amount": 1000.00,
                                                  "method": "Crédito_en_tiempo",
                                                  "status": "Pendiente",
                                                  "due_date": "2023-01-01",
                                                  "interest_rate": 0.05,
                                                  "account_number": "1234567890"
                                              }
                                          })
    
class PaymentUpdate(BaseUpdate):

    id: int = Field(..., description="Payment's unique identifier", gt = 0)
    amount: Optional[float] = Field(None, description="Amount paid", gt = 0)
    method: Optional[PaymentMethod] = Field(None, description="Payment method used")
    status: Optional[PaymentStatus] = Field(None, description="Current status of the payment")
    due_date: Optional[date] = Field(None, description="Due date for the credit payment")
    interest_rate: Optional[float] = Field(None, description="Interest rate applied to the credit", gt = 0)
    account_number: Optional[str] = Field(None, description="Account number for the bank transfer", gt = 0)
    updated_at: datetime = Field(default_factory = datetime.now, description="Timestamp when the payment was last updated")

    model_config : ConfigDict = ConfigDict(str_strip_whitespace=True,
                                          use_enum_values=True,
                                          json_schema_extra={
                                              "example": {
                                                  "amount": 1000.00,
                                                  "method": "Crédito_en_tiempo",
                                                  "status": "Pendiente",
                                                  "due_date": "2023-01-01",
                                                  "interest_rate": 0.05,
                                                  "account_number": "1234567890",
                                                  "updated_at": "2023-01-01T00:00:00Z"
                                              }
                                          })

class PaymentRead(BaseRead):

    id: int = Field(..., description="Payment's unique identifier")
    client_id: int = Field(..., description="Client associated with the payment")
    amount: float = Field(..., description="Amount paid")
    method: PaymentMethod = Field(..., description="Payment method used")
    status: PaymentStatus = Field(..., description="Current status of the payment")
    due_date: Optional[date] = Field(None, description="Due date for the credit payment")
    interest_rate: Optional[float] = Field(None, description="Interest rate applied to the credit")
    account_number: Optional[str] = Field(None, description="Account number for the bank transfer")

    model_config : ConfigDict = ConfigDict(str_strip_whitespace=True,
                                          use_enum_values=True,
                                          json_schema_extra={
                                              "example": {
                                                  "id": 1,
                                                  "client_id": 1,
                                                  "amount": 1000.00,
                                                  "method": "Crédito_en_tiempo",
                                                  "status": "Pendiente",
                                                  "due_date": "2023-01-01",
                                                  "interest_rate": 0.05,
                                                  "account_number": "1234567890"
                                              }
                                          })

class PaymentFilter(BaseFilter):
    
    client_id: Optional[int] = Field(None, description="Client associated with the payment")
    max_amount: Optional[float] = Field(None, description="Max amount paid", ge = 0)
    min_amount: Optional[float] = Field(None, description="Min amount paid", ge = 0)
    method: Optional[PaymentMethod] = Field(None, description="Payment method used")
    status: Optional[PaymentStatus] = Field(None, description="Current status of the payment")
    max_due_date: Optional[date] = Field(None, description="Max due date for the credit payment")
    min_due_date: Optional[date] = Field(None, description="Min due date for the credit payment")
    max_interest_rate: Optional[float] = Field(None, description="Max interest rate applied to the credit", ge = 0)
    min_interest_rate: Optional[float] = Field(None, description="Min interest rate applied to the credit", ge = 0)
    
    def apply(self, query:  Select) -> Select:
        
        if self.client_id:
            query = query.where(Payment.client_id == self.client_id)
        
        if self.max_amount:
            query = query.where(Payment.amount <= self.max_amount)
        
        if self.min_amount:
            query = query.where(Payment.amount >= self.min_amount)
        
        if self.method:
            query = query.where(Payment.method == self.method)
        
        if self.status:
            query = query.where(Payment.status == self.status)
        
        if self.max_due_date:
            query = query.where(Payment.due_date <= self.max_due_date)
        
        if self.min_due_date:
            query = query.where(Payment.due_date >= self.min_due_date)
        
        if self.max_interest_rate:
            query = query.where(Payment.interest_rate <= self.max_interest_rate)
        
        if self.min_interest_rate:
            query = query.where(Payment.interest_rate >= self.min_interest_rate)
        
        return query