import os
from pathlib import Path
from typing import Optional

from pydantic import EmailStr, SecretStr, Field
from pydantic_settings import BaseSettings, SettingsConfigDict
from jinja2 import Environment, FileSystemLoader, select_autoescape

class Settings(BaseSettings):
    # General
    app_name: str = "InventaryApp"
    environment: str = "development"  # development | production | staging
    debug: bool = True
    model_config = SettingsConfigDict(env_file=os.path.join(os.path.dirname(__file__), "../../../.env"), env_file_encoding='utf-8', extra='allow')
    BACKEND_DIR: Path = Path(__file__).resolve().parent.parent.parent
    FRONTEND_DIR: Path = BACKEND_DIR.parent / "frontend"
    STATIC_DIR: Path = FRONTEND_DIR / "my-app" / "static"
    port: int = 8000

    # Database
    db_url: str = Field(..., alias="database_url")
    
    #Storage
    storage_endpoint_url: str = Field(..., alias="storage_endpoint_url")
    storage_access_key: SecretStr = Field(..., alias="access_key")
    storage_secret_key: SecretStr = Field(..., alias="secret_key")
    storage_region: str = Field(..., alias="region")
    bucket_name: str = Field(..., alias="bucket_name")
    image_folder: str = Field(..., alias="image_folder")
    invoice_folder: str = Field(..., alias="invoice_folder")
    
    # Invoices
    INVOICES_PATH: Path = STATIC_DIR / "invoices"

    # Email
    smtp_host: str = Field(..., alias="smtp_host")
    smtp_port: int = Field(..., alias="smtp_port")
    smtp_comp_email: EmailStr = Field(..., alias="comp_user")
    smtp_comp_password: SecretStr = Field(..., alias="comp_password")
    
    # Templates
    templates_dir: str = Field(os.path.join(os.path.dirname(__file__), "../templates"), alias="templates_dir")
    jinja_env : Optional[Environment] = Field(default=None, alias="jinja_env")

    # Company
    company_name: str = Field(..., alias="company_name")
    company_email: EmailStr = Field(..., alias="company_email")
    company_phone: str = Field(..., alias="company_phone")
    company_address: str = Field(..., alias="company_address")
    frontend_url: str = Field(..., alias="frontend_url")
    home_url: str = Field(..., alias="home_url")
    logo_url: str = Field(..., alias="logo_url")
    footer_message: str = Field(..., alias="footer_message")

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
        # Configura Jinja2 environment
        self.jinja_env = Environment(
            loader=FileSystemLoader(self.templates_dir),
            autoescape=select_autoescape(["html", "xml"])
        )


SETTINGS = Settings()