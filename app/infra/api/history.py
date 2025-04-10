from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.infra.database.session import SessionLocal
from app.infra.database.crud.user_crud import get_user_by_username
from app.infra.database.models.entries import EntryORM
from app.infra.database.models.parsed_entry import ParsedEntryORM
from app.schemas.sch_history import PredictionHistoryResponse, PredictionHistoryItem
from app.schemas.sch_history import EntryOut, ParsedEntryOut

router = APIRouter()


# Временно мок-юзер
def get_mock_user(db: Session = Depends(lambda: SessionLocal())):
    user = get_user_by_username(db, "user")
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@router.get("/", response_model=PredictionHistoryResponse)
def get_prediction_history(user=Depends(get_mock_user), db: Session = Depends(lambda: SessionLocal())):
    entries = db.query(EntryORM).filter(EntryORM.user_id == user.id).all()
    history = []

    for entry in entries:
        parsed = db.query(ParsedEntryORM).filter(ParsedEntryORM.entry_id == entry.id).first()
        history.append(
            PredictionHistoryItem(
                entry=entry,
                parsed=parsed
            )
        )

    return {"history": history}
