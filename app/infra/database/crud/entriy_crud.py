from sqlalchemy.orm import Session
from app.infra.database.models.entries import EntryORM
from app.domain.enums import InputType, EntryStatus


def create_entry(
    db: Session,
    user_id: int,
    input_type: InputType,
    data: str,
    status: EntryStatus = EntryStatus.CREATED,
    error_reason: str | None = None
) -> EntryORM:
    entry = EntryORM(
        user_id=user_id,
        input_type=input_type.value,
        data=data,
        status=status.value,
        error_reason=error_reason
    )
    db.add(entry)
    db.commit()
    db.refresh(entry)
    return entry


def get_entry(db: Session, entry_id: int) -> EntryORM | None:
    return db.query(EntryORM).filter(EntryORM.id == entry_id).first()


def get_entries_by_user(db: Session, user_id: int) -> list[EntryORM]:
    return db.query(EntryORM).filter(EntryORM.user_id == user_id).all()


def update_entry_status(
    db: Session,
    entry_id: int,
    new_status: EntryStatus,
    error_reason: str | None = None
) -> EntryORM | None:
    entry = db.query(EntryORM).filter(EntryORM.id == entry_id).first()
    if entry:
        entry.status = new_status.value
        entry.error_reason = error_reason
        db.commit()
        db.refresh(entry)
        return entry
    return None


def delete_entry(db: Session, entry_id: int) -> bool:
    entry = db.query(EntryORM).filter(EntryORM.id == entry_id).first()
    if entry:
        db.delete(entry)
        db.commit()
        return True
    return False
