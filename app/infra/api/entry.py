from fastapi import (
    APIRouter,
    UploadFile,
    File,
    Form,
    Depends,
    HTTPException,
)
from sqlalchemy.orm import Session
from typing import Optional
from app.infra.services.balance_manager import BalanceManagerORM

from app.infra.database.session import get_db
from app.infra.database.crud.entry_crud import create_entry
from app.infra.services.minio_service import upload_file
from app.infra.messaging.producer import publish_task
from app.infra.database.crud.user_crud import get_user_by_username
from app.schemas.sch_entry import EntryUploadResponse
from app.domain.enums import (
    MLModelType,
    InputType,
    EntryStatus,
) 
from app.utils.logger import get_logger

router = APIRouter()
logger = get_logger(__name__)

def get_mock_user(db: Session = Depends(get_db)):
    user = get_user_by_username(db, "user")
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.post("/", response_model=EntryUploadResponse, summary="Загрузите текст или аудио для предсказания")
async def upload_entry(
    model_type: MLModelType = Form(...),
    text: Optional[str] = Form(None),
    file: Optional[UploadFile] = File(None),
    db: Session = Depends(get_db),
    user=Depends(get_mock_user),
):
    if bool(text) == bool(file):
        raise HTTPException(
            status_code=400,
            detail="Неверный формат, передайте либо текст либо файл"
        )
    
    if file:
        content = await file.read()
        filename = upload_file(content)
        input_type = InputType.VOICE
        data_field = filename
    else:
        input_type = InputType.TEXT
        data_field = text

    entry = create_entry(
        db=db,
        user_id=user.id,
        input_type=input_type,
        data=data_field,
        status=EntryStatus.CREATED
    )

    publish_task({
        "entry_id": entry.id,
        "user_id": user.id,
        "model_type": model_type.value,
        "data": data_field
    })

    logger.info(f"Создан entry #{entry.id} и опубликована задача")

    return EntryUploadResponse(
        entry_id=entry.id,
        message="Данные успешно загружены и переданы на обработку",
    )