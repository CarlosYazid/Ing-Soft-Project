from pydantic import EmailStr, SecretStr, Field
from pydantic_settings import BaseSettings, SettingsConfigDict
import os


class Settings(BaseSettings):
    # General
    app_name: str = "InventaryApp"
    environment: str = "development"  # development | production | staging
    debug: bool = True
    model_config = SettingsConfigDict(env_file=os.path.join(os.path.dirname(__file__), "../../.env"), env_file_encoding='utf-8', extra='allow')

    # Supabase
    db_url: str = Field(..., alias="database_url")
    db_key: SecretStr = Field(..., alias="database_key")
    employee_table: str = Field(..., alias="employee_table")
    client_table: str = Field(..., alias="client_table")
    bucket_name: str = Field(..., alias="bucket_name")
    service_table: str = Field(..., alias="service_table")
    product_table: str = Field(..., alias="product_table")
    service_inputs_table: str = Field(..., alias="service_inputs_table")
    order_table: str = Field(..., alias="order_table")
    order_service_table: str = Field(..., alias="order_service_table")
    order_product_table: str = Field(..., alias="order_product_table")
    payment_table: str = Field(..., alias="payment_table")

    #Groq
    groq_api_key: SecretStr = Field(..., alias="groq_api_key")
    groq_model: str = Field(..., alias="groq_model")

    # SMTP (Gmail)
    smtp_host: str = "smtp.gmail.com"
    smtp_port: int = 587
    smtp_corp_email: EmailStr = Field(..., alias="corp_user")
    smtp_corp_password: SecretStr = Field(..., alias="corp_password")

    frontend_url: str = Field(..., alias="frontend_url")
    home_url: str = Field(..., alias="home_url")

    # Auth
    sign_in_redirect_url: str = Field(..., alias="sign_in_redirect_url")
    reset_password_url: str = Field(..., alias="reset_password_url")
    algorithm: str = Field(..., alias="jwt_algorithm")
    jwt_secret: SecretStr = Field(..., alias="jwt_secret")
    
    # Otros (opcional: CORS, JWT, etc.)
    allowed_origins: list[str] = ["*"]
    allow_credentials: bool = True
    allow_methods: list[str] = ["*"]
    allow_headers: list[str] = ["*"]
    
    def model_post_init(self, __context):
        # Solo agrega si no está ya en la lista
        if self.frontend_url not in self.allowed_origins:
            self.allowed_origins.append(self.frontend_url)


SETTINGS = Settings()