# config.py
import os
import secrets
from pathlib import Path
from datetime import timedelta

BASE_DIR = Path(__file__).resolve().parent

# Database Configuration
DATABASE_URL = os.getenv(
    "DATABASE_URL",
    f"sqlite:///{BASE_DIR}/pharmacy_erp.db"
)

# JWT Configuration
DEBUG = os.getenv("DEBUG", "True").lower() == "true"
ENV = os.getenv("ENV", "development")

_jwt_secret = os.getenv("JWT_SECRET_KEY")
if not _jwt_secret or _jwt_secret == "your-secret-key-change-in-production":
    if ENV == "production":
        raise ValueError(
            "SEGURANÇA: JWT_SECRET_KEY não configurada para produção! "
            "Defina a variável de ambiente JWT_SECRET_KEY."
        )
    _jwt_secret = secrets.token_hex(32)

JWT_SECRET_KEY = _jwt_secret
JWT_ALGORITHM = os.getenv("JWT_ALGORITHM", "HS256")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", "30"))

# CORS Configuration
CORS_ORIGINS = [
    "http://localhost",
    "http://localhost:3000",
    "http://localhost:5500",
    "http://localhost:8000",
    "http://localhost:5173",
]

# App Configuration
ALLOWED_HOSTS = ["*"]

# Timezone
TIMEZONE = "America/Sao_Paulo"

# Pagination
DEFAULT_PAGE_SIZE = 10
MAX_PAGE_SIZE = 100

# Alert Thresholds (days)
ALERT_EXPIRATION_DAYS = 30
ALERT_LOW_STOCK_PERCENTAGE = 20

