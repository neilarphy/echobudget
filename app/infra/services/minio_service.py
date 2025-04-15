from minio import Minio
from minio.error import S3Error
from app.config import settings
from pathlib import Path
import uuid
import io

client = Minio(
    settings.MINIO_URL,
    access_key=settings.MINIO_ROOT_USER,
    secret_key=settings.MINIO_ROOT_PASSWORD,
    secure=False,
)

def upload_file(
        file_data: bytes,
        filename: str = None,
) -> str:
    if not filename:
        filename = f"{uuid.uuid4()}.wav"
    path = f"{settings.MINIO_BUCKET_NAME}/{filename}"

    if not client.bucket_exists(settings.MINIO_BUCKET_NAME):
        client.make_bucket(settings.MINIO_BUCKET_NAME)

    client.put_object(
        bucket_name=settings.MINIO_BUCKET_NAME,
        object_name=filename,
        data=io.BytesIO(file_data),
        length=len(file_data),
    )

    return filename

def download_file(filename: str) -> bytes:
    response = client.get_object(
        bucket_name=settings.MINIO_BUCKET_NAME,
        object_name=filename,
    )

    return response.read()