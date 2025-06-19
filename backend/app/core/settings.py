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
    admin_table: str = Field(..., alias="admin_table")
    client_table: str = Field(..., alias="client_table")

    # SMTP (Gmail)
    smtp_host: str = "smtp.gmail.com"
    smtp_port: int = 587
    smtp_corp_email: EmailStr = Field(..., alias="corp_user")
    smtp_corp_password: SecretStr = Field(..., alias="corp_password")

    frontend_url: str = Field(..., alias="frontend_url")
    reset_password_url: str = Field(..., alias="reset_password_url")
    
    # Otros (opcional: CORS, JWT, etc.)
    allowed_origins: list[str] = []
    allow_credentials: bool = True
    allow_methods: list[str] = ["*"]
    allow_headers: list[str] = ["*"]
    
    def model_post_init(self, __context):
        # Solo agrega si no está ya en la lista
        if self.frontend_url not in self.allowed_origins:
            self.allowed_origins.append(self.frontend_url)


SETTINGS = Settings()