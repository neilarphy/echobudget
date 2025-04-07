from sqlalchemy.orm import Session
from app.infra.database.models.transactionlog import TransactionLogORM
from app.domain.enums import TransactionType, TransactionSource


def create_transaction_log(
    db: Session,
    user_id: int,
    amount: int,
    type_: TransactionType,
    source: TransactionSource
) -> TransactionLogORM:
    log = TransactionLogORM(
        user_id=user_id,
        amount=amount,
        type=type_.value,
        source=source.value
    )
    db.add(log)
    db.commit()
    db.refresh(log)
    return log


def get_transaction_logs_by_user(db: Session, user_id: int) -> list[TransactionLogORM]:
    return db.query(TransactionLogORM).filter(TransactionLogORM.user_id == user_id).all()


def get_transaction_log(db: Session, log_id: int) -> TransactionLogORM | None:
    return db.query(TransactionLogORM).filter(TransactionLogORM.id == log_id).first()


def delete_transaction_log(db: Session, log_id: int) -> bool:
    log = db.query(TransactionLogORM).filter(TransactionLogORM.id == log_id).first()
    if log:
        db.delete(log)
        db.commit()
        return True
    return False
