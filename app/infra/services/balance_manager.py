# app/infra/services/balance_manager.py

from app.infra.database.models.users import UserORM
from app.infra.database.models.transactionlog import TransactionLogORM
from app.domain.enums import TransactionType, TransactionSource
from sqlalchemy.orm import Session

class BalanceManagerORM:
    def __init__(self, db: Session, user: UserORM):
        self.db = db
        self.user = user

    def get_balance(self) -> int:
        return self.user.balance

    def add_balance(self, amount: int, source: TransactionSource = TransactionSource.TOPUP) -> TransactionLogORM:
        self.user.balance += amount
        log = TransactionLogORM(
            user_id=self.user.id,
            amount=amount,
            type=TransactionType.CREDIT.value,
            source=source.value
        )
        self.db.add(log)
        self.db.add(self.user)
        return log

    def deduct_balance(self, amount: int, source: TransactionSource = TransactionSource.INFERENCE) -> tuple[bool, TransactionLogORM | None]:
        if self.user.balance >= amount:
            self.user.balance -= amount
            log = TransactionLogORM(
                user_id=self.user.id,
                amount=amount,
                type=TransactionType.DEBIT.value,
                source=source.value
            )
            self.db.add(log)
            self.db.add(self.user)
            
            return True, log
        return False, None
