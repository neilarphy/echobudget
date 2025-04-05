from sqlalchemy.orm import Session
from app.infra.database.models.parsed_entry import ParsedEntryORM
from datetime import datetime


def create_parsed_entry(
    db: Session,
    entry_id: int,
    user_id: int,
    amount: float,
    category: str,
    comment: str,
    model_name: str
) -> ParsedEntryORM:
    parsed_entry = ParsedEntryORM(
        entry_id=entry_id,
        user_id=user_id,
        amount=amount,
        category=category,
        comment=comment,
        model_name=model_name,
        created_at=datetime.utcnow()
    )
    db.add(parsed_entry)
    db.commit()
    db.refresh(parsed_entry)
    return parsed_entry


def get_parsed_entry_by_entry_id(
    db: Session,
    entry_id: int
) -> ParsedEntryORM | None:
    return db.query(ParsedEntryORM).filter(ParsedEntryORM.entry_id == entry_id).first()


def get_parsed_entries_by_user(
    db: Session,
    user_id: int
) -> list[ParsedEntryORM]:
    return db.query(ParsedEntryORM).filter(ParsedEntryORM.user_id == user_id).all()


def delete_parsed_entry(
    db: Session,
    parsed_entry_id: int
) -> bool:
    entry = db.query(ParsedEntryORM).filter(ParsedEntryORM.id == parsed_entry_id).first()
    if entry:
        db.delete(entry)
        db.commit()
        return True
    return False
