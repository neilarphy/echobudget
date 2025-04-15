from app.domain.enums import TransactionType, TransactionSource
from typing import TYPE_CHECKING, Union

if TYPE_CHECKING:
    from app.domain.user import User
    from app.domain.transaction_log import TransactionLog

class BalanceManager:
    def __init__(
            self,
            owner: "User",
            initial_balance: int = 0
    ):
        self.__owner = owner
        self.__balance = initial_balance
        self.__history: list["TransactionLog"] = []

    def get_balance(self):
        return self.__balance
        
    def add_balance(
            self,
            amount:int,
            source: TransactionSource = TransactionSource.TOPUP 
    ) -> "TransactionLog":
        self.__balance += amount
        log = TransactionLog(
            log_id=0,
            user=self.__owner,
            amount=amount,
            type_=TransactionType.CREDIT,
            source=source
        )
        self.__history.append(log)
        return log

    def deduct_balance(
            self,
            amount: int,
            source: TransactionSource = TransactionSource.INFERENCE
    ) -> tuple[bool, Union["TransactionLog" , None]]:
        if self.__balance >= amount:
            self.__balance -= amount
            log =TransactionLog(
                log_id=0,
                user=self.__owner,
                amount=amount,
                type_=TransactionType.DEBIT,
                source=source
            )
            self.__history.append(log)
            return True, log
        return False, None