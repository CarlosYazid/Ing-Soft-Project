from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from typing import Optional
from datetime import datetime
from enum import Enum
from pathlib import Path
import os

from pydantic import BaseModel, Field, ConfigDict, EmailStr
from sqlmodel import SQLModel, Field as FieldDB, Relationship

from models import Client
from core import SETTINGS

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


class Payment(SQLModel, table=True):
    """
    Model for payments.
    """
    id: Optional[int] = FieldDB(primary_key=True, description="Payment's unique identifier")
    client_id: int = FieldDB(foreign_key="client.id", description="Client associated with the payment")
    amount: float = FieldDB(..., description="Amount paid")
    method: PaymentMethod = FieldDB(..., description="Payment method used")
    status: PaymentStatus = FieldDB(..., description="Current status of the payment")
    due_date: Optional[datetime] = FieldDB(None, description="Due date for the credit payment")
    interest_rate: Optional[float] = FieldDB(None, description="Interest rate applied to the credit")
    account_number: Optional[str] = FieldDB(None, description="Account number for the bank transfer")
    created_at: datetime = FieldDB(default_factory=datetime.now(), description="Timestamp when the payment was created")
    updated_at: datetime = FieldDB(default_factory=datetime.now(), description="Timestamp when the payment was last updated")

    client: Client = Relationship(back_populates="payments")

class PaymentCreate(BaseModel):
    
    client_id: int = Field(..., description="Client associated with the payment", gt = 0)
    amount: float = Field(..., description="Amount paid", gt = 0)
    method: PaymentMethod = Field(default=PaymentMethod.CASH, description="Payment method used")
    status: PaymentStatus = Field(default=PaymentStatus.PENDING, description="Current status of the payment")
    due_date: Optional[datetime] = Field(None, description="Due date for the credit payment")
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
                                                  "due_date": "2023-01-01T00:00:00Z",
                                                  "interest_rate": 0.05,
                                                  "account_number": "1234567890"
                                              }
                                          })
    
class PaymentUpdate(BaseModel):

    id: int = Field(..., description="Payment's unique identifier", gt = 0)
    amount: Optional[float] = Field(None, description="Amount paid", gt = 0)
    method: Optional[PaymentMethod] = Field(None, description="Payment method used")
    status: Optional[PaymentStatus] = Field(None, description="Current status of the payment")
    due_date: Optional[datetime] = Field(None, description="Due date for the credit payment")
    interest_rate: Optional[float] = Field(None, description="Interest rate applied to the credit", gt = 0)
    account_number: Optional[str] = Field(None, description="Account number for the bank transfer", gt = 0)
    updated_at: datetime = Field(default=datetime.now(), description="Timestamp when the payment was last updated")

    model_config : ConfigDict = ConfigDict(str_strip_whitespace=True,
                                          use_enum_values=True,
                                          json_schema_extra={
                                              "example": {
                                                  "amount": 1000.00,
                                                  "method": "Crédito_en_tiempo",
                                                  "status": "Pendiente",
                                                  "due_date": "2023-01-01T00:00:00Z",
                                                  "interest_rate": 0.05,
                                                  "account_number": "1234567890",
                                                  "updated_at": "2023-01-01T00:00:00Z"
                                              }
                                          })

class PaymentRead(BaseModel):

    id: int = Field(..., description="Payment's unique identifier")
    client_id: int = Field(..., description="Client associated with the payment")
    amount: float = Field(..., description="Amount paid")
    method: PaymentMethod = Field(..., description="Payment method used")
    status: PaymentStatus = Field(..., description="Current status of the payment")
    due_date: Optional[datetime] = Field(None, description="Due date for the credit payment")
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
                                                  "due_date": "2023-01-01T00:00:00Z",
                                                  "interest_rate": 0.05,
                                                  "account_number": "1234567890"
                                              }
                                          })

class EmailType(str, Enum):
    """
    Enum for email types.
    """
    PLAIN = "plain"
    HTML = "html"
    
class Email(BaseModel):
    """
    Model for email details.
    """
    subject: str = Field(..., description="Email subject")
    body: str = Field(..., description="Email body")
    to: EmailStr = Field(..., description="Recipient email address")
    cc: Optional[EmailStr | list[EmailStr]] = Field(None, description="CC email addresses")
    bcc: Optional[EmailStr | list[EmailStr]] = Field(None, description="BCC email addresses")
    attachments: list["File"] = Field(default_factory=list, description="List of files to attach to the email")
    type: EmailType = Field(EmailType.PLAIN, description="Type of email content (plain or HTML)")
    
    model_config: ConfigDict = ConfigDict(str_strip_whitespace=True,
                                          json_schema_extra={
                                              "example": {
                                                  "subject": "Test Email",
                                                  "body": "This is a test email.",
                                                  "to": "recipient@example.com",
                                                  "cc": ["cc1@example.com", "cc2@example.com"],
                                                  "bcc": ["bcc1@example.com", "bcc2@example.com"],
                                                  "attachments": [
                                                      {
                                                          "path": "/path/to/file1.txt"
                                                      },
                                                      {
                                                          "path": "/path/to/file2.pdf"
                                                      }
                                                  ]
                                              }
                                          })
    
    def to_Mime(self):
        """Converts the Email model to a MIME message."""


        msg = MIMEMultipart()
        msg['From'] = SETTINGS.smtp_comp_email
        msg['To'] = self.to
        if self.cc:
            msg['Cc'] = self.cc
        if self.bcc:
            msg['Bcc'] = self.bcc
        msg['Subject'] = self.subject
        
        msg.attach(MIMEText(self.body, self.type.value))

        for attachment in filter(lambda a: isinstance(a, File), self.attachments):
            msg.attach(attachment.to_Mime())

        return msg

class FileType(str, Enum):
    
    PDF = "application/pdf"
    DOCX = "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
    XLSX = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    PPTX = "application/vnd.openxmlformats-officedocument.presentationml.presentation"
    CSV = "text/csv"
    IMAGE_JPEG = "image/jpeg"
    IMAGE_PNG = "image/png"
    IMAGE_GIF = "image/gif"
    TEXT = "text/plain"
    OTHER = "application/octet-stream"
    
    @classmethod
    def from_extension(cls, extension: str) -> "FileType":
        ext = extension.lower()
        mapping = {
            '.pdf': cls.PDF,
            '.doc': cls.DOCX,
            '.docx': cls.DOCX,
            '.xls': cls.XLSX,
            '.xlsx': cls.XLSX,
            '.ppt': cls.PPTX,
            '.pptx': cls.PPTX,
            '.csv': cls.CSV,
            '.jpg': cls.IMAGE_JPEG,
            '.jpeg': cls.IMAGE_JPEG,
            '.png': cls.IMAGE_PNG,
            '.gif': cls.IMAGE_GIF,
            '.txt': cls.TEXT
        }
        return mapping.get(ext, cls.OTHER)
    
    @classmethod
    def from_file(cls, file_path):
        _, extension = os.path.splitext(file_path)
        return cls.from_extension(extension)

class File(BaseModel):
    path: str | Path = Field(..., description="File path")
    name : Optional[str] = Field(None, description="File name, if not provided will be derived from path")

    @property
    def name(self) -> str:
        return self.name or os.path.basename(self.path)

    @property
    def content(self) -> bytes:
        with open(self.path, 'rb') as f:
            return f.read()
    
    def exists(self) -> bool:
        return os.path.exists(self.path)

    @property
    def type(self) -> FileType:
        return FileType.from_file(self.path)

    @property
    def size(self) -> int:
        return os.path.getsize(self.path)

    def to_Mime(self):
        mime = MIMEBase('application', self.type.value)
        mime.set_payload(self.content)
        encoders.encode_base64(mime)
        mime.add_header('Content-Disposition', f'attachment; filename={self.name}')
        mime.add_header('Content-Type', self.type.value)
        mime.add_header('Content-Transfer-Encoding', 'base64')
        return mime


class InvoiceItem(BaseModel):
    name: str
    quantity: int
    unit_price: float

    @property
    def total(self) -> float:
        return self.quantity * self.unit_price
    
    model_config: ConfigDict = ConfigDict(str_to_lower=False)

class Invoice(BaseModel):
    number: int = Field(..., description="Invoice number") # Id of order
    date: datetime = Field(..., description="Date of the invoice")
    client: Client = Field(..., description="Client associated with the invoice")
    items: list[InvoiceItem] = Field(default_factory=list, description="List of items in the invoice")
    tax_rate: float = Field(0.0, description="Tax rate applied to the invoice")

    @property
    def total(self) -> float:
        return sum(item.total for item in self.items) + self.tax_amount

    @property
    def subtotal(self) -> float:
        return sum(item.total for item in self.items)

    @property
    def tax_amount(self) -> float:
        return self.subtotal * self.tax_rate

    model_config: ConfigDict = ConfigDict(str_to_lower=False)

class InvoiceRequest(BaseModel):
    order_id: int = Field(..., description="Order ID for which the invoice is generated")
    tax_rate: float = Field(0.0, description="Tax rate applied to the invoice")

    model_config: ConfigDict = ConfigDict(str_to_lower=True,
                                          str_strip_whitespace=True,
                                          json_schema_extra={
                                              "example": {
                                                  "order_id": 1,
                                                  "tax_rate": 0.15
                                              }
                                          })