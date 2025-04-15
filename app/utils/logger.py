import logging
import sys
from logging.handlers import RotatingFileHandler
from colorlog import ColoredFormatter
from app.config import settings

def get_logger(name: str) -> logging.Logger:
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    if logger.hasHandlers():
        return logger
    settings.LOG_FILE_PATH.parent.mkdir(parents=True, exist_ok=True)
    #формат
    formatter = ColoredFormatter(
        "%(log_color)s[%(asctime)s] [%(levelname)s] [%(name)s] - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        log_colors={
            "DEBUG": "cyan",
            "INFO": "green",
            "WARNING": "yellow",
            "ERROR": "red",
            "CRITICAL": "bol_red",
        },
    )

    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    #ротация
    file_handler = RotatingFileHandler(
        filename=settings.LOG_FILE_PATH,
        maxBytes=settings.LOG_FILE_SIZE_MB,
        backupCount=settings.LOG_FILE_BACKUPS,
        encoding="utf-8",
    )
    file_formatter = logging.Formatter(
        "[%(asctime)s] [%(levelname)s] [%(name)s] - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )

    file_handler.setFormatter(file_formatter)
    logger.addHandler(file_handler)

    return logger
