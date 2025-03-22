from datetime import datetime
from app.domain.enums import TransactionType, TransactionSource
from app.domain.user import User


class TransactionLog:
    def __init__(
            self, 
            log_id: int, 
            user: User,
            amount: int, 
            type_: TransactionType, 
            source: TransactionSource, 
            created_at: datetime = None
        ):
        self.__log_id = log_id
        self.__user = user
        self.__amount = amount
        self.__type = type_
        self.__source = source
        self.__created_at = created_at or datetime.utcnow()

    def is_debit(self) -> bool:
        return self.__type == TransactionType.DEBIT

    def get_user(self) -> User:
        return self.__user

    def get_amount(self) -> int:
        return self.__amount

    def get_type(self) -> TransactionType:
        return self.__type

    def get_source(self) -> TransactionSource:
        return self.__source

    def get_created_at(self) -> datetime:
        return self.__created_at

    def to_dict(self) -> dict:
        return {
            "user": self.__user.get_username(),
            "amount": self.__amount,
            "type": self.__type.value,
            "source": self.__source.value,
            "created_at": self.__created_at.isoformat()
        }