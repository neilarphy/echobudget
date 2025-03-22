from app.domain.transaction_log import TransactionLog
from app.domain.enums import TransactionType, TransactionSource
from app.domain.auth import AuthService

class User:
    def __init__(self, user_id: int, username: str, password_hash: str, role: str = "user"):
        self.__user_id = user_id
        self.__username = username
        self.__password_hash = password_hash
        self.__role = role
        self.__balance = 0

    def is_admin(self) -> bool:
        return self.__role == "admin"
    
    def check_password(self, password: str) -> bool:
        return AuthService.verify_password(password, self.__password_hash)

    def get_balance(self) -> int:
        return self.__balance
    
    def get_username(self) -> str:
        return self.__username

    def add_credits(self, amount: int) -> TransactionLog:
        self.__balance += amount
        return TransactionLog(
            log_id=0,
            user=self,
            amount=amount,
            type_=TransactionType.CREDIT,
            source=TransactionSource.TOPUP
        )

    def deduct_credits(self, amount: int) -> tuple[bool, TransactionLog]:
        if self.__balance >= amount:
            self.__balance -= amount
            log = TransactionLog(
                log_id=0,
                user=self,
                amount=amount,
                type_=TransactionType.DEBIT,
                source=TransactionSource.INFERENCE
            )
            return True, log
        return False