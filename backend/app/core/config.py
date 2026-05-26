import os
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    # App
    APP_NAME: str = "Quant Trading Platform"
    DEBUG: bool = os.getenv("FASTAPI_DEBUG", "false").lower() == "true"
    FASTAPI_HOST: str = os.getenv("FASTAPI_HOST", "0.0.0.0")
    FASTAPI_PORT: int = int(os.getenv("FASTAPI_PORT", 8000))
    
    # Database
    DATABASE_URL: str = os.getenv("DATABASE_URL", "mysql+pymysql://root:password@localhost:3306/quant_db")
    
    # Redis
    REDIS_URL: str = os.getenv("REDIS_URL", "redis://localhost:6379/0")
    
    # JWT
    SECRET_KEY: str = os.getenv("SECRET_KEY", "your-secret-key-change-this")
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    
    # Data Source
    TUSHARE_TOKEN: str = os.getenv("TUSHARE_TOKEN", "")
    
    # Broker
    BROKER_API_KEY: str = os.getenv("BROKER_API_KEY", "")
    BROKER_SECRET: str = os.getenv("BROKER_SECRET", "")
    
    class Config:
        env_file = ".env"
        case_sensitive = True

settings = Settings()
