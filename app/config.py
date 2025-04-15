import os
from dotenv import load_dotenv
from pydantic_settings import BaseSettings
from pathlib import Path

load_dotenv()

class Settings(BaseSettings):
    DATABASE_URL: str
    RABBITMQ_URL: str

    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str

    RABBITMQ_DEFAULT_USER: str
    RABBITMQ_DEFAULT_PASS: str
    RABBITMQ_QUEUE_NAME: str = "ml_tasks"
    RABBITMQ_QUEUE_DURABLE: bool = True

    LOG_FILE_PATH: Path = Path("./logs/echobudget.log")
    LOG_FILE_SIZE_MB: int = 5
    LOG_FILE_BACKUPS: int = 3

    MINIO_ROOT_USER: str
    MINIO_ROOT_PASSWORD: str
    MINIO_BUCKET_NAME: str 
    MINIO_URL: str

    class Config:
        env_file_encoding = "utf-8"


settings = Settings()
