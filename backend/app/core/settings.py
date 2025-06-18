from pydantic import BaseSettings, EmailStr, SecretStr, Field

class Settings(BaseSettings):
    # General
    app_name: str = "InventaryApp"
    environment: str = "development"  # development | production | staging
    debug: bool = True

    # Supabase
    db_url: str = Field(..., env="DATABASE_URL")
    db_key: SecretStr = Field(..., env="DATABASE_KEY")

    # SMTP (Gmail)
    smtp_host: str = "smtp.gmail.com"
    smtp_port: int = 587
    smtp_corp_email: EmailStr = Field(..., env="CORP_USER")
    smtp_corp_password: SecretStr = Field(..., env="CORP_PASSWORD")

    # Otros (opcional: CORS, JWT, etc.)
    allowed_origins: list[str] = ["http://localhost:5173"]
    allow_credentials: bool = True
    allow_methods: list[str] = ["*"]
    allow_headers: list[str] = ["*"]

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


SETTINGS = Settings()