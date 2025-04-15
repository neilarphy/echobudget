from app.domain.auth import AuthService
from app.domain.enums import UserRole
from app.domain.balance import BalanceManager

class User:
    def __init__(
            self, 
            user_id: int, 
            username: str, 
            email: str,
            password_hash: str, 
            role: str = UserRole.USER.value
        ):
        self.__user_id = user_id
        self.__username = username
        self.__email = email
        self.__password_hash = password_hash
        self.__role = role
        self.__balance_manager = BalanceManager(owner=self)

    def is_admin(self) -> bool:
        return self.__role == "admin"
    
    def get_username(self) -> str:
        return self.__username
    
    def get_user_id(self) -> int:
        return self.__user_id
    
    def get_email(self) -> str:
        return self.__email
    
    def check_password(self, password: str) -> bool:
        return AuthService.verify_password(password, self.__password_hash)

    def get_balance_manager(self) -> BalanceManager:
        return self.__balance_manager
    
    