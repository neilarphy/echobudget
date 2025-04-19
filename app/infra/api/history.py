from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.infra.database.session import get_db
from app.infra.database.crud.user_crud import get_user_by_username
from app.infra.database.crud.entry_crud import get_entries_by_user, get_entry
from app.infra.database.crud.parsedentry_crud import get_parsed_entries_by_user, get_parsed_entry_by_entry_id
from app.schemas.sch_history import PredictionHistoryResponse, PredictionHistoryItem
from app.utils.logger import get_logger

logger = get_logger(__name__)

router = APIRouter()


# Временно мок-юзер
def get_mock_user(db: Session = Depends(get_db)):
    user = get_user_by_username(db, "user")
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@router.get("/", response_model=PredictionHistoryResponse)
def get_prediction_history(
    user=Depends(get_mock_user), 
    db: Session = Depends(get_db)
):
    entries = get_entries_by_user(db, user.id)
    history = []

    for entry in entries:
        try:
            parsed =get_parsed_entry_by_entry_id(db, entry.id)
        except Exception as e:
            logger.error(f"Ошибка при получении parsed для entry {entry.id}: {e}")
            parsed = None
        
        history.append(
            PredictionHistoryItem(
                entry=entry,
                parsed=parsed
            )
        )

    return {"history": history}

@router.get("/{entry_id}", response_model=PredictionHistoryItem)
def get_prediction_by_id(
    entry_id: int,
    user=Depends(get_mock_user),
    db: Session = Depends(get_db)
):
    entry = get_entry(db, entry_id)
    if not entry:
        raise HTTPException(status_code=404, detail="Entry not found")

    parsed = get_parsed_entry_by_entry_id(db, entry_id)

    return PredictionHistoryItem(entry=entry, parsed=parsed)
